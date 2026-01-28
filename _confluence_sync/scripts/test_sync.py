#!/usr/bin/env python3
"""
Test script for Confluence sync functionality.

Tests syncing small directories to hub-proposal destination.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict, Any

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import from sync-to-confluence.py (note: Python module name can't have hyphens, so we import directly)
import importlib.util
spec = importlib.util.spec_from_file_location("sync_to_confluence", Path(__file__).parent / "sync-to-confluence.py")
sync_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_module)
sync_destination = sync_module.sync_destination
from config_loader import load_destination_config, get_destination, ConfigError
from git_utils import get_repo_root


def create_test_directories(base_path: Path) -> Dict[str, Path]:
    """Create test directories with a few Markdown files."""
    test_dirs = {}
    
    # Test directory 1: simple docs
    test_dir1 = base_path / "test-docs-1"
    test_dir1.mkdir(exist_ok=True)
    
    (test_dir1 / "README.md").write_text("""# Test Documentation 1

This is a test documentation directory.

## Features

- Feature 1
- Feature 2
- Feature 3
""")
    
    (test_dir1 / "getting-started.md").write_text("""# Getting Started

This guide will help you get started.

## Prerequisites

- Item 1
- Item 2

## Installation

Follow these steps.
""")
    
    (test_dir1 / "advanced.md").write_text("""# Advanced Topics

Advanced documentation here.

## Topic 1

Content for topic 1.

## Topic 2

Content for topic 2.
""")
    
    test_dirs["test-docs-1"] = test_dir1
    
    # Test directory 2: nested structure
    test_dir2 = base_path / "test-docs-2"
    test_dir2.mkdir(exist_ok=True)
    
    (test_dir2 / "README.md").write_text("""# Test Documentation 2

Another test directory with nested structure.
""")
    
    nested = test_dir2 / "nested"
    nested.mkdir(exist_ok=True)
    
    (nested / "subpage.md").write_text("""# Subpage

This is a nested page.

See [Getting Started](../getting-started.md) for more info.
""")
    
    (test_dir2 / "overview.md").write_text("""# Overview

Overview of the system.

## Components

- Component A
- Component B
""")
    
    test_dirs["test-docs-2"] = test_dir2
    
    return test_dirs


def create_test_config(test_dirs: Dict[str, Path], config_path: Path) -> None:
    """Create a test configuration file."""
    test_dirs_relative = {}
    repo_root = get_repo_root()
    
    for name, path in test_dirs.items():
        try:
            rel_path = path.relative_to(repo_root)
            test_dirs_relative[name] = str(rel_path)
        except ValueError:
            # If not under repo root, use absolute path (for testing)
            test_dirs_relative[name] = str(path.resolve())
    
    # Get relative paths from repo_root
    repo_root = get_repo_root()
    path1 = test_dirs.get('test-docs-1')
    path2 = test_dirs.get('test-docs-2')
    
    # Calculate relative paths from repo_root
    rel_path1 = str(path1.relative_to(repo_root)) if path1 else "test-docs-1"
    rel_path2 = str(path2.relative_to(repo_root)) if path2 else "test-docs-2"
    
    config_content = f"""destinations:
  - id: hub-proposal
    name: Hub Proposal Documentation (Test)
    confluence:
      url: https://zeta-tm.atlassian.net
      space_key: ~5570580ad15fced37e40a38c7171943fae763b
      root_page_title: Hub Proposal Test
      root_page_id: null
    source:
      folders:
        - path: {rel_path1}
          create_root_parent: true
          title: Test Docs 1
        - path: {rel_path2}
          create_root_parent: true
          title: Test Docs 2
    credentials:
      username: ramki@zeta.tech
      token_env_var: CONFLUENCE_TOKEN
    options:
      add_git_metadata: true
      github_repo_override: null
      dry_run: false
      parallel_threads: 3
"""
    
    config_path.write_text(config_content)


def test_sync_small_directories(dry_run: bool = False):
    """Test syncing small test directories to hub-proposal."""
    print("=" * 80)
    print("Test: Syncing Small Directories to Hub Proposal")
    if dry_run:
        print("(DRY RUN MODE - No changes will be made)")
    print("=" * 80)
    print()
    
    # Check for required environment variable (unless dry run)
    if not dry_run and not os.getenv('CONFLUENCE_TOKEN'):
        print("ERROR: CONFLUENCE_TOKEN environment variable not set")
        print("Please set it before running tests:")
        print("  export CONFLUENCE_TOKEN=your-token")
        print("\nOr run with --dry-run to test without API calls")
        return False
    
    # Get repo root
    repo_root = get_repo_root()
    print(f"Repository root: {repo_root}")
    print()
    
    # Create test directories
    print("Creating test directories...")
    test_base = repo_root / "_confluence_sync" / "test-data"
    test_base.mkdir(exist_ok=True)
    
    # Clean up any existing test directories
    for item in test_base.iterdir():
        if item.is_dir() and item.name.startswith("test-docs"):
            shutil.rmtree(item)
    
    test_dirs = create_test_directories(test_base)
    
    for name, path in test_dirs.items():
        md_files = list(path.rglob("*.md"))
        print(f"  {name}: {len(md_files)} Markdown files")
        for md_file in md_files:
            print(f"    - {md_file.relative_to(path)}")
    print()
    
    # Count total files
    total_files = sum(len(list(d.rglob("*.md"))) for d in test_dirs.values())
    print(f"Total files to sync: {total_files}")
    print()
    
    if total_files >= 20:
        print(f"WARNING: {total_files} files exceeds the limit of 20. Aborting test.")
        return False
    
    # Create test data directory
    test_data_dir = test_base / "data"
    test_data_dir.mkdir(exist_ok=True)
    (test_data_dir / "hub-proposal").mkdir(exist_ok=True)
    
    # Create test config
    test_config_path = test_base / "test-confluence-destinations.yaml"
    create_test_config(test_dirs, test_config_path)
    print(f"Created test config: {test_config_path}")
    print()
    
    # Load config
    try:
        config = load_destination_config(test_config_path, data_dir=test_data_dir)
        dest_config = get_destination(config, "hub-proposal")
    except ConfigError as e:
        print(f"ERROR: Failed to load config: {e}")
        print(f"  Config path: {test_config_path}")
        print(f"  Repo root: {repo_root}")
        print(f"  Test dirs: {[(k, str(v)) for k, v in test_dirs.items()]}")
        return False
    
    # Set dry_run in config
    if dry_run:
        dest_config['options']['dry_run'] = True
    
    # Run sync
    print("Running sync...")
    print("-" * 80)
    try:
        results = sync_destination(
            destination_id="hub-proposal",
            destination_config=dest_config,
            repo_root=repo_root,
            data_dir=test_data_dir,
            dry_run_override=dry_run
        )
        
        print("-" * 80)
        print()
        print("Sync Results:")
        print(f"  Total files processed: {len(results)}")
        
        created = sum(1 for r in results if r.status == 'created')
        updated = sum(1 for r in results if r.status == 'updated')
        skipped = sum(1 for r in results if r.status == 'skipped')
        errors = sum(1 for r in results if r.status == 'error')
        
        print(f"  Created: {created}")
        print(f"  Updated: {updated}")
        print(f"  Skipped: {skipped}")
        print(f"  Errors: {errors}")
        print()
        
        if errors > 0:
            print("Errors encountered:")
            for result in results:
                if result.status == 'error':
                    print(f"  - {result.file_path}: {result.error_message}")
            print()
        
        # Show some example results
        if results:
            print("Sample results:")
            for result in results[:5]:
                status_icon = "✓" if result.status in ['created', 'updated'] else "⊘" if result.status == 'skipped' else "✗"
                print(f"  {status_icon} {result.file_path} -> {result.status}")
                if result.page_id:
                    print(f"      Page ID: {result.page_id}")
                    print(f"      URL: {result.confluence_url}")
            if len(results) > 5:
                print(f"  ... and {len(results) - 5} more")
            print()
        
        return errors == 0
        
    except Exception as e:
        print(f"ERROR: Sync failed with exception: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_sync_existing_hub_proposal(dry_run: bool = False):
    """Test syncing a small subset of existing directories to hub-proposal."""
    print("=" * 80)
    print("Test: Syncing Existing Small Directories to Hub Proposal")
    if dry_run:
        print("(DRY RUN MODE - No changes will be made)")
    print("=" * 80)
    print()
    
    # Check for required environment variable (unless dry run)
    if not dry_run and not os.getenv('CONFLUENCE_TOKEN'):
        print("ERROR: CONFLUENCE_TOKEN environment variable not set")
        print("Or run with --dry-run to test without API calls")
        return False
    
    # Get repo root
    repo_root = get_repo_root()
    print(f"Repository root: {repo_root}")
    print()
    
    # Find small directories in olympus-hub-docs
    hub_docs = repo_root / "olympus-hub-docs"
    if not hub_docs.exists():
        print(f"ERROR: {hub_docs} does not exist")
        return False
    
    # Find directories with few files
    small_dirs = []
    for item in hub_docs.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            md_files = list(item.rglob("*.md"))
            if 0 < len(md_files) < 10:  # Between 1 and 9 files
                small_dirs.append((item, len(md_files)))
    
    if not small_dirs:
        print("No small directories found in olympus-hub-docs")
        return False
    
    # Sort by file count and take smallest
    small_dirs.sort(key=lambda x: x[1])
    test_dir, file_count = small_dirs[0]
    
    print(f"Selected directory: {test_dir.relative_to(repo_root)}")
    print(f"  Files: {file_count}")
    print()
    
    # Load existing config (data directory is sibling to scripts directory)
    data_dir = Path(__file__).parent.parent / "data"
    try:
        config = load_destination_config(data_dir=data_dir)
        dest_config = get_destination(config, "hub-proposal")
    except ConfigError as e:
        print(f"ERROR: Failed to load config: {e}")
        return False
    
    # Temporarily modify config to use only the test directory
    original_folders = dest_config['source']['folders']
    dest_config['source']['folders'] = [
        {
            'path': str(test_dir.relative_to(repo_root)),
            'create_root_parent': True,
            'title': f"Test: {test_dir.name}"
        }
    ]
    
    # Set dry_run in config
    if dry_run:
        dest_config['options']['dry_run'] = True
    
    print("Running sync with modified config...")
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
        print("Sync Results:")
        print(f"  Total files processed: {len(results)}")
        
        created = sum(1 for r in results if r.status == 'created')
        updated = sum(1 for r in results if r.status == 'updated')
        skipped = sum(1 for r in results if r.status == 'skipped')
        errors = sum(1 for r in results if r.status == 'error')
        
        print(f"  Created: {created}")
        print(f"  Updated: {updated}")
        print(f"  Skipped: {skipped}")
        print(f"  Errors: {errors}")
        print()
        
        # Restore original config
        dest_config['source']['folders'] = original_folders
        
        return errors == 0
        
    except Exception as e:
        print(f"ERROR: Sync failed with exception: {e}")
        import traceback
        traceback.print_exc()
        # Restore original config
        dest_config['source']['folders'] = original_folders
        return False


def main():
    """Run all tests."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test Confluence sync functionality')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode (no API calls)')
    parser.add_argument('--test', choices=['1', '2', 'all'], default='all', help='Which test to run (1, 2, or all)')
    args = parser.parse_args()
    
    print("\n" + "=" * 80)
    print("Confluence Sync Tests")
    if args.dry_run:
        print("(DRY RUN MODE - No changes will be made)")
    print("=" * 80 + "\n")
    
    test1_result = None
    test2_result = None
    
    # Test 1: Sync test directories
    if args.test in ['1', 'all']:
        print("\n[Test 1] Syncing Small Test Directories")
        print("-" * 80)
        test1_result = test_sync_small_directories(dry_run=args.dry_run)
    
    # Test 2: Sync existing small directory
    if args.test in ['2', 'all']:
        print("\n[Test 2] Syncing Existing Small Directory")
        print("-" * 80)
        test2_result = test_sync_existing_hub_proposal(dry_run=args.dry_run)
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    if test1_result is not None:
        print(f"Test 1 (Test Directories): {'PASSED' if test1_result else 'FAILED'}")
    if test2_result is not None:
        print(f"Test 2 (Existing Directory): {'PASSED' if test2_result else 'FAILED'}")
    print()
    
    all_passed = (test1_result is None or test1_result) and (test2_result is None or test2_result)
    if all_passed:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
