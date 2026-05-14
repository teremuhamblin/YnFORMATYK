import json
from pathlib import Path

class PermissionManager:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.permissions = json.loads(
            (self.base_dir / "plugins" / "permissions.json").read_text()
        )

    def check(self, plugin_name, capability):
        plugin_caps = self.permissions["plugins"].get(plugin_name)
        default_caps = self.permissions["default"]

        allowed = plugin_caps.get(capability, default_caps.get(capability, False))
        if not allowed:
            raise PermissionError(
                f"[SECURITY] Plugin '{plugin_name}' n'a pas la permission '{capability}'"
            )
        return True
