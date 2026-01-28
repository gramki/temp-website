#!/usr/bin/env python3
"""
Content Preparer Module - Phase 1 of Confluence Sync

This module handles preparing all Markdown content for Confluence sync.
It performs all local file processing, content conversion, and metadata
extraction WITHOUT making any API calls to Confluence.

Clear boundaries:
- Input: Markdown files, sync state, configuration
- Output: List of PreparedContent objects ready for syncing
- No dependencies on Confluence API
- Fully testable without network access
"""

import re
from pathlib import Path
from typing import Dict, Optional, List, Tuple, Any
from dataclasses import dataclass, field

try:
    import markdown
    from markdown.extensions import codehilite, tables, fenced_code
except ImportError:
    raise ImportError("'markdown' library not found. Install with: pip install markdown")

from ignore_handler import IgnoreHandler
from git_utils import get_file_commit_hash, get_file_commit_date, get_file_github_url
from sync_state import compute_content_hash, compute_content_signature
from html import escape as html_escape
from title_mapping import get_title_mapping_loader


def escape_xml(text: str) -> str:
    """Escape special characters for XML/HTML."""
    if text is None:
        return ''
    return html_escape(str(text), quote=True)


def escape_title_for_confluence(title: str) -> str:
    """Escape a page title for use in Confluence storage format."""
    if title is None:
        return ''
    # Escape XML special characters
    escaped = escape_xml(title)
    return escaped


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
    content_signature: str  # For rename detection
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
    renamed_from: Optional[str] = None  # Old path if this is a renamed file
    image_paths: List[Path] = field(default_factory=list)  # List of image file paths to upload as attachments


class ContentPreparer:
    """
    Prepares Markdown content for Confluence sync.
    
    This class handles all local file processing and content conversion:
    - Scans directory structure and finds Markdown files
    - Converts Markdown to Confluence Storage Format
    - Builds link resolution cache for cross-references
    - Applies title mappings from .confluence-mapping.yaml files
    - Extracts Git metadata (commit hash, GitHub URLs)
    
    It does NOT make any API calls to Confluence.
    All API interactions are handled by ConfluenceSync class.
    """
    
    def __init__(
        self,
        repo_root: Path,
        github_repo_url: Optional[str] = None,
        add_git_metadata: bool = False,
        file_to_title: Optional[Dict[str, str]] = None,
        file_to_page_id: Optional[Dict[str, str]] = None,
        attachment_handler: Optional[Any] = None
    ):
        """
        Initialize content preparer.
        
        Args:
            repo_root: Repository root directory
            github_repo_url: GitHub repository URL for metadata
            add_git_metadata: Whether to add Git metadata
            file_to_title: Cache of file paths to page titles (for link conversion)
            file_to_page_id: Cache of file paths to page IDs (for link conversion - more reliable than titles)
            attachment_handler: Optional AttachmentHandler instance for image uploads
        """
        self.repo_root = repo_root
        self.github_repo_url = github_repo_url
        self.add_git_metadata = add_git_metadata
        self.file_to_title = file_to_title or {}
        self.file_to_page_id = file_to_page_id or {}
        self.ignore_handler: Optional[IgnoreHandler] = None
        self.attachment_handler = attachment_handler
    
    def markdown_to_storage_format(
        self,
        markdown_content: str,
        current_file_path: Path,
        root_path: Path,
        commit_hash: Optional[str] = None
    ) -> str:
        """
        Convert Markdown to Confluence Storage Format.
        
        Args:
            markdown_content: Markdown content to convert
            current_file_path: Path to current file (for link conversion)
            root_path: Root path (for link conversion)
            commit_hash: Optional commit hash for Git metadata
            
        Returns:
            Confluence storage format (HTML-like)
        """
        # Convert Markdown to HTML first
        md = markdown.Markdown(
            extensions=[
                'codehilite',
                'tables',
                'fenced_code',
                'nl2br',
                'sane_lists'
            ]
        )
        html = md.convert(markdown_content)
        
        # Add anchor macros to headings for deep linking
        html = self._add_anchors_to_headings(html)
        
        # Convert HTML links to Confluence page links
        if current_file_path and root_path:
            html = self.convert_html_links_to_confluence(html, current_file_path, root_path)
        
        # Add Git metadata if enabled
        if self.add_git_metadata:
            html = self._add_git_metadata(html, current_file_path, commit_hash)
        
        # Convert HTML to Confluence Storage Format
        storage_format = self._html_to_storage_format(html)
        
        return storage_format
    
    def _add_anchors_to_headings(self, html: str) -> str:
        """
        Add Confluence anchor macros to headings for deep linking.
        
        Args:
            html: HTML content with headings
            
        Returns:
            HTML with anchor macros added to headings
        """
        def add_anchor(match):
            tag = match.group(1)
            content = match.group(2)
            # Generate slug from heading text (similar to GitHub's anchor generation)
            # Remove HTML tags from content first
            import html as html_module
            text_content = html_module.unescape(re.sub(r'<[^>]+>', '', content))
            # Generate slug: lowercase, replace spaces/hyphens with dashes, remove special chars
            slug = re.sub(r'[^\w\s-]', '', text_content.lower())
            slug = re.sub(r'[\s_]+', '-', slug).strip('-')
            # Limit length
            if len(slug) > 50:
                slug = slug[:50].rstrip('-')
            if not slug:
                slug = 'heading'
            # Add anchor macro before heading content
            anchor = f'<ac:structured-macro ac:name="anchor"><ac:parameter ac:name="">{slug}</ac:parameter></ac:structured-macro>'
            return f'<{tag}>{anchor}{content}</{tag}>'
        
        # Match headings: <h1>content</h1> through <h6>content</h6>
        return re.sub(r'<(h[1-6])>([^<]+)</\1>', add_anchor, html)
    
    def convert_html_links_to_confluence(self, html: str, current_file_path: Path, root_path: Path) -> str:
        """
        Convert HTML links to .md files to Confluence page links.
        
        For existing pages (found in file_to_page_id), uses page ID-based linking.
        For new pages (not yet synced), falls back to title-based linking.
        
        Args:
            html: HTML content
            current_file_path: Path to the current file
            root_path: Root path of the sync operation
            
        Returns:
            HTML with links converted to Confluence format
        """
        link_pattern = r'<a\s+[^>]*href=["\']([^"\']+\.md[^"\']*)["\'][^>]*>([^<]+)</a>'
        
        def replace_link(match):
            link_path = match.group(1)
            link_text = match.group(2).strip()
            
            # Remove anchor/fragment if present
            if '#' in link_path:
                link_path, anchor = link_path.split('#', 1)
            else:
                anchor = None
            
            # Resolve relative path
            if link_path.startswith('/'):
                target_path = root_path / link_path.lstrip('/')
            elif link_path.startswith('./'):
                target_path = current_file_path.parent / link_path[2:]
            elif link_path.startswith('../'):
                target_path = current_file_path.parent / link_path
            else:
                target_path = current_file_path.parent / link_path
            
            # Normalize path
            try:
                abs_target = target_path.resolve()
                abs_root = root_path.resolve()
                
                try:
                    target_str = str(abs_target.relative_to(abs_root))
                except ValueError:
                    return match.group(0)
                
                target_str = target_str.replace('\\', '/')
                
                # Look up page ID first (more reliable than title), then fall back to title
                possible_paths = [
                    target_str,
                    target_str.lstrip('./'),
                ]
                
                page_id = None
                page_title = None
                
                # Try to find page ID first (most reliable)
                for path_variant in possible_paths:
                    if path_variant in self.file_to_page_id:
                        page_id = self.file_to_page_id[path_variant]
                        break
                
                # If no page ID, try to find page title
                if not page_id:
                    for path_variant in possible_paths:
                        if path_variant in self.file_to_title:
                            page_title = self.file_to_title[path_variant]
                            break
                
                # Note: Confluence Cloud does NOT support ri:page-id or ri:content-id
                # in storage format - it strips these attributes. Must use ri:content-title.
                # We still look up page_id first to verify the page exists, but use title for linking.
                
                # Get title - prefer from cache, or use page_id lookup result if available
                resolved_title = page_title
                if page_id and not resolved_title:
                    # We have page_id but no title - look up the title from cache
                    for path_variant in possible_paths:
                        if path_variant in self.file_to_title:
                            resolved_title = self.file_to_title[path_variant]
                            break
                
                if resolved_title:
                    # Use title-based linking (Confluence Cloud only supports this)
                    # Escape title for XML safety
                    escaped_title = escape_title_for_confluence(resolved_title)
                    # Preserve anchor if present
                    if anchor:
                        return f'<ac:link ac:anchor="{escape_xml(anchor)}"><ri:page ri:content-title="{escaped_title}"/><ac:plain-text-link-body><![CDATA[{link_text}]]></ac:plain-text-link-body></ac:link>'
                    else:
                        return f'<ac:link><ri:page ri:content-title="{escaped_title}"/><ac:plain-text-link-body><![CDATA[{link_text}]]></ac:plain-text-link-body></ac:link>'
                else:
                    # No page found - return as regular link
                    return f'<a href="{link_path}">{link_text}</a>'
            except Exception:
                return match.group(0)
        
        return re.sub(link_pattern, replace_link, html)
    
    def _html_to_storage_format(self, html: str) -> str:
        """Convert HTML to Confluence Storage Format."""
        # Remove DOCTYPE, html, head, body tags if present
        html = re.sub(r'<!DOCTYPE[^>]*>', '', html, flags=re.IGNORECASE)
        html = re.sub(r'<html[^>]*>', '', html, flags=re.IGNORECASE)
        html = re.sub(r'</html>', '', html, flags=re.IGNORECASE)
        html = re.sub(r'<head[^>]*>.*?</head>', '', html, flags=re.IGNORECASE | re.DOTALL)
        html = re.sub(r'<body[^>]*>', '', html, flags=re.IGNORECASE)
        html = re.sub(r'</body>', '', html, flags=re.IGNORECASE)
        
        result = html.strip()
        
        # Ensure we have at least some content (Confluence requires non-empty body)
        if not result or len(result) < 10:
            result = '<p></p>'  # Minimal valid Confluence storage format
        
        return result
    
    def _add_git_metadata(self, content: str, file_path: Optional[Path] = None, commit_hash: Optional[str] = None) -> str:
        """Add Git metadata to content using Confluence info macro."""
        if not self.add_git_metadata:
            return content
        
        metadata_parts = []
        
        if commit_hash:
            metadata_parts.append(f"Commit: {commit_hash}")
        
        if file_path and self.github_repo_url and self.repo_root:
            github_url = get_file_github_url(
                file_path,
                self.repo_root,
                self.github_repo_url,
                commit_hash
            )
            if github_url:
                metadata_parts.append(f'<a href="{github_url}">View on GitHub</a>')
        
        if metadata_parts:
            metadata_html = '<p><ac:structured-macro ac:name="info"><ac:rich-text-body><p>'
            metadata_html += '<strong>Source:</strong> ' + ' | '.join(metadata_parts)
            metadata_html += '</p></ac:rich-text-body></ac:structured-macro></p>'
            content = content + '\n\n' + metadata_html
        
        return content
    
    def prepare_directory_content(
        self,
        directory: Path,
        parent_id: Optional[str] = None,
        root_path: Optional[Path] = None,
        source_folder: Optional[str] = None,
        commit_hash: Optional[str] = None,
        destination_id: Optional[str] = None,
        sync_state: Optional[Dict[str, Any]] = None,
        files_processed_count: Optional[List[int]] = None,
        prepared_contents: Optional[List[PreparedContent]] = None,
        parent_id_map: Optional[Dict[str, str]] = None,
        progress_callback: Optional[callable] = None,
        directory_pages: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[List[PreparedContent], Dict[str, str], List[Dict[str, Any]]]:
        """
        Phase 1: Prepare all content locally (no API calls).
        Recursively processes directory and prepares all content for syncing.
        
        Args:
            directory: Directory to process
            parent_id: Parent page ID (for hierarchy)
            root_path: Root path for relative path calculation
            source_folder: Source folder identifier
            commit_hash: Fallback commit hash
            destination_id: Destination ID for state lookup
            sync_state: Cached sync state
            files_processed_count: Mutable counter for progress
            prepared_contents: List to accumulate prepared content
            parent_id_map: Map of directory paths to parent IDs
            progress_callback: Optional callback for progress updates
            directory_pages: List to accumulate directory page info
            
        Returns:
            Tuple of (prepared_contents list, parent_id_map dict, directory_pages list)
        """
        if prepared_contents is None:
            prepared_contents = []
        if parent_id_map is None:
            parent_id_map = {}
        if directory_pages is None:
            directory_pages = []
        if files_processed_count is None:
            files_processed_count = [0]
        if root_path is None:
            root_path = directory
        
        # Initialize ignore handler if not already done
        if self.ignore_handler is None:
            self.ignore_handler = IgnoreHandler(root_path)
        
        # Check if this directory should have a page (not root, has content, not ignored)
        is_root = (directory == root_path)
        dir_rel_path = str(directory.relative_to(root_path)) if not is_root else directory.name
        
        # Prepare folder entry if needed (not root, and has subdirectories or files)
        if not is_root:
            # Check if directory has content (subdirs or files)
            has_content = False
            for item in directory.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    if not (self.ignore_handler and self.ignore_handler.should_ignore_directory(item)):
                        has_content = True
                        break
                elif item.is_file() and item.suffix == '.md' and not item.name.startswith('.'):
                    if not (self.ignore_handler and self.ignore_handler.should_ignore(item)):
                        has_content = True
                        break
            
            if has_content:
                # Generate default folder title from directory name
                # DESIGN NOTE (ADR 0012): Do NOT auto-generate unique titles.
                # If a title conflict occurs, use .confluence-mapping.yaml to specify a unique title.
                default_folder_title = directory.name.replace('_', ' ').replace('-', ' ').title()
                # Remove leading numbers and clean up
                import re
                default_folder_title = re.sub(r'^\d+[-_\s]*', '', default_folder_title).strip()
                if not default_folder_title:
                    default_folder_title = directory.name
                
                # Check for README in this directory (for title, but README stays as separate page)
                readme_path = directory / 'README.md'
                if readme_path.exists() and not (self.ignore_handler and self.ignore_handler.should_ignore(readme_path)):
                    try:
                        with open(readme_path, 'r', encoding='utf-8') as f:
                            readme_content = f.read()
                        # Extract title from README (optional - can use for folder title)
                        for line in readme_content.split('\n'):
                            line = line.strip()
                            if line.startswith('# '):
                                readme_title = line[2:].strip()
                                if readme_title:
                                    default_folder_title = readme_title  # Use README title for folder
                                break
                    except:
                        pass
                
                # Apply title mapping from .confluence-mapping.yaml if present
                # The mapping file in the PARENT directory controls this folder's title
                parent_dir = directory.parent
                title_mapper = get_title_mapping_loader()
                folder_title = title_mapper.get_folder_title(
                    parent_directory=parent_dir,
                    folder_name=directory.name,
                    default_title=default_folder_title
                )
                
                # Get previous history for folder
                folder_prev_history = None
                if sync_state and destination_id:
                    folder_key = f"{source_folder}/{dir_rel_path}" if source_folder else dir_rel_path
                    # Check for folder history (separate from page history)
                    folders = sync_state.get('folders', {})
                    if folder_key in folders:
                        folder_prev_history = folders[folder_key]
                
                # Add to folder pages list (folders, not directory pages)
                directory_pages.append({
                    'dir_path': directory,
                    'dir_rel_path': dir_rel_path,
                    'folder_title': folder_title,  # From directory name or README title
                    'parent_id': parent_id,  # Parent folder or page ID
                    'source_folder': source_folder,
                    'folder_key': f"{source_folder}/{dir_rel_path}" if source_folder else dir_rel_path,
                    'prev_history': folder_prev_history,
                    'readme_path': readme_path if readme_path.exists() else None  # Track README for title
                })
        
        # Process Markdown files in this directory
        md_files = sorted(directory.glob('*.md'))
        for md_file in md_files:
            if md_file.name.startswith('.'):
                continue
            
            if self.ignore_handler and self.ignore_handler.should_ignore(md_file):
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title
                title = None
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
                    elif line.startswith('#'):
                        title = line[1:].strip()
                        break
                
                # Generate default title from file content or filename
                # DESIGN NOTE (ADR 0012): Do NOT auto-generate unique titles.
                # If a title conflict occurs, use .confluence-mapping.yaml to specify a unique title.
                if not title:
                    title = md_file.stem.replace('_', ' ').replace('-', ' ').title()
                
                # Apply title mapping from .confluence-mapping.yaml if present
                # The mapping file in the same directory controls this page's title
                title_mapper = get_title_mapping_loader()
                title = title_mapper.get_page_title(
                    directory=directory,
                    filename=md_file.name,
                    default_title=title
                )
                
                rel_path = str(md_file.relative_to(root_path))
                file_key = f"{source_folder}/{rel_path}" if source_folder else rel_path
                
                # Get file-specific commit hash and date
                file_commit_hash = None
                file_commit_date = None
                if self.add_git_metadata:
                    file_commit_hash = get_file_commit_hash(md_file, self.repo_root)
                    file_commit_date = get_file_commit_date(md_file, self.repo_root)
                
                commit_hash_to_use = file_commit_hash or commit_hash
                
                # Get previous history from cached sync_state
                prev_history = None
                if sync_state and destination_id:
                    if source_folder:
                        prefixed_path = f"{source_folder}/{rel_path}"
                        if prefixed_path in sync_state.get('sync_history', {}):
                            prev_history = sync_state['sync_history'][prefixed_path]
                    if not prev_history and rel_path in sync_state.get('sync_history', {}):
                        prev_history = sync_state['sync_history'][rel_path]
                
                # Check force sync
                force_sync = False
                if sync_state and destination_id:
                    force_sync_paths = sync_state.get('force_sync_paths', [])
                    for force_path in force_sync_paths:
                        if file_key.startswith(force_path) or rel_path.startswith(force_path):
                            force_sync = True
                            break
                
                # Convert to storage format
                storage_format = self.markdown_to_storage_format(content, md_file, root_path, commit_hash_to_use)
                content_hash = compute_content_hash(storage_format)
                # Compute content signature for rename detection
                content_sig = compute_content_signature(content)
                
                # Get directory relative path for this file
                file_dir_rel_path = str(directory.relative_to(root_path)) if directory != root_path else directory.name
                
                # Get parent ID (will be resolved during sync phase when folders are created)
                # For now, use the directory's relative path - parent ID will be resolved in Phase 2a
                dir_parent_id = parent_id_map.get(file_dir_rel_path, parent_id)
                
                # Get GitHub URL
                github_url = None
                if self.add_git_metadata:
                    github_url = get_file_github_url(md_file, self.repo_root, self.github_repo_url, commit_hash_to_use)
                
                # Get existing page ID from state (if available)
                existing_page_id = None
                if prev_history and prev_history.get('page_id'):
                    existing_page_id = prev_history['page_id']
                
                # Find images in this file for later upload
                image_paths = []
                if self.attachment_handler:
                    image_paths = self.attachment_handler.find_images_in_markdown(content, md_file)
                
                prepared = PreparedContent(
                    file_path=str(md_file),
                    rel_path=rel_path,
                    source_folder=source_folder,
                    title=title,
                    content=content,
                    storage_format=storage_format,
                    content_hash=content_hash,
                    content_signature=content_sig,
                    parent_id=dir_parent_id,  # Will be updated when directory page is created
                    commit_hash=commit_hash_to_use,
                    commit_date=file_commit_date,
                    github_url=github_url,
                    file_key=file_key,
                    prev_history=prev_history,
                    force_sync=force_sync,
                    existing_page_id=existing_page_id,
                    renamed_from=None,  # Will be set if rename detected
                    image_paths=image_paths
                )
                # Store directory relative path for later parent ID update
                prepared._dir_rel_path = file_dir_rel_path  # Store for parent ID update
                prepared_contents.append(prepared)
                
                files_processed_count[0] += 1
                if progress_callback:
                    file_display = rel_path if len(rel_path) <= 60 else "..." + rel_path[-57:]
                    progress_callback(files_processed_count[0], file_display)
                
            except Exception as e:
                print(f"  ✗ Error preparing {md_file}: {e}")
                continue
        
        # Recursively process subdirectories
        for subdir in sorted(directory.iterdir()):
            if subdir.is_dir() and not subdir.name.startswith('.'):
                if self.ignore_handler and self.ignore_handler.should_ignore_directory(subdir):
                    continue
                # Get parent ID for subdirectory (will be set when folder is created)
                subdir_parent_id = parent_id_map.get(dir_rel_path, parent_id) if not is_root else parent_id
                
                # Recursively prepare subdirectory
                self.prepare_directory_content(
                    subdir,
                    subdir_parent_id,
                    root_path,
                    source_folder=source_folder,
                    commit_hash=commit_hash,
                    destination_id=destination_id,
                    sync_state=sync_state,
                    files_processed_count=files_processed_count,
                    prepared_contents=prepared_contents,
                    parent_id_map=parent_id_map,
                    progress_callback=progress_callback,
                    directory_pages=directory_pages
                )
        
        return prepared_contents, parent_id_map, directory_pages
