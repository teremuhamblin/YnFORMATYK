import json, requests
from pathlib import Path

class MarketplaceUpdater:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

    def update(self, plugin_name, pkg_url):
        print(f"[Marketplace] Mise à jour : {plugin_name}")
        data = requests.get(pkg_url).json()

        plugin_dir = self.base_dir / "plugins" / "external" / plugin_name
        if not plugin_dir.exists():
            print("[Marketplace] Plugin introuvable")
            return

        for file_name, content in data["files"].items():
            with open(plugin_dir / file_name, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"[Marketplace] Mise à jour terminée : {plugin_name}")
