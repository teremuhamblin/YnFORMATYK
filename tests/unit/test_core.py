# ==========================================================
# YnFOR — Tests Unitaires : Core
# ==========================================================

import pytest
from src.core import CoreEngine

def test_core_initialization():
    engine = CoreEngine()
    assert engine is not None

def test_core_process():
    engine = CoreEngine()
    result = engine.process("input")
    assert result == "processed: input"
