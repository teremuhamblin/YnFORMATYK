# 📘 Guide d’utilisation — Test E2E YnFOR

Ce document explique comment utiliser le script E2E `run_e2e_test.py`, qui exécute un **test complet du pipeline YnFOR**.

---

# 1. 🎯 Objectif du test E2E

Le test E2E valide le flux complet :

1. L’utilisateur fournit une donnée brute  
2. `utils` la normalise  
3. `core` la traite  
4. `api` récupère une donnée externe (mockée)  
5. Le système assemble le résultat final  

Ce test garantit que **tout le système fonctionne ensemble**.

---

# 2. ▶️ Exécution du test

Depuis la racine du projet :

```bash
python3 tests/e2e/run_e2e_test.py
```

---

# 3. 🧪 Résultat attendu

Le script affiche :

- les étapes du pipeline  
- les valeurs intermédiaires  
- les résultats finaux  
- un résumé clair :  
  - ✔ Succès  
  - ❌ Échec  

---

# 4. 🛠 Options (à venir)

Le script pourra être étendu avec :

- `--verbose`  
- `--input "texte"`  
- `--mock-api off`  
- `--json-output`  

---

# 5. 📦 Structure interne du test

Le test E2E utilise :

- `normalize_text()`  
- `CoreEngine.process()`  
- `ApiClient.get()` (mocké)  

---

# 6. 🧩 Exemple de flux

Entrée : `"  DATA  "`  
Normalisation → `"data"`  
Traitement → `"processed: data"`  
API → `{"status": "ok"}`  
Résultat final → OK

---

# © YnFOR — Documentation E2E Officielle
