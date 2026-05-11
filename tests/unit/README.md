# 🧪 Tests Unitaires — YnFOR

Le dossier `unit/` contient l’ensemble des **tests unitaires** du projet YnFOR.  
Ils permettent de vérifier le bon fonctionnement des fonctions, classes et modules de manière isolée.

---

## 🎯 Objectifs
- Garantir la stabilité du code  
- Détecter rapidement les régressions  
- Valider le comportement attendu des modules  
- Assurer une base solide pour les évolutions futures  

---

## 📁 Structure recommandée

```
tests/
 └─ unit/
     ├─ test_core.md
     ├─ test_core.py
     ├─ test_utils.md
     ├─ test_utils.py
     ├─ test_core.md
     ├─ test_core.py
     └─ README.md
```

---

## ▶️ Exécuter les tests

Depuis la racine du projet :

```bash
pytest tests/unit -vv
```

Pour exécuter un fichier spécifique :

```bash
pytest tests/unit/test_core.py -vv
```

---

## 🧩 Bonnes pratiques YnFOR
- Un fichier de test par module  
- Des noms explicites : `test_<fonction>.py`  
- Des tests courts, isolés et reproductibles  
- Utiliser `pytest` pour sa simplicité et sa lisibilité  
- Toujours valider les cas normaux + cas limites  

---

## 📄 Licence
Projet YnFOR — MIT Licence.
