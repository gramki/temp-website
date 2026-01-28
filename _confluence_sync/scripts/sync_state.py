#!/usr/bin/env python3
"""
State management for per-destination Confluence sync using JSONL format.

JSONL (JSON Lines) format allows streaming updates - each line is a separate JSON object.
This is much more efficient for large syncs with hundreds of files.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, Optional, Any, Iterator, Tuple
from datetime import datetime


def get_data_dir(data_dir: Optional[Path] = None) -> Path:
    """
    Get the data directory path.
    
    Args:
        data_dir: Optional explicit data directory path
        
    Returns:
        Path to data directory
    """
    if data_dir:
        return Path(data_dir).resolve()
    # Default: data directory sibling to scripts directory
    script_dir = Path(__file__).parent
    # Go up one level from scripts/ to _confluence_sync/, then to data/
    return script_dir.parent / 'data'


def get_destination_data_dir(destination_id: str, data_dir: Optional[Path] = None) -> Path:
    """
    Get the data directory for a specific destination.
    
    Args:
        destination_id: Destination ID
        data_dir: Optional explicit data directory path
        
    Returns:
        Path to destination-specific data directory
    """
    base_data_dir = get_data_dir(data_dir)
    dest_dir = base_data_dir / destination_id
    dest_dir.mkdir(parents=True, exist_ok=True)
    return dest_dir


def get_state_file_path(destination_id: str, data_dir: Optional[Path] = None) -> Path:
    """
    Get the path to the state file for a destination.
    
    Args:
        destination_id: Destination ID
        data_dir: Optional explicit data directory path
        
    Returns:
        Path to state file (JSONL format)
    """
    dest_dir = get_destination_data_dir(destination_id, data_dir)
    return dest_dir / 'sync-state.jsonl'


def get_metadata_file_path(destination_id: str, data_dir: Optional[Path] = None) -> Path:
    """
    Get the path to the metadata file for a destination.
    
    Args:
        destination_id: Destination ID
        data_dir: Optional explicit data directory path
        
    Returns:
        Path to metadata file (JSON format for small metadata)
    """
    dest_dir = get_destination_data_dir(destination_id, data_dir)
    return dest_dir / 'sync-metadata.json'


def load_sync_state(destination_id: str, data_dir: Optional[Path] = None, migrate: bool = True) -> Dict[str, Any]:
    """
    Load sync state for a destination from JSONL format.
    
    Args:
        destination_id: Destination ID
        
    Returns:
        State dictionary with sync_history populated from JSONL
    """
    # Migrate old format if needed
    if migrate:
        migrate_old_state_format(destination_id, data_dir)
    
    state_file = get_state_file_path(destination_id, data_dir)
    metadata_file = get_metadata_file_path(destination_id, data_dir)
    
    # Load metadata (destination-level info)
    metadata = {
        'destination_id': destination_id,
        'last_sync_timestamp': None,
        'last_sync_commit': None,
        'confluence_space': None,
        'root_page_id': None
    }
    
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata.update(json.load(f))
        except Exception as e:
            print(f"  ⚠ Warning: Error loading metadata file: {e}")
    
    # Load sync history from JSONL (separate pages and folders)
    sync_history = {}  # Pages: file_path -> entry
    folders = {}  # Folders: folder_path -> entry
    if state_file.exists():
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        entry_type = entry.get('type', 'page')  # Default to 'page' for backward compatibility
                        key = entry.get('file_path') or entry.get('folder_path')
                        if key:
                            if entry_type == 'folder':
                                folders[key] = entry
                            else:
                                sync_history[key] = entry
                    except json.JSONDecodeError as e:
                        print(f"  ⚠ Warning: Skipping invalid JSONL line {line_num}: {e}")
        except Exception as e:
            print(f"  ⚠ Warning: Error reading state file: {e}")
    
    return {
        'destination_id': destination_id,
        'sync_history': sync_history,  # Pages
        'folders': folders,  # Folders
        **metadata
    }


def append_page_history(
    destination_id: str,
    file_path: str,
    source_folder: Optional[str] = None,
    page_id: Optional[str] = None,
    page_title: Optional[str] = None,
    page_title_original: Optional[str] = None,
    commit_hash: Optional[str] = None,
    sync_status: Optional[str] = None,
    content_hash: Optional[str] = None,
    version: Optional[int] = None,
    previous_commit: Optional[str] = None,
    previous_sync_date: Optional[str] = None,
    previous_content_hash: Optional[str] = None,
    parent_id: Optional[str] = None,
    previous_parent_id: Optional[str] = None,
    content_signature: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> None:
    """
    Append a page history entry to the JSONL state file (streaming update).
    
    Args:
        destination_id: Destination ID
        file_path: Relative file path
        source_folder: Optional source folder identifier
        page_id: Confluence page ID
        page_title: Actual page title used in Confluence (may have suffix)
        page_title_original: Original page title from Markdown (without suffix)
        commit_hash: Current commit hash
        sync_status: Status ('created', 'updated', 'skipped')
        content_hash: Hash of page content for drift detection
        version: Confluence page version number
        previous_commit: Previous commit hash
        previous_sync_date: Previous sync date
        previous_content_hash: Previous content hash
        parent_id: Current parent page ID (for detecting parent changes)
        previous_parent_id: Previous parent page ID
        content_signature: Content signature for rename detection
    """
    state_file = get_state_file_path(destination_id, data_dir)
    
    # Use prefixed path if source folder provided
    if source_folder:
        key = f"{source_folder}/{file_path}"
    else:
        key = file_path
    
    # Create history entry
    entry = {
        'file_path': key,
        'page_id': page_id,
        'page_title': page_title,  # Actual title in Confluence
        'last_sync_commit': commit_hash,
        'last_sync_date': datetime.utcnow().isoformat() + 'Z',
        'last_sync_status': sync_status,
        'content_hash': content_hash,
        'version': version
    }
    
    # Add page_title_original if provided (for tracking original title from Markdown)
    if page_title_original:
        entry['page_title_original'] = page_title_original
    elif page_title:
        # For backward compatibility: if no original provided, use actual as original
        entry['page_title_original'] = page_title
    
    # Add parent_id if provided (for detecting parent changes)
    if parent_id:
        entry['parent_id'] = parent_id
    
    # Add content_signature if provided (for rename detection)
    if content_signature:
        entry['content_signature'] = content_signature
    
    # Add previous values if provided
    if previous_commit:
        entry['previous_commit'] = previous_commit
    if previous_sync_date:
        entry['previous_sync_date'] = previous_sync_date
    if previous_content_hash:
        entry['previous_content_hash'] = previous_content_hash
    if previous_parent_id:
        entry['previous_parent_id'] = previous_parent_id
    
    # Append to JSONL file (streaming update - no need to rewrite entire file)
    try:
        with open(state_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"  ⚠ Warning: Could not append to state file: {e}")


def get_page_history(
    destination_id: str,
    file_path: str,
    source_folder: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> Optional[Dict[str, Any]]:
    """
    Get sync history for a specific page from JSONL state.
    
    Args:
        destination_id: Destination ID
        file_path: Relative file path (from source folder root)
        source_folder: Optional source folder identifier
        
    Returns:
        Page history dictionary or None if not found
    """
    state = load_sync_state(destination_id, data_dir)
    
    # Try with source folder prefix if provided
    if source_folder:
        prefixed_path = f"{source_folder}/{file_path}"
        if prefixed_path in state['sync_history']:
            return state['sync_history'][prefixed_path]
    
    # Try without prefix
    if file_path in state['sync_history']:
        return state['sync_history'][file_path]
    
    return None


def update_page_history(
    destination_id: str,
    file_path: str,
    source_folder: Optional[str] = None,
    page_id: Optional[str] = None,
    page_title: Optional[str] = None,
    page_title_original: Optional[str] = None,
    commit_hash: Optional[str] = None,
    sync_status: Optional[str] = None,
    content_hash: Optional[str] = None,
    version: Optional[int] = None,
    previous_commit: Optional[str] = None,
    previous_sync_date: Optional[str] = None,
    previous_content_hash: Optional[str] = None,
    parent_id: Optional[str] = None,
    previous_parent_id: Optional[str] = None,
    content_signature: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> None:
    """
    Update sync history for a page (appends to JSONL).
    
    This is a convenience wrapper that gets previous values and calls append_page_history.
    For better performance with many files, consider calling append_page_history directly.
    """
    # Get existing history to preserve previous values
    existing = get_page_history(destination_id, file_path, source_folder, data_dir)
    
    # Use existing values if not provided
    if not previous_commit and existing:
        previous_commit = existing.get('last_sync_commit')
    if not previous_sync_date and existing:
        previous_sync_date = existing.get('last_sync_date')
    if not previous_content_hash and existing:
        previous_content_hash = existing.get('content_hash')
    if not previous_parent_id and existing:
        previous_parent_id = existing.get('parent_id')  # Use current parent_id as previous if not provided
    
    append_page_history(
        destination_id,
        file_path,
        source_folder,
        page_id,
        page_title,
        page_title_original,
        commit_hash,
        sync_status,
        content_hash,
        version,
        previous_commit,
        previous_sync_date,
        previous_content_hash,
        parent_id,
        previous_parent_id,
        content_signature,
        data_dir
    )


def update_destination_metadata(
    destination_id: str,
    data_dir: Optional[Path] = None,
    confluence_space: Optional[str] = None,
    root_page_id: Optional[str] = None,
    commit_hash: Optional[str] = None
) -> None:
    """
    Update destination-level metadata (small JSON file, not JSONL).
    
    Args:
        destination_id: Destination ID
        confluence_space: Confluence space key
        root_page_id: Root page ID
        commit_hash: Latest commit hash
    """
    metadata_file = get_metadata_file_path(destination_id)
    
    metadata = {}
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        except Exception:
            pass
    
    metadata['destination_id'] = destination_id
    
    if confluence_space:
        metadata['confluence_space'] = confluence_space
    
    if root_page_id:
        metadata['root_page_id'] = root_page_id
    
    if commit_hash:
        metadata['last_sync_commit'] = commit_hash
    
    metadata['last_sync_timestamp'] = datetime.utcnow().isoformat() + 'Z'
    
    try:
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"  ⚠ Warning: Could not save metadata file: {e}")


def compute_content_hash(content: str) -> str:
    """
    Compute SHA-256 hash of content for drift detection.
    
    Args:
        content: Content string
        
    Returns:
        Hex digest of SHA-256 hash
    """
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def compute_content_signature(markdown_content: str) -> str:
    """
    Compute identity signature from content structure (headings, first 500 chars).
    
    This signature is used to detect file renames - if a file's path changes but
    its signature matches an existing entry, it's likely a rename rather than a new file.
    
    Args:
        markdown_content: Markdown content string
        
    Returns:
        Short hex digest (16 chars) of signature hash
    """
    lines = markdown_content.split('\n')
    # Extract headings (lines starting with #)
    headings = [l.strip() for l in lines if l.strip().startswith('#')]
    # Take first 5 headings and first 500 chars of content
    signature_base = '\n'.join(headings[:5]) + '\n' + markdown_content[:500]
    # Return short hash (16 chars) for efficiency
    return hashlib.sha256(signature_base.encode('utf-8')).hexdigest()[:16]


def find_by_signature(sync_state: Dict[str, Any], signature: str, exclude_path: str) -> Optional[Dict[str, Any]]:
    """
    Find existing entry by content signature (for rename detection).
    
    Args:
        sync_state: Loaded sync state dictionary
        signature: Content signature to search for
        exclude_path: Path to exclude from search (the new path being checked)
        
    Returns:
        Dictionary with 'old_path' and entry data if found, None otherwise
    """
    sync_history = sync_state.get('sync_history', {})
    for path, entry in sync_history.items():
        if path != exclude_path and entry.get('content_signature') == signature:
            return {'old_path': path, **entry}
    return None


# ========== Folder History Methods ==========

def append_folder_history(
    destination_id: str,
    folder_path: str,
    source_folder: Optional[str] = None,
    folder_id: Optional[str] = None,
    folder_title: Optional[str] = None,
    parent_id: Optional[str] = None,
    status: Optional[str] = None,  # 'created', 'updated', 'deleted', 'unchanged'
    data_dir: Optional[Path] = None
) -> None:
    """
    Append a folder entry to the sync state JSONL file.
    
    Args:
        destination_id: Destination ID
        folder_path: Relative folder path
        source_folder: Optional source folder identifier
        folder_id: Confluence folder ID
        folder_title: Folder title
        parent_id: Parent folder or page ID
        status: Sync status ('created', 'updated', 'deleted', 'unchanged')
    """
    state_file = get_state_file_path(destination_id, data_dir)
    
    # Use prefixed path if source folder provided
    if source_folder:
        key = f"{source_folder}/{folder_path}"
    else:
        key = folder_path
    
    # Create folder entry
    entry = {
        'type': 'folder',  # Distinguish from page entries
        'folder_path': key,
        'folder_id': folder_id,
        'folder_title': folder_title,
        'parent_id': parent_id,
        'status': status,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
    
    # Append to JSONL file
    try:
        with open(state_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"  ⚠ Warning: Could not append folder to state file: {e}")


def get_folder_history(
    destination_id: str,
    folder_path: str,
    source_folder: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> Optional[Dict[str, Any]]:
    """
    Get the latest folder entry for a given path.
    
    Args:
        destination_id: Destination ID
        folder_path: Relative folder path
        source_folder: Optional source folder identifier
        
    Returns:
        Folder history dictionary or None if not found
    """
    state = load_sync_state(destination_id, data_dir)
    folders = state.get('folders', {})
    
    # Try with source folder prefix if provided
    if source_folder:
        prefixed_path = f"{source_folder}/{folder_path}"
        if prefixed_path in folders:
            return folders[prefixed_path]
    
    # Try without prefix
    if folder_path in folders:
        return folders[folder_path]
    
    return None


def update_folder_history(
    destination_id: str,
    folder_path: str,
    source_folder: Optional[str] = None,
    folder_id: Optional[str] = None,
    folder_title: Optional[str] = None,
    parent_id: Optional[str] = None,
    status: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> None:
    """
    Update folder history (appends to JSONL).
    
    This is a convenience wrapper that gets previous values and calls append_folder_history.
    """
    # Get existing history to preserve previous values
    existing = get_folder_history(destination_id, folder_path, source_folder, data_dir)
    
    # Use existing values if not provided
    if not folder_id and existing:
        folder_id = existing.get('folder_id')
    if not folder_title and existing:
        folder_title = existing.get('folder_title')
    if not parent_id and existing:
        parent_id = existing.get('parent_id')
    
    append_folder_history(
        destination_id,
        folder_path,
        source_folder,
        folder_id,
        folder_title,
        parent_id,
        status,
        data_dir
    )


def migrate_old_state_format(destination_id: str, data_dir: Optional[Path] = None) -> None:
    """
    Migrate old JSON format state file to new JSONL format.
    
    Args:
        destination_id: Destination ID
    """
    # Check old location (next to script)
    old_state_file = Path(__file__).parent / f'sync-state-{destination_id}.json'
    new_state_file = get_state_file_path(destination_id, data_dir)
    metadata_file = get_metadata_file_path(destination_id, data_dir)
    
    if not old_state_file.exists():
        return  # No old format to migrate
    
    if new_state_file.exists():
        return  # Already migrated
    
    try:
        # Load old format
        with open(old_state_file, 'r', encoding='utf-8') as f:
            old_state = json.load(f)
        
        # Extract metadata
        metadata = {
            'destination_id': destination_id,
            'last_sync_timestamp': old_state.get('last_sync_timestamp'),
            'last_sync_commit': old_state.get('last_sync_commit'),
            'confluence_space': old_state.get('confluence_space'),
            'root_page_id': old_state.get('root_page_id')
        }
        
        # Save metadata
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        # Convert sync_history to JSONL
        sync_history = old_state.get('sync_history', {})
        with open(new_state_file, 'w', encoding='utf-8') as f:
            for file_path, history in sync_history.items():
                entry = {'file_path': file_path, **history}
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        
        print(f"  ✓ Migrated old state format to JSONL for {destination_id}")
        
        # Optionally backup old file
        # old_state_file.rename(old_state_file.with_suffix('.json.backup'))
        
    except Exception as e:
        print(f"  ⚠ Warning: Could not migrate old state format: {e}")


def compact_sync_state(destination_id: str, data_dir: Optional[Path] = None) -> Tuple[int, int]:
    """
    Compact the sync state JSONL file by removing duplicate entries.
    
    The JSONL format uses append-only writes, which can result in duplicate
    entries for the same file/folder path. This function reads all entries,
    keeps only the latest entry for each path, and rewrites the file.
    
    Args:
        destination_id: Destination ID
        data_dir: Optional data directory
        
    Returns:
        Tuple of (original_lines, compacted_lines)
    """
    state_file = get_state_file_path(destination_id, data_dir)
    
    if not state_file.exists():
        return (0, 0)
    
    # Read all entries
    pages = {}  # file_path -> entry
    folders = {}  # folder_path -> entry
    original_count = 0
    
    try:
        with open(state_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                original_count += 1
                try:
                    entry = json.loads(line)
                    entry_type = entry.get('type', 'page')
                    key = entry.get('file_path') or entry.get('folder_path')
                    if key:
                        if entry_type == 'folder':
                            folders[key] = entry
                        else:
                            pages[key] = entry
                except json.JSONDecodeError:
                    continue  # Skip invalid lines
        
        # Calculate compacted count
        compacted_count = len(pages) + len(folders)
        
        if compacted_count >= original_count:
            # No duplicates to remove
            return (original_count, compacted_count)
        
        # Rewrite file with deduplicated entries
        # Write folders first, then pages (preserves logical order)
        with open(state_file, 'w', encoding='utf-8') as f:
            for entry in folders.values():
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
            for entry in pages.values():
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        
        return (original_count, compacted_count)
        
    except Exception as e:
        print(f"  ⚠ Warning: Could not compact sync state: {e}")
        return (original_count, original_count)
