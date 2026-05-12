#!/bin/bash
source core/infra/logger.sh

MODULE_DIR="modules"
REGISTRY="core/infra/module-registry.json"

log_info "Chargement des modules YnFOR..."

if [ ! -d "$MODULE_DIR" ]; then
    log_warn "Aucun dossier modules/ trouvé"
    exit 0
fi

for module in $MODULE_DIR/*; do
    if [ -d "$module" ]; then
        name=$(basename "$module")
        log_info "Module détecté : $name"

        if [ -f "$module/init.sh" ]; then
            source "$module/init.sh"
            log_info "Module $name chargé ✔️"
        else
            log_warn "init.sh manquant pour $name"
        fi
    fi
done
