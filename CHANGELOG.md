# 📝 CHANGELOG — YnFOR (v1.0 → v6.0)
Toutes les évolutions majeures du framework YnFOR, regroupées dans un changelog clair, moderne et percutant.

---

# 🔰 v1.x — Fondation & Mise en place
## ⭐ v1.0 — Initialisation du projet
- [x] Création du dépôt YnFOR  
- [x] Mise en place de l’arborescence initiale (`core/`, `assets/`, `docs/`, `tests/`)  
- [x] Ajout des premiers scripts internes  
- [x] Documentation initiale (README, STRUCTURE.md v1)  

## ⭐ v1.5 — Organisation & Cohérence
- [x] Réorganisation complète de la structure  
- [x] Ajout des conventions internes  
- [x] Documentation enrichie  
- [x] Préparation du futur InfraCORE  

---

# ⚙️ v2.x — Modularité & Pipeline interne
## ⭐ v2.0 — Système de modules
- [x] Création du dossier `modules/`  
- [x] Standardisation des modules (`init.sh`, `config`, `hooks`)  
- [x] Ajout des premiers modules internes  
- [x] Tests unitaires basiques  

## ⭐ v2.5 — Pipeline interne
- [x] Ajout d’un pipeline interne pré‑InfraCORE  
- [x] Normalisation des logs internes  
- [x] Ajout des tests E2E (Python)  
- [x] Préparation du runtime interne  

---

# 🧬 v3.x — InfraCORE & Automatisation CI/CD
## ⭐ v3.0 — Naissance d’InfraCORE
- [x] Création du dossier `core/infra/`  
- [x] Ajout du logger standardisé  
- [x] Ajout du validator (structure stricte)  
- [x] Ajout du loader (modules auto‑détectés)  
- [x] Ajout du runtime YnFOR  
- [x] Ajout du fichier `module-registry.json`  
- [x] Ajout du dossier `config/` + `ynfor.conf`  

## ⭐ v3.5 — CI/CD & GitHub Actions
- [x] Ajout du workflow InfraCORE (validator → loader → runtime)  
- [x] Correction automatique via Autofix GitHub  
- [x] Mise à jour des permissions GitHub Actions  
- [x] Compatibilité Node.js 24  
- [x] Nettoyage YAML & optimisation des steps  

---

# 🛡️ v4.x — Sécurité & Analyse statique
## ⭐ v4.0 — CodeQL avancé
- [x] Ajout du workflow CodeQL personnalisé  
- [x] Désactivation du Default Setup CodeQL  
- [x] Scan ciblé sur `actions`  
- [x] Suppression des faux positifs Python  
- [x] Compatibilité CodeQL 2026+  
- [x] Résolution des warnings de configuration  

## ⭐ v4.5 — Stabilisation & Qualité
- [x] Correction des erreurs structurelles détectées par la CI  
- [x] Harmonisation des logs (INFO / STEP / OK / ERROR)  
- [x] Documentation InfraCORE mise à jour  
- [x] STRUCTURE.md v2  
- [x] ROADMAP.md v2  

---

# 🚀 v5.x — Hyper‑Automatisation & Maturité
## ⭐ v5.0 — Release majeure
- [x] Stabilisation complète d’InfraCORE  
- [x] CI/CD 100% automatisée  
- [x] CodeQL 100% propre  
- [x] Workflows modernisés (Node 24, actions v4 ready)  
- [x] Documentation complète (README, STRUCTURE, ROADMAP)  
- [x] Release v5.0 publiée  
- [x] Milestone v3.0 → v5.0 complétée  
- [x] Issue globale fermée  

---

# 🚀 v6.x — Hyper‑Automatisation & Maturité
## ⭐ v6.0 — Mise à jour majeure
- Ajout du Plugin Kernel (découverte, chargement, cycle de vie)
- Support des dossiers `plugins/core`, `plugins/community`, `plugins/external`
- Système de hooks de base (`pre_run`, `post_run`, `on_error`)
- Exemple de plugin core : `example_core_plugin`

# 🏁 Résumé global
YnFOR a évolué d’un simple squelette (v1.0) à un framework **modulaire, automatisé, sécurisé et professionnel** (v6.0).  
La base est solide, la CI est propre, l’infra est stable, et le projet est prêt pour les versions avancées (v7+).
