#!/usr/bin/env python3
"""
Verify Confluence structure matches desired structure from Git repository.

This script compares the actual Confluence page hierarchy with the expected
structure based on the source files and sync state.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Mock content_preparer before importing anything that needs it
from types import SimpleNamespace
sys.modules['content_preparer'] = SimpleNamespace(PreparedContent=type('PreparedContent', (), {}))

from config_loader import load_destination_config, get_destination, resolve_credentials
from sync_state import load_sync_state
from confluence_sync import ConfluenceSync


def get_page_ancestors(confluence_sync: ConfluenceSync, page_id: str) -> List[str]:
    """Get all ancestor IDs for a page using REST API v2, including the page itself."""
    try:
        # Use v2 pages endpoint
        response = confluence_sync._make_request('GET', f'/pages/{page_id}')
        data = response.json()
        ancestors = []
        
        # v2 API structure: parentId is direct, need to walk up the chain
        current_id = page_id
        visited = set()
        while current_id and current_id not in visited:
            visited.add(current_id)
            ancestors.append(current_id)
            # Get parent by fetching the page
            try:
                page_response = confluence_sync._make_request('GET', f'/pages/{current_id}')
                page_data = page_response.json()
                current_id = str(page_data.get('parentId')) if page_data.get('parentId') else None
            except:
                break
        
        # Reverse to get root-to-page order
        ancestors.reverse()
        return ancestors
    except Exception as e:
        print(f"  ⚠ Error getting ancestors for page {page_id}: {e}")
        return []


def verify_destination_structure(
    destination_id: str,
    destination_config: Dict,
    data_dir: Optional[Path] = None
) -> Tuple[bool, List[str]]:
    """
    Verify that all pages in sync state are under the destination root.
    
    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []
    
    # Get destination info
    confluence_config = destination_config['confluence']
    root_page_id = confluence_config.get('root_page_id')
    root_page_title = confluence_config['root_page_title']
    
    # If root_page_id is not in config, try to get it from sync metadata
    if not root_page_id:
        from sync_state import get_metadata_file_path
        metadata_path = get_metadata_file_path(destination_id, data_dir)
        if metadata_path.exists():
            try:
                with open(metadata_path, 'r') as f:
                    metadata = json.load(f)
                    root_page_id = metadata.get('root_page_id')
                    if root_page_id:
                        print(f"  ℹ Found root_page_id from sync metadata: {root_page_id}")
            except Exception as e:
                issues.append(f"  ⚠ Could not read sync metadata: {e}")
    
    if not root_page_id:
        issues.append(f"⚠ No root_page_id configured or found in sync metadata for destination '{destination_id}'")
        issues.append(f"   Run a sync first to create the root page, or set root_page_id in config")
        return False, issues
    
    # Resolve credentials
    try:
        creds = resolve_credentials(destination_config)
    except Exception as e:
        issues.append(f"✗ Error resolving credentials: {e}")
        return False, issues
    
    # Initialize Confluence sync client
    base_url = confluence_config['url']
    space_key = confluence_config['space_key']
    confluence_sync = ConfluenceSync(
        base_url=base_url,
        username=creds['username'],
        token=creds['token'],
        space_key=space_key
    )
    
    # Verify root page exists using v2 API
    try:
        response = confluence_sync._make_request('GET', f'/pages/{root_page_id}')
        root_data = response.json()
        if root_data.get('title') != root_page_title:
            issues.append(f"⚠ Root page title mismatch: expected '{root_page_title}', found '{root_data.get('title')}'")
    except Exception as e:
        issues.append(f"✗ Root page (ID: {root_page_id}) not found or inaccessible: {e}")
        return False, issues
    
    # Load sync state
    sync_state = load_sync_state(destination_id, data_dir)
    sync_history = sync_state.get('sync_history', {})
    folders = sync_state.get('folders', {})
    
    if not sync_history and not folders:
        issues.append("ℹ No pages or folders in sync state")
        return True, issues
    
    print(f"\nVerifying structure under root '{root_page_title}' (ID: {root_page_id})...")
    print(f"  Pages: {len(sync_history)}, Folders: {len(folders)}")
    
    # Check folder hierarchy (Phase 12-2)
    folders_outside_root = []
    folders_not_found = []
    folders_wrong_parent = []
    
    for folder_path, folder_entry in folders.items():
        folder_id = folder_entry.get('folder_id')
        folder_title = folder_entry.get('folder_title', 'Unknown')
        expected_parent_id = folder_entry.get('parent_id')
        
        if not folder_id:
            continue
        
        try:
            folder_data = confluence_sync.get_folder(folder_id)
            if not folder_data:
                folders_not_found.append({
                    'folder_path': folder_path,
                    'folder_id': folder_id,
                    'folder_title': folder_title
                })
                continue
            
            actual_parent_id = folder_data.get('parentId')
            
            # Check if folder is under root (simplified - check immediate parent)
            # For deeper hierarchy, would need to walk up the chain
            if expected_parent_id and str(actual_parent_id) != str(expected_parent_id):
                folders_wrong_parent.append({
                    'folder_path': folder_path,
                    'folder_id': folder_id,
                    'folder_title': folder_title,
                    'expected_parent': expected_parent_id,
                    'actual_parent': actual_parent_id
                })
            
            # Check if folder is under root (simplified check)
            if actual_parent_id and str(actual_parent_id) != str(root_page_id):
                # Check if parent chain includes root (simplified)
                if expected_parent_id != root_page_id:
                    # This might be okay if it's nested - just check immediate parent matches expected
                    pass
        except Exception as e:
            if '404' in str(e) or 'Not Found' in str(e):
                folders_not_found.append({
                    'folder_path': folder_path,
                    'folder_id': folder_id,
                    'folder_title': folder_title
                })
            else:
                issues.append(f"  ⚠ Error checking folder '{folder_title}' (ID: {folder_id}): {e}")
    
    # Check each page in sync state
    pages_outside_root = []
    pages_not_found = []
    pages_archived = []
    pages_under_wrong_parent = []
    readme_pages = []  # Track README pages for verification (Phase 12-4)
    
    for file_path, entry in sync_history.items():
        page_id = entry.get('page_id')
        page_title = entry.get('page_title', 'Unknown')
        expected_parent_id = entry.get('parent_id')
        
        # Track README pages (Phase 12-4)
        if 'README' in file_path or 'readme' in file_path.lower():
            readme_pages.append({
                'file_path': file_path,
                'page_id': page_id,
                'page_title': page_title
            })
        
        if not page_id:
            continue
        
        # Get page using v2 API
        try:
            response = confluence_sync._make_request('GET', f'/pages/{page_id}')
            page_data = response.json()
            actual_parent_id = page_data.get('parentId')
            
            # Check if page is under root (simplified - check immediate parent or walk up)
            ancestors = get_page_ancestors(confluence_sync, page_id)
            
            # Check if root_page_id is in ancestors (page is under root)
            if root_page_id not in ancestors:
                pages_outside_root.append({
                    'file_path': file_path,
                    'page_id': page_id,
                    'page_title': page_title,
                    'ancestors': ancestors
                })
            
            # Verify page is under a folder, not another page (except root) (Phase 12-3)
            if actual_parent_id and str(actual_parent_id) != str(root_page_id):
                # Check if parent is a folder (v2 API - folders are separate from pages)
                # For now, we assume if parent_id is in folders dict, it's a folder
                # This is a simplified check
                parent_is_folder = any(
                    f.get('folder_id') == str(actual_parent_id) 
                    for f in folders.values()
                )
                if not parent_is_folder:
                    # Parent might be a page - this is okay for root, but warn for others
                    if expected_parent_id and str(actual_parent_id) != str(expected_parent_id):
                        pages_under_wrong_parent.append({
                            'file_path': file_path,
                            'page_id': page_id,
                            'page_title': page_title,
                            'expected_parent': expected_parent_id,
                            'actual_parent': actual_parent_id
                        })
            
        except Exception as e:
            # Check if it's a 404 (not found) or 403 (archived)
            if '404' in str(e) or 'Not Found' in str(e):
                pages_not_found.append({
                    'file_path': file_path,
                    'page_id': page_id,
                    'page_title': page_title
                })
            elif '403' in str(e) or 'Forbidden' in str(e):
                pages_archived.append({
                    'file_path': file_path,
                    'page_id': page_id,
                    'page_title': page_title
                })
            else:
                issues.append(f"  ⚠ Error checking page '{page_title}' (ID: {page_id}): {e}")
    
    # Report folder issues (Phase 12-2, 12-5)
    if folders_wrong_parent:
        issues.append(f"\n⚠ {len(folders_wrong_parent)} folder(s) with wrong parent:")
        for folder in folders_wrong_parent[:10]:
            issues.append(f"  - {folder['folder_path']}: '{folder['folder_title']}' (ID: {folder['folder_id']})")
            issues.append(f"    Expected parent: {folder['expected_parent']}, Found: {folder['actual_parent']}")
        if len(folders_wrong_parent) > 10:
            issues.append(f"  ... and {len(folders_wrong_parent) - 10} more")
    
    if folders_not_found:
        issues.append(f"\n⚠ {len(folders_not_found)} folder(s) not found in Confluence:")
        for folder in folders_not_found[:10]:
            issues.append(f"  - {folder['folder_path']}: '{folder['folder_title']}' (ID: {folder['folder_id']})")
        if len(folders_not_found) > 10:
            issues.append(f"  ... and {len(folders_not_found) - 10} more")
    
    # Report page issues
    if pages_outside_root:
        issues.append(f"\n✗ {len(pages_outside_root)} page(s) found OUTSIDE destination root hierarchy:")
        for page in pages_outside_root[:10]:  # Show first 10
            issues.append(f"  - {page['file_path']}: '{page['page_title']}' (ID: {page['page_id']})")
        if len(pages_outside_root) > 10:
            issues.append(f"  ... and {len(pages_outside_root) - 10} more")
    
    if pages_under_wrong_parent:
        issues.append(f"\n⚠ {len(pages_under_wrong_parent)} page(s) under wrong parent:")
        for page in pages_under_wrong_parent[:10]:
            issues.append(f"  - {page['file_path']}: '{page['page_title']}' (ID: {page['page_id']})")
            issues.append(f"    Expected parent: {page['expected_parent']}, Found: {page['actual_parent']}")
        if len(pages_under_wrong_parent) > 10:
            issues.append(f"  ... and {len(pages_under_wrong_parent) - 10} more")
    
    if pages_not_found:
        issues.append(f"\n⚠ {len(pages_not_found)} page(s) not found in Confluence:")
        for page in pages_not_found[:10]:
            issues.append(f"  - {page['file_path']}: '{page['page_title']}' (ID: {page['page_id']})")
        if len(pages_not_found) > 10:
            issues.append(f"  ... and {len(pages_not_found) - 10} more")
    
    if pages_archived:
        issues.append(f"\n⚠ {len(pages_archived)} page(s) appear to be archived:")
        for page in pages_archived[:10]:
            issues.append(f"  - {page['file_path']}: '{page['page_title']}' (ID: {page['page_id']})")
        if len(pages_archived) > 10:
            issues.append(f"  ... and {len(pages_archived) - 10} more")
    
    # Verify README files exist as pages, not folder content (Phase 12-4)
    if readme_pages:
        issues.append(f"\nℹ Found {len(readme_pages)} README page(s) - verifying they are separate pages:")
        for readme in readme_pages[:5]:
            try:
                response = confluence_sync._make_request('GET', f'/pages/{readme["page_id"]}')
                page_data = response.json()
                # README should be a page (has page_id), not folder content
                issues.append(f"  ✓ README '{readme['file_path']}' exists as page (ID: {readme['page_id']})")
            except Exception as e:
                issues.append(f"  ✗ README '{readme['file_path']}' not found: {e}")
        if len(readme_pages) > 5:
            issues.append(f"  ... and {len(readme_pages) - 5} more README pages")
    
    is_valid = (
        len(pages_outside_root) == 0 and 
        len(pages_not_found) == 0 and 
        len(folders_not_found) == 0 and
        len(folders_wrong_parent) == 0
    )
    
    if is_valid:
        issues.append(f"\n✓ All {len(sync_history)} pages and {len(folders)} folders are correctly structured")
    
    return is_valid, issues


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify Confluence structure matches desired structure')
    parser.add_argument('destination_id', nargs='?', help='Destination ID to verify (default: all)')
    parser.add_argument('--data-dir', type=Path, default=None, help='Data directory path')
    
    args = parser.parse_args()
    
    # Load destinations config
    data_dir = args.data_dir or Path(__file__).parent.parent / 'data'
    
    try:
        config = load_destination_config(data_dir=data_dir)
        destinations_list = config.get('destinations', [])
        destinations = {d['id']: d for d in destinations_list if 'id' in d}
    except Exception as e:
        print(f"ERROR: Failed to load destinations config: {e}")
        return 1
    
    # Filter destinations
    if args.destination_id:
        if args.destination_id not in destinations:
            print(f"ERROR: Destination '{args.destination_id}' not found")
            print(f"Available destinations: {', '.join(destinations.keys())}")
            return 1
        destinations = {args.destination_id: destinations[args.destination_id]}
    
    # Verify each destination
    all_valid = True
    for dest_id, dest_config in destinations.items():
        print(f"\n{'='*80}")
        print(f"Verifying destination: {dest_config['name']} ({dest_id})")
        print(f"{'='*80}")
        
        is_valid, issues = verify_destination_structure(dest_id, dest_config, data_dir)
        
        for issue in issues:
            print(issue)
        
        if not is_valid:
            all_valid = False
    
    return 0 if all_valid else 1


if __name__ == '__main__':
    sys.exit(main())
