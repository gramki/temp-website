#!/usr/bin/env python3
"""
Detect and fix broken links in Confluence pages.

This script:
- Scans Confluence pages for broken internal links
- Attempts to fix links by searching for pages with similar titles
- Reports fixed and unfixable broken links
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json

sys.path.insert(0, str(Path(__file__).parent))

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    print("ERROR: 'requests' library not found. Install with: pip install requests")
    sys.exit(1)

try:
    from config_loader import load_destination_config, get_destination, resolve_credentials, ConfigError, get_repo_root
except ImportError as e:
    print(f"ERROR: Failed to import required modules: {e}")
    sys.exit(1)


class BrokenLinkFixer:
    """Detect and fix broken links in Confluence."""
    
    def __init__(self, base_url: str, username: str, token: str, space_key: str):
        """
        Initialize Confluence link fixer.
        
        Args:
            base_url: Confluence base URL
            username: Confluence username/email
            token: Confluence API token
            space_key: Confluence space key
        """
        base_url = base_url.rstrip('/')
        if '/wiki' not in base_url:
            self.base_url = f"{base_url}/wiki"
        else:
            self.base_url = base_url
        
        self.api_url = f"{self.base_url}/rest/api"
        self.username = username
        self.token = token
        self.space_key = space_key
        self.auth = HTTPBasicAuth(username, token)
        
        # Cache of all pages in space (title -> page_id)
        self.page_cache: Dict[str, str] = {}
        self.page_titles_lower: Dict[str, str] = {}  # lowercase -> original title
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make API request with error handling."""
        endpoint = endpoint.lstrip('/')
        url = f"{self.api_url}/{endpoint}"
        headers = kwargs.pop('headers', {})
        headers.setdefault('Content-Type', 'application/json')
        headers.setdefault('Accept', 'application/json')
        
        try:
            response = requests.request(
                method,
                url,
                auth=self.auth,
                headers=headers,
                timeout=30,
                **kwargs
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f"ERROR: API request failed: {e}")
            if e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"  Details: {json.dumps(error_detail, indent=2)}")
                except:
                    print(f"  Response: {e.response.text[:500]}")
            raise
    
    def build_page_cache(self) -> None:
        """Build cache of all pages in the space."""
        print("Building page cache...")
        start = 0
        limit = 100
        
        while True:
            try:
                response = self._make_request(
                    'GET',
                    '/content',
                    params={
                        'spaceKey': self.space_key,
                        'start': start,
                        'limit': limit,
                        'expand': 'version'
                    }
                )
                data = response.json()
                results = data.get('results', [])
                
                if not results:
                    break
                
                for page in results:
                    page_id = str(page['id'])
                    title = page.get('title', '')
                    if title:
                        self.page_cache[title] = page_id
                        self.page_titles_lower[title.lower()] = title
                
                start += len(results)
                
                if len(results) < limit:
                    break
                    
            except Exception as e:
                print(f"ERROR: Failed to build page cache: {e}")
                break
        
        print(f"  Cached {len(self.page_cache)} pages")
    
    def extract_links_from_content(self, content: str) -> List[Tuple[str, str]]:
        """
        Extract Confluence page links from content.
        
        Args:
            content: Confluence Storage Format content
            
        Returns:
            List of (link_title, full_link_xml) tuples
        """
        links = []
        
        # Pattern for Confluence page links: <ac:link><ri:page ri:content-title="Title" .../>
        link_pattern = r'<ac:link>.*?<ri:page\s+[^>]*ri:content-title=["\']([^"\']+)["\'][^>]*/>.*?</ac:link>'
        
        for match in re.finditer(link_pattern, content, re.DOTALL):
            link_title = match.group(1)
            full_link = match.group(0)
            links.append((link_title, full_link))
        
        return links
    
    def find_page_by_title_fuzzy(self, target_title: str) -> Optional[str]:
        """
        Find a page by title using fuzzy matching (case-insensitive, partial match).
        
        Args:
            target_title: Target page title
            
        Returns:
            Page ID if found, None otherwise
        """
        target_lower = target_title.lower().strip()
        
        # Exact match (case-insensitive)
        if target_lower in self.page_titles_lower:
            original_title = self.page_titles_lower[target_lower]
            return self.page_cache[original_title]
        
        # Partial match - check if any page title contains the target or vice versa
        for lower_title, original_title in self.page_titles_lower.items():
            if target_lower in lower_title or lower_title in target_lower:
                # Prefer exact matches or very close matches
                if abs(len(target_lower) - len(lower_title)) <= 3:
                    return self.page_cache[original_title]
        
        return None
    
    def check_link(self, link_title: str) -> Tuple[bool, Optional[str]]:
        """
        Check if a link is broken and find a fix if possible.
        
        Args:
            link_title: Page title from the link
            
        Returns:
            Tuple of (is_broken, fixed_page_id)
        """
        # Check if page exists
        if link_title in self.page_cache:
            return False, self.page_cache[link_title]  # Link is valid
        
        # Try fuzzy matching
        fixed_page_id = self.find_page_by_title_fuzzy(link_title)
        if fixed_page_id:
            return True, fixed_page_id  # Link is broken but can be fixed
        
        return True, None  # Link is broken and cannot be fixed
    
    def fix_link_in_content(self, content: str, old_title: str, new_page_id: str, new_title: str) -> str:
        """
        Fix a broken link in content by replacing it with the correct page reference.
        
        Args:
            content: Confluence Storage Format content
            old_title: Old (broken) page title
            new_page_id: New page ID to link to
            new_title: New page title
            
        Returns:
            Updated content
        """
        # Find and replace the link
        # Pattern: <ac:link>...<ri:page ri:content-title="old_title".../>...</ac:link>
        pattern = f'<ac:link>.*?<ri:page\\s+[^>]*ri:content-title=["\']{re.escape(old_title)}["\'][^>]*/>.*?</ac:link>'
        
        replacement = f'<ac:link><ri:page ri:content-title="{new_title}" ri:space-key="{self.space_key}"/><ac:plain-text-link-body><![CDATA[{new_title}]]></ac:plain-text-link-body></ac:link>'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        return content
    
    def get_page_title_by_id(self, page_id: str) -> Optional[str]:
        """Get page title by page ID."""
        for title, pid in self.page_cache.items():
            if pid == page_id:
                return title
        return None
    
    def scan_and_fix_page(self, page_id: str, dry_run: bool = False) -> Dict[str, any]:
        """
        Scan a page for broken links and fix them.
        
        Args:
            page_id: Page ID to scan
            dry_run: If True, don't make changes
            
        Returns:
            Dictionary with scan results
        """
        try:
            # Get page content
            response = self._make_request(
                'GET',
                f'/content/{page_id}',
                params={'expand': 'version,body.storage'}
            )
            page_data = response.json()
            
            page_title = page_data.get('title', 'Unknown')
            version = page_data['version']['number']
            content = page_data.get('body', {}).get('storage', {}).get('value', '')
            
            # Extract links
            links = self.extract_links_from_content(content)
            
            broken_links = []
            fixed_links = []
            unfixable_links = []
            
            updated_content = content
            
            for link_title, full_link in links:
                is_broken, fixed_page_id = self.check_link(link_title)
                
                if is_broken:
                    if fixed_page_id:
                        # Can be fixed
                        fixed_title = self.get_page_title_by_id(fixed_page_id)
                        if fixed_title:
                            fixed_links.append({
                                'old_title': link_title,
                                'new_title': fixed_title,
                                'new_page_id': fixed_page_id
                            })
                            if not dry_run:
                                updated_content = self.fix_link_in_content(
                                    updated_content,
                                    link_title,
                                    fixed_page_id,
                                    fixed_title
                                )
                    else:
                        # Cannot be fixed
                        unfixable_links.append({
                            'title': link_title,
                            'link_xml': full_link[:100]  # Truncate for display
                        })
                else:
                    broken_links.append({
                        'title': link_title,
                        'status': 'valid'
                    })
            
            # Update page if there are fixes and not dry run
            if fixed_links and not dry_run:
                page_data_update = {
                    'id': page_id,
                    'type': 'page',
                    'title': page_title,
                    'version': {'number': version + 1},
                    'space': {'key': self.space_key},
                    'body': {
                        'storage': {
                            'value': updated_content,
                            'representation': 'storage'
                        }
                    }
                }
                
                # Preserve ancestors
                ancestors = page_data.get('ancestors', [])
                if ancestors:
                    page_data_update['ancestors'] = [{'id': str(ancestors[-1]['id'])}]
                
                self._make_request('PUT', f'/content/{page_id}', json=page_data_update)
            
            return {
                'page_id': page_id,
                'page_title': page_title,
                'total_links': len(links),
                'broken_links': len(broken_links),
                'fixed_links': fixed_links,
                'unfixable_links': unfixable_links,
                'updated': len(fixed_links) > 0 and not dry_run
            }
            
        except Exception as e:
            return {
                'page_id': page_id,
                'error': str(e)
            }


def main():
    parser = argparse.ArgumentParser(
        description='Detect and fix broken links in Confluence pages',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--config',
        type=Path,
        help='Path to destination config file (default: confluence-destinations.yaml in repo root)'
    )
    
    parser.add_argument(
        '--destination',
        required=True,
        help='Destination ID to scan'
    )
    
    parser.add_argument(
        '--page-id',
        help='Specific page ID to scan (if not provided, scans all pages)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be fixed without making changes'
    )
    
    args = parser.parse_args()
    
    # Load config
    try:
        config = load_destination_config(args.config)
        dest_config = get_destination(config, args.destination)
    except ConfigError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    
    # Resolve credentials
    try:
        creds = resolve_credentials(dest_config)
    except ConfigError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    
    # Initialize fixer
    confluence_config = dest_config['confluence']
    base_url = confluence_config['url']
    space_key = confluence_config['space_key']
    
    fixer = BrokenLinkFixer(base_url, creds['username'], creds['token'], space_key)
    
    # Build page cache
    fixer.build_page_cache()
    print()
    
    # Scan pages
    if args.page_id:
        # Scan specific page
        results = [fixer.scan_and_fix_page(args.page_id, args.dry_run)]
    else:
        # Scan all pages
        print("Scanning all pages...")
        results = []
        for page_id in fixer.page_cache.values():
            result = fixer.scan_and_fix_page(page_id, args.dry_run)
            results.append(result)
    
    # Generate report
    print("\n" + "="*80)
    print("Broken Link Report")
    print("="*80 + "\n")
    
    total_pages = len(results)
    pages_with_broken = sum(1 for r in results if r.get('unfixable_links') or r.get('fixed_links'))
    total_fixed = sum(len(r.get('fixed_links', [])) for r in results)
    total_unfixable = sum(len(r.get('unfixable_links', [])) for r in results)
    pages_updated = sum(1 for r in results if r.get('updated'))
    
    print(f"Summary:")
    print(f"  Pages scanned: {total_pages}")
    print(f"  Pages with broken links: {pages_with_broken}")
    print(f"  Links fixed: {total_fixed}")
    print(f"  Links unfixable: {total_unfixable}")
    if not args.dry_run:
        print(f"  Pages updated: {pages_updated}")
    print()
    
    # Detailed report
    if total_fixed > 0:
        print("Fixed Links:")
        for result in results:
            if result.get('fixed_links'):
                print(f"\n  Page: {result.get('page_title')} (ID: {result.get('page_id')})")
                for fix in result['fixed_links']:
                    print(f"    '{fix['old_title']}' → '{fix['new_title']}'")
        print()
    
    if total_unfixable > 0:
        print("Unfixable Links:")
        for result in results:
            if result.get('unfixable_links'):
                print(f"\n  Page: {result.get('page_title')} (ID: {result.get('page_id')})")
                for link in result['unfixable_links']:
                    print(f"    '{link['title']}'")
        print()
    
    if args.dry_run:
        print("\nDRY RUN - No changes were made")
    elif pages_updated > 0:
        print(f"\n✓ Fixed {total_fixed} broken link(s) in {pages_updated} page(s)")


if __name__ == '__main__':
    main()
