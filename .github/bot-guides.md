# 🤖 YnFOR Bot — Guide

## Présentation

**YnFOR Bot** est le bot officiel du projet **YnFOR**.  
Il agit comme un assistant automatique pour :

- générer des fichiers (docs, manifests, templates)
- maintenir la cohérence du système de plugins
- automatiser certaines tâches répétitives

---

## Rôle dans le dépôt

- Créer / mettre à jour :
  - fichiers de documentation
  - manifests de plugins
  - templates de nouveaux modules
- Vérifier :
  - structure des dossiers
  - présence des fichiers clés
  - cohérence des versions

---

## Apparition dans les contributions

YnFOR Bot apparaît dans :

- l’onglet **Contributors** (si tu pushes des commits avec son identité)
- l’historique des commits
- les PR automatiques (si tu en crées via script ou GitHub App)

---

## Identité Git

Pour que le bot apparaisse comme contributeur, configure son identité Git :

```bash
git config user.name "ynfor-bot"
git config user.email "bot@ynfor.local"
