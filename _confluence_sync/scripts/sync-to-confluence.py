#!/usr/bin/env python3
"""
Sync Markdown files to Confluence using REST API directly.

This script:
- Reads Markdown files from a directory structure
- Converts Markdown to Confluence Storage Format
- Creates/updates pages in Confluence preserving folder hierarchy
- Uses page IDs (not titles) for parent relationships to avoid resolution issues
- Only updates pages when content has actually changed (compares body content)
- Preserves comments (stored separately from page body)
- Parallel processing for folders and pages (configurable thread count)
- Sync state optimization (trusts sync state to avoid unnecessary API calls)
- Orphan detection and deletion (pages/folders removed from source)

⚠️ WARNING: This is a ONE-WAY sync (Markdown → Confluence).
Edits made directly in Confluence will be overwritten on next sync.

Performance Features:
- Parallel folder creation (grouped by depth level, max 8 threads per level)
- Parallel page syncing (configurable via parallel_threads option, default: 5)
- Sync state trust (skips API calls for unchanged folders)
- Parent-child ordering maintained through depth-based processing

See ADR 0013 for parallel folder sync design.
See ADR 0014 for environment file wrapper.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, Optional, List, Tuple, Any
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Import local modules (scripts directory)
sys.path.insert(0, str(Path(__file__).parent))
try:
    from ignore_handler import IgnoreHandler
    from config_loader import load_destination_config, get_destination, resolve_credentials, ConfigError, get_repo_root
    from sync_state import load_sync_state, get_page_history, update_page_history, update_destination_metadata, compute_content_hash, find_by_signature, get_metadata_file_path, compact_sync_state, get_destination_data_dir
    from git_utils import get_current_commit_hash, get_file_commit_hash, get_file_commit_date, get_file_github_url, get_github_repo_url, get_repo_root as get_git_repo_root
    from report_generator import SyncResult, generate_sync_report, save_report_to_file
    from content_preparer import ContentPreparer, PreparedContent
    from confluence_sync import ConfluenceSync, ParentPageNotFoundError, DuplicateTitleError, PageNotFoundError, TitleConflictError, HierarchyValidationError
    from orphan_handler import OrphanHandler
    from attachment_handler import AttachmentHandler
    import requests
except ImportError as e:
    print(f"ERROR: Failed to import required modules: {e}")
    sys.exit(1)

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    print("ERROR: 'requests' library not found. Install with: pip install requests")
    sys.exit(1)

try:
    import markdown
    from markdown.extensions import codehilite, tables, fenced_code
except ImportError:
    print("ERROR: 'markdown' library not found. Install with: pip install markdown")
    sys.exit(1)


@dataclass
class PreparedContent:
    """Represents content prepared for syncing to Confluence."""
    file_path: str
    rel_path: str
    source_folder: Optional[str]
    title: str
    content: str  # Markdown content
    storage_format: str  # Confluence storage format
    content_hash: str
    parent_id: Optional[str]
    commit_hash: Optional[str]
    commit_date: Optional[str]
    github_url: Optional[str]
    file_key: str
    prev_history: Optional[Dict[str, Any]]
    force_sync: bool
    existing_page_id: Optional[str] = None
    status: str = 'pending'  # 'pending', 'syncing', 'synced', 'failed', 'skipped'
    page_id: Optional[str] = None
    sync_status: Optional[str] = None  # 'created', 'updated', 'skipped'
    version: Optional[int] = None
    sync_result: Optional[Any] = None  # Will be SyncResult
    error: Optional[str] = None


class ProgressTracker:
    """Track and display sync progress."""
    
    def __init__(self, total_steps: int = 0):
        self.total_steps = total_steps
        self.current_step = 0
        self.step_names = []
        self.step_totals = {}
        self.step_current = {}
    
    def add_step(self, name: str, total: int = 0):
        """Add a step to track."""
        self.step_names.append(name)
        self.step_totals[name] = total
        self.step_current[name] = 0
    
    def start_step(self, name: str):
        """Start a step."""
        if name in self.step_names:
            self.current_step = self.step_names.index(name) + 1
            print(f"\n[{self.current_step}/{len(self.step_names)}] {name}")
            if self.step_totals.get(name, 0) > 0:
                print(f"  Progress: 0/{self.step_totals[name]}")
    
    def update_step(self, name: str, current: int, total: Optional[int] = None, show_every: int = 1, current_file: Optional[str] = None, status: Optional[str] = None):
        """Update progress for a step."""
        if name not in self.step_current:
            return
        
        self.step_current[name] = current
        if total is not None:
            self.step_totals[name] = total
        
        total_count = self.step_totals.get(name, 0)
        if total_count > 0:
            # Show progress more frequently - every N items, or always for small totals
            should_show = (current % show_every == 0) or (current == total_count) or (current == 1) or (total_count < 50)
            
            if should_show:
                percent = int((current / total_count) * 100)
                # Use a progress bar that's more visible
                bar_length = 40
                filled = int(bar_length * current / total_count)
                bar = '█' * filled + '░' * (bar_length - filled)
                
                # Show file name if provided (truncate if too long)
                file_info = ""
                if current_file:
                    file_display = current_file if len(current_file) <= 40 else "..." + current_file[-37:]
                    status_indicator = ""
                    if status:
                        if status == 'skipped':
                            status_indicator = " [no-change-skipped]"
                        elif status in ['created', 'updated']:
                            status_indicator = " [changed]"
                    file_info = f" | {file_display}{status_indicator}"
                
                # Use carriage return to update in place (overwrite previous line)
                print(f"\r  [{bar}] {current}/{total_count} ({percent}%){file_info}", end='', flush=True)
    
    def complete_step(self, name: str):
        """Mark a step as complete."""
        if name in self.step_current:
            total = self.step_totals.get(name, 0)
            current = self.step_current.get(name, 0)
            if total > 0:
                bar = '█' * 40
                print(f"\r  [{bar}] {current}/{total} (100%) ✓")
            else:
                print(f"  ✓ Complete")
            print()  # Newline after completion



def sync_destination(
    destination_id: str,
    destination_config: Dict[str, Any],
    repo_root: Path,
    data_dir: Optional[Path] = None,
    dry_run_override: Optional[bool] = None,
    cache_prepared: bool = False,
    force_update: bool = False
) -> List[SyncResult]:
    """
    Sync a destination to Confluence.
    
    This function orchestrates the entire sync process:
    1. Phase 1: Prepare content (scan files, convert Markdown, build link cache)
    2. Phase 2a: Create folders (parallelized by depth level, trusts sync state)
    3. Phase 2b: Sync pages (parallelized with configurable thread count)
    4. Phase 3: Detect and delete orphaned pages/folders
    
    Performance optimizations:
    - Folders are processed in parallel within each depth level (max 8 threads per level)
    - Pages are synced using ThreadPoolExecutor (configurable via parallel_threads option)
    - Sync state is trusted for unchanged folders (no API calls)
    - Parent-child ordering maintained through depth-based processing
    
    Args:
        destination_id: Unique identifier for this destination
        destination_config: Configuration dictionary for this destination
        repo_root: Root path of the Git repository
        data_dir: Optional data directory (defaults to _confluence_sync/data)
        dry_run_override: Override dry_run setting from config
        cache_prepared: If True, cache prepared content to disk for debugging
        force_update: If True, force update all pages even if content unchanged
        
    Returns:
        List of SyncResult objects for each synced file
        
    See Also:
        ADR 0013: Parallel Folder Sync and Sync State Trust
        ADR 0014: Environment File Wrapper Script
    """
    results: List[SyncResult] = []
    
    # Get destination info
    destination_name = destination_config['name']
    confluence_config = destination_config['confluence']
    source_config = destination_config['source']
    options = destination_config.get('options', {})
    
    # Resolve credentials
    try:
        creds = resolve_credentials(destination_config)
    except ConfigError as e:
        print(f"ERROR: {e}")
        return results
    
    # Get options
    dry_run = dry_run_override if dry_run_override is not None else options.get('dry_run', False)
    add_git_metadata = options.get('add_git_metadata', False)
    github_repo_override = options.get('github_repo_override')
    parallel_threads = options.get('parallel_threads', 5)  # Default to 5 parallel threads
    
    # Get Git info (repo-level, but individual files will use their own commit hashes)
    repo_commit_hash = get_current_commit_hash(repo_root) if add_git_metadata else None
    github_repo_url = get_github_repo_url(repo_root, github_repo_override) if add_git_metadata else None
    
    # Load sync state
    sync_state = load_sync_state(destination_id, data_dir)
    
    # Initialize Confluence sync client
    base_url = confluence_config['url']
    space_key = confluence_config['space_key']
    root_page_title = confluence_config['root_page_title']
    root_page_id = confluence_config.get('root_page_id')
    
    print(f"\n{'='*80}")
    print(f"Syncing destination: {destination_name} ({destination_id})")
    print(f"Space: {space_key}")
    print(f"Root page: {root_page_title}")
    if dry_run:
        print("DRY RUN MODE - No changes will be made")
    print(f"{'='*80}\n")
    
    # Initialize Confluence sync client (needed for dry-run validation)
    try:
        creds = resolve_credentials(destination_config)
        confluence_sync = ConfluenceSync(base_url, creds['username'], creds['token'], space_key)
    except Exception as e:
        print(f"ERROR: Could not initialize Confluence client: {e}")
        return results
    
    if dry_run:
        # Enhanced dry-run mode (Phase 8): Prepare all content and validate without syncing
        print("\n[DRY RUN] Enhanced validation mode - preparing content and checking for issues...")
        
        # Initialize content preparer
        preparer = ContentPreparer(
            repo_root=repo_root,
            github_repo_url=get_github_repo_url(repo_root, github_repo_override) if add_git_metadata else None,
            add_git_metadata=add_git_metadata,
            attachment_handler=None  # No attachments in dry-run
        )
        
        # Get root page ID for validation
        root_parent_id = root_page_id
        if not root_parent_id:
            metadata_file = get_metadata_file_path(destination_id, data_dir)
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r') as f:
                        metadata = json.load(f)
                        root_parent_id = metadata.get('root_page_id')
                except:
                    pass
        
        # Phase 1: Prepare all content locally
        all_prepared_contents: List[PreparedContent] = []
        all_folder_pages = []
        parent_id_map: Dict[str, str] = {}
        
        for folder_config in source_config['folders']:
            folder_path = repo_root / folder_config['path']
            source_folder_id = folder_config['path']
            
            if not folder_path.exists():
                continue
            
            files_processed = [0]
            folder_prepared, folder_parent_map, folder_directory_pages = preparer.prepare_directory_content(
                directory=folder_path,
                parent_id=root_parent_id,
                root_path=folder_path,
                source_folder=source_folder_id,
                commit_hash=repo_commit_hash if add_git_metadata else None,
                destination_id=destination_id,
                sync_state=sync_state,
                files_processed_count=files_processed,
                prepared_contents=[],
                parent_id_map={},
                progress_callback=None,
                directory_pages=[]
            )
            all_prepared_contents.extend(folder_prepared)
            all_folder_pages.extend(folder_directory_pages)
            parent_id_map.update(folder_parent_map)
        
        print(f"\n✓ Prepared {len(all_prepared_contents)} files and {len(all_folder_pages)} folders")
        
        # Phase 8: Validate prepared content
        validation_results = {
            'folder_hierarchy_issues': [],
            'page_hierarchy_issues': [],
            'folder_title_conflicts': [],
            'page_title_conflicts': [],
            'readme_issues': []
        }
        
        # Validate prepared folder hierarchy (Phase 8-2)
        print("\n[DRY RUN] Validating folder hierarchy...")
        for folder_info in all_folder_pages:
            dir_rel_path = folder_info['dir_rel_path']
            folder_title = folder_info['folder_title']
            expected_parent_id = folder_info['parent_id']
            
            # Check if parent folder exists in prepared folders
            from pathlib import Path as PathLib
            if dir_rel_path and dir_rel_path != '.':
                dir_path_obj = PathLib(dir_rel_path)
                parent_dir_rel_path = str(dir_path_obj.parent) if dir_path_obj.parent != PathLib('.') else ''
            else:
                parent_dir_rel_path = ''
            
            # Find parent folder in prepared folders
            parent_found = False
            if parent_dir_rel_path:
                for f in all_folder_pages:
                    if f['dir_rel_path'] == parent_dir_rel_path:
                        parent_found = True
                        break
            elif expected_parent_id == root_parent_id:
                parent_found = True  # Root is the parent
            
            if not parent_found and expected_parent_id != root_parent_id:
                validation_results['folder_hierarchy_issues'].append({
                    'folder_path': dir_rel_path,
                    'folder_title': folder_title,
                    'issue': f"Parent folder '{parent_dir_rel_path}' not found in prepared folders"
                })
        
        # Validate prepared page hierarchy (Phase 8-3)
        print("[DRY RUN] Validating page hierarchy...")
        for prepared in all_prepared_contents:
            file_path = prepared.file_key
            page_title = prepared.title
            expected_parent_id = prepared.parent_id
            
            # Check if parent folder exists
            if hasattr(prepared, '_dir_rel_path'):
                dir_rel_path = prepared._dir_rel_path
                parent_folder_found = any(
                    f['dir_rel_path'] == dir_rel_path 
                    for f in all_folder_pages
                )
                if not parent_folder_found and expected_parent_id != root_parent_id:
                    validation_results['page_hierarchy_issues'].append({
                        'file_path': file_path,
                        'page_title': page_title,
                        'issue': f"Parent folder for '{dir_rel_path}' not found in prepared folders"
                    })
        
        # Check for title conflicts (Phase 8-4, 8-5)
        # IMPORTANT: A title conflict occurs when a folder/page with the same title
        # exists under a DIFFERENT parent. If it exists under the same parent,
        # it's an update candidate, not a conflict.
        print("[DRY RUN] Checking for title conflicts...")
        try:
            root_page_id = confluence_sync.root_page_id
            
            # Check folder title conflicts
            for folder_info in all_folder_pages:
                folder_title = folder_info['folder_title']
                expected_parent_id = folder_info['parent_id']
                
                # Find ALL folders with this title in the space
                all_folders = confluence_sync.find_folders_by_title_space_wide(
                    title=folder_title,
                    root_page_id=root_page_id
                )
                
                # Check if any exist under a different parent (conflict)
                for folder_id, actual_parent_id in all_folders:
                    # If parent matches expected, it's an update candidate (not a conflict)
                    if expected_parent_id and str(actual_parent_id) == str(expected_parent_id):
                        continue  # Same parent = update candidate, not conflict
                    elif not expected_parent_id and not actual_parent_id:
                        continue  # Both root-level = update candidate
                    else:
                        # Different parent = TITLE CONFLICT
                        validation_results['folder_title_conflicts'].append({
                            'folder_title': folder_title,
                            'folder_path': folder_info['dir_rel_path'],
                            'expected_parent_id': expected_parent_id,
                            'conflicting_folder_id': folder_id,
                            'conflicting_parent_id': actual_parent_id
                        })
                        break  # Found a conflict, no need to check more
            
            # Check page title conflicts
            for prepared in all_prepared_contents:
                page_title = prepared.title
                expected_parent_id = prepared.parent_id
                
                # Find ALL pages with this title in the space
                all_pages = confluence_sync.find_pages_by_title_space_wide(
                    title=page_title,
                    root_page_id=root_page_id
                )
                
                # Check if any exist under a different parent (conflict)
                for page_id, actual_parent_id in all_pages:
                    # If it's the same page from sync state, skip (update candidate)
                    if prepared.existing_page_id and str(page_id) == str(prepared.existing_page_id):
                        continue  # Same page = update candidate
                    
                    # If parent matches expected, it's an update candidate (not a conflict)
                    if expected_parent_id and str(actual_parent_id) == str(expected_parent_id):
                        continue  # Same parent = update candidate, not conflict
                    elif not expected_parent_id and not actual_parent_id:
                        continue  # Both root-level = update candidate
                    else:
                        # Different parent = TITLE CONFLICT
                        validation_results['page_title_conflicts'].append({
                            'page_title': page_title,
                            'file_path': prepared.file_key,
                            'expected_parent_id': expected_parent_id,
                            'conflicting_page_id': page_id,
                            'conflicting_parent_id': actual_parent_id
                        })
                        break  # Found a conflict, no need to check more
        except Exception as e:
            print(f"  ⚠ Could not check title conflicts: {e}")
        
        # Verify README handling (Phase 8-6)
        print("[DRY RUN] Verifying README handling...")
        readme_files = [p for p in all_prepared_contents if 'README' in p.file_key or 'readme' in p.file_key.lower()]
        for readme in readme_files:
            # README should be a regular page, not folder content
            if readme.parent_id:
                validation_results['readme_issues'].append({
                    'file_path': readme.file_key,
                    'page_title': readme.title,
                    'status': '✓ README will be created as separate page'
                })
        
        # Print dry-run report (Phase 8-7)
        print("\n" + "="*80)
        print("DRY RUN REPORT")
        print("="*80)
        print(f"\nSummary:")
        print(f"  Files to sync: {len(all_prepared_contents)}")
        print(f"  Folders to create: {len(all_folder_pages)}")
        
        if validation_results['folder_hierarchy_issues']:
            print(f"\n⚠ Folder Hierarchy Issues ({len(validation_results['folder_hierarchy_issues'])}):")
            for issue in validation_results['folder_hierarchy_issues'][:10]:
                print(f"  - {issue['folder_path']}: {issue['issue']}")
        
        if validation_results['page_hierarchy_issues']:
            print(f"\n⚠ Page Hierarchy Issues ({len(validation_results['page_hierarchy_issues'])}):")
            for issue in validation_results['page_hierarchy_issues'][:10]:
                print(f"  - {issue['file_path']}: {issue['issue']}")
        
        if validation_results['folder_title_conflicts']:
            print(f"\n⚠ Folder Title Conflicts ({len(validation_results['folder_title_conflicts'])}):")
            for conflict in validation_results['folder_title_conflicts'][:10]:
                print(f"  - '{conflict['folder_title']}' ({conflict['folder_path']}) - existing folder ID: {conflict['existing_folder_id']}")
        
        if validation_results['page_title_conflicts']:
            print(f"\n⚠ Page Title Conflicts ({len(validation_results['page_title_conflicts'])}):")
            for conflict in validation_results['page_title_conflicts'][:10]:
                print(f"  - '{conflict['page_title']}' ({conflict['file_path']}) - existing page ID: {conflict['existing_page_id']}")
        
        if validation_results['readme_issues']:
            print(f"\nℹ README Files ({len(validation_results['readme_issues'])}):")
            for readme in validation_results['readme_issues'][:5]:
                print(f"  - {readme['file_path']}: {readme['status']}")
        
        total_issues = (
            len(validation_results['folder_hierarchy_issues']) +
            len(validation_results['page_hierarchy_issues']) +
            len(validation_results['folder_title_conflicts']) +
            len(validation_results['page_title_conflicts'])
        )
        
        if total_issues == 0:
            print("\n✓ No issues detected - sync should proceed successfully")
        else:
            print(f"\n⚠ {total_issues} issue(s) detected - review before syncing")
        
        print("="*80)
        return results
    
    try:
        # Count total files to sync for progress tracking
        total_files = 0
        for folder_config in source_config['folders']:
            folder_path = repo_root / folder_config['path']
            if folder_path.exists():
                # Count Markdown files recursively
                total_files += len(list(folder_path.rglob('*.md')))
        
        # Initialize progress tracker
        progress = ProgressTracker()
        progress.add_step('Finding/Creating root page', 1)
        progress.add_step('Building title cache', total_files)
        progress.add_step('Preparing content', total_files)  # Phase 1: Prepare all content locally
        progress.add_step('Syncing files', total_files)  # Phase 2: Sync in parallel
        
        # Initialize Confluence sync client (for API calls)
        confluence_sync = ConfluenceSync(base_url, creds['username'], creds['token'], space_key)
        
        # Initialize attachment handler (for image uploads)
        attachment_handler = AttachmentHandler(confluence_sync)
        
        # Initialize content preparer (for local content preparation)
        preparer = ContentPreparer(
            repo_root=repo_root,
            github_repo_url=github_repo_url,
            add_git_metadata=add_git_metadata,
            attachment_handler=attachment_handler
        )
        
        # Find or create root page
        progress.start_step('Finding/Creating root page')
        
        # First, try to load root_page_id from sync metadata if not in config
        if not root_page_id:
            metadata_file = get_metadata_file_path(destination_id, data_dir)
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r') as f:
                        metadata = json.load(f)
                        root_page_id = metadata.get('root_page_id')
                        if root_page_id:
                            print(f"  ℹ Found root_page_id in sync metadata: {root_page_id}")
                except Exception as e:
                    print(f"  ⚠ Could not load sync metadata: {e}")
        
        if root_page_id:
            # Verify the root page still exists and is not archived (using v2 API)
            try:
                response = confluence_sync._make_request('GET', f'/pages/{root_page_id}')
                page_data = response.json()
                root_parent_id = root_page_id
                print(f"Found root page: {root_page_title} (ID: {root_parent_id})")
            except Exception as e:
                # Root page doesn't exist or is archived - create a new one
                print(f"⚠ Root page (ID: {root_page_id}) not found or archived, creating new one...")
                root_parent_id = None
        else:
            root_parent_id = None
        
        if not root_parent_id:
            # Find existing root page under space homepage or create it
            homepage_id = confluence_sync.get_space_homepage_id()
            if not homepage_id:
                raise Exception("Could not get space homepage ID. Cannot create root page.")
            
            # Check sync state for root page
            root_file_key = f"__root__{root_page_title}"
            root_prev_history = get_page_history(destination_id, root_file_key, None, data_dir)
            
            # Create root page using storage format
            root_content = f"# {root_page_title}\n\n*Root page for synced documentation*"
            root_storage = preparer.markdown_to_storage_format(root_content, None, repo_root, repo_commit_hash if add_git_metadata else None)
            root_hash = compute_content_hash(root_storage)
            
            try:
                root_parent_id, root_status, _, root_actual_title = confluence_sync.find_or_create_page(
                    file_path=root_file_key,
                    title=root_page_title,
                    title_original=root_page_title,
                    storage_format=root_storage,
                    content_hash=root_hash,
                    parent_id=homepage_id,
                    sync_state_entry=root_prev_history,
                    root_page_id=None  # Root page itself has no root
                )
                if root_status == 'created':
                    print(f"Created root page: {root_page_title} (ID: {root_parent_id})")
                elif root_status == 'found':
                    print(f"Found root page: {root_page_title} (ID: {root_parent_id})")
                else:
                    print(f"Root page: {root_page_title} (ID: {root_parent_id}) - {root_status}")
            except Exception as e:
                raise Exception(
                    f"Failed to create or find root page '{root_page_title}': {e}"
                ) from e
        
        progress.complete_step('Finding/Creating root page')
        
        # Update destination metadata
        update_destination_metadata(
            destination_id,
            data_dir=data_dir,
            confluence_space=space_key,
            root_page_id=root_parent_id,
            commit_hash=repo_commit_hash if add_git_metadata else None
        )
        
        # Build title and page ID cache for link conversion (needed by preparer)
        print("\nBuilding link cache for link conversion...")
        progress.start_step('Building link cache')
        file_to_title: Dict[str, str] = {}
        file_to_page_id: Dict[str, str] = {}
        
        # First, try to get page IDs from sync state (most reliable)
        if sync_state and 'sync_history' in sync_state:
            for file_path, page_entry in sync_state['sync_history'].items():
                if isinstance(page_entry, dict):
                    page_id = page_entry.get('page_id')
                    page_title = page_entry.get('page_title')
                    if page_id and page_title:
                        # Normalize file path (remove source folder prefix if present)
                        normalized_path = file_path
                        for folder_config in source_config['folders']:
                            folder_prefix = folder_config['path'] + '/'
                            if file_path.startswith(folder_prefix):
                                normalized_path = file_path[len(folder_prefix):]
                                break
                        file_to_page_id[normalized_path] = str(page_id)
                        file_to_title[normalized_path] = page_title
        
        # Also build from Markdown files (for new files not yet in sync state)
        for folder_config in source_config['folders']:
            folder_path = repo_root / folder_config['path']
            if folder_path.exists():
                ignore_handler = IgnoreHandler(folder_path)
                for md_file in folder_path.rglob('*.md'):
                    if md_file.name.startswith('.'):
                        continue
                    if ignore_handler.should_ignore(md_file):
                        continue
                    try:
                        rel_path = str(md_file.relative_to(folder_path))
                        # Only add if not already in cache (from sync state)
                        if rel_path not in file_to_title:
                            with open(md_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            title = None
                            for line in content.split('\n'):
                                line = line.strip()
                                if line.startswith('# '):
                                    title = line[2:].strip()
                                    break
                                elif line.startswith('#'):
                                    title = line[1:].strip()
                                    break
                            if not title:
                                title = md_file.stem.replace('_', ' ').replace('-', ' ').title()
                            file_to_title[rel_path] = title
                    except:
                        pass
        
        preparer.file_to_title = file_to_title
        preparer.file_to_page_id = file_to_page_id
        progress.complete_step('Building link cache')
        print(f"  Cached {len(file_to_title)} page titles and {len(file_to_page_id)} page IDs")
        
        # Phase 1: Prepare all content locally (fast, no API calls)
        print("\n[Phase 1] Preparing all content locally...")
        progress.start_step('Preparing content')
        all_prepared_contents: List[PreparedContent] = []
        parent_id_map: Dict[str, str] = {}
        
        def progress_callback(current: int, file_display: str):
            progress.update_step('Preparing content', current, show_every=10, current_file=file_display)
        
        # Store source folder parent mappings for Phase 2a
        source_folder_parent_ids: Dict[str, str] = {}  # source_folder_id -> parent_id for that source
        source_folder_titles: Dict[str, str] = {}  # source_folder_id -> title (for create_root_parent)
        
        for folder_config in source_config['folders']:
            folder_path = repo_root / folder_config['path']
            source_folder_id = folder_config['path']
            
            # Check if we should create a parent folder for this source
            create_root_parent = folder_config.get('create_root_parent', True)
            source_folder_title = folder_config.get('title', folder_path.name.replace('_', ' ').replace('-', ' ').title())
            
            # Store for Phase 2a - will create parent folders there
            if create_root_parent:
                source_folder_parent_ids[source_folder_id] = root_parent_id  # Parent for the source folder
                source_folder_titles[source_folder_id] = source_folder_title
            
            print(f"\nPreparing folder: {folder_path}")
            if create_root_parent:
                print(f"  → Will create parent folder: '{source_folder_title}'")
            
            # Prepare all content in this folder
            # Note: parent_id here is for the source folder's content, which will be updated in Phase 2a
            files_processed = [0]
            folder_prepared, folder_parent_map, folder_directory_pages = preparer.prepare_directory_content(
                directory=folder_path,
                parent_id=root_parent_id,  # Will be updated after source parent folder is created
                root_path=folder_path,
                source_folder=source_folder_id,
                commit_hash=repo_commit_hash,
                destination_id=destination_id,
                sync_state=sync_state,
                files_processed_count=files_processed,
                prepared_contents=[],
                parent_id_map={},
                progress_callback=progress_callback,
                directory_pages=[]
            )
            all_prepared_contents.extend(folder_prepared)
            parent_id_map.update(folder_parent_map)
            
            # Store directory pages for later creation
            if not hasattr(sync_destination, '_all_directory_pages'):
                sync_destination._all_directory_pages = []
            sync_destination._all_directory_pages.extend(folder_directory_pages)
        
        # Store source folder info for Phase 2a
        sync_destination._source_folder_parent_ids = source_folder_parent_ids
        sync_destination._source_folder_titles = source_folder_titles
        
        progress.complete_step('Preparing content')
        print(f"\n✓ Prepared {len(all_prepared_contents)} files for syncing")
        
        # Cache prepared content to disk if requested
        if cache_prepared:
            cache_dir = get_destination_data_dir(destination_id, data_dir) / 'prepared-content'
            cache_dir.mkdir(parents=True, exist_ok=True)
            print(f"\n[DEBUG] Saving prepared content to {cache_dir}")
            for prepared in all_prepared_contents:
                # Create subdirectories as needed
                rel_path = Path(prepared.file_key)
                cache_file = cache_dir / rel_path.with_suffix('.html')
                cache_file.parent.mkdir(parents=True, exist_ok=True)
                try:
                    with open(cache_file, 'w', encoding='utf-8') as f:
                        f.write(f"<!-- File: {prepared.file_key} -->\n")
                        f.write(f"<!-- Title: {prepared.title} -->\n")
                        f.write(f"<!-- Content Hash: {prepared.content_hash} -->\n")
                        f.write(f"<!-- Parent ID: {prepared.parent_id} -->\n\n")
                        f.write(prepared.storage_format)
                except Exception as e:
                    print(f"  ⚠ Could not cache {prepared.file_key}: {e}")
            print(f"  ✓ Cached {len(all_prepared_contents)} files to {cache_dir}")
        
        # Phase 1.5: Detect file renames before syncing
        print("\n[Phase 1.5] Detecting file renames...")
        for prepared in all_prepared_contents:
            if not prepared.prev_history and prepared.content_signature:
                # File not in state - check if it's a rename
                rename_match = find_by_signature(sync_state, prepared.content_signature, prepared.file_key)
                if rename_match:
                    # This is a renamed file
                    prepared.renamed_from = rename_match['old_path']
                    prepared.existing_page_id = rename_match.get('page_id')
                    # Update prev_history to use old entry
                    prepared.prev_history = rename_match
                    print(f"  ✓ Detected rename: {rename_match['old_path']} → {prepared.file_key}")
        
        # Phase 2a: Create folders first (sequentially, to establish hierarchy) using REST API v2
        all_folder_pages = getattr(sync_destination, '_all_directory_pages', [])  # Now contains folder entries
        folder_id_map = {}  # Map folder_key -> folder_id
        
        # Step 2a.1: Create source folder parents first (e.g., "Olympus Hub", "Olympus Seer")
        source_folder_parent_ids = getattr(sync_destination, '_source_folder_parent_ids', {})
        source_folder_titles = getattr(sync_destination, '_source_folder_titles', {})
        source_folder_created_ids = {}  # source_folder_id -> created folder_id
        
        if source_folder_titles:
            print(f"\n[Phase 2a.1] Creating {len(source_folder_titles)} source folder parents...")
            for source_folder_id, source_folder_title in source_folder_titles.items():
                parent_id = source_folder_parent_ids.get(source_folder_id, root_parent_id)
                
                # Check if already exists in sync state
                source_folder_key = f"__source__{source_folder_id}"
                existing_folder_id = None
                
                # Check sync state for existing source folder
                folders_state = sync_state.get('folders', {})
                if source_folder_key in folders_state:
                    existing_info = folders_state[source_folder_key]
                    if existing_info.get('folder_id'):
                        existing_folder_id = existing_info['folder_id']
                        try:
                            folder_data = confluence_sync.get_folder(existing_folder_id)
                            if folder_data:
                                print(f"  ✓ Found existing source folder: {source_folder_title} (ID: {existing_folder_id})")
                                source_folder_created_ids[source_folder_id] = existing_folder_id
                                folder_id_map[source_folder_key] = existing_folder_id
                                continue
                        except Exception:
                            existing_folder_id = None  # Folder doesn't exist
                
                # Create the source folder parent
                try:
                    folder_id, folder_status = confluence_sync.create_folder(
                        title=source_folder_title,
                        space_id=confluence_sync.space_id,
                        parent_id=parent_id,
                        root_page_id=root_parent_id
                    )
                    source_folder_created_ids[source_folder_id] = folder_id
                    folder_id_map[source_folder_key] = folder_id
                    print(f"  ✓ Created source folder: {source_folder_title} (ID: {folder_id})")
                    
                    # Record in sync state
                    from sync_state import append_folder_history
                    append_folder_history(
                        destination_id,
                        source_folder_key,
                        source_folder=None,
                        folder_id=folder_id,
                        folder_title=source_folder_title,
                        parent_id=parent_id,
                        status='created',
                        data_dir=data_dir
                    )
                except Exception as e:
                    print(f"  ⚠ Warning: Could not create source folder '{source_folder_title}': {e}")
            
            # Update parent IDs for pages at the root of each source folder
            for prepared in all_prepared_contents:
                if hasattr(prepared, 'source_folder') and prepared.source_folder:
                    source_folder = prepared.source_folder
                    # Check if this page is at the root of the source folder (no dir_rel_path or root dir)
                    if hasattr(prepared, '_dir_rel_path'):
                        dir_rel_path = prepared._dir_rel_path
                        if not dir_rel_path or dir_rel_path == '.' or dir_rel_path == prepared.source_folder:
                            # This is a root-level page for this source folder
                            if source_folder in source_folder_created_ids:
                                prepared.parent_id = source_folder_created_ids[source_folder]
        
        if all_folder_pages:
            print(f"\n[Phase 2a] Creating {len(all_folder_pages)} folders...")
            # Sort by depth (shallow first) to ensure parents are created before children
            def get_depth(folder_info):
                return str(folder_info['dir_path']).count('/')
            all_folder_pages.sort(key=get_depth)
            
            # Group folders by depth for parallel processing within each depth level
            from collections import defaultdict
            folders_by_depth = defaultdict(list)
            for folder_info in all_folder_pages:
                depth = get_depth(folder_info)
                folders_by_depth[depth].append(folder_info)
            
            # Process folders by depth level, parallelizing within each level
            folder_parallel_threads = min(parallel_threads, 8)  # Limit folder threads to avoid API rate limits
            
            def process_single_folder(folder_info):
                """Process a single folder - can be called in parallel."""
                dir_rel_path = folder_info['dir_rel_path']
                folder_title = folder_info['folder_title']
                folder_key = folder_info['folder_key']
                folder_initial_parent_id = folder_info['parent_id']
                folder_prev_history = folder_info['prev_history']
                
                # Resolve actual parent ID from folder_id_map (parent folder should already be created)
                # Calculate parent directory's relative path
                from pathlib import Path as PathLib
                if dir_rel_path and dir_rel_path != '.':
                    dir_path_obj = PathLib(dir_rel_path)
                    if dir_path_obj.parent == PathLib('.'):
                        parent_dir_rel_path = ''
                    else:
                        parent_dir_rel_path = str(dir_path_obj.parent)
                else:
                    parent_dir_rel_path = ''
                
                # Look up parent folder ID from map (thread-safe read)
                # NOTE: Parent folders are guaranteed to be in folder_id_map because:
                # 1. Folders are processed by depth level (shallow to deep)
                # 2. Parent folders have lower depth than children
                # 3. When processing depth N, all folders at depth N-1 are already processed
                resolved_parent_folder_id = None
                source_folder = folder_info.get('source_folder')
                
                if parent_dir_rel_path:
                    # Find parent folder key
                    parent_folder_key = None
                    for f in all_folder_pages:
                        if f['dir_rel_path'] == parent_dir_rel_path:
                            parent_folder_key = f['folder_key']
                            break
                    
                    if parent_folder_key and parent_folder_key in folder_id_map:
                        # Parent folder ID is guaranteed to exist (parent processed at earlier depth)
                        resolved_parent_folder_id = folder_id_map[parent_folder_key]
                    elif parent_dir_rel_path == '' or parent_dir_rel_path == '.':
                        if source_folder and source_folder in source_folder_created_ids:
                            resolved_parent_folder_id = source_folder_created_ids[source_folder]
                        else:
                            resolved_parent_folder_id = folder_initial_parent_id
                    else:
                        resolved_parent_folder_id = folder_initial_parent_id
                else:
                    if source_folder and source_folder in source_folder_created_ids:
                        resolved_parent_folder_id = source_folder_created_ids[source_folder]
                    else:
                        resolved_parent_folder_id = folder_initial_parent_id
                
                # Check sync state first for existing folder - TRUST SYNC STATE unless conflict
                # Only make API calls when we encounter a conflict during creation
                folder_id = None
                folder_status = None
                
                if folder_prev_history and folder_prev_history.get('folder_id'):
                    # Trust sync state - use existing folder_id
                    # Conflicts will be detected during create_folder if folder doesn't exist or has wrong parent
                    folder_id = folder_prev_history['folder_id']
                    folder_status = 'found'
                    return {
                        'folder_key': folder_key,
                        'dir_rel_path': dir_rel_path,
                        'folder_id': folder_id,
                        'folder_status': folder_status,
                        'resolved_parent_folder_id': resolved_parent_folder_id,
                        'folder_title': folder_title,
                        'source_folder': source_folder,
                        'message': f"  ℹ Using existing folder '{folder_title}' from sync state (ID: {folder_id}) - trusting sync state"
                    }
                
                # If not in sync state, need to create/find folder
                if not folder_id:
                    try:
                        folder_id, folder_status = confluence_sync.create_folder(
                            title=folder_title,
                            space_id=confluence_sync.space_id,
                            parent_id=resolved_parent_folder_id,
                            root_page_id=root_parent_id
                        )
                        
                        if folder_status == 'title_conflict':
                            parent_dir = folder_info.get('dir_path', Path(dir_rel_path)).parent
                            raise Exception(
                                f"Title conflict: Folder '{folder_title}' already exists elsewhere in the space.\n"
                                f"  To resolve: Add a .confluence-mapping.yaml file in '{parent_dir}' with:\n"
                                f"    folders:\n"
                                f"      {folder_info['dir_path'].name}: \"Unique Title Here\"\n"
                                f"  See ADR 0012 for details."
                            )
                    except TitleConflictError as e:
                        raise Exception(f"Title conflict creating folder '{folder_title}': {e}") from e
                    except Exception as create_error:
                        error_str = str(create_error)
                        if 'already exists' in error_str.lower() or '400' in error_str:
                            if folder_prev_history and folder_prev_history.get('folder_id'):
                                try:
                                    folder_data = confluence_sync.get_folder(folder_prev_history['folder_id'])
                                    if folder_data:
                                        folder_id = folder_prev_history['folder_id']
                                        folder_status = 'found'
                                    else:
                                        raise create_error
                                except Exception:
                                    raise create_error
                            else:
                                raise create_error
                        else:
                            raise create_error
                
                return {
                    'folder_key': folder_key,
                    'dir_rel_path': dir_rel_path,
                    'folder_id': folder_id,
                    'folder_status': folder_status,
                    'resolved_parent_folder_id': resolved_parent_folder_id,
                    'folder_title': folder_title,
                    'source_folder': source_folder,
                    'message': f"  ✓ {'Created' if folder_status == 'created' else 'Found'}: {folder_title} (ID: {folder_id})"
                }
            
            # Process folders by depth level, parallelizing within each level
            for depth in sorted(folders_by_depth.keys()):
                depth_folders = folders_by_depth[depth]
                if len(depth_folders) == 1:
                    # Single folder at this depth - process directly
                    folder_info = depth_folders[0]
                    result = process_single_folder(folder_info)
                    folder_id_map[result['folder_key']] = result['folder_id']
                    parent_id_map[result['dir_rel_path']] = result['folder_id']
                    print(result['message'])
                else:
                    # Multiple folders at this depth - process in parallel
                    with ThreadPoolExecutor(max_workers=folder_parallel_threads) as executor:
                        future_to_folder = {executor.submit(process_single_folder, folder_info): folder_info 
                                           for folder_info in depth_folders}
                        for future in as_completed(future_to_folder):
                            try:
                                result = future.result()
                                folder_id_map[result['folder_key']] = result['folder_id']
                                parent_id_map[result['dir_rel_path']] = result['folder_id']
                                print(result['message'])
                            except Exception as e:
                                folder_info = future_to_folder[future]
                                print(f"  ✗ Error processing folder '{folder_info['folder_title']}': {e}")
                                raise
            
            # Now update prepared contents and sync state for all processed folders
            for folder_info in all_folder_pages:
                dir_rel_path = folder_info['dir_rel_path']
                folder_title = folder_info['folder_title']
                folder_key = folder_info['folder_key']
                folder_id = folder_id_map.get(folder_key)
                
                if not folder_id:
                    continue  # Folder processing failed, skip
                
                # Resolve parent ID (already resolved during parallel processing)
                from pathlib import Path as PathLib
                if dir_rel_path and dir_rel_path != '.':
                    dir_path_obj = PathLib(dir_rel_path)
                    if dir_path_obj.parent == PathLib('.'):
                        parent_dir_rel_path = ''
                    else:
                        parent_dir_rel_path = str(dir_path_obj.parent)
                else:
                    parent_dir_rel_path = ''
                
                resolved_parent_folder_id = None
                source_folder = folder_info.get('source_folder')
                
                if parent_dir_rel_path:
                    parent_folder_key = None
                    for f in all_folder_pages:
                        if f['dir_rel_path'] == parent_dir_rel_path:
                            parent_folder_key = f['folder_key']
                            break
                    if parent_folder_key and parent_folder_key in folder_id_map:
                        resolved_parent_folder_id = folder_id_map[parent_folder_key]
                    elif parent_dir_rel_path == '' or parent_dir_rel_path == '.':
                        if source_folder and source_folder in source_folder_created_ids:
                            resolved_parent_folder_id = source_folder_created_ids[source_folder]
                        else:
                            resolved_parent_folder_id = folder_info['parent_id']
                    else:
                        resolved_parent_folder_id = folder_info['parent_id']
                else:
                    if source_folder and source_folder in source_folder_created_ids:
                        resolved_parent_folder_id = source_folder_created_ids[source_folder]
                    else:
                        resolved_parent_folder_id = folder_info['parent_id']
                
                folder_status = 'found' if folder_key in folder_id_map else 'created'
                
                # Update all prepared contents that should be under this folder
                for prepared in all_prepared_contents:
                    if hasattr(prepared, '_dir_rel_path') and prepared._dir_rel_path == dir_rel_path:
                        prepared.parent_id = folder_id
                
                # Validate folder hierarchy
                is_valid, issues = confluence_sync.validate_folder_hierarchy(
                    folder_id=folder_id,
                    expected_parent_id=resolved_parent_folder_id,
                    root_page_id=root_parent_id,
                    folder_path=dir_rel_path
                )
                if not is_valid:
                    print(f"  ⚠ Hierarchy validation issues for folder '{folder_title}': {issues}")
                
                # Update sync state for folder
                from sync_state import append_folder_history
                append_folder_history(
                    destination_id,
                    dir_rel_path,
                    source_folder=source_folder,
                    folder_id=folder_id,
                    folder_title=folder_title,
                    parent_id=resolved_parent_folder_id,
                    status=folder_status,
                    data_dir=data_dir
                )
        
        # Phase 2b: Sync file pages to Confluence in parallel
        # Pages are synced using ThreadPoolExecutor with configurable thread count
        # This significantly speeds up large syncs (1000+ files)
        print(f"\n[Phase 2b] Syncing {len(all_prepared_contents)} files to Confluence using {parallel_threads} parallel threads...")
        progress.start_step('Syncing files')
        
        def sync_progress_callback(current: int, file_display: str, status: Optional[str] = None):
            progress.update_step('Syncing files', current, show_every=5, current_file=file_display, status=status)
        
        sync_results = confluence_sync.sync_prepared_content_parallel(
            all_prepared_contents,
            parallel_threads=parallel_threads,
            progress_callback=sync_progress_callback,
            root_page_id=root_parent_id,
            force_update=force_update
        )
        results.extend(sync_results)
        progress.complete_step('Syncing files')
        
        # Phase 2c: Upload attachments and update image references
        print("\n[Phase 2c] Uploading attachments and updating image references...")
        attachment_count = 0
        for prepared in all_prepared_contents:
            if prepared.sync_result and prepared.sync_result.status != 'error' and prepared.page_id:
                # Upload images as attachments
                if hasattr(prepared, 'image_paths') and prepared.image_paths:
                    for image_path in prepared.image_paths:
                        attachment_name = attachment_handler.upload_attachment(prepared.page_id, image_path)
                        if attachment_name:
                            attachment_count += 1
                            print(f"  ✓ Uploaded: {image_path.name} to page '{prepared.title}'")
        
        if attachment_count > 0:
            print(f"  ✓ Uploaded {attachment_count} attachment(s)")
        else:
            print("  No attachments to upload")
        
        # Update sync state for all synced files
        for prepared in all_prepared_contents:
            if prepared.sync_result and prepared.sync_result.status != 'error':
                # Get previous parent ID from history
                prev_parent_id = prepared.prev_history.get('parent_id') if prepared.prev_history else None
                
                # If this was a rename, remove old path from state and add new path
                if prepared.renamed_from:
                    # Note: We don't delete the old entry from JSONL (append-only), but new entry will be the active one
                    pass
                
                # Note: file_key already includes source_folder prefix, so don't pass source_folder
                # to avoid double-prefixing in sync_state.py
                update_page_history(
                    destination_id,
                    prepared.file_key,
                    None,  # source_folder already in file_key
                    page_id=prepared.page_id,
                    page_title=getattr(prepared, 'actual_title_used', prepared.title),  # Use actual title used in Confluence
                    page_title_original=prepared.title,  # Store original title from Markdown
                    commit_hash=prepared.commit_hash,
                    sync_status=prepared.sync_status,
                    content_hash=prepared.content_hash,
                    version=prepared.version,
                    previous_commit=prepared.prev_history.get('last_sync_commit') if prepared.prev_history else None,
                    previous_sync_date=prepared.prev_history.get('last_sync_date') if prepared.prev_history else None,
                    previous_content_hash=prepared.prev_history.get('content_hash') if prepared.prev_history else None,
                    parent_id=prepared.parent_id,
                    previous_parent_id=prev_parent_id,
                    content_signature=prepared.content_signature,  # Store signature for future rename detection
                    data_dir=data_dir
                )
        
        # Phase 3: Handle orphaned pages and folders (files/directories deleted from repo)
        # Orphaned items are pages/folders in Confluence that no longer exist in source
        # Only items tracked in sync state are deleted (manually created content is preserved)
        print("\n[Phase 3] Detecting and deleting orphaned pages and folders...")
        discovered_file_keys = {prepared.file_key for prepared in all_prepared_contents}
        renamed_old_paths = {prepared.renamed_from for prepared in all_prepared_contents if prepared.renamed_from}
        discovered_folder_keys = {f['folder_key'] for f in all_folder_pages}
        
        orphan_handler = OrphanHandler(confluence_sync)
        orphan_pages, orphan_folders = orphan_handler.find_orphans(
            sync_state, 
            discovered_file_keys, 
            renamed_old_paths,
            discovered_folder_keys
        )
        
        total_orphans = len(orphan_pages) + len(orphan_folders)
        if total_orphans > 0:
            print(f"  Found {len(orphan_pages)} orphaned page(s) and {len(orphan_folders)} orphaned folder(s)")
            deleted_paths = orphan_handler.delete_orphans(orphan_pages, orphan_folders)
            print(f"  ✓ Deleted {len(deleted_paths)} orphaned item(s)")
            
            # Mark deleted orphans in state (by appending entries with null id)
            # Note: JSONL is append-only, so we mark as deleted rather than removing
            for deleted_path in deleted_paths:
                # Find the orphan entry
                orphan_entry = next((o for o in orphan_pages + orphan_folders if o['path'] == deleted_path), None)
                if orphan_entry:
                    if orphan_entry.get('type') == 'folder':
                        # Mark folder as deleted
                        from sync_state import append_folder_history
                        append_folder_history(
                            destination_id,
                            deleted_path,
                            source_folder=None,  # Will be extracted from path if needed
                            folder_id=None,  # Mark as deleted
                            folder_title=orphan_entry.get('folder_title'),
                            parent_id=None,
                            status='deleted',
                            data_dir=data_dir
                        )
                    else:
                        # Mark page as deleted
                        from sync_state import append_page_history
                        append_page_history(
                            destination_id,
                            deleted_path,
                            source_folder=None,  # Will be extracted from path if needed
                            page_id=None,  # Mark as deleted
                            page_title=orphan_entry.get('page_title'),
                            sync_status='deleted',
                            content_hash=None,
                            version=None,
                            data_dir=data_dir
                        )
        else:
            print("  No orphaned pages or folders found")
        
        print(f"\n✓ Sync completed for destination '{destination_id}'")
        print(f"  Processed {len(results)} files")
        
        # Compact sync state to remove duplicates
        original, compacted = compact_sync_state(destination_id, data_dir)
        if compacted < original:
            print(f"  Compacted sync state: {original} -> {compacted} entries ({original - compacted} duplicates removed)")
        
    except Exception as e:
        print(f"\n✗ Sync failed for destination '{destination_id}': {e}")
        import traceback
        traceback.print_exc()
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Sync Markdown files to Confluence using destination-based configuration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Sync a specific destination
  %(prog)s --destination hub-docs
  
  # Sync all destinations
  %(prog)s --all
  
  # Dry run for a destination
  %(prog)s --destination hub-docs --dry-run
  
  # Use custom config file
  %(prog)s --config path/to/config.yaml --destination hub-docs
        """
    )
    
    parser.add_argument(
        '--data-dir',
        type=Path,
        help='Path to data directory (default: data folder next to script)'
    )
    
    parser.add_argument(
        '--config',
        type=Path,
        help='Path to destination config file (default: confluence-destinations.yaml in data directory)'
    )
    
    parser.add_argument(
        '--destination',
        help='Destination ID to sync (required unless --all is used)'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Sync all destinations in config'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be synced without making changes'
    )
    
    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate report only (no sync)'
    )
    
    parser.add_argument(
        '--migrate-sync-state',
        action='store_true',
        help='Migrate sync state from directory pages to folders (Phase 16)'
    )
    
    parser.add_argument(
        '--cache-prepared',
        action='store_true',
        help='Save prepared content (Confluence storage format) to disk for debugging'
    )
    
    parser.add_argument(
        '--force-update',
        action='store_true',
        help='Force update all pages regardless of content hash (useful after link fix or format changes)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.all and not args.destination:
        parser.error("Either --destination or --all must be specified")
    
    if args.all and args.destination:
        parser.error("Cannot use both --destination and --all")
    
    # Get data directory
    data_dir = args.data_dir
    if data_dir:
        data_dir = Path(data_dir).resolve()
    
    # Get repo root
    repo_root = get_repo_root()
    
    # Load config
    try:
        config = load_destination_config(args.config, data_dir)
    except ConfigError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    
    # Get destinations to sync
    if args.all:
        destinations = [(d['id'], d) for d in config['destinations']]
    else:
        try:
            dest_config = get_destination(config, args.destination)
            destinations = [(args.destination, dest_config)]
        except ConfigError as e:
            print(f"ERROR: {e}")
            sys.exit(1)
    
    # Migrate sync state if requested (Phase 16-4)
    if args.migrate_sync_state:
        print("\n" + "="*80)
        print("Migrating Sync State from Directory Pages to Folders")
        print("="*80)
        from migrate_sync_state_to_folders import migrate_sync_state
        for dest_id, dest_config in destinations:
            print(f"\nMigrating destination: {dest_id}")
            report = migrate_sync_state(dest_id, data_dir=data_dir, dry_run=False)
            if report['errors']:
                print(f"  ⚠ Migration completed with {len(report['errors'])} error(s)")
            else:
                print(f"  ✓ Migration completed successfully")
        print("\n" + "="*80)
        return 0
    
    # Sync each destination
    all_results: Dict[str, List[SyncResult]] = {}
    errors: List[str] = []
    
    for dest_id, dest_config in destinations:
        try:
            results = sync_destination(
                dest_id,
                dest_config,
                repo_root,
                data_dir=data_dir,
                dry_run_override=args.dry_run if args.dry_run else None,
                cache_prepared=args.cache_prepared if hasattr(args, 'cache_prepared') else False,
                force_update=args.force_update if hasattr(args, 'force_update') else False
            )
            all_results[dest_id] = results
            
            # Generate and save report
            if not args.dry_run and not args.report:
                sync_state = load_sync_state(dest_id, data_dir)
                repo_commit_hash = get_current_commit_hash(repo_root)
                confluence_url = dest_config['confluence']['url']
                space_key = dest_config['confluence']['space_key']
                
                report_text = generate_sync_report(
                    dest_id,
                    dest_config['name'],
                    sync_state,
                    repo_commit_hash,
                    results,
                    confluence_url,
                    space_key
                )
                
                report_file = save_report_to_file(dest_id, report_text, data_dir)
                print(f"\nReport saved to: {report_file}")
                print("\n" + report_text)
                
        except Exception as e:
            error_msg = f"Destination '{dest_id}': {e}"
            errors.append(error_msg)
            print(f"\n✗ {error_msg}")
            if args.all:
                # Continue with other destinations
                continue
            else:
                # Single destination failed
                sys.exit(1)
    
    # Summary
    if args.all:
        print(f"\n{'='*80}")
        print("Sync Summary")
        print(f"{'='*80}")
        for dest_id, results in all_results.items():
            created = sum(1 for r in results if r.status == 'created')
            updated = sum(1 for r in results if r.status == 'updated')
            skipped = sum(1 for r in results if r.status == 'skipped')
            errors_count = sum(1 for r in results if r.status == 'error')
            print(f"  {dest_id}: {created} created, {updated} updated, {skipped} skipped, {errors_count} errors")
        
        if errors:
            print(f"\nErrors encountered:")
            for error in errors:
                print(f"  - {error}")
        
        if not errors:
            print("\n✓ All destinations synced successfully!")
        else:
            print(f"\n⚠ {len(errors)} destination(s) had errors")
            sys.exit(1)
    else:
        if not errors:
            print("\n✓ Sync completed successfully!")
        else:
            sys.exit(1)


if __name__ == '__main__':
    main()
