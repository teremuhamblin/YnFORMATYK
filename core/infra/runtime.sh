#!/bin/bash
source core/infra/logger.sh
source core/infra/validator.sh
source core/infra/loader.sh

log_info "Initialisation YnFOR Runtime..."

# 1) Validation
./core/infra/validator.sh

# 2) Chargement des modules
./core/infra/loader.sh

log_info "YnFOR Runtime opérationnel ✔️"
