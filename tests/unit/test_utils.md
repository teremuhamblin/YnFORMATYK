# 🧪 Test — Utils

```python
import pytest
from src.utils import normalize_text, add_numbers

def test_normalize_text():
    assert normalize_text("  Hello  ") == "hello"

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
```
