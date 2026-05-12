#!/bin/bash
source core/infra/logger.sh

REQUIRED_DIRS=(
  "core"
  "config"
  "assets"
  "docs"
  "tests"
)

log_info "Validation de la structure YnFOR..."

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        log_error "Dossier manquant : $dir"
        exit 1
    fi
done

log_info "Structure valide ✔️"
