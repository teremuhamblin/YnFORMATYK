# 🧪 Test — API

```python
import pytest
from src.api import ApiClient

def test_api_client_init():
    client = ApiClient(base_url="https://api.example.com")
    assert client.base_url.startswith("https://")

def test_api_get(monkeypatch):
    class MockResponse:
        def json(self):
            return {"status": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("src.api.requests.get", mock_get)

    client = ApiClient("https://api.example.com")
    response = client.get("/status")

    assert response["status"] == "ok"
```
