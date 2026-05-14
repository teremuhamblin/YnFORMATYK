# core/logger.py
import time
from pathlib import Path

class Logger:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.log_core = self.base_dir / "logs" / "core.log"
        self.log_plugins = self.base_dir / "logs" / "plugins.log"
        self.log_security = self.base_dir / "logs" / "security.log"
        self.log_telemetry = self.base_dir / "logs" / "telemetry.log"

    # ---------------------------------------------------------
    # Format enrichi
    # ---------------------------------------------------------
    def _format(self, level, message, plugin=None, trace=None):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        trace_id = trace.trace_id if trace else "-"
        span_id = trace.span_id if trace else "-"
        plugin_name = plugin if plugin else "core"

        return f"[{timestamp}] [{level}] [plugin={plugin_name}] [trace={trace_id}/{span_id}] {message}"

    # ---------------------------------------------------------
    # Écriture dans les fichiers
    # ---------------------------------------------------------
    def _write(self, file, msg):
        with open(file, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

    # ---------------------------------------------------------
    # API publique
    # ---------------------------------------------------------
    def info(self, msg, plugin=None, trace=None):
        formatted = self._format("INFO", msg, plugin, trace)
        self._write(self.log_core, formatted)

    def plugin(self, msg, plugin, trace=None):
        formatted = self._format("PLUGIN", msg, plugin, trace)
        self._write(self.log_plugins, formatted)

    def security(self, msg, plugin=None, trace=None):
        formatted = self._format("SECURITY", msg, plugin, trace)
        self._write(self.log_security, formatted)

    def telemetry(self, msg, plugin=None, trace=None):
        formatted = self._format("TELEMETRY", msg, plugin, trace)
        self._write(self.log_telemetry, formatted)

    def error(self, msg, plugin=None, trace=None):
        formatted = self._format("ERROR", msg, plugin, trace)
        self._write(self.log_core, formatted)
