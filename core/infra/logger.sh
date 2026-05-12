#!/bin/bash

timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

log_info() {
    echo "[INFO]  ($(timestamp)) $1"
}

log_warn() {
    echo "[WARN]  ($(timestamp)) $1"
}

log_error() {
    echo "[ERROR] ($(timestamp)) $1"
}
