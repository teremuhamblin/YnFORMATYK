import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PluginReloadHandler(FileSystemEventHandler):
    def __init__(self, kernel):
        self.kernel = kernel

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            plugin_name = Path(event.src_path).parent.name
            print(f"[HotReload] Modification détectée : {plugin_name}")
            self.kernel.reload_plugin(plugin_name)

class HotReloadEngine:
    def __init__(self, kernel, base_dir):
        self.kernel = kernel
        self.base_dir = Path(base_dir)

    def start(self):
        observer = Observer()
        handler = PluginReloadHandler(self.kernel)
        observer.schedule(handler, str(self.base_dir / "plugins"), recursive=True)
        observer.start()
        print("[HotReload] Activé")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
