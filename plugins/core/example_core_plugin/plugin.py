# plugins/core/example_core_plugin/plugin.py

class PluginImpl:
    def __init__(self):
        self.name = "example_core_plugin"
        self.logger = None

    def init(self, context):
        self.logger = context.get("logger")
        if self.logger:
            self.logger.info(f"[{self.name}] init")

    def start(self):
        if self.logger:
            self.logger.info(f"[{self.name}] start")

    def stop(self):
        if self.logger:
            self.logger.info(f"[{self.name}] stop")

    def on_pre_run(self, payload):
        if self.logger:
            self.logger.info(f"[{self.name}] pre_run: {payload}")

    def on_post_run(self, payload):
        if self.logger:
            self.logger.info(f"[{self.name}] post_run: {payload}")
