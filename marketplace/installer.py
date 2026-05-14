import json, shutil, requests
from pathlib import Path

class MarketplaceInstaller:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

    def install(self, pkg_url):
        print(f"[Marketplace] Téléchargement : {pkg_url}")
        data = requests.get(pkg_url).json()

        plugin_name = data["name"]
        target_dir = self.base_dir / "plugins" / "external" / plugin_name
        target_dir.mkdir(parents=True, exist_ok=True)

        for file_name, content in data["files"].items():
            with open(target_dir / file_name, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"[Marketplace] Plugin installé : {plugin_name}")
