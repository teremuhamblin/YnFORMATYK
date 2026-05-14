# Mise à jour ;
- Marketplace interne (v6.1 → v6.3)  
- Hot‑Reload Plugins (v6.4 → v6.6)  
- Permissions Plugins (v6.7 → v6.9)  

🎯 Milestone — v6.1 → v6.9 — Plugin System NG+ (Marketplace, Hot‑Reload, Permissions)

`md

🧩 Milestone v6.1 → v6.9 — Plugin System NG+

🎯 Objectif global
Étendre le système de plugins YnFOR avec :
- Marketplace interne (installation, mise à jour, découverte)
- Hot‑Reload des plugins sans redémarrage
- Permissions avancées (sandbox, accès contrôlé, capabilities)

---

🗂️ Versions incluses
- v6.1 — Base Marketplace
- v6.2 — Catalogue dynamique
- v6.3 — Installation & Update Engine
- v6.4 — Hot‑Reload Kernel
- v6.5 — Watcher temps réel
- v6.6 — Reload sélectif par plugin
- v6.7 — Permissions de base
- v6.8 — Capabilities avancées
- v6.9 — Sandbox & Security Layer

---

✅ Tâches (toutes complétées)

🛒 Marketplace interne
- [x] Création du dossier /marketplace
- [x] Format standardisé des plugins distants (plugin.pkg.json)
- [x] Catalogue dynamique (local + distant)
- [x] Commande d’installation automatique
- [x] Commande de mise à jour
- [x] Vérification de compatibilité version YnFOR
- [x] Vérification de signature (v6.3)

🔥 Hot‑Reload Plugins
- [x] Ajout du FileSystemWatcher
- [x] Détection des modifications de fichiers plugin
- [x] Déchargement propre du plugin
- [x] Rechargement dynamique sans redémarrage
- [x] Reload sélectif (plugin seul)
- [x] Reload global (tous les plugins)
- [x] Logs détaillés du rechargement

🔐 Permissions Plugins
- [x] Système de permissions déclaratives (permissions.json)
- [x] Capabilities : filesystem, network, telemetry, hooks
- [x] Vérification au chargement
- [x] Refus automatique si permission manquante
- [x] Sandbox d’exécution (v6.9)
- [x] Logs de sécurité
- [x] Documentation complète

---

📅 Statut
Milestone terminé — versions v6.1 → v6.9 livrées
`

---

🐞 Issue — Implémentation complète Marketplace + Hot‑Reload + Permissions (v6.1 → v6.9)

`md

🐞 Issue — Implémentation Marketplace + Hot‑Reload + Permissions (v6.1 → v6.9)

🎯 Description
Étendre le Plugin System YnFOR avec :
- Marketplace interne
- Hot‑Reload dynamique
- Permissions avancées & sandbox

---

📦 Détails techniques

🛒 Marketplace interne
- [x] Création du module marketplace/
- [x] Format plugin.pkg.json
- [x] Catalogue local + distant
- [x] Installation automatique (download → extract → register)
- [x] Moteur de mise à jour
- [x] Vérification de compatibilité version
- [x] Vérification de signature (SHA256)

🔥 Hot‑Reload
- [x] Ajout du watcher (inotify / watchdog)
- [x] Détection des modifications plugin
- [x] Déchargement propre (stop → unload)
- [x] Rechargement dynamique (load → init → start)
- [x] Reload sélectif
- [x] Reload global
- [x] Logs enrichis

🔐 Permissions Plugins
- [x] Fichier permissions.json
- [x] Capabilities :  
  - [x] filesystem  
  - [x] network  
  - [x] telemetry  
  - [x] hooks  
- [x] Vérification au chargement
- [x] Refus si permission manquante
- [x] Sandbox d’exécution (limitation API)
- [x] Logs de sécurité

---

🧪 Tests
- [x] Test installation plugin
- [x] Test mise à jour plugin
- [x] Test hot‑reload simple
- [x] Test hot‑reload multiple
- [x] Test permissions OK
- [x] Test permissions refusées
- [x] Test sandbox

---

🏁 Résultat
Le Plugin System NG+ est opérationnel, sécurisé, extensible et dynamique.

---

🔒 Statut
Issue fermée — livré en v6.9
`

---

🚀 Release — YnFOR v6.1 → v6.9 — Plugin System NG+

`md

🚀 Release — YnFOR v6.1 → v6.9 — Plugin System NG+

🧩 Aperçu global
Cette release étend le Plugin System YnFOR avec :
- Marketplace interne
- Hot‑Reload dynamique
- Permissions avancées & sandbox

---

🛒 Marketplace interne (v6.1 → v6.3)
- [x] Catalogue dynamique
- [x] Installation automatique
- [x] Moteur de mise à jour
- [x] Vérification de compatibilité
- [x] Vérification de signature
- [x] Format plugin.pkg.json

---

🔥 Hot‑Reload Plugins (v6.4 → v6.6)
- [x] Watcher temps réel
- [x] Détection des modifications
- [x] Déchargement propre
- [x] Rechargement dynamique
- [x] Reload sélectif
- [x] Reload global
- [x] Logs enrichis

---

🔐 Permissions & Sandbox (v6.7 → v6.9)
- [x] Permissions déclaratives
- [x] Capabilities avancées
- [x] Vérification stricte au chargement
- [x] Sandbox d’exécution
- [x] Logs de sécurité
- [x] Documentation complète

---

📁 Structure ajoutée
`
marketplace/
   catalog.json
   installer.py
   updater.py

plugins/
   permissions.json

core/
   hot_reload.py
   security_layer.py
`

---

🏁 Statut
Versions v6.1 → v6.9 publiées — Plugin System NG+ complet
`

---
