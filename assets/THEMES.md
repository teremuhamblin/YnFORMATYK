###### THEMES.md >> markdown 
# YnFOR
>harte visuelle & palette globale
- Ce document définit le thème visuel global du dépôt YnFOR (UI, docs, schémas, badges, diagrams).

---

1. Palette principale

| Rôle            | Nom interne        | Couleur | Hex      | Usage principal                                  |
|-----------------|--------------------|---------|----------|--------------------------------------------------|
| Primaire        | yn-primary       | 🟦      | #2563EB| Actions clés, liens, boutons principaux          |
| Primaire foncé  | yn-primary-dark  | 🟦      | #1D4ED8| Hover, focus, états actifs                       |
| Primaire clair  | yn-primary-light | 🟦      | #DBEAFE| Fonds de sections, tags discrets                 |
| Secondaire      | yn-secondary     | 🟩      | #10B981| Statuts OK, succès, validations                   |
| Accent          | yn-accent        | 🟪      | #8B5CF6| Éléments mis en avant, badges, highlights        |
| Alerte          | yn-danger        | 🟥      | #EF4444| Erreurs, warnings critiques                      |
| Attention       | yn-warning       | 🟧      | #F59E0B| Warnings, états intermédiaires                   |
| Info            | yn-info          | 🟦      | #0EA5E9| Messages d’information, tooltips                 |

---

2. Neutres & fond

| Rôle            | Nom interne      | Hex      | Usage                                      |
|-----------------|------------------|----------|--------------------------------------------|
| Fond principal  | yn-bg          | #020617| Fond global sombre (docs, dashboards)      |
| Fond carte      | yn-surface     | #0F172A| Blocs, cartes, encadrés                    |
| Bordure         | yn-border      | #1E293B| Séparateurs, contours de composants        |
| Texte principal | yn-text        | #E5E7EB| Texte standard                             |
| Texte faible    | yn-text-muted  | #9CA3AF| Descriptions, métadonnées                  |
| Désactivé       | yn-disabled    | #4B5563| Boutons/états inactifs                     |

---

3. Typographie

- Police principale: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif
- Hiérarchie:
  - Titres (h1–h3): gras, tracking léger, couleur yn-text
  - Sous-titres (h4–h6): semi-gras, yn-text
  - Texte courant: normal, yn-text
  - Texte secondaire: normal, yn-text-muted, taille -1 niveau

---

4. Usage dans les fichiers Markdown

4.1. Badges & statuts

- Succès: utiliser yn-secondary  
- Erreur: utiliser yn-danger  
- Info: utiliser yn-info  
- Expérimental / beta: utiliser yn-accent

Exemple (avec shields.io) :

`md
!Status
!Stability
!Tests
`

---

5. Mini “graphique visuel” du dépôt

> Représentation conceptuelle des zones du dépôt et de leurs couleurs dominantes.

`text
[ Core Engine ]───────────────■ Primaire (#2563EB)
       │
       ├── [ Modules ]────────■ Accent (#8B5CF6)
       │        └─ Docs tech ─■ Texte (#E5E7EB) + Fond (#020617)
       │
       └── [ Interfaces ]────■ Secondaire (#10B981) + Info (#0EA5E9)

[ CI/CD ]─────────────────────■ Warning (#F59E0B) pour états intermédiaires
[ Monitoring ]───────────────■ Danger (#EF4444) pour erreurs
`

---

6. Règles rapides

- Max 2 couleurs fortes par écran/section (yn-primary + 1 autre).
- Fond sombre constant (yn-bg) pour tout ce qui est YnFOR.
- Ne jamais utiliser le rouge hors contexte d’erreur/critique.
- Accent violet réservé aux éléments vraiment importants (pas pour tout).

`

---
