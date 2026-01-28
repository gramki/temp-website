#!/usr/bin/env python3
"""
Migration script to convert old sync state format (directory pages) to folder entries.

This script:
1. Detects old sync state format (directory pages in sync_history)
2. Converts directory page entries to folder entries
3. Creates backup of old sync state before migration
4. Updates sync state to use folder tracking

Usage:
    python migrate_sync_state_to_folders.py --destination DEST_ID [--data-dir PATH] [--dry-run]
"""

import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from sync_state import (
    get_state_file_path,
    get_metadata_file_path,
    get_destination_data_dir,
    load_sync_state,
    get_folder_history
)
from config_loader import load_destination_config, get_destination, ConfigError


def is_directory_page_entry(entry: Dict) -> bool:
    """Check if a sync state entry is a directory page (old format)."""
    # Directory pages have specific characteristics:
    # - file_path starts with directory path
    # - page_title matches directory name pattern
    # - Often has __root__ or directory-like patterns
    file_path = entry.get('file_path', '')
    page_title = entry.get('page_title', '')
    
    # Check for directory page indicators
    if '__root__' in file_path:
        return False  # Root page, not directory page
    
    # Directory pages often have paths that end with directory names
    # and titles that match directory names
    # This is a heuristic - may need refinement
    return False  # Conservative: don't auto-detect, require explicit migration


def detect_old_directory_pages(sync_state: Dict) -> List[Dict]:
    """
    Detect old directory page entries in sync state.
    
    Returns:
        List of entries that appear to be directory pages
    """
    directory_pages = []
    sync_history = sync_state.get('sync_history', {})
    
    for file_path, entry in sync_history.items():
        # Check if this looks like a directory page
        # Directory pages in old format might have been created with specific patterns
        # For now, we'll rely on manual identification or specific patterns
        
        # Pattern 1: Entry with file_path that's a directory path (no .md extension)
        if not file_path.endswith('.md') and '/' in file_path:
            # Could be a directory page
            directory_pages.append({
                'file_path': file_path,
                'entry': entry
            })
    
    return directory_pages


def migrate_directory_page_to_folder(
    destination_id: str,
    file_path: str,
    entry: Dict,
    data_dir: Optional[Path] = None
) -> Optional[str]:
    """
    Migrate a directory page entry to a folder entry.
    
    Args:
        destination_id: Destination ID
        file_path: Original file path (directory path)
        entry: Directory page entry from sync state
        data_dir: Optional data directory path
        
    Returns:
        Folder path (dir_rel_path) if migration successful, None otherwise
    """
    from sync_state import append_folder_history
    
    # Extract folder information from entry
    folder_id = entry.get('page_id')  # Directory page ID becomes folder ID
    folder_title = entry.get('page_title', '')
    parent_id = entry.get('parent_id')
    
    if not folder_id:
        return None  # No ID to migrate
    
    # Determine folder path from file_path
    # file_path might be like "olympus-hub-docs/subdirectory" or similar
    folder_path = file_path  # Use as-is for now
    
    # Append folder history entry
    append_folder_history(
        destination_id=destination_id,
        folder_path=folder_path,
        source_folder=None,  # Will be extracted if needed
        folder_id=folder_id,
        folder_title=folder_title,
        parent_id=parent_id,
        status='migrated',  # Mark as migrated
        data_dir=data_dir
    )
    
    return folder_path


def migrate_sync_state(
    destination_id: str,
    data_dir: Optional[Path] = None,
    dry_run: bool = False
) -> Dict[str, any]:
    """
    Migrate sync state from directory pages to folders.
    
    Args:
        destination_id: Destination ID to migrate
        data_dir: Optional data directory path
        dry_run: If True, don't make changes, just report
        
    Returns:
        Migration report dictionary
    """
    report = {
        'destination_id': destination_id,
        'dry_run': dry_run,
        'backup_created': False,
        'directory_pages_found': 0,
        'folders_migrated': 0,
        'errors': []
    }
    
    # Load sync state
    try:
        sync_state = load_sync_state(destination_id, data_dir, migrate=False)  # Don't auto-migrate
    except Exception as e:
        report['errors'].append(f"Failed to load sync state: {e}")
        return report
    
    # Detect old directory pages
    directory_pages = detect_old_directory_pages(sync_state)
    report['directory_pages_found'] = len(directory_pages)
    
    if not directory_pages:
        print(f"  ℹ No directory pages found in sync state for '{destination_id}'")
        return report
    
    print(f"  Found {len(directory_pages)} potential directory page(s) to migrate")
    
    if dry_run:
        print("  [DRY RUN] Would migrate the following:")
        for dp in directory_pages:
            print(f"    - {dp['file_path']}: '{dp['entry'].get('page_title')}' (ID: {dp['entry'].get('page_id')})")
        return report
    
    # Create backup before migration
    state_file = get_state_file_path(destination_id, data_dir)
    if state_file.exists():
        backup_file = state_file.parent / f"sync-state.jsonl.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        try:
            shutil.copy2(state_file, backup_file)
            report['backup_created'] = True
            print(f"  ✓ Created backup: {backup_file.name}")
        except Exception as e:
            report['errors'].append(f"Failed to create backup: {e}")
            print(f"  ✗ Failed to create backup: {e}")
            return report
    
    # Migrate each directory page to folder
    for dp in directory_pages:
        file_path = dp['file_path']
        entry = dp['entry']
        
        try:
            folder_path = migrate_directory_page_to_folder(
                destination_id,
                file_path,
                entry,
                data_dir
            )
            if folder_path:
                report['folders_migrated'] += 1
                print(f"  ✓ Migrated: {file_path} -> folder '{folder_path}'")
            else:
                report['errors'].append(f"Could not migrate {file_path}: missing folder_id")
        except Exception as e:
            report['errors'].append(f"Error migrating {file_path}: {e}")
            print(f"  ✗ Error migrating {file_path}: {e}")
    
    print(f"\n  ✓ Migration complete: {report['folders_migrated']}/{report['directory_pages_found']} migrated")
    
    return report


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Migrate sync state from directory pages to folders'
    )
    parser.add_argument(
        '--destination',
        required=True,
        help='Destination ID to migrate'
    )
    parser.add_argument(
        '--data-dir',
        type=Path,
        help='Data directory path (default: data folder next to script)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be migrated without making changes'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Migrate all destinations'
    )
    
    args = parser.parse_args()
    
    # Load config
    try:
        config = load_destination_config(data_dir=args.data_dir)
    except ConfigError as e:
        print(f"ERROR: {e}")
        return 1
    
    # Get destinations to migrate
    if args.all:
        destinations = [d['id'] for d in config.get('destinations', [])]
    else:
        if args.destination not in [d['id'] for d in config.get('destinations', [])]:
            print(f"ERROR: Destination '{args.destination}' not found")
            return 1
        destinations = [args.destination]
    
    # Migrate each destination
    all_reports = []
    for dest_id in destinations:
        print(f"\n{'='*80}")
        print(f"Migrating destination: {dest_id}")
        print(f"{'='*80}")
        
        report = migrate_sync_state(
            dest_id,
            data_dir=args.data_dir,
            dry_run=args.dry_run
        )
        all_reports.append(report)
    
    # Summary
    print(f"\n{'='*80}")
    print("Migration Summary")
    print(f"{'='*80}")
    for report in all_reports:
        print(f"\n{report['destination_id']}:")
        print(f"  Directory pages found: {report['directory_pages_found']}")
        print(f"  Folders migrated: {report['folders_migrated']}")
        if report['backup_created']:
            print(f"  Backup created: ✓")
        if report['errors']:
            print(f"  Errors: {len(report['errors'])}")
            for error in report['errors'][:5]:
                print(f"    - {error}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
