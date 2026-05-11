from src.utils import normalize_text
from src.core import CoreEngine
from src.api import ApiClient

def test_full_pipeline(monkeypatch):
    # Mock API
    class MockResponse:
        def json(self):
            return {"status": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import src.api.requests
    src.api.requests.get = mock_get

    # Pipeline
    text = "  DATA  "
    normalized = normalize_text(text)

    engine = CoreEngine()
    processed = engine.process(normalized)

    client = ApiClient("https://api.example.com")
    api_response = client.get("/status")

    assert normalized == "data"
    assert processed == "processed: data"
    assert api_response["status"] == "ok"
```
