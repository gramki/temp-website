#!/usr/bin/env python3
"""
Unit tests for orphan handler.
"""

import unittest
from pathlib import Path
import sys
from unittest.mock import Mock, MagicMock

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from orphan_handler import OrphanHandler


class TestOrphanHandler(unittest.TestCase):
    """Test orphan detection and deletion."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_confluence = Mock()
        self.handler = OrphanHandler(self.mock_confluence)
    
    def test_find_orphans_returns_deleted_files(self):
        """Should find files in state but not in discovered files."""
        sync_state = {
            'sync_history': {
                'file1.md': {'page_id': '123', 'page_title': 'File 1'},
                'file2.md': {'page_id': '456', 'page_title': 'File 2'},
            }
        }
        discovered_files = {'file1.md'}
        renamed_files = set()
        
        orphans = self.handler.find_orphans(sync_state, discovered_files, renamed_files)
        
        self.assertEqual(len(orphans), 1)
        self.assertEqual(orphans[0]['path'], 'file2.md')
        self.assertEqual(orphans[0]['page_id'], '456')
    
    def test_find_orphans_excludes_renamed_files(self):
        """Should not mark renamed files as orphans."""
        sync_state = {
            'sync_history': {
                'old-path.md': {'page_id': '123', 'page_title': 'File'},
            }
        }
        discovered_files = {'new-path.md'}
        renamed_files = {'old-path.md'}  # This was renamed, not deleted
        
        orphans = self.handler.find_orphans(sync_state, discovered_files, renamed_files)
        
        self.assertEqual(len(orphans), 0)
    
    def test_find_orphans_empty_state(self):
        """Should return empty list if state is empty."""
        sync_state = {'sync_history': {}}
        discovered_files = {'file1.md'}
        renamed_files = set()
        
        orphans = self.handler.find_orphans(sync_state, discovered_files, renamed_files)
        
        self.assertEqual(len(orphans), 0)
    
    def test_delete_orphans_calls_api(self):
        """Should call delete_page for each orphan."""
        orphans = [
            {'path': 'file1.md', 'page_id': '123', 'page_title': 'File 1'},
            {'path': 'file2.md', 'page_id': '456', 'page_title': 'File 2'},
        ]
        
        self.mock_confluence.delete_page.return_value = True
        
        deleted = self.handler.delete_orphans(orphans)
        
        self.assertEqual(self.mock_confluence.delete_page.call_count, 2)
        self.assertEqual(len(deleted), 2)
        self.assertIn('file1.md', deleted)
        self.assertIn('file2.md', deleted)
    
    def test_delete_orphans_handles_api_errors(self):
        """Should handle API errors gracefully."""
        orphans = [
            {'path': 'file1.md', 'page_id': '123', 'page_title': 'File 1'},
        ]
        
        self.mock_confluence.delete_page.return_value = False
        
        deleted = self.handler.delete_orphans(orphans)
        
        self.assertEqual(len(deleted), 0)


if __name__ == '__main__':
    unittest.main()
