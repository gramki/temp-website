#!/bin/bash
# Helper script to sync olympus-hub-docs to Confluence
# Uses the sync-wrapper.sh to ensure venv is set up

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$SCRIPT_DIR/sync-wrapper.sh" --destination hub-docs "$@"
