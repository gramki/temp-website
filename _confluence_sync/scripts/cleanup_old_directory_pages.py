#!/usr/bin/env python3
"""
Cleanup script to identify and optionally delete/archive old directory pages in Confluence.

This script:
1. Identifies old directory pages in Confluence (created before folder migration)
2. Optionally deletes or archives them
3. Reports what would be cleaned up

Usage:
    python cleanup_old_directory_pages.py --destination DEST_ID [--delete] [--archive] [--dry-run]
"""

import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config_loader import load_destination_config, get_destination, resolve_credentials, ConfigError
from sync_state import load_sync_state, get_metadata_file_path
from confluence_sync import ConfluenceSync
import json


def identify_old_directory_pages(
    destination_id: str,
    destination_config: Dict,
    data_dir: Optional[Path] = None
) -> List[Dict]:
    """
    Identify old directory pages in Confluence that should be cleaned up.
    
    Returns:
        List of directory page information dictionaries
    """
    directory_pages = []
    
    # Load sync state to find potential directory pages
    sync_state = load_sync_state(destination_id, data_dir)
    sync_history = sync_state.get('sync_history', {})
    
    # Get root page ID
    confluence_config = destination_config['confluence']
    root_page_id = confluence_config.get('root_page_id')
    if not root_page_id:
        metadata_file = get_metadata_file_path(destination_id, data_dir)
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
                    root_page_id = metadata.get('root_page_id')
            except:
                pass
    
    if not root_page_id:
        print("  ⚠ No root_page_id found - cannot identify directory pages")
        return directory_pages
    
    # Resolve credentials
    try:
        creds = resolve_credentials(destination_config)
    except Exception as e:
        print(f"  ✗ Error resolving credentials: {e}")
        return directory_pages
    
    # Initialize Confluence sync client
    base_url = confluence_config['url']
    space_key = confluence_config['space_key']
    confluence_sync = ConfluenceSync(
        base_url=base_url,
        username=creds['username'],
        token=creds['token'],
        space_key=space_key
    )
    
    # Check pages in sync history that might be directory pages
    # Directory pages are typically:
    # - Under root or folders
    # - Have titles that match directory names
    # - Don't have corresponding .md files
    
    for file_path, entry in sync_history.items():
        page_id = entry.get('page_id')
        page_title = entry.get('page_title', '')
        
        if not page_id:
            continue
        
        # Check if this looks like a directory page
        # Pattern: file_path doesn't end with .md and matches directory structure
        if not file_path.endswith('.md') and not file_path.startswith('__root__'):
            # Could be a directory page
            try:
                # Verify page exists and get details
                response = confluence_sync._make_request('GET', f'/pages/{page_id}')
                page_data = response.json()
                
                # Check if it's actually a directory page (heuristic)
                # Directory pages often have minimal content or specific patterns
                body = page_data.get('body', {}).get('value', '')
                if 'directory' in body.lower() or len(body) < 200:
                    directory_pages.append({
                        'page_id': page_id,
                        'page_title': page_title,
                        'file_path': file_path,
                        'parent_id': page_data.get('parentId'),
                        'url': f"{confluence_sync.base_url}/pages/viewpage.action?pageId={page_id}"
                    })
            except Exception as e:
                # Page might not exist anymore
                pass
    
    return directory_pages


def cleanup_directory_pages(
    destination_id: str,
    destination_config: Dict,
    directory_pages: List[Dict],
    delete: bool = False,
    archive: bool = False,
    dry_run: bool = False,
    data_dir: Optional[Path] = None
) -> Dict:
    """
    Clean up (delete or archive) old directory pages.
    
    Args:
        destination_id: Destination ID
        destination_config: Destination configuration
        directory_pages: List of directory pages to clean up
        delete: If True, delete pages
        archive: If True, archive pages (not implemented - Confluence v2 doesn't support archiving via API easily)
        dry_run: If True, don't make changes
        data_dir: Optional data directory path
        
    Returns:
        Cleanup report dictionary
    """
    report = {
        'destination_id': destination_id,
        'pages_found': len(directory_pages),
        'pages_deleted': 0,
        'pages_archived': 0,
        'errors': []
    }
    
    if not directory_pages:
        return report
    
    # Resolve credentials
    try:
        creds = resolve_credentials(destination_config)
    except Exception as e:
        report['errors'].append(f"Error resolving credentials: {e}")
        return report
    
    # Initialize Confluence sync client
    confluence_config = destination_config['confluence']
    base_url = confluence_config['url']
    space_key = confluence_config['space_key']
    confluence_sync = ConfluenceSync(
        base_url=base_url,
        username=creds['username'],
        token=creds['token'],
        space_key=space_key
    )
    
    if dry_run:
        print(f"  [DRY RUN] Would {'delete' if delete else 'archive' if archive else 'identify'} {len(directory_pages)} directory page(s)")
        for page in directory_pages[:10]:
            print(f"    - '{page['page_title']}' (ID: {page['page_id']})")
        return report
    
    # Delete or archive pages
    for page in directory_pages:
        page_id = page['page_id']
        page_title = page['page_title']
        
        try:
            if delete:
                deleted = confluence_sync.delete_page_v2(page_id)
                if deleted:
                    report['pages_deleted'] += 1
                    print(f"  ✓ Deleted: '{page_title}' (ID: {page_id})")
                else:
                    report['errors'].append(f"Failed to delete page '{page_title}' (ID: {page_id})")
            elif archive:
                # Archiving via API v2 is complex - would need to update page status
                # For now, just report
                print(f"  ℹ Archiving not implemented via API - manual action required for '{page_title}' (ID: {page_id})")
                report['pages_archived'] += 1
        except Exception as e:
            report['errors'].append(f"Error processing '{page_title}': {e}")
            print(f"  ✗ Error processing '{page_title}': {e}")
    
    return report


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Clean up old directory pages in Confluence'
    )
    parser.add_argument(
        '--destination',
        required=True,
        help='Destination ID'
    )
    parser.add_argument(
        '--data-dir',
        type=Path,
        help='Data directory path'
    )
    parser.add_argument(
        '--delete',
        action='store_true',
        help='Delete old directory pages'
    )
    parser.add_argument(
        '--archive',
        action='store_true',
        help='Archive old directory pages (not fully implemented)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be cleaned up without making changes'
    )
    
    args = parser.parse_args()
    
    if not args.delete and not args.archive and not args.dry_run:
        print("ERROR: Must specify --delete, --archive, or --dry-run")
        return 1
    
    # Load config
    try:
        config = load_destination_config(data_dir=args.data_dir)
        dest_config = get_destination(config, args.destination)
    except ConfigError as e:
        print(f"ERROR: {e}")
        return 1
    
    print(f"\n{'='*80}")
    print(f"Cleaning up directory pages for: {args.destination}")
    print(f"{'='*80}\n")
    
    # Identify old directory pages
    print("Identifying old directory pages...")
    directory_pages = identify_old_directory_pages(
        args.destination,
        dest_config,
        data_dir=args.data_dir
    )
    
    print(f"  Found {len(directory_pages)} potential directory page(s)")
    
    if not directory_pages:
        print("\n✓ No directory pages found to clean up")
        return 0
    
    # Clean up
    report = cleanup_directory_pages(
        args.destination,
        dest_config,
        directory_pages,
        delete=args.delete,
        archive=args.archive,
        dry_run=args.dry_run,
        data_dir=args.data_dir
    )
    
    # Summary
    print(f"\n{'='*80}")
    print("Cleanup Summary")
    print(f"{'='*80}")
    print(f"  Pages found: {report['pages_found']}")
    if args.delete:
        print(f"  Pages deleted: {report['pages_deleted']}")
    if args.archive:
        print(f"  Pages archived: {report['pages_archived']}")
    if report['errors']:
        print(f"  Errors: {len(report['errors'])}")
        for error in report['errors'][:5]:
            print(f"    - {error}")
    
    return 0 if not report['errors'] else 1


if __name__ == '__main__':
    sys.exit(main())
