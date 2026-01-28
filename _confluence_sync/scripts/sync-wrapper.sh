#!/bin/bash
# Envelope/wrapper script for Confluence sync
# Ensures virtual environment is set up with all requirements before running sync

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# Go to _confluence_sync directory (parent of scripts/)
CONFLUENCE_SYNC_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
# Go to repo root (parent of _confluence_sync)
REPO_ROOT="$(cd "$CONFLUENCE_SYNC_DIR/.." && pwd)"

cd "$REPO_ROOT" || exit 1

VENV_DIR="$CONFLUENCE_SYNC_DIR/scripts/venv"
DATA_DIR="$CONFLUENCE_SYNC_DIR/data"
REQUIREMENTS_FILE="$CONFLUENCE_SYNC_DIR/requirements.txt"
ENV_FILE="$DATA_DIR/.env"

# Function to setup virtual environment
setup_venv() {
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
    fi
    
    echo "Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
    
    # Use python -m pip to ensure we're using the venv's pip
    PYTHON="$VENV_DIR/bin/python"
    if [ ! -f "$PYTHON" ]; then
        PYTHON="python3"
    fi
    
    echo "Upgrading pip..."
    "$PYTHON" -m pip install --upgrade pip --quiet 2>/dev/null || "$PYTHON" -m ensurepip --upgrade 2>/dev/null || true
    
    if [ -f "$REQUIREMENTS_FILE" ]; then
        echo "Installing/updating requirements..."
        "$PYTHON" -m pip install -r "$REQUIREMENTS_FILE" --quiet
        echo "✓ Virtual environment ready"
    else
        echo "⚠ Warning: requirements.txt not found at $REQUIREMENTS_FILE"
    fi
}

# Function to check for .env file
check_env() {
    if [ ! -f "$ENV_FILE" ]; then
        echo "⚠ Warning: .env file not found at $ENV_FILE"
        echo "  Create it with: echo 'CONFLUENCE_TOKEN=your-token' > $ENV_FILE"
        echo "  Or set CONFLUENCE_TOKEN environment variable"
    else
        # Load environment variables from .env
        export $(grep -v '^#' "$ENV_FILE" | grep -v '^$' | xargs)
    fi
}

# Setup virtual environment
setup_venv

# Check for .env file
check_env

# Run the sync script with all arguments passed through
# Use the venv's python if available, otherwise use system python
if [ -f "$VENV_DIR/bin/python" ]; then
    "$VENV_DIR/bin/python" "$CONFLUENCE_SYNC_DIR/scripts/sync-to-confluence.py" "$@"
else
    python3 "$CONFLUENCE_SYNC_DIR/scripts/sync-to-confluence.py" "$@"
fi
