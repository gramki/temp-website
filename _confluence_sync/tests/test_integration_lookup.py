#!/usr/bin/env python3
"""
Integration tests for page lookup scenarios in Confluence sync.

Tests full sync scenarios with the new lookup hierarchy.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys
import tempfile
import shutil
import json

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from confluence_sync import ConfluenceSync, ParentPageNotFoundError, DuplicateTitleError
from sync_state import load_sync_state, update_page_history, get_page_history


class TestIntegrationLookup(unittest.TestCase):
    """Integration tests for lookup scenarios."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.test_dir)
        
        self.confluence = ConfluenceSync(
            base_url='https://test.atlassian.net',
            username='test@example.com',
            token='test-token',
            space_key='TEST'
        )
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_integration_01_full_sync_with_pages_in_sync_state(self, mock_request):
        """IT-LOOKUP-01: Full sync with pages in sync state."""
        # Setup: Sync state has entries for all files
        destination_id = 'test-dest'
        data_dir = self.test_dir
        
        # Create mock sync state entries
        sync_state = {
            'destination_id': destination_id,
            'sync_history': {
                'file1.md': {
                    'page_id': '111',
                    'content_hash': 'hash1',
                    'parent_id': 'root',
                    'version': 1
                },
                'file2.md': {
                    'page_id': '222',
                    'content_hash': 'hash2',
                    'parent_id': 'root',
                    'version': 1
                }
            }
        }
        
        # Mock: GET pages to verify they exist
        def mock_get_side_effect(method, endpoint, **kwargs):
            if method == 'GET' and 'content/111' in endpoint:
                return Mock(json=lambda: {'version': {'number': 1}, 'body': {'storage': {'value': '<p>File 1</p>'}}, 'ancestors': [{'id': 'root'}], 'title': 'File 1'})
            elif method == 'GET' and 'content/222' in endpoint:
                return Mock(json=lambda: {'version': {'number': 1}, 'body': {'storage': {'value': '<p>File 2</p>'}}, 'ancestors': [{'id': 'root'}], 'title': 'File 2'})
            return Mock(json=lambda: {})
        
        mock_request.side_effect = mock_get_side_effect
        
        # Execute: Lookup pages using sync state
        entry1 = sync_state['sync_history']['file1.md']
        page_id1, status1, _ = self.confluence.find_or_create_page(
            file_path='file1.md',
            title='File 1',
            storage_format='<p>File 1</p>',
            content_hash='hash1',
            parent_id='root',
            sync_state_entry=entry1,
            previous_content_hash='hash1',
            previous_parent_id='root'
        )
        
        entry2 = sync_state['sync_history']['file2.md']
        page_id2, status2, _ = self.confluence.find_or_create_page(
            file_path='file2.md',
            title='File 2',
            storage_format='<p>File 2</p>',
            content_hash='hash2',
            parent_id='root',
            sync_state_entry=entry2,
            previous_content_hash='hash2',
            previous_parent_id='root'
        )
        
        # Verify: Pages found via sync state, skipped (no changes)
        self.assertEqual(page_id1, '111')
        self.assertEqual(status1, 'skipped')
        self.assertEqual(page_id2, '222')
        self.assertEqual(status2, 'skipped')
    
    @patch.object(ConfluenceSync, 'find_page_by_title')
    @patch.object(ConfluenceSync, '_make_request')
    def test_integration_02_full_sync_with_missing_sync_state(self, mock_request, mock_find):
        """IT-LOOKUP-02: Full sync with missing sync state (recovery scenario)."""
        # Setup: No sync state, but pages exist in Confluence
        mock_find.return_value = '12345'  # Found via parent-scoped search
        
        # Mock: GET page
        mock_response = Mock()
        mock_response.json.return_value = {
            'version': {'number': 2},
            'body': {'storage': {'value': '<p>Existing</p>'}},
            'ancestors': [{'id': 'root'}],
            'title': 'Existing Page'
        }
        mock_request.return_value = mock_response
        
        # Execute: Lookup without sync state
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='existing.md',
            title='Existing Page',
            storage_format='<p>Existing</p>',
            content_hash='existing_hash',
            parent_id='root',
            sync_state_entry=None,  # No sync state
            previous_content_hash=None
        )
        
        # Verify: Page found via parent-scoped search
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'found')
        mock_find.assert_called_once_with('Existing Page', parent_id='root')
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_integration_03_directory_page_creation_order(self, mock_request):
        """IT-LOOKUP-03: Directory page creation order (parents before children)."""
        # Setup: Create directory pages in order
        parent_id_map = {}
        root_id = 'root'
        
        # Mock: Create parent directory
        def mock_create_parent(method, endpoint, **kwargs):
            if method == 'POST' and endpoint == '/content':
                return Mock(json=lambda: {'id': 'dir1', 'version': {'number': 1}})
            return Mock(json=lambda: {})
        
        mock_request.side_effect = mock_create_parent
        
        # Execute: Create parent directory
        parent_id, status1, _ = self.confluence.find_or_create_page(
            file_path='parent',
            title='Parent',
            storage_format='<p>Parent</p>',
            content_hash='parent_hash',
            parent_id=root_id,
            sync_state_entry=None
        )
        parent_id_map['parent'] = parent_id
        
        # Mock: Create child directory
        def mock_create_child(method, endpoint, **kwargs):
            if method == 'POST' and endpoint == '/content':
                return Mock(json=lambda: {'id': 'dir2', 'version': {'number': 1}})
            return Mock(json=lambda: {})
        
        mock_request.side_effect = mock_create_child
        
        # Execute: Create child directory
        child_id, status2, _ = self.confluence.find_or_create_page(
            file_path='parent/child',
            title='Child',
            storage_format='<p>Child</p>',
            content_hash='child_hash',
            parent_id=parent_id_map['parent'],  # Use parent from map
            sync_state_entry=None
        )
        
        # Verify: Both created, child has correct parent
        self.assertEqual(parent_id, 'dir1')
        self.assertEqual(status1, 'created')
        self.assertEqual(child_id, 'dir2')
        self.assertEqual(status2, 'created')
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_integration_04_parent_change_detection_and_update(self, mock_request):
        """IT-LOOKUP-04: Parent change detection and update."""
        # Setup: Page exists in sync state under old parent
        sync_state_entry = {
            'page_id': '12345',
            'content_hash': 'abc123',
            'parent_id': 'old_parent',
            'version': 3
        }
        
        # Mock: GET current page (under new parent)
        mock_get_response = Mock()
        mock_get_response.json.return_value = {
            'version': {'number': 3},
            'body': {'storage': {'value': '<p>Content</p>'}},
            'ancestors': [{'id': 'old_parent'}],  # Currently under old parent
            'title': 'Test Page'
        }
        
        # Mock: PUT to update parent
        mock_put_response = Mock()
        mock_put_response.json.return_value = {
            'id': '12345',
            'version': {'number': 4}
        }
        
        mock_request.side_effect = [mock_get_response, mock_put_response]
        
        # Execute: Try to sync with new parent
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>Content</p>',
            content_hash='abc123',
            parent_id='new_parent',  # New parent
            sync_state_entry=sync_state_entry,
            previous_content_hash='abc123',
            previous_parent_id='old_parent'  # Old parent
        )
        
        # Verify: Page updated with new parent
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'updated')
        self.assertEqual(version, 4)
        # Verify PUT was called with new parent
        put_call = [call for call in mock_request.call_args_list if call[0][0] == 'PUT'][0]
        self.assertIn('ancestors', put_call[1]['json'])
        self.assertEqual(put_call[1]['json']['ancestors'], [{'id': 'new_parent'}])


if __name__ == '__main__':
    unittest.main()
