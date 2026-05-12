#!/bin/bash
source core/infra/logger.sh
cd "$(git rev-parse --show-toplevel)"

REQUIRED_DIRS=(
  "core"
  "assets"
  "docs"
  "tests"
)

OPTIONAL_DIRS=(
  "config"
)

for dir in "${REQUIRED_DIRS[@]}"; do
  if [ ! -d "$dir" ]; then
    log_error "Dossier manquant : $dir"
    exit 1
  fi
done

for opt in "${OPTIONAL_DIRS[@]}"; do
  if [ ! -d "$opt" ]; then
    log_warn "Dossier optionnel manquant : $opt"
  fi
done
