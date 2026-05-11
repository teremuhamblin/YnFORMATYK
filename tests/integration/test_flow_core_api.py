from src.core import CoreEngine
from src.api import ApiClient

def test_core_api_flow(monkeypatch):
    engine = CoreEngine()

    class MockResponse:
        def json(self):
            return {"data": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import src.api.requests
    src.api.requests.get = mock_get

    client = ApiClient("https://api.example.com")
    processed = engine.process("input")
    response = client.get("/data")

    assert processed == "processed: input"
    assert response["data"] == "ok"
```
