# Confluence Sync Scripts

This directory contains all executable scripts and Python modules for the Confluence sync tool.

## Structure

- **Virtual Environment:**
  - `venv/` - Python virtual environment (auto-managed by wrapper script)

- **Wrapper Scripts:**
  - `sync-wrapper.sh` - Main wrapper that sets up venv, loads .env, and runs sync
  - `../run-sync-with-env.py` - Python wrapper that loads .env and executes sync

- **Main Scripts:**
  - `sync-to-confluence.py` - Main sync script (entry point)
  - `fix-broken-links.py` - Broken link detection and fixing

- **Core Modules:**
  - `content_preparer.py` - Content preparation (Phase 1)
  - `confluence_sync.py` - Confluence API sync (Phase 2)
  - `config_loader.py` - Configuration loading and validation
  - `sync_state.py` - State management
  - `git_utils.py` - Git utilities
  - `report_generator.py` - Report generation
  - `ignore_handler.py` - .confluence-ignore file handling

- **Test Scripts:**
  - `test_sync.py` - Full test suite
  - `test_sync_simple.py` - Simple test script

- **Helper Scripts:**
  - `sync-hub-docs.sh` - Helper to sync hub-docs destination
  - `sync-hub-proposal.sh` - Helper to sync hub-proposal destination

## Usage

### Recommended: Use Wrapper Scripts

**Option 1: Shell wrapper** (automatically sets up venv and loads .env):

```bash
# From repository root
bash _confluence_sync/scripts/sync-wrapper.sh --destination hub-proposal

# Or use helper scripts (which use the wrapper internally)
bash _confluence_sync/scripts/sync-hub-proposal.sh
bash _confluence_sync/scripts/sync-hub-docs.sh
```

**Option 2: Python wrapper** (loads .env, requires venv to be set up):

```bash
# From repository root
python3 _confluence_sync/run-sync-with-env.py --destination hub-proposal
```

### Direct Usage (if venv is already activated and token is set)

```bash
# Activate venv first
source _confluence_sync/scripts/venv/bin/activate

# Set token (or use .env file)
export CONFLUENCE_TOKEN=your-token

# Then run scripts
python _confluence_sync/scripts/sync-to-confluence.py --destination hub-proposal
```

## Virtual Environment

The virtual environment (`venv/`) is automatically created and managed by `sync-wrapper.sh`. It:
- Creates the venv if it doesn't exist
- Upgrades pip
- Installs all requirements from `../requirements.txt`
- Activates before running scripts

## Environment Variables

The wrapper script loads environment variables from `../data/.env` (sibling to `scripts/`). Create this file with:

```bash
echo "CONFLUENCE_TOKEN=your-token" > _confluence_sync/data/.env
```

## Data Directory

The `data/` directory (sibling to `scripts/`) contains:
- `.env` - Environment variables (CONFLUENCE_TOKEN)
- `confluence-destinations.yaml` - Configuration file
- `{destination_id}/` - Per-destination state and reports
