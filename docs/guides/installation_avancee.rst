===============================
Installation Avancée — YnFOR
===============================

Ce guide décrit les méthodes d’installation avancées pour déployer YnFOR
dans un environnement professionnel ou de production.

-----------------------
1. Installation Docker
-----------------------

YnFOR peut être exécuté dans un conteneur Docker pour garantir
portabilité, isolation et reproductibilité.

Construction de l’image ::

    docker build -t ynfor .

Exécution du conteneur ::

    docker run -d -p 8080:8080 --name ynfor ynfor

-------------------------
2. Reverse Proxy (Nginx)
-------------------------

Pour une mise en production, il est recommandé d’utiliser un reverse proxy.

Exemple de configuration Nginx ::

    server {
        listen 80;
        server_name ynfor.example.com;

        location / {
            proxy_pass http://localhost:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }

-------------------------
3. Variables d’environnement
-------------------------

Créer un fichier ``.env`` à la racine ::

    ENV=production
    API_KEY=xxxx
    LOG_LEVEL=INFO

-------------------------
4. Monitoring & Logs
-------------------------

Pour un suivi avancé :

- Grafana
- Prometheus
- Loki
- ELK Stack

Les logs YnFOR se trouvent dans ::

    logs/app.log

-------------------------
5. Sécurisation
-------------------------

- Utiliser HTTPS (Let’s Encrypt)
- Restreindre les accès SSH
- Mettre à jour régulièrement les dépendances
- Activer les audits de sécurité
