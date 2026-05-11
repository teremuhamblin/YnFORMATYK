from src.utils import normalize_text
from src.core import CoreEngine

def test_utils_core_flow():
    engine = CoreEngine()
    text = "  Hello World  "
    normalized = normalize_text(text)
    result = engine.process(normalized)

    assert result == "processed: hello world"
```
