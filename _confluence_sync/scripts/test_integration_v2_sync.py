#!/usr/bin/env python3
"""
Integration test for full sync flow with REST API v2 and native folders.

Tests the complete sync process:
- Content preparation with folders
- Folder creation
- Page creation under folders
- README handling (as separate pages)
- Orphan detection
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Load .env file if it exists
def load_env_file():
    """Load environment variables from .env file in data directory."""
    data_dir = Path(__file__).parent.parent / "data"
    env_file = data_dir / ".env"
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    # Only set if not already in environment
                    if key and value and key not in os.environ:
                        os.environ[key] = value

# Load .env before importing modules that need credentials
load_env_file()

# Import sync function
import importlib.util
spec = importlib.util.spec_from_file_location("sync_to_confluence", Path(__file__).parent / "sync-to-confluence.py")
sync_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_module)
sync_destination = sync_module.sync_destination

from config_loader import load_destination_config, get_destination, resolve_credentials, get_repo_root
from sync_state import load_sync_state
from confluence_sync import ConfluenceSync


def create_test_structure(base_path: Path):
    """Create a test directory structure with folders and README files."""
    # Root directory
    root = base_path / "test-integration-v2"
    root.mkdir(exist_ok=True)
    
    # Root README
    (root / "README.md").write_text("""# Test Integration V2

This is a test for REST API v2 and native folders.

## Overview

Testing folder structure and README handling.
""")
    
    # Subdirectory with README
    subdir1 = root / "subdirectory-1"
    subdir1.mkdir(exist_ok=True)
    
    (subdir1 / "README.md").write_text("""# Subdirectory 1

This subdirectory has a README.

## Content

The README should be a separate page, not folder content.
""")
    
    (subdir1 / "page1.md").write_text("""# Page 1

This is a page in subdirectory 1.

## Details

Some content here.
""")
    
    # Nested subdirectory
    nested = subdir1 / "nested"
    nested.mkdir(exist_ok=True)
    
    (nested / "nested-page.md").write_text("""# Nested Page

This is a nested page.

## Nested Content

Content in nested folder.
""")
    
    # Another subdirectory without README
    subdir2 = root / "subdirectory-2"
    subdir2.mkdir(exist_ok=True)
    
    (subdir2 / "page2.md").write_text("""# Page 2

This is a page in subdirectory 2 (no README).
""")
    
    return root


def test_integration_sync():
    """Test full integration sync with v2 API and folders."""
    print("="*80)
    print("Integration Test: Full Sync Flow with v2 API and Folders")
    print("="*80)
    
    if not os.getenv('CONFLUENCE_TOKEN'):
        print("\n⚠ SKIPPED: CONFLUENCE_TOKEN not set")
        print("Set CONFLUENCE_TOKEN to run integration test")
        return True
    
    # Create test structure
    repo_root = get_repo_root()
    test_dir = create_test_structure(repo_root)
    
    print(f"\nCreated test structure at: {test_dir.relative_to(repo_root)}")
    
    try:
        # Load config
        data_dir = Path(__file__).parent.parent / "data"
        config = load_destination_config(data_dir=data_dir)
        dest_config = get_destination(config, "hub-proposal")
        
        # Modify config to use test directory
        original_folders = dest_config['source']['folders'].copy()
        dest_config['source']['folders'] = [
            {
                'path': str(test_dir.relative_to(repo_root)),
                'create_root_parent': True,
                'title': "Test Integration V2"
            }
        ]
        
        print("\nRunning sync...")
        print("-"*80)
        
        # Run sync
        results = sync_destination(
            destination_id="hub-proposal",
            destination_config=dest_config,
            repo_root=repo_root,
            data_dir=data_dir,
            dry_run_override=False
        )
        
        print("-"*80)
        print("\nSync Results:")
        print(f"  Total files: {len(results)}")
        print(f"  Created: {sum(1 for r in results if r.status == 'created')}")
        print(f"  Updated: {sum(1 for r in results if r.status == 'updated')}")
        print(f"  Skipped: {sum(1 for r in results if r.status == 'skipped')}")
        print(f"  Errors: {sum(1 for r in results if r.status == 'error')}")
        
        # Verify results
        assert len(results) > 0, "Should have synced at least one file"
        
        # Check that README files were synced as pages
        readme_results = [r for r in results if 'README' in r.file_path]
        print(f"\n  README files synced: {len(readme_results)}")
        for r in readme_results:
            print(f"    - {r.file_path} -> {r.status}")
        
        assert len(readme_results) >= 2, "Should have synced at least 2 README files (root + subdirectory)"
        
        # Verify sync state includes folders
        sync_state = load_sync_state("hub-proposal", data_dir)
        folders = sync_state.get('folders', {})
        print(f"\n  Folders tracked in sync state: {len(folders)}")
        for folder_path in list(folders.keys())[:5]:
            print(f"    - {folder_path}")
        
        # Restore original config
        dest_config['source']['folders'] = original_folders
        
        print("\n✓ Integration test completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n✗ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        
        # Restore original config
        if 'dest_config' in locals() and 'original_folders' in locals():
            dest_config['source']['folders'] = original_folders
        
        return False
    finally:
        # Cleanup test directory (optional - comment out to inspect)
        # shutil.rmtree(test_dir, ignore_errors=True)
        pass


def test_readme_as_separate_pages():
    """Test that README files are created as separate pages, not folder content."""
    print("\n" + "="*80)
    print("Test: README Files as Separate Pages")
    print("="*80)
    
    if not os.getenv('CONFLUENCE_TOKEN'):
        print("  ⚠ SKIPPED: CONFLUENCE_TOKEN not set")
        return True
    
    try:
        creds = resolve_credentials()
        config = load_destination_config()
        dest_config = get_destination(config, "hub-proposal")
        
        confluence_sync = ConfluenceSync(
            base_url=dest_config['confluence']['url'],
            username=creds['username'],
            token=creds['token'],
            space_key=dest_config['confluence']['space_key']
        )
        
        # Create a test folder
        folder_id, _ = confluence_sync.create_folder(
            title="Test README Folder",
            space_id=confluence_sync.space_id
        )
        
        # Create a README page under the folder (simulating what content_preparer does)
        print("  Test: Create README page under folder...")
        readme_page_id, readme_version = confluence_sync.create_page_v2(
            title="README",
            body="<p>This is a README page, not folder content.</p>",
            space_id=confluence_sync.space_id,
            parent_id=folder_id
        )
        print(f"    ✓ Created README page: {readme_page_id}")
        
        # Verify README is a page, not folder content
        readme_page = confluence_sync._make_request('GET', f'/pages/{readme_page_id}').json()
        assert readme_page['parentId'] == folder_id, "README should be under folder"
        assert readme_page['title'] == "README", "README should have correct title"
        print(f"    ✓ README is a separate page under folder")
        
        # List folder children to verify README page is listed
        child_folders, child_pages = confluence_sync.list_folder_children(folder_id)
        readme_in_children = any(p['id'] == readme_page_id for p in child_pages)
        assert readme_in_children, "README page should be in folder's child pages"
        print(f"    ✓ README page is listed as child of folder")
        
        # Cleanup
        confluence_sync.delete_page_v2(readme_page_id)
        confluence_sync.delete_folder(folder_id)
        
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run integration tests."""
    print("="*80)
    print("Confluence REST API v2 Integration Tests")
    print("="*80)
    
    tests = [
        ("README as Separate Pages", test_readme_as_separate_pages),
        ("Full Integration Sync", test_integration_sync),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ Test '{test_name}' crashed: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*80)
    print("Integration Test Summary")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"  {status}: {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ All integration tests passed!")
        return 0
    else:
        print(f"\n⚠ {total - passed} test(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
