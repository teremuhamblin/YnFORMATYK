# 🔄 Tests End‑to‑End (E2E) — YnFOR

Le dossier `e2e/` contient les **tests de bout en bout** du projet YnFOR.  
Contrairement aux tests unitaires ou d’intégration, les tests E2E simulent un **scénario utilisateur complet**, en enchaînant toutes les étapes du pipeline :

```
Entrée utilisateur → Utils → Core → API → Résultat final
```

---

## 🎯 Objectifs
- Vérifier le fonctionnement global du système YnFOR  
- Tester un flux complet du début à la fin  
- Simuler un comportement utilisateur réel  
- Détecter les erreurs de cohérence entre modules  
- Garantir la stabilité du pipeline complet  

---

## 📁 Contenu du dossier

```
e2e/
 ├─ README.md
 ├─ UTILISATION.md
 └─ run_e2e_test.py
```

---

## ▶️ Exécution rapide

```bash
python3 tests/e2e/run_e2e_test.py
```

---

## 📄 Licence
Projet YnFOR — MIT Licence.
