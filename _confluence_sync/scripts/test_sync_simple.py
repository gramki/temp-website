#!/usr/bin/env python3
"""
Simple test script for Confluence sync - uses existing small directories.
"""

import os
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import from sync-to-confluence.py
import importlib.util
spec = importlib.util.spec_from_file_location("sync_to_confluence", Path(__file__).parent / "sync-to-confluence.py")
sync_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_module)
sync_destination = sync_module.sync_destination

from config_loader import load_destination_config, get_destination, ConfigError, get_repo_root
from git_utils import get_repo_root as get_git_repo_root


def find_small_directory(repo_root: Path, min_files: int = 1, max_files: int = 10) -> Path:
    """Find a small directory with few Markdown files."""
    hub_docs = repo_root / "olympus-hub-docs"
    if not hub_docs.exists():
        return None
    
    for item in hub_docs.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            md_files = list(item.rglob("*.md"))
            if min_files <= len(md_files) <= max_files:
                return item
    
    return None


def main():
    """Run a simple sync test."""
    print("=" * 80)
    print("Simple Confluence Sync Test")
    print("=" * 80)
    print()
    
    # Check for token (unless dry run)
    dry_run = os.getenv('DRY_RUN', 'false').lower() == 'true'
    if not dry_run and not os.getenv('CONFLUENCE_TOKEN'):
        print("ERROR: CONFLUENCE_TOKEN environment variable not set")
        print("Set DRY_RUN=true to run in dry-run mode")
        return 1
    
    # Get repo root
    repo_root = get_repo_root()
    print(f"Repository root: {repo_root}")
    print()
    
    # Find a small directory
    test_dir = find_small_directory(repo_root, min_files=1, max_files=10)
    if not test_dir:
        print("No suitable small directory found")
        return 1
    
    md_files = list(test_dir.rglob("*.md"))
    print(f"Selected directory: {test_dir.relative_to(repo_root)}")
    print(f"  Files: {len(md_files)}")
    for md_file in md_files[:5]:
        print(f"    - {md_file.relative_to(test_dir)}")
    if len(md_files) > 5:
        print(f"    ... and {len(md_files) - 5} more")
    print()
    
    if len(md_files) >= 20:
        print(f"WARNING: {len(md_files)} files exceeds limit of 20")
        return 1
    
    # Load config (data directory is sibling to scripts directory)
    data_dir = Path(__file__).parent.parent / "data"
    try:
        config = load_destination_config(data_dir=data_dir)
        dest_config = get_destination(config, "hub-proposal")
    except ConfigError as e:
        print(f"ERROR: Failed to load config: {e}")
        return 1
    
    # Modify config to use only the test directory
    original_folders = dest_config['source']['folders'].copy()
    dest_config['source']['folders'] = [
        {
            'path': str(test_dir.relative_to(repo_root)),
            'create_root_parent': True,
            'title': f"Test: {test_dir.name}"
        }
    ]
    
    print("Running sync...")
    if dry_run:
        print("(DRY RUN MODE)")
    print("-" * 80)
    
    try:
        results = sync_destination(
            destination_id="hub-proposal",
            destination_config=dest_config,
            repo_root=repo_root,
            data_dir=data_dir,
            dry_run_override=dry_run
        )
        
        print("-" * 80)
        print()
        print("Results:")
        print(f"  Total: {len(results)}")
        print(f"  Created: {sum(1 for r in results if r.status == 'created')}")
        print(f"  Updated: {sum(1 for r in results if r.status == 'updated')}")
        print(f"  Skipped: {sum(1 for r in results if r.status == 'skipped')}")
        print(f"  Errors: {sum(1 for r in results if r.status == 'error')}")
        print()
        
        if results:
            print("Sample results:")
            for result in results[:5]:
                status_icon = "✓" if result.status in ['created', 'updated'] else "⊘" if result.status == 'skipped' else "✗"
                print(f"  {status_icon} {result.file_path} -> {result.status}")
            if len(results) > 5:
                print(f"  ... and {len(results) - 5} more")
        
        # Restore original config
        dest_config['source']['folders'] = original_folders
        
        return 0
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        # Restore original config
        dest_config['source']['folders'] = original_folders
        return 1


if __name__ == '__main__':
    sys.exit(main())
