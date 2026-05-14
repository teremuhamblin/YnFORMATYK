# core/tracer.py
import uuid
import time

class Trace:
    def __init__(self):
        self.trace_id = uuid.uuid4().hex
        self.start_time = time.time()

    def new_span(self):
        return Span(self.trace_id)

class Span:
    def __init__(self, trace_id):
        self.trace_id = trace_id
        self.span_id = uuid.uuid4().hex[:12]
        self.timestamp = time.time()

    def to_dict(self):
        return {
            "trace_id": self.trace_id,
            "span_id": self.span_id,
            "timestamp": self.timestamp
        }
