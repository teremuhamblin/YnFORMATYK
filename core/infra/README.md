###### core/infra/README.md >> markdown 
# 📄🧩 YnFOR
>infraCORE

Le dossier core/infra/ contient le noyau interne du framework YnFOR.  
Il regroupe les composants essentiels permettant d’assurer la cohérence, la stabilité et le chargement dynamique du système.

InfraCORE fournit quatre briques fondamentales :

- Logger — système de logs standardisé  
- Validator — vérification de la structure du projet  
- Loader — détection et chargement automatique des modules  
- Runtime — point d’entrée interne orchestrant l’infrastructure  

---

📁 Structure

`
core/infra/
 ├── logger.sh            # Gestion des logs YnFOR
 ├── validator.sh         # Validation de la structure du projet
 ├── loader.sh            # Chargement automatique des modules
 ├── runtime.sh           # Orchestration interne YnFOR
 └── module-registry.json # Registre des modules détectés
`

---

⚙️ Composants

1. logger.sh
Fournit un système de logs uniforme :

- [INFO] — informations générales  
- [WARN] — avertissements  
- [ERROR] — erreurs critiques  

Chaque message inclut un timestamp pour faciliter le suivi.

---

2. validator.sh
Vérifie que la structure minimale du projet YnFOR est présente :

- core/
- config/
- assets/
- docs/
- tests/

En cas de dossier manquant, le script renvoie une erreur explicite.

---

3. loader.sh
Détecte automatiquement les modules présents dans modules/ et charge leurs fichiers init.sh si disponibles.

Chaque module chargé est enregistré dans module-registry.json.

---

4. runtime.sh
Point d’entrée interne :

1. Valide la structure  
2. Charge les modules  
3. Initialise l’environnement YnFOR  

Il sert de base à toute exécution interne ou automatisée.

---

🧪 Intégration CI/CD

Le workflow GitHub ynfor-infra.yml utilise directement les scripts :

- Validation de la structure  
- Chargement des modules  
- Exécution du runtime  

Cela garantit que chaque push respecte les standards YnFOR.

---

🚀 Objectif d’InfraCORE

InfraCORE transforme YnFOR en un framework :

- Modulaire
- Auto‑organisé
- Scalable
- Facile à maintenir
- Prêt pour des extensions et plugins

Il constitue la fondation technique du projet.

---

📌 Version

InfraCORE v1.0  
Compatible avec YnFOR v1.x
`

---
