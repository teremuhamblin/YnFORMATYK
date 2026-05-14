# hooks/system_hooks.py

class HookBus:
    def __init__(self):
        self._handlers = {
            "pre_run": [],
            "post_run": [],
            "on_error": [],
        }

    def register(self, event_name, handler):
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)

    def emit(self, event_name, payload=None):
        for handler in self._handlers.get(event_name, []):
            handler(payload)
