===========================
Bonnes Pratiques — YnFOR
===========================

Ce document regroupe les bonnes pratiques recommandées pour maintenir
un projet YnFOR propre, stable et professionnel.

-------------------------
1. Qualité du Code
-------------------------

- Code modulaire et lisible
- Fonctions courtes et cohérentes
- Commentaires uniquement lorsque nécessaire
- Respect des conventions internes

-------------------------
2. Sécurité
-------------------------

- Ne jamais stocker de secrets dans le code
- Utiliser des variables d’environnement
- Mettre à jour les dépendances
- Vérifier les permissions des fichiers sensibles

-------------------------
3. Documentation
-------------------------

- Toujours documenter les nouvelles fonctionnalités
- Garder la documentation à jour
- Utiliser un style clair et concis
- Ajouter des exemples lorsque pertinent

-------------------------
4. Conventions Git
-------------------------

Branches recommandées ::

    main
    dev
    feature/<nom>
    fix/<nom>

Commits : utiliser *Conventional Commits* ::

    feat: ajout d'une nouvelle fonctionnalité
    fix: correction d’un bug
    docs: mise à jour documentation

-------------------------
5. Tests
-------------------------

- Ajouter des tests unitaires pour chaque module
- Tester les cas limites
- Automatiser les tests via GitHub Actions
