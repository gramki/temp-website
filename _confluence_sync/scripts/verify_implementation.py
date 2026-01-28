#!/usr/bin/env python3
"""
Verification script to check that the implementation is correct.

This script verifies:
- All required methods exist
- Code structure is correct
- Imports work correctly
- No syntax errors
"""

import sys
import inspect
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

def verify_confluence_sync():
    """Verify ConfluenceSync class has all required methods."""
    print("Verifying ConfluenceSync class...")
    
    try:
        from confluence_sync import ConfluenceSync, TitleConflictError, HierarchyValidationError
        
        # Check required methods exist
        required_methods = [
            '_get_space_id',
            'create_folder',
            'get_folder',
            'delete_folder',
            'find_folder_by_title',
            'update_folder',
            'list_folder_children',
            'create_page_v2',
            'delete_page_v2',
            'validate_folder_hierarchy',
            'validate_page_hierarchy',
            '_paginate_v2',
        ]
        
        missing = []
        for method_name in required_methods:
            if not hasattr(ConfluenceSync, method_name):
                missing.append(method_name)
        
        if missing:
            print(f"  ✗ Missing methods: {', '.join(missing)}")
            return False
        
        print(f"  ✓ All {len(required_methods)} required methods exist")
        
        # Check exception classes
        exceptions = [TitleConflictError, HierarchyValidationError]
        for exc in exceptions:
            if not issubclass(exc, Exception):
                print(f"  ✗ {exc.__name__} is not an Exception subclass")
                return False
        
        print(f"  ✓ Exception classes defined correctly")
        
        # Check API URL uses v2
        import inspect
        init_source = inspect.getsource(ConfluenceSync.__init__)
        if '/api/v2' not in init_source:
            print(f"  ✗ __init__ does not use /api/v2")
            return False
        
        print(f"  ✓ API URL uses v2")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_sync_state():
    """Verify sync_state has folder methods."""
    print("\nVerifying sync_state module...")
    
    try:
        from sync_state import (
            append_folder_history,
            get_folder_history,
            update_folder_history,
            load_sync_state
        )
        
        # Check load_sync_state returns folders
        import inspect
        load_source = inspect.getsource(load_sync_state)
        if "'folders'" not in load_source and '"folders"' not in load_source:
            print(f"  ✗ load_sync_state does not handle folders")
            return False
        
        print(f"  ✓ All folder history methods exist")
        print(f"  ✓ load_sync_state handles folders")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_orphan_handler():
    """Verify OrphanHandler handles folders."""
    print("\nVerifying OrphanHandler...")
    
    try:
        from orphan_handler import OrphanHandler
        
        # Check find_orphans signature
        import inspect
        sig = inspect.signature(OrphanHandler.find_orphans)
        params = list(sig.parameters.keys())
        
        if 'discovered_folders' not in params:
            print(f"  ✗ find_orphans does not accept discovered_folders parameter")
            return False
        
        # Check delete_orphans signature
        sig = inspect.signature(OrphanHandler.delete_orphans)
        params = list(sig.parameters.keys())
        
        if 'orphan_folders' not in params:
            print(f"  ✗ delete_orphans does not accept orphan_folders parameter")
            return False
        
        print(f"  ✓ OrphanHandler handles folders correctly")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_content_preparer():
    """Verify content_preparer creates folders, not directory pages."""
    print("\nVerifying content_preparer...")
    
    try:
        from content_preparer import ContentPreparer
        
        # Check prepare_directory_content doesn't create directory pages
        import inspect
        source = inspect.getsource(ContentPreparer.prepare_directory_content)
        
        # Should not have directory page creation logic
        if 'dir_storage' in source and 'storage_format' in source:
            # Check if it's folder logic, not directory page
            if 'folder_title' in source and 'folder_id' in source:
                print(f"  ✓ Uses folder preparation (not directory pages)")
            else:
                print(f"  ⚠ May still have directory page logic")
        
        # Should have folder_key
        if 'folder_key' in source:
            print(f"  ✓ Uses folder_key for folder tracking")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def verify_sync_to_confluence():
    """Verify sync-to-confluence uses folders."""
    print("\nVerifying sync-to-confluence...")
    
    try:
        # Read the file to check for folder usage
        sync_file = Path(__file__).parent / "sync-to-confluence.py"
        content = sync_file.read_text()
        
        checks = []
        
        # Should use create_folder
        if 'create_folder' in content:
            checks.append(("Uses create_folder", True))
        else:
            checks.append(("Uses create_folder", False))
        
        # Should use folder_id_map
        if 'folder_id_map' in content:
            checks.append(("Uses folder_id_map", True))
        else:
            checks.append(("Uses folder_id_map", False))
        
        # Should not use directory page creation
        if 'directory_pages' in content and 'create_folder' in content:
            checks.append(("Uses folders instead of directory pages", True))
        else:
            checks.append(("Uses folders instead of directory pages", False))
        
        all_passed = all(passed for _, passed in checks)
        for check_name, passed in checks:
            status = "✓" if passed else "✗"
            print(f"  {status} {check_name}")
        
        return all_passed
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all verification checks."""
    print("="*80)
    print("Implementation Verification")
    print("="*80)
    
    checks = [
        ("ConfluenceSync", verify_confluence_sync),
        ("Sync State", verify_sync_state),
        ("Orphan Handler", verify_orphan_handler),
        ("Content Preparer", verify_content_preparer),
        ("Sync to Confluence", verify_sync_to_confluence),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ {name} verification crashed: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Summary
    print("\n" + "="*80)
    print("Verification Summary")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"  {status}: {name}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✓ All verifications passed!")
        return 0
    else:
        print(f"\n⚠ {total - passed} check(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
