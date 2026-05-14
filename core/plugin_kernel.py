# core/plugin_kernel.py
import importlib
import json
from pathlib import Path


# ============================================================
# 🔐 SECURITY LAYER — Permissions Manager intégré
# ============================================================

class PermissionManager:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.permissions_file = self.base_dir / "plugins" / "permissions.json"

        if not self.permissions_file.exists():
            raise FileNotFoundError("[SECURITY] permissions.json introuvable")

        self.permissions = json.loads(self.permissions_file.read_text())

    def check(self, plugin_name, capability):
        plugin_caps = self.permissions["plugins"].get(plugin_name, {})
        default_caps = self.permissions["default"]

        allowed = plugin_caps.get(capability, default_caps.get(capability, False))

        if not allowed:
            raise PermissionError(
                f"[SECURITY] Plugin '{plugin_name}' n'a pas la permission '{capability}'"
            )

        return True


# ============================================================
# 🧩 PLUGIN CLASS
# ============================================================

class Plugin:
    def __init__(self, name, path, manifest, security):
        self.name = name
        self.path = path
        self.manifest = manifest
        self.security = security
        self.module = None
        self.instance = None

    # --------------------------------------------------------
    # 🔧 Chargement avec vérification des permissions
    # --------------------------------------------------------
    def load(self):
        # Vérification des permissions déclaratives
        for cap in ["filesystem", "network", "telemetry", "hooks"]:
            self.security.check(self.name, cap)

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


# ============================================================
# ⚙️ PLUGIN KERNEL — Kernel + Hot‑Reload + Security Layer
# ============================================================

class PluginKernel:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.plugins = {}
        self.context = {}

        # Chargement du Security Layer
        self.security = PermissionManager(base_dir)

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

                self.plugins[name] = Plugin(
                    name=name,
                    path=rel_path,
                    manifest=manifest,
                    security=self.security
                )

    # ---------------------------------------------------------
    # 🔧 Cycle de vie global
    # ---------------------------------------------------------
    def load_all(self):
        for plugin in self.plugins.values():
            plugin.load()

    def init_all(self, context):
        self.context = context
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
