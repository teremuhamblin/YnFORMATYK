# core/plugin_kernel.py
import importlib
import json
from pathlib import Path


class Plugin:
    def __init__(self, name, path, manifest):
        self.name = name
        self.path = path
        self.manifest = manifest
        self.module = None
        self.instance = None

    def load(self):
        module_path = f"{self.path}.plugin"
        self.module = importlib.import_module(module_path)
        self.instance = getattr(self.module, "PluginImpl")()
        return self

    def init(self, context):
        if hasattr(self.instance, "init"):
            self.instance.init(context)

    def start(self):
        if hasattr(self.instance, "start"):
            self.instance.start()

    def stop(self):
        if hasattr(self.instance, "stop"):
            self.instance.stop()


class PluginKernel:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.plugins = {}
        self.context = {}  # nécessaire pour reload_plugin()

    # ---------------------------------------------------------
    # 🔍 Découverte des plugins
    # ---------------------------------------------------------
    def discover_plugins(self):
        plugins_root = self.base_dir / "plugins"
        for scope in ["core", "community", "external"]:
            scope_dir = plugins_root / scope
            if not scope_dir.exists():
                continue
            for plugin_dir in scope_dir.iterdir():
                if not plugin_dir.is_dir():
                    continue
                manifest_path = plugin_dir / "plugin.json"
                if not manifest_path.exists():
                    continue
                with open(manifest_path, "r", encoding="utf-8") as f:
                    manifest = json.load(f)
                name = manifest.get("name", plugin_dir.name)
                rel_path = f"plugins.{scope}.{plugin_dir.name}"
                self.plugins[name] = Plugin(name, rel_path, manifest)

    # ---------------------------------------------------------
    # 🔧 Cycle de vie global
    # ---------------------------------------------------------
    def load_all(self):
        for plugin in self.plugins.values():
            plugin.load()

    def init_all(self, context):
        self.context = context  # stocké pour reload_plugin()
        for plugin in self.plugins.values():
            plugin.init(context)

    def start_all(self):
        for plugin in self.plugins.values():
            plugin.start()

    def stop_all(self):
        for plugin in self.plugins.values():
            plugin.stop()

    # ---------------------------------------------------------
    # 🔥 Hot‑Reload intégré
    # ---------------------------------------------------------
    def reload_plugin(self, name):
        if name not in self.plugins:
            print(f"[HotReload] Plugin inconnu : {name}")
            return

        plugin = self.plugins[name]
        print(f"[HotReload] Rechargement : {name}")

        # 1. Stop propre
        plugin.stop()

        # 2. Reload du module Python
        importlib.reload(plugin.module)

        # 3. Rechargement complet
        plugin.load()
        plugin.init(self.context)
        plugin.start()

        print(f"[HotReload] Plugin rechargé : {name}")
