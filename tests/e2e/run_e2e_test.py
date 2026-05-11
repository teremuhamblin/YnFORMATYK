#!/usr/bin/env python3
# ==========================================================
# YnFOR — Test End-to-End (E2E)
# Pipeline complet : Utils → Core → API
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
# Logs
# ----------------------------------------------------------
def info(msg):
    print(f"{Color.BLUE}[INFO]{Color.RESET} {msg}")

def step(msg):
    print(f"{Color.CYAN}[STEP]{Color.RESET} {msg}")

def success(msg):
    print(f"{Color.GREEN}[OK]{Color.RESET} {msg}")

def error(msg):
    print(f"{Color.RED}[ERROR]{Color.RESET} {msg}")

# ----------------------------------------------------------
# Test E2E complet
# ----------------------------------------------------------
def run_e2e_test():
    info("Initialisation du test E2E YnFOR...")

    # Import des modules
    from src.utils import normalize_text
    from src.core import CoreEngine
    from src.api import ApiClient

    # Mock API
    class MockResponse:
        def json(self):
            return {"status": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import src.api.requests
    src.api.requests.get = mock_get

    # Pipeline
    step("1. Normalisation du texte...")
    raw = "  DATA  "
    normalized = normalize_text(raw)
    info(f"Normalisé : {normalized}")

    step("2. Traitement via CoreEngine...")
    engine = CoreEngine()
    processed = engine.process(normalized)
    info(f"Traitement : {processed}")

    step("3. Appel API mocké...")
    client = ApiClient("https://api.example.com")
    api_response = client.get("/status")
    info(f"Réponse API : {api_response}")

    # Vérifications
    assert normalized == "data"
    assert processed == "processed: data"
    assert api_response["status"] == "ok"

    success("Test E2E réussi.")
    return True

# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def main():
    try:
        result = run_e2e_test()
        if result:
            success("Pipeline complet validé.")
            sys.exit(0)
    except Exception:
        error("Le test E2E a échoué.")
        print(traceback.format_exc())
        sys.exit(1)

# ----------------------------------------------------------
if __name__ == "__main__":
    main()
