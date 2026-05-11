###### docs/api/index.md >> markdown 
# 📡 API 
>YnFOR
### Documentation Officielle
Bienvenue dans la documentation API du projet YnFOR.  
- Cette section décrit les endpoints disponibles, les formats supportés, les méthodes d’authentification et les bonnes pratiques d’intégration.

---

### 🧭 Objectifs de l’API
```md
- Fournir une interface simple et cohérente  
- Permettre l’intégration avec des services externes  
- Offrir un accès sécurisé aux fonctionnalités internes  
- Garantir stabilité, performance et évolutivité
```

---

### 🔐 Authentification
L’API YnFOR utilise une authentification par token.
>Exemple d’en‑tête HTTP
```http
Authorization: Bearer VOTRETOKENAPI
Content-Type: application/json
```
>Les tokens doivent être définis dans votre fichier .env :
```text
API_KEY=xxxx
```

---

### 📍 Endpoints disponibles
1. GET /status
>Retourne l’état du système.
- Réponse :
```json
{
  "status": "online",
  "version": "1.0.0",
  "uptime": "12345s"
}
```

---

2. POST /process
>Lance un traitement interne.
- Exemple de requête :
```json
{
  "input": "données à traiter"
}
```

Réponse :
```json
{
  "success": true,
  "result": "résultat du traitement"
}
```

---

3. GET /logs (optionnel)
>Retourne les logs récents (si activé).

---

### 📦 Formats supportés
- JSON (par défaut)  
- XML (optionnel selon configuration)  

---

### 🧪 Exemples d’utilisation
>cURL
```bash
curl -X POST https://api.ynfor.com/process \
  -H "Authorization: Bearer VOTRETOKENAPI" \
  -H "Content-Type: application/json" \
  -d '{"input": "test"}'
```

>JavaScript (fetch)
```javascript
fetch("https://api.ynfor.com/process", {
  method: "POST",
  headers: {
    "Authorization": "Bearer VOTRETOKENAPI",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ input: "test" })
});
```

---

### 🛡️ Sécurité API
- Utiliser HTTPS  
- Ne jamais exposer votre token  
- Régénérer les clés en cas de doute  
- Limiter les accès par IP (optionnel)  

---

### 🧭 Roadmap API
- Ajout d’un endpoint /metrics  
- Ajout d’un endpoint /tasks  
- Versioning API (v1, v2…)  
- Documentation OpenAPI (Swagger)  

---

### 🤝 Contribution
>Les contributions à l’API suivent les règles définies dans :
- .github/CONTRIBUTING.md  
- .github/CODEOFCONDUCT.md  

---

### 📄 Licence
Voir le fichier LICENSE à la racine du projet.

---

#### 🧬 Vision API YnFOR
###### L’API YnFOR vise à devenir une interface robuste, sécurisée et extensible, permettant l’intégration fluide de services internes et externes, tout en respectant les standards modernes de développement.

---
