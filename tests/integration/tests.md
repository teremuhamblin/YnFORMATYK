# 🔗 Tests d’Intégration — Documentation Complète YnFOR

Ce document regroupe l’ensemble des **tests d’intégration** du projet YnFOR.  
Il explique les objectifs, les flux testés, les scripts Python associés et la logique de chaque scénario.

Les tests d’intégration valident le **fonctionnement global** entre plusieurs modules du système :

- Utils ↔ Core  
- Core ↔ API  
- Pipeline complet (Utils → Core → API)

---

# 📁 Structure des tests

```
tests/
 └─ integration/
      ├─ test_utils_core.py
      ├─ test_flow_core_api.py
      ├─ test_full_pipeline.py
      └─ tests.md
```

---

# 1. 🧩 Test d’intégration : Utils + Core  
Fichier : `test_utils_core.py`

## 🎯 Objectif
Vérifier que les fonctions utilitaires (`utils`) fournissent des données correctes au moteur principal (`core`).

## 🔍 Flux testé
1. Normalisation d’un texte via `normalize_text()`
2. Traitement du texte normalisé via `CoreEngine.process()`
3. Vérification du résultat final

## 🐍 Script Python

```python
from src.utils import normalize_text
from src.core import CoreEngine

def test_utils_core_flow():
    engine = CoreEngine()
    text = "  Hello World  "
    normalized = normalize_text(text)
    result = engine.process(normalized)

    assert result == "processed: hello world"
```

## ✔ Résultat attendu
- Le texte est normalisé → `"hello world"`
- Le moteur Core le traite → `"processed: hello world"`

---

# 2. 🔗 Test d’intégration : Core + API  
Fichier : `test_flow_core_api.py`

## 🎯 Objectif
Valider l’interaction entre :
- le moteur Core (`CoreEngine`)
- le client API (`ApiClient`)

## 🔍 Flux testé
1. Traitement d’une donnée via CoreEngine  
2. Appel API simulé (mock)  
3. Vérification de la cohérence du flux global  

## 🐍 Script Python

```python
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

## ✔ Résultat attendu
- Le moteur Core traite `"input"`  
- L’API renvoie un JSON simulé  
- Le flux complet fonctionne sans erreur  

---

# 3. 🔄 Test d’intégration : Pipeline complet YnFOR  
Fichier : `test_full_pipeline.py`

## 🎯 Objectif
Tester **tout le pipeline YnFOR** :

```
Utils → Core → API
```

## 🔍 Flux testé
1. Normalisation du texte  
2. Traitement via CoreEngine  
3. Appel API mocké  
4. Vérification de la cohérence globale  

## 🐍 Script Python

```python
from src.utils import normalize_text
from src.core import CoreEngine
from src.api import ApiClient

def test_full_pipeline(monkeypatch):
    class MockResponse:
        def json(self):
            return {"status": "ok"}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import src.api.requests
    src.api.requests.get = mock_get

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

## ✔ Résultat attendu
- Normalisation → `"data"`
- Traitement → `"processed: data"`
- API → `{"status": "ok"}`

---

# ▶️ Exécution des tests

### Tous les tests d’intégration

```bash
pytest tests/integration -vv
```

### Test spécifique

```bash
pytest tests/integration/test_full_pipeline.py -vv
```

---

# 🧠 Conclusion

Ces tests d’intégration garantissent que :

- les modules YnFOR fonctionnent ensemble  
- les flux complets sont cohérents  
- les interactions API sont correctement gérées  
- le système est stable et évolutif  

Ils constituent une base solide pour la qualité du projet YnFOR.

---

# © YnFOR — Tests d’Intégration Officiels
