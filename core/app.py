# core/app.py
from pathlib import Path
from core.plugin_kernel import PluginKernel
from hooks.system_hooks import HookBus


class Logger:
    def info(self, msg):
        print(f"[INFO] {msg}")

    def error(self, msg):
        print(f"[ERROR] {msg}")


def main():
    base_dir = Path(__file__).resolve().parent.parent
    logger = Logger()

    logger.info("YnFOR v6.0.0 — démarrage")

    hooks = HookBus()
    kernel = PluginKernel(base_dir)
    kernel.discover_plugins()
    kernel.load_all()

    context = {
        "logger": logger,
        "hooks": hooks,
    }
    kernel.init_all(context)

    # Enregistrer les hooks exposés par les plugins
    for plugin in kernel.plugins.values():
        inst = plugin.instance
        if hasattr(inst, "on_pre_run"):
            hooks.register("pre_run", inst.on_pre_run)
        if hasattr(inst, "on_post_run"):
            hooks.register("post_run", inst.on_post_run)

    kernel.start_all()

    hooks.emit("pre_run", {"task": "demo"})
    # TODO: logique principale YnFOR ici
    hooks.emit("post_run", {"task": "demo"})

    kernel.stop_all()
    logger.info("YnFOR v6.0.0 — arrêt")


if __name__ == "__main__":
    main()
