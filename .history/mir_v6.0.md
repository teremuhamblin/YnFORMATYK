🎯 Milestone — v6.0.0 — Plugin System Avancé
`md

🧩 Milestone v6.0.0 — Plugin System Avancé

🎯 Objectif global
Introduire un système de plugins modulaire, dynamique et extensible pour YnFOR, incluant :
- Plugin Kernel NG
- Hooks intelligents
- Modules dynamiques
- Exemple de plugin core

---

✅ Tâches (toutes complétées)

- [x] Création du noyau PluginKernel (découverte, chargement, cycle de vie)
- [x] Ajout du système de hooks (prerun, postrun, on_error)
- [x] Mise en place de l’arborescence /plugins/core, /community, /external
- [x] Support des manifests plugin.json
- [x] Exemple de plugin fonctionnel : examplecoreplugin
- [x] Intégration des hooks dans core/app.py
- [x] Ajout du fichier plugins.yml pour la configuration
- [x] Mise à jour de la documentation (README, CHANGELOG, ROADMAP)
- [x] Stabilisation et tests de base

---

📅 Statut
Milestone terminé — version v6.0.0 publiée
`

---

🐞 Issue — Implémentation complète du Plugin System v6.0
`md

🐞 Issue — Implémentation du Plugin System v6.0

🎯 Description
Développer et intégrer le système de plugins avancé pour YnFOR, incluant :
- Plugin Kernel NG
- Hooks intelligents
- Exemple de plugin
- Configuration centralisée
- Documentation complète

---

📦 Détails techniques

🔧 Plugin Kernel
- [x] Découverte automatique des plugins
- [x] Chargement dynamique via importlib
- [x] Cycle de vie complet (init, start, stop)
- [x] Gestion des manifests JSON
- [x] Support multi‑scopes (core, community, external)

🪝 Hooks intelligents
- [x] HookBus centralisé
- [x] Événements : prerun, postrun, on_error
- [x] Enregistrement automatique des handlers exposés par les plugins
- [x] Emission d’événements depuis core/app.py

🧩 Exemple plugin
- [x] Plugin examplecoreplugin
- [x] Manifest complet (plugin.json)
- [x] Implémentation des hooks
- [x] Logs intégrés

⚙️ Configuration
- [x] Fichier config/plugins.yml
- [x] Activation/désactivation des scopes
- [x] Support futur pour plugins désactivés

📘 Documentation
- [x] Mise à jour du README
- [x] Ajout du CHANGELOG v6.0
- [x] Mise à jour de la ROADMAP

---

🏁 Résultat
Le système de plugins v6.0 est fonctionnel, stable et extensible.

---

🔒 Statut
Issue fermée — livré en v6.0.0
`

---

🚀 Release — YnFOR v6.0.0 — Plugin System Avancé
`md

🚀 Release — YnFOR v6.0.0 — Plugin System Avancé

🧩 Nouveautés principales
YnFOR v6 introduit un système de plugins complet, modulaire et extensible.

🔧 Plugin Kernel NG
- [x] Découverte automatique des plugins
- [x] Chargement dynamique
- [x] Cycle de vie complet (init, start, stop)
- [x] Gestion des manifests plugin.json
- [x] Support multi‑scopes : core, community, external

🪝 Hooks intelligents
- [x] HookBus centralisé
- [x] Hooks : prerun, postrun, on_error
- [x] Enregistrement automatique des handlers
- [x] Intégration dans core/app.py

🧩 Exemple plugin
- [x] Plugin examplecoreplugin
- [x] Implémentation des hooks
- [x] Logs intégrés
- [x] Manifest complet

⚙️ Configuration
- [x] Ajout de config/plugins.yml
- [x] Activation/désactivation des scopes
- [x] Préparation pour plugins désactivés

📘 Documentation
- [x] README mis à jour
- [x] CHANGELOG v6.0 ajouté
- [x] ROADMAP mise à jour

---

📁 Structure livrée
`
core/
plugins/
hooks/
config/
logs/
README.md
CHANGELOG.md
ROADMAP.md
`

---

🏁 Statut
Version stable publiée — YnFOR v6.0.0
`

---
