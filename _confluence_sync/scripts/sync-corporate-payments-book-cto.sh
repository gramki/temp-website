#!/bin/bash
# Sync us-bank-commercial-card/corporate-payments-book to Confluence CTO space.
# Usage: bash _confluence_sync/scripts/sync-corporate-payments-book-cto.sh [--force-update]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFLUENCE_SYNC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$CONFLUENCE_SYNC_DIR" || exit 1
exec python3 run-sync-with-env.py --destination corporate-payments-book-cto "$@"
