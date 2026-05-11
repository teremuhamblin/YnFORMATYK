===========================
Troubleshooting — YnFOR
===========================

Ce guide aide à diagnostiquer et résoudre les problèmes courants
rencontrés lors de l’utilisation de YnFOR.

-------------------------
1. Le projet ne démarre pas
-------------------------

Vérifier les points suivants :

- Le fichier ``.env`` est présent et complet
- Les dépendances sont installées
- La version de Python/Node est compatible
- Les permissions des fichiers sont correctes

Commande utile ::

    ynfor status

-------------------------
2. Erreurs API
-------------------------

Causes possibles :

- Mauvaise clé API
- Service externe indisponible
- Problème réseau

Vérifier le fichier ``.env`` ::

    API_KEY=xxxx

-------------------------
3. Problèmes Docker
-------------------------

Conteneur qui ne démarre pas ::

    docker logs ynfor

Reconstruction forcée ::

    docker build --no-cache -t ynfor .

-------------------------
4. Logs & Diagnostic
-------------------------

Les logs se trouvent dans ::

    logs/app.log

Pour un diagnostic avancé ::

    ynfor --debug

-------------------------
5. Support
-------------------------

Si le problème persiste :

- Ouvrir une *Issue* GitHub
- Fournir les logs
- Décrire les étapes pour reproduire
