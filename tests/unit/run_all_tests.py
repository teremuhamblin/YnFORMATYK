#!/usr/bin/env python3
# ==========================================================
# YnFOR — Test Runner (Unit)
# Exécute : utils + core + api
# Auteur : YnFOR System
# ==========================================================

import sys
import traceback

# ----------------------------------------------------------
# Couleurs (logs)
# ----------------------------------------------------------
class Color:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

# ----------------------------------------------------------
# Fonctions de logs
# ----------------------------------------------------------
def info(msg):
    print(f"{Color.BLUE}[INFO]{Color.RESET} {msg}")

def success(msg):
    print(f"{Color.GREEN}[OK]{Color.RESET} {msg}")

def warn(msg):
    print(f"{Color.YELLOW}[WARN]{Color.RESET} {msg}")

def error(msg):
    print(f"{Color.RED}[ERROR]{Color.RESET} {msg}")

# ----------------------------------------------------------
# Tests Utils
# ----------------------------------------------------------
def test_utils():
    info("Tests Utils — démarrage...")

    from src.utils import normalize_text, add_numbers

    assert normalize_text("  Hello  ") == "hello"
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

    success("Tests Utils — OK")

# ----------------------------------------------------------
# Tests Core
# ----------------------------------------------------------
def test_core():
    info("Tests Core — démarrage...")

    from src.core import CoreEngine

    engine = CoreEngine()
    assert engine is not None

    result = engine.process("input")
    assert result == "processed: input"

    success("Tests Core — OK")

# ----------------------------------------------------------
# Tests API
# ----------------------------------------------------------
def test_api():
    info("Tests API — démarrage...")

    from src.api import ApiClient

    # Test init
    client = ApiClient("https://api.example.com")
    assert client.base_url.startswith("https://")

    # Mock GET
    class MockResponse:
        def json(self):
            return {"status": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import src.api.requests
    src.api.requests.get = mock_get

    response = client.get("/status")
    assert response["status"] == "ok"

    success("Tests API — OK")

# ----------------------------------------------------------
# Runner principal
# ----------------------------------------------------------
def main():
    info("Initialisation du Test Runner YnFOR (unit)...")

    tests = [
        ("Utils", test_utils),
        ("Core", test_core),
        ("API", test_api),
    ]

    total = len(tests)
    passed = 0

    for name, func in tests:
        info(f"Exécution du test : {name}")
        try:
            func()
            passed += 1
        except Exception as e:
            error(f"Échec dans {name}")
            print(traceback.format_exc())

    print("\n==========================================================")
    print(f" Résultat final : {passed}/{total} tests réussis")
    print("==========================================================\n")

    if passed == total:
        success("Tous les tests unitaires ont réussi.")
        sys.exit(0)
    else:
        error("Certains tests ont échoué.")
        sys.exit(1)

# ----------------------------------------------------------
# Entrée
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
