# Confluence Sync Script

Python script to sync Markdown files from your Git repository to Confluence using a destination-based configuration system. Preserves folder hierarchy and supports multiple destinations per repository.

## Features

- ✅ **Destination-based architecture**: Sync different folders to different Confluence spaces or root pages
- ✅ **Multiple source folders**: Combine content from multiple repository folders into a single destination
- ✅ **Direct Confluence REST API integration** (no third-party tool dependencies)
- ✅ **Preserves folder structure** as parent/child page relationships
- ✅ **Uses page IDs** (not titles) for reliable parent resolution
- ✅ **Creates parent pages automatically**
- ✅ **Updates existing pages** instead of creating duplicates
- ✅ **Change detection**: Only updates pages when content actually changes
- ✅ **Converts Markdown cross-links** to Confluence page links
- ✅ **Git metadata integration**: Automatically adds commit hash and GitHub links to pages
- ✅ **README embedding**: Automatically embeds README.md content in directory pages
- ✅ **Broken link detection**: Script to find and fix broken internal links
- ✅ **Detailed sync reports**: Per-destination reports with full sync history
- ✅ **Per-destination state tracking**: Isolated state management for each destination
- ✅ **Supports `.confluence-ignore` files** for excluding files/directories
- ✅ **Parallel processing**: Parallel folder and page syncing for faster performance
- ✅ **Sync state optimization**: Trusts sync state to avoid unnecessary API calls
- ✅ **Orphan detection**: Automatically detects and deletes pages/folders removed from source

## Installation

The sync tool uses a Python virtual environment that is automatically managed by the wrapper script. No manual installation needed!

### Automatic Setup (Recommended)

The wrapper script (`scripts/sync-wrapper.sh`) automatically:
- Creates and manages the virtual environment in `scripts/venv/`
- Installs all required dependencies from `requirements.txt`
- Loads environment variables from `data/.env`

### Manual Setup (Optional)

If you prefer to set up manually:

```bash
cd _confluence_sync
python3 -m venv scripts/venv
source scripts/venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create `data/.env` file with your Confluence API token:

```bash
echo "CONFLUENCE_TOKEN=your-api-token-here" > _confluence_sync/data/.env
```

Or set it as an environment variable:

```bash
export CONFLUENCE_TOKEN=your-api-token-here
```

## Quick Start

### 1. Create Configuration File

Create a `confluence-destinations.yaml` file in `_confluence_sync/data/`:

```yaml
destinations:
  - id: my-docs
    name: My Documentation
    confluence:
      url: https://yourcompany.atlassian.net
      space_key: DOCS
      root_page_title: My Documentation
    source:
      folders:
        - path: docs
          create_root_parent: true
    credentials:
      username: your-email@example.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
      dry_run: false
```

### 2. Set API Token

Create `_confluence_sync/data/.env` file:

```bash
echo "CONFLUENCE_TOKEN=your-api-token-here" > _confluence_sync/data/.env
```

Or set as environment variable:

```bash
export CONFLUENCE_TOKEN=your-api-token-here
```

### 3. Run Sync

Use the wrapper script (recommended - automatically sets up venv):

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --destination my-docs
```

Or use the Python wrapper with .env file:

```bash
python3 _confluence_sync/run-sync-with-env.py --destination my-docs
```

Or use helper scripts for specific destinations:

```bash
bash _confluence_sync/scripts/sync-hub-proposal.sh
bash _confluence_sync/scripts/sync-hub-docs.sh
```

Or run directly (if venv is already activated and token is set):

```bash
python _confluence_sync/scripts/sync-to-confluence.py --destination my-docs
```

## Configuration

### Getting a Confluence API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Copy the token and add it to `_confluence_sync/data/.env`:
   ```bash
   echo "CONFLUENCE_TOKEN=your-token" > _confluence_sync/data/.env
   ```
   Or set it as an environment variable:
   ```bash
   export CONFLUENCE_TOKEN=your-token
   ```

### Finding Your Space Key

- For regular spaces: The space key is usually visible in the space URL or settings
- For personal spaces: Use the format `~accountID` (e.g., `~5570580ad15fced37e40a38c7171943fae763b`)

## Usage

### Basic Usage

Sync a specific destination (using wrapper script):

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --destination my-docs
```

Sync all destinations:

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --all
```

### Dry Run

Preview what would be synced without making changes:

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --destination my-docs --dry-run
```

### Multiple Source Folders

Sync multiple folders to a single destination:

```yaml
source:
  folders:
    - path: user-guides
      create_root_parent: true
    - path: api-reference
      create_root_parent: true
    - path: tutorials
      create_root_parent: false
```

### Multiple Destinations

Define multiple destinations in your config:

```yaml
destinations:
  - id: hub-docs
    name: Hub Documentation
    confluence:
      url: https://company.atlassian.net
      space_key: HUB
      root_page_title: Hub Docs
    source:
      folders:
        - path: olympus-hub-docs
          create_root_parent: true
    credentials:
      username: dev@company.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
      parallel_threads: 12  # Use 12 parallel threads for faster syncing

  - id: seer-docs
    name: Seer Documentation
    confluence:
      url: https://company.atlassian.net
      space_key: SEER
      root_page_title: Seer Docs
    source:
      folders:
        - path: olympus-seer-docs
          create_root_parent: true
    credentials:
      username: dev@company.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
      parallel_threads: 12
```

## Advanced Features

### Parallel Processing

The sync tool uses parallel processing for faster performance:

- **Page syncing**: Configurable parallel threads (default: 5, recommended: 8-12)
- **Folder creation**: Parallelized by depth level (max 8 threads per level)
- **Parent-child ordering**: Maintained through depth-based processing

Configure in your destination config:

```yaml
options:
  parallel_threads: 12  # Use 12 parallel threads for page syncing
```

**Performance**: Large syncs (1000+ files) complete much faster with parallel processing.

### Sync State Optimization

The sync tool optimizes performance by trusting sync state:

- **Unchanged folders**: Uses `folder_id` from sync state without API call
- **Change detection**: Only makes API calls when metadata changes
- **Incremental syncs**: Much faster due to state trust

This significantly reduces API calls for incremental syncs while maintaining correctness.

### Git Metadata

When enabled, each page includes:
- Commit hash of the synced version
- Link to the file on GitHub at that commit

Enable in config:
```yaml
options:
  add_git_metadata: true
  github_repo_override: null  # Optional: override auto-detected URL
```

### README Embedding

README.md files are automatically embedded into their parent directory pages, ensuring directory pages always have meaningful content.

### Broken Link Detection

Find and fix broken internal links:

```bash
# Scan all pages (using wrapper to ensure venv is set up)
bash _confluence_sync/scripts/sync-wrapper.sh --destination my-docs
python _confluence_sync/scripts/fix-broken-links.py --destination my-docs

# Scan specific page
python _confluence_sync/scripts/fix-broken-links.py --destination my-docs --page-id 12345

# Dry run
python _confluence_sync/scripts/fix-broken-links.py --destination my-docs --dry-run
```

### Orphan Detection

The sync automatically detects and deletes orphaned pages and folders:

- **Orphaned pages**: Pages in Confluence that no longer have corresponding source files
- **Orphaned folders**: Folders in Confluence that no longer exist in source
- **Automatic cleanup**: Orphans are deleted during Phase 3 of sync

**Note**: Only pages/folders tracked in sync state are deleted. Manually created content is not affected.

### Ignoring Files

Create `.confluence-ignore` files (similar to `.gitignore`) to exclude files and directories:

```
# Ignore specific files
private-notes.md
draft.md

# Ignore directories
temp/
drafts/

# Ignore patterns
*.draft.md
**/private/**
```

## Sync Reports

After each sync, a detailed report is generated:

- **Location**: `_confluence_sync/data/{destination-id}/sync-report-{timestamp}.txt`
- **Contents**: 
  - Sync metadata (commit, timestamp, space)
  - Summary statistics (created, updated, skipped, errors)
  - Detailed per-file results table
  - Error details (if any)

Reports include:
- File paths
- Sync status (created/updated/skipped/error)
- Page IDs and titles
- Commit hashes (old → new)
- Confluence and GitHub URLs

## State Management

Each destination maintains its own state file:

- **Location**: `_confluence_sync/data/{destination-id}/sync-state.jsonl`
- **Purpose**: Tracks what was synced, when, and from which commit
- **Used for**: Change detection, reporting, incremental updates
- **Format**: JSONL (JSON Lines) for efficient streaming updates

State files are automatically managed - you typically don't need to interact with them directly.

## Command-Line Options

```
--config PATH          Path to destination config file
                       (default: confluence-destinations.yaml in repo root)

--destination ID       Destination ID to sync (required unless --all)

--all                  Sync all destinations in config

--dry-run              Show what would be synced without making changes

--report               Generate report only (no sync) - coming soon
```

## Examples

### Single Destination

```bash
# Using wrapper script (recommended)
bash _confluence_sync/scripts/sync-wrapper.sh --destination hub-docs

# Or using helper script
bash _confluence_sync/scripts/sync-hub-proposal.sh
```

### All Destinations

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --all
```

### Custom Config

```bash
bash _confluence_sync/scripts/sync-wrapper.sh \
  --config path/to/config.yaml \
  --destination my-docs
```

## Configuration Reference

See [USER-GUIDE.md](USER-GUIDE.md) for complete configuration documentation, including:

- All configuration options
- Multiple destination examples
- Source folder configuration
- Best practices
- Troubleshooting guide

## Architecture

### Destination-Based System

- **Per-destination configuration**: Each destination has its own settings
- **Per-destination state**: Isolated state tracking prevents conflicts
- **Per-destination reports**: Detailed reports for each sync operation
- **Flexible source mapping**: Multiple folders can map to one destination

### File Structure

```
_confluence_sync/
├── scripts/                    # All executable scripts and modules
│   ├── venv/                   # Python virtual environment (auto-managed)
│   ├── sync-wrapper.sh         # Wrapper script (sets up venv, loads .env)
│   ├── sync-to-confluence.py   # Main sync script
│   ├── config_loader.py        # Config file loading and validation
│   ├── sync_state.py           # Per-destination state management
│   ├── git_utils.py            # Git utilities (commit hash, GitHub URLs)
│   ├── report_generator.py     # Report generation
│   ├── fix-broken-links.py     # Broken link detection and fixing
│   ├── ignore_handler.py       # .confluence-ignore file handling
│   ├── content_preparer.py     # Content preparation module
│   ├── confluence_sync.py     # Confluence API sync module
│   ├── test_sync.py            # Test suite
│   ├── test_sync_simple.py     # Simple test script
│   ├── sync-hub-proposal.sh   # Helper script for hub-proposal
│   └── sync-hub-docs.sh        # Helper script for hub-docs
├── data/                        # All runtime data
│   ├── .env                    # Environment variables (CONFLUENCE_TOKEN)
│   ├── confluence-destinations.yaml  # Destination configuration
│   ├── {destination_id}/       # Per-destination data
│   │   ├── sync-state.jsonl    # Sync history
│   │   ├── sync-metadata.json  # Destination metadata
│   │   └── sync-report-*.txt  # Sync reports
│   └── ...
├── decisions/                  # Architecture Decision Records (ADRs)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── USER-GUIDE.md               # Comprehensive user guide
```

## How It Works

1. **Wrapper Script**: `sync-wrapper.sh` or `run-sync-with-env.py` ensures virtual environment is set up and loads `.env` from `data/`
2. **Load Configuration**: Reads `confluence-destinations.yaml` from `data/` directory
3. **Resolve Credentials**: Gets API token from `data/.env` or environment variable
4. **Load State**: Loads per-destination sync state from `data/{destination-id}/` (if exists)
5. **Build Title Cache**: Scans all Markdown files to build link resolution cache
6. **Sync Folders** (Phase 2a): For each source folder:
   - Find or create root page
   - Create folders in parallel (grouped by depth level)
   - Trust sync state for unchanged folders (skip API calls)
   - Maintain parent-child ordering through depth-based processing
7. **Sync Pages** (Phase 2b): For each Markdown file:
   - Sync pages in parallel using configurable thread pool
   - Convert Markdown links to Confluence links
   - Add Git metadata (if enabled)
   - Only update pages when content changes
8. **Orphan Detection** (Phase 3): Detect and delete orphaned pages/folders
9. **Update State**: Save sync state to `data/{destination-id}/sync-state.jsonl`
10. **Generate Report**: Create detailed sync report in `data/{destination-id}/`

## Important Notes

⚠️ **WARNING**: This is a ONE-WAY sync (Markdown → Confluence).

- Edits made directly in Confluence will be overwritten on next sync
- The tool only creates and updates pages; it doesn't delete them
- Manual deletions in Confluence are not synced back to Git

## Troubleshooting

### Common Issues

**"Configuration file not found"**
- Create `confluence-destinations.yaml` in your repository root

**"API token not found"**
- Create `_confluence_sync/data/.env` with `CONFLUENCE_TOKEN=your-token`
- Or set `export CONFLUENCE_TOKEN=your-token`

**"Destination not found"**
- Check your config file for the correct destination ID
- List available destinations from the error message

**"Folder not found"**
- Verify folder paths in config are relative to repository root
- Ensure folders exist

See [USER-GUIDE.md](USER-GUIDE.md) for detailed troubleshooting guide.

## Migration from Old CLI

If you were using the old `--dir`, `--url`, `--space` arguments:

1. Create `_confluence_sync/data/confluence-destinations.yaml` with your settings
2. Create `_confluence_sync/data/.env` with `CONFLUENCE_TOKEN=your-token`
3. Run: `bash _confluence_sync/scripts/sync-wrapper.sh --destination {id}`

See [USER-GUIDE.md](USER-GUIDE.md) Migration Guide for detailed steps.

## Documentation

- **[USER-GUIDE.md](USER-GUIDE.md)**: Comprehensive user guide with examples, troubleshooting, and best practices
- **Sync Reports**: Detailed per-sync reports in `_confluence_sync/data/{destination-id}/sync-report-*.txt`
- **State Files**: Per-destination state tracking in `_confluence_sync/data/{destination-id}/sync-state.jsonl`

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
