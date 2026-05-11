###### STRUCTURE.md >> markdown 
>Organisation du projet YnFOR
# Structure 
## 1. Racine du projet
```md
- `README.md` — Présentation générale
- `STRUCTURES.md` — Structure interne
- `ROADMAP.md` — Plan d’évolution
- `CHANGELOG.md` — Historique des versions
```

## 2. Dossier `.github/`
Contient tout ce qui concerne la gestion du projet :

### ISSUE_TEMPLATE/
- `bug_report.md` — Template pour signaler un bug
- `feature_request.md` — Template pour proposer une amélioration

### workflows/
- `ci.yml` — Workflow CI simple pour valider les commits

### CODEOWNERS
Définit les responsables du code.

### PULL_REQUEST_TEMPLATE.md
Standardise les PR pour garder un projet propre.

## 3. Structure visuelle :
```text
YnFOR/
├── README.md
├── STRUCTURES.md
├── ROADMAP.md
├── CHANGELOG.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    ├── PULL_REQUEST_TEMPLATE.md
    ├── workflows/
    │   └── ci.yml
    └── CODEOWNERS
```
