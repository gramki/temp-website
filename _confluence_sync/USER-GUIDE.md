# Confluence Sync User Guide

Complete guide to syncing Markdown documentation from Git repositories to Confluence using the destination-based sync system.

## Table of Contents

1. [Introduction](#introduction)
2. [Quick Start](#quick-start)
3. [Configuration Guide](#configuration-guide)
4. [Source Folders](#source-folders)
5. [Command-Line Usage](#command-line-usage)
6. [Understanding Sync Reports](#understanding-sync-reports)
7. [State Management](#state-management)
8. [Advanced Features](#advanced-features)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)
11. [Migration Guide](#migration-guide)
12. [FAQ](#faq)

---

## Introduction

### What This Tool Does

The Confluence Sync tool automatically syncs Markdown files from your Git repository to Confluence, preserving folder hierarchy as parent-child page relationships. It supports:

- **Multiple destinations**: Sync different folders to different Confluence spaces or root pages
- **Multiple source folders**: Combine content from multiple repository folders into a single Confluence destination
- **Git metadata**: Automatically add commit hashes and GitHub links to pages
- **Change detection**: Only updates pages when content actually changes
- **Link conversion**: Converts Markdown cross-links to Confluence page links
- **Broken link detection**: Identify and fix broken internal links
- **Parallel processing**: Parallel folder and page syncing for faster performance
- **Sync state optimization**: Trusts sync state to avoid unnecessary API calls

### Key Concepts

- **Destination**: A Confluence target (space + root page) where content is synced
- **Source Folder**: A folder in your Git repository that contains Markdown files to sync
- **Root Page**: The top-level Confluence page under which all synced content is organized
- **Sync State**: Per-destination tracking of what was synced, when, and from which commit

### Benefits of Destination-Based Approach

- **Isolation**: Each destination has its own state and reports
- **Flexibility**: Sync the same repo to multiple Confluence spaces
- **Organization**: Keep different documentation sets separate
- **Configuration**: All settings in one YAML file

---

## Quick Start

### Installation

The sync tool uses a Python virtual environment that is automatically managed by the wrapper script. No manual installation needed!

#### Automatic Setup (Recommended)

The wrapper script (`scripts/sync-wrapper.sh`) automatically:
- Creates and manages the virtual environment in `scripts/venv/`
- Installs all required dependencies from `requirements.txt`
- Loads environment variables from `data/.env`

#### Manual Setup (Optional)

If you prefer to set up manually:

```bash
cd _confluence_sync
python3 -m venv scripts/venv
source scripts/venv/bin/activate
pip install -r requirements.txt
```

#### Environment Variables

Create `data/.env` file with your Confluence API token:

```bash
echo "CONFLUENCE_TOKEN=your-api-token-here" > _confluence_sync/data/.env
```

Or set it as an environment variable:

```bash
export CONFLUENCE_TOKEN=your-api-token-here
```

### Creating Your First Destination

1. Create a `confluence-destinations.yaml` file in `_confluence_sync/data/`:

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
      github_repo_override: null
      dry_run: false
      parallel_threads: 12  # Optional: number of parallel threads (default: 5)
```

2. Set your Confluence API token:

Create `_confluence_sync/data/.env` file:

```bash
echo "CONFLUENCE_TOKEN=your-api-token-here" > _confluence_sync/data/.env
```

Or set as environment variable:

```bash
export CONFLUENCE_TOKEN=your-api-token-here
```

3. Run your first sync:

Using the wrapper script (recommended):

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --destination my-docs
```

Or run directly (if venv is already activated):

```bash
python _confluence_sync/scripts/sync-to-confluence.py --destination my-docs
```

### Verifying Results

1. Check the console output for sync status
2. Review the generated report file: `_confluence_sync/data/{destination-id}/sync-report-{timestamp}.txt`
3. Visit your Confluence space to see the synced pages

---

## Configuration Guide

### Config File Structure

The `confluence-destinations.yaml` file defines one or more destinations:

```yaml
destinations:
  - id: unique-destination-id
    name: Human-readable name
    confluence:
      url: https://yourcompany.atlassian.net
      space_key: SPACE_KEY
      root_page_title: Root Page Title
      root_page_id: null  # Optional: use existing page ID
    source:
      folders:
        - path: relative/path/to/folder
          create_root_parent: true
        - path: another/folder
          create_root_parent: false
    credentials:
      username: user@example.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
      github_repo_override: null  # Optional: override auto-detected GitHub URL
      dry_run: false
```

### Configuration Options

#### Destination ID (`id`)

- **Required**: Yes
- **Type**: String
- **Description**: Unique identifier for this destination
- **Used for**: State files, report files, CLI selection
- **Example**: `hub-docs`, `seer-docs`, `api-reference`

#### Confluence Configuration

- **`url`**: Confluence base URL (e.g., `https://yourcompany.atlassian.net`)
- **`space_key`**: Confluence space key (e.g., `DOCS`, `~accountID` for personal spaces)
- **`root_page_title`**: Title of the root page (will be created if doesn't exist)
- **`root_page_id`**: Optional - if provided, uses this existing page as root

#### Source Folders

- **`path`**: Relative path from repository root to folder containing Markdown files
- **`create_root_parent`**: Whether to create a parent page for this folder's root directory

#### Credentials

- **`username`**: Your Confluence username/email
- **`token_env_var`**: Name of environment variable containing API token

**Security Note**: API tokens must be stored in environment variables, never in the config file.

#### Options

- **`add_git_metadata`**: Add commit hash and GitHub link to each page
- **`github_repo_override`**: Override auto-detected GitHub repository URL
- **`dry_run`**: If true, show what would be synced without making changes
- **`parallel_threads`**: Number of parallel threads for page syncing (default: 5, recommended: 8-12 for large syncs)
- **`parallel_threads`**: Number of parallel threads for page syncing (default: 5, recommended: 8-12)

### Example Configurations

#### Single Folder to Single Destination

```yaml
destinations:
  - id: api-docs
    name: API Documentation
    confluence:
      url: https://company.atlassian.net
      space_key: API
      root_page_title: API Documentation
    source:
      folders:
        - path: api-docs
          create_root_parent: true
    credentials:
      username: dev@company.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
```

#### Multiple Folders to Single Destination

```yaml
destinations:
  - id: all-docs
    name: All Documentation
    confluence:
      url: https://company.atlassian.net
      space_key: DOCS
      root_page_title: Documentation
    source:
      folders:
        - path: user-guides
          create_root_parent: true
        - path: api-reference
          create_root_parent: true
        - path: tutorials
          create_root_parent: false
    credentials:
      username: docs@company.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
```

#### Multiple Destinations from Same Repo

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
```

---

## Source Folders

### Specifying Multiple Folders

You can sync multiple folders to a single destination:

```yaml
source:
  folders:
    - path: folder1
      create_root_parent: true
    - path: folder2
      create_root_parent: true
```

Each folder maintains its own hierarchy under the root page.

### Per-Folder Settings

#### `create_root_parent`

- **Default**: `true`
- **Description**: Whether to create a parent page for the folder's root directory
- **When to use `false`**: If you want the folder's contents directly under the root page

**Example**:

```yaml
source:
  folders:
    - path: main-docs
      create_root_parent: true    # Creates "Main Docs" page
    - path: appendices
      create_root_parent: false   # Contents go directly under root
```

### Folder Hierarchy Preservation

The tool preserves your folder structure as parent-child relationships in Confluence:

```
docs/
  ├── getting-started.md
  └── advanced/
      └── concepts.md
```

Becomes:

```
Root Page
  ├── Getting Started (page)
  └── Advanced (page)
      └── Concepts (page)
```

### Handling Folder Name Conflicts

If multiple folders have files with the same relative path, they will be synced separately under their respective folder parent pages.

---

## Command-Line Usage

### Basic Commands

#### Sync a Specific Destination

```bash
bash _confluence_sync/scripts/sync-wrapper.sh --destination hub-docs
```

#### Sync All Destinations

```bash
python _confluence_sync/sync-to-confluence.py --all
```

#### Dry Run (Preview Changes)

```bash
python _confluence_sync/sync-to-confluence.py --destination hub-docs --dry-run
```

#### Use Custom Config File

```bash
python _confluence_sync/sync-to-confluence.py \
  --config path/to/custom-config.yaml \
  --destination hub-docs
```

### Command-Line Arguments

- **`--config PATH`**: Path to destination config file (default: `confluence-destinations.yaml` in `data/` directory)
- **`--destination ID`**: Destination ID to sync (required unless `--all`)
- **`--all`**: Sync all destinations in config
- **`--dry-run`**: Override config's `dry_run` option
- **`--report`**: Generate report only (no sync) - *coming soon*

### Examples

#### Sync Single Destination

```bash
# Set token
export CONFLUENCE_TOKEN=your-token

# Sync
python _confluence_sync/sync-to-confluence.py --destination hub-docs
```

#### Sync Multiple Destinations

```bash
python _confluence_sync/sync-to-confluence.py --all
```

#### Preview Before Syncing

```bash
python _confluence_sync/sync-to-confluence.py --destination hub-docs --dry-run
```

---

## Understanding Sync Reports

### Report Location

Reports are saved to: `_confluence_sync/data/{destination-id}/sync-report-{timestamp}.txt`

Example: `_confluence_sync/data/hub-docs/sync-report-20240115-143022.txt`

### Report Format

Each report includes:

1. **Header**: Destination name, ID, timestamp
2. **Sync Metadata**: Commit hash, space, root page info
3. **Summary Statistics**: Total files, created, updated, skipped, errors
4. **Detailed Results Table**: Per-file sync information
5. **Errors Section**: Any errors encountered

### Report Table Columns

- **File Path**: Relative path to synced file
- **Status**: `✓ Created`, `↻ Updated`, `⊘ Skipped`, or `✗ Error`
- **Page ID**: Confluence page ID
- **Page Title**: Page title in Confluence
- **Commit**: Commit hash (old → new if updated)
- **Date**: Sync date (old → new if updated)
- **Confluence URL**: Link to page in Confluence
- **GitHub URL**: Link to file on GitHub
- **Error**: Error message (if any)

### Reading Sync Status

- **✓ Created**: New page was created
- **↻ Updated**: Existing page was updated (content changed)
- **⊘ Skipped**: Page exists and content hasn't changed
- **✗ Error**: Error occurred while processing this file

### Interpreting Commit Hashes

- **Single hash**: First sync or no previous sync
- **Old → New**: Page was updated (shows previous and current commits)
- **Same hash**: Content unchanged since last sync

---

## State Management

### How Sync State Works

The sync tool maintains state for each destination in: `_confluence_sync/data/{destination-id}/sync-state.jsonl`

This file tracks (in JSONL format for efficient streaming):
- Which files were synced
- Page IDs and titles
- Last sync commit hash and date
- Previous commit hash (for comparison)
- Content hashes for change detection

### State File Locations

State files are stored in `_confluence_sync/data/{destination-id}/` directories:
- `_confluence_sync/data/hub-docs/sync-state.jsonl`
- `_confluence_sync/data/seer-docs/sync-state.jsonl`
- etc.

### When State is Updated

State is updated:
- After each successful file sync
- When pages are created, updated, or skipped
- At the end of a successful sync operation

### Recovering from Corrupted State

If a state file becomes corrupted:

1. **Option 1**: Delete the state file - next sync will start fresh
2. **Option 2**: The tool will automatically detect corruption and start fresh

**Note**: Starting fresh means all pages will be detected as "new" and may create duplicates if pages already exist. Use with caution.

### State File Format

The sync state is stored in JSONL format (JSON Lines) for efficient streaming updates:

```json
{"type": "page", "file_path": "docs/getting-started.md", "page_id": "12345", "page_title": "Getting Started", "last_sync_commit": "abc123", "last_sync_date": "2024-01-15T10:30:00Z", "last_sync_status": "updated", "previous_commit": "xyz789", "previous_sync_date": "2024-01-10T14:20:00Z", "content_hash": "abc123...", "version": 2, "parent_id": "67890"}
{"type": "folder", "folder_path": "docs", "folder_id": "67890", "folder_title": "Documentation", "parent_id": "root", "status": "found", "timestamp": "2024-01-15T10:30:00Z"}
```

**Note**: The state file is append-only (JSONL format). Each sync appends new entries rather than overwriting. The sync tool automatically compacts duplicates when needed.

---

## Advanced Features

### Parallel Processing

The sync tool uses parallel processing to speed up large syncs:

- **Page syncing**: Configurable parallel threads (default: 5, recommended: 8-12)
- **Folder creation**: Parallelized by depth level (max 8 threads per level)
- **Parent-child ordering**: Maintained through depth-based processing

Configure parallel threads in your destination config:

```yaml
options:
  parallel_threads: 12  # Use 12 parallel threads for page syncing
```

**Performance Benefits**:
- Large syncs (1000+ files) complete much faster
- Folder creation is parallelized while maintaining hierarchy
- Sync state trust eliminates unnecessary API calls

**How It Works**:
1. Folders are grouped by depth (shallow to deep)
2. Folders at the same depth are processed in parallel
3. Pages are synced using a thread pool (configurable size)
4. Sync state is trusted for unchanged folders (no API calls)

### Sync State Optimization

The sync tool optimizes performance by trusting sync state:

- **Unchanged folders**: If folder title and parent haven't changed, uses `folder_id` from sync state without API call
- **Change detection**: Only makes API calls when metadata changes or conflicts are detected
- **Incremental syncs**: Subsequent syncs are much faster due to state trust

This optimization significantly reduces API calls for incremental syncs while maintaining correctness.

### Orphan Detection

The sync automatically detects and deletes orphaned pages and folders:

- **Orphaned pages**: Pages in Confluence that no longer have corresponding source files
- **Orphaned folders**: Folders in Confluence that no longer exist in source
- **Automatic cleanup**: Orphans are deleted during Phase 3 of sync

**Important**: Only pages/folders tracked in sync state are deleted. Manually created content in Confluence is not affected.

### Git Metadata Integration

When `add_git_metadata: true` is set, each page includes:

- **Commit hash**: The Git commit from which the page was synced
- **GitHub link**: Direct link to the file on GitHub at that commit

The metadata appears as a Confluence info panel at the bottom of each page.

**Example**:

```
Source: Commit: abc123 | View on GitHub
```

### README Embedding

README.md files are automatically embedded into their parent directory pages:

- If README title matches directory title: README content replaces directory page content
- If README title differs: README content is still embedded in directory page

This ensures directory pages always have meaningful content.

### Broken Link Detection

Use the `fix-broken-links.py` script to find and fix broken internal links:

```bash
# Scan all pages in a destination (ensure venv is activated)
source _confluence_sync/scripts/venv/bin/activate
python _confluence_sync/scripts/fix-broken-links.py --destination hub-docs

# Scan specific page
python _confluence_sync/scripts/fix-broken-links.py --destination hub-docs --page-id 12345

# Dry run (preview fixes)
python _confluence_sync/scripts/fix-broken-links.py --destination hub-docs --dry-run
```

The script:
- Detects broken page links
- Attempts to fix them using fuzzy title matching
- Reports fixed and unfixable links

### Environment File Wrapper

For convenience, use the Python wrapper script that automatically loads `.env`:

```bash
python3 _confluence_sync/run-sync-with-env.py --destination my-docs
```

This wrapper:
- Loads environment variables from `data/.env`
- Sets up environment before running sync
- No need to manually export `CONFLUENCE_TOKEN`

The `.env` file should be located at `_confluence_sync/data/.env`:

```bash
echo "CONFLUENCE_TOKEN=your-token-here" > _confluence_sync/data/.env
```

### Using `.confluence-ignore` Files

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

Patterns support:
- Simple filenames: `file.md`
- Wildcards: `*.md`, `**/temp/`
- Directory patterns: `folder/`
- Negation: `!important.md`

---

## Troubleshooting

### Common Errors and Solutions

#### "Configuration file not found"

**Error**: `Configuration file not found: confluence-destinations.yaml`

**Solution**: Create `confluence-destinations.yaml` in `_confluence_sync/data/` directory.

#### "API token not found in environment variable"

**Error**: `API token not found in environment variable 'CONFLUENCE_TOKEN'`

**Solution**: Create `_confluence_sync/data/.env` file:
```bash
echo "CONFLUENCE_TOKEN=your-token-here" > _confluence_sync/data/.env
```
Or set the environment variable:
```bash
export CONFLUENCE_TOKEN=your-token-here
```

#### "Destination 'X' not found"

**Error**: `Destination 'X' not found. Available destinations: ...`

**Solution**: Check your config file for the correct destination ID, or list available destinations from the error message.

#### "Folder not found"

**Error**: `Folder not found: path/to/folder`

**Solution**: 
- Verify the folder path in your config is correct
- Ensure the path is relative to repository root
- Check that the folder exists

#### "Page exists but wasn't found"

**Warning**: `Page 'X' exists but wasn't found. Searching again...`

**Solution**: This is usually harmless - the tool will find and update the page. If it persists, the page may be in a different space or have permission issues.

### Authentication Issues

#### Invalid Credentials

**Error**: `401 Unauthorized` or `403 Forbidden`

**Solutions**:
1. Verify your username is correct
2. Check that your API token is valid (tokens can expire)
3. Ensure you have permission to create/update pages in the space

#### Getting a New API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Copy the token
4. Update `_confluence_sync/data/.env` with the new token, or set: `export CONFLUENCE_TOKEN=your-new-token`

### Page Creation Failures

#### "A page with this title already exists"

**Error**: `400 Bad Request: A page with this title already exists`

**Solution**: The tool should handle this automatically. If it doesn't:
- Check if the page exists in a different parent
- Manually delete or rename the conflicting page in Confluence

#### "Can not set page as its own parent"

**Error**: `400 Bad Request: Can not set page as its own parent`

**Solution**: This is handled automatically for README files. If it occurs for other files, there may be a title conflict - check your Markdown files for duplicate H1 titles.

### Link Resolution Problems

#### Links Not Working in Confluence

**Symptoms**: Markdown links appear as plain text or broken links

**Solutions**:
1. Ensure target files are in the same sync scope
2. Check that target pages exist in Confluence
3. Verify link syntax in Markdown: `[text](path/to/file.md)`
4. Run the broken link fixer: `fix-broken-links.py`

### State File Issues

#### Corrupted State File

**Warning**: `Corrupted state file sync-state.jsonl. Starting fresh.`

**Solution**: The tool will automatically recover. If you want to force a fresh start, delete the state file manually.

#### State File Out of Sync

**Symptoms**: Pages show as "new" even though they exist

**Solutions**:
1. Delete the state file to force a fresh scan
2. The tool will detect existing pages and update them instead of creating duplicates

---

## Best Practices

### Organizing Destinations

- **By product/component**: One destination per major component
- **By audience**: Separate destinations for user docs vs. developer docs
- **By space**: Match Confluence space organization

### Naming Conventions

- **Destination IDs**: Use lowercase with hyphens: `hub-docs`, `api-reference`
- **Root page titles**: Use clear, descriptive names: "API Documentation", "User Guides"
- **Folder paths**: Use consistent naming in your repository

### Folder Structure Recommendations

- **Flat structures**: Work well for small documentation sets
- **Hierarchical structures**: Better for large, organized documentation
- **README files**: Place in each directory to provide context

### When to Use Multiple Destinations vs. Multiple Folders

**Use Multiple Destinations When**:
- Content goes to different Confluence spaces
- Different root pages are needed
- Different sync schedules or permissions

**Use Multiple Folders When**:
- Combining related content into one space
- Organizing by topic under one root page
- Maintaining separate source folders but unified destination

### Git Workflow Integration

- **Sync after commits**: Add sync to your CI/CD pipeline
- **Branch protection**: Sync only from main/master branch
- **Commit messages**: Include destination ID for traceability

---

## Migration Guide

### Migrating from Old CLI-Based Approach

If you were using the old `--dir`, `--url`, `--space` arguments:

1. **Create config file**: Convert your old command-line usage to `confluence-destinations.yaml`

**Old**:
```bash
python sync-to-confluence.py \
  --dir docs \
  --url https://company.atlassian.net \
  --space DOCS \
  --username user@company.com \
  --token $TOKEN
```

**New**:
```yaml
destinations:
  - id: docs
    name: Documentation
    confluence:
      url: https://company.atlassian.net
      space_key: DOCS
      root_page_title: Documentation
    source:
      folders:
        - path: docs
          create_root_parent: true
    credentials:
      username: user@company.com
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: false
      dry_run: false
```

2. **Set environment variable**:
```bash
export CONFLUENCE_TOKEN=your-token
```

3. **Run sync**:
```bash
python _confluence_sync/sync-to-confluence.py --destination docs
```

### Converting Existing `.env` Setup

If you had a `.env` file:

1. **Extract values** from `.env`:
   - `CONFLUENCE_URL` → `confluence.url`
   - `CONFLUENCE_USERNAME` → `credentials.username`
   - `CONFLUENCE_SPACE` → `confluence.space_key`
   - `CONFLUENCE_TOKEN` → Set as environment variable (don't put in config!)

2. **Create config file** with extracted values

3. **Set token** as environment variable (not in config file)

### Moving from Single to Multiple Destinations

1. **Identify your current setup**: What folder(s) sync to what space/page?

2. **Create destination configs**: One entry per destination

3. **Test each destination**: Sync individually before using `--all`

4. **Update automation**: Update CI/CD scripts to use new CLI format

---

## FAQ

### Can I sync the same folder to multiple destinations?

Yes! Just create multiple destination entries with the same `source.folders` path but different `confluence` settings.

### What happens if I delete a file from my repo?

The sync tool automatically detects and deletes orphaned pages during Phase 3 of the sync. However, this only applies to pages that were previously synced (tracked in sync state). Manually created pages in Confluence are not affected.

To force deletion of orphaned pages:
1. Delete the file from your repository
2. Run sync - orphaned pages will be automatically detected and deleted

### Can I edit pages directly in Confluence?

Yes, but your edits will be overwritten on the next sync. This is a one-way sync (Markdown → Confluence).

### How do I handle large documentation sets?

- Use multiple destinations to split content across spaces
- Use multiple folders to organize under one destination
- Consider using `.confluence-ignore` to exclude draft/temporary files

### Can I sync from a specific Git branch?

The tool uses the current Git HEAD commit. To sync from a specific branch:
1. Check out the branch: `git checkout branch-name`
2. Run sync
3. Check out your original branch

### What if my Confluence space uses a different URL format?

The tool automatically handles Confluence Cloud URLs. For on-premise or custom URLs, ensure the `url` in config points to your Confluence instance root.

### How do I handle special characters in page titles?

The tool preserves your Markdown H1 titles. If you have issues:
- Ensure titles are valid Confluence page titles
- Avoid special characters that Confluence doesn't support
- The tool will fall back to cleaned filename if H1 is invalid

### Can I sync only specific files or folders?

Use `.confluence-ignore` files to exclude what you don't want to sync. The tool syncs everything in specified folders by default.

### What's the difference between `create_root_parent: true` and `false`?

- **`true`**: Creates a page for the folder itself (e.g., "Docs" page containing "Getting Started" page)
- **`false`**: Contents go directly under the root page (no intermediate folder page)

### How do I update the root page content?

Edit the root page directly in Confluence, or create a README.md file in the root of your source folder - it will be embedded in the root page.

---

## Getting Help

- **Check the report files**: Detailed information about each sync
- **Review state files**: See what was synced and when
- **Use dry-run mode**: Preview changes before applying them
- **Check Confluence directly**: Verify pages exist and have correct content

For issues or questions, refer to the main README.md or check the sync report files for detailed error messages.
