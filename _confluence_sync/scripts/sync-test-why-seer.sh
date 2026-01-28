#!/bin/bash
# Helper script to sync the test-why-seer destination (small test with why-seer folder only)

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# Go to _confluence_sync directory (parent of scripts/)
CONFLUENCE_SYNC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# Go to repo root (parent of _confluence_sync)
REPO_ROOT="$(cd "$CONFLUENCE_SYNC_DIR/.." && pwd)"

cd "$REPO_ROOT" || exit 1

# Call the wrapper script
bash "$CONFLUENCE_SYNC_DIR/scripts/sync-wrapper.sh" --destination test-why-seer "$@"
