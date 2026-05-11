# 🔗 Tests d’Intégration — YnFOR

Le dossier `integration/` contient les **tests d’intégration** du projet YnFOR.  
Contrairement aux tests unitaires, ils vérifient le **fonctionnement global** entre plusieurs modules :  
- Core ↔ Utils  
- API ↔ Core  
- API ↔ Utils  
- Pipeline complet YnFOR  

---

## 🎯 Objectifs
- Vérifier que les modules fonctionnent ensemble  
- Tester les flux réels (end-to-end)  
- Détecter les erreurs d’intégration  
- Garantir la stabilité du système complet  

---

## 📁 Structure recommandée

```
tests/
 └─ integration/
      ├─ test_flow_core_api.md
      ├─ test_utils_core.md
      ├─ test_full_pipeline.md
      ├─ test_flow_core_api.py
      ├─ test_utils_core.py
      ├─ test_full_pipeline.py
      └─ README.md
```

---

## ▶️ Exécuter les tests d’intégration

```bash
pytest tests/integration -vv
```

Ou via un fichier spécifique :

```bash
pytest tests/integration/test_full_pipeline.py -vv
```

---

## 🧩 Bonnes pratiques YnFOR
- Tester les **flux complets**, pas les détails internes  
- Utiliser des **mocks** pour les appels API  
- Garder les tests lisibles et courts  
- Toujours tester les cas normaux + cas limites  

---

## 📄 Licence
Projet YnFOR — MIT Licence.
