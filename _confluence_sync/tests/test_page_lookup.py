#!/usr/bin/env python3
"""
Unit tests for page lookup hierarchy in Confluence sync.

Tests the unified find_or_create_page() method and related lookup logic.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from confluence_sync import ConfluenceSync, ParentPageNotFoundError, DuplicateTitleError, PageNotFoundError


class TestPageLookup(unittest.TestCase):
    """Test page lookup hierarchy."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.confluence = ConfluenceSync(
            base_url='https://test.atlassian.net',
            username='test@example.com',
            token='test-token',
            space_key='TEST'
        )
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_01_page_found_in_sync_state(self, mock_request):
        """Test 1: Page found in sync state - uses stored page_id."""
        # Setup: Sync state has page_id
        sync_state_entry = {
            'page_id': '12345',
            'content_hash': 'abc123',
            'parent_id': '67890',
            'version': 5
        }
        
        # Mock: GET page to verify it exists and get version
        mock_response = Mock()
        mock_response.json.return_value = {'version': {'number': 5}}
        mock_request.return_value = mock_response
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>Test</p>',
            content_hash='abc123',
            parent_id='67890',
            sync_state_entry=sync_state_entry,
            previous_content_hash='abc123',
            previous_parent_id='67890'
        )
        
        # Verify
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'skipped')  # Content and parent unchanged
        self.assertEqual(version, 5)
        mock_request.assert_called_once()
    
    @patch.object(ConfluenceSync, 'find_page_by_title')
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_02_page_not_in_sync_state_found_by_parent_scoped_search(self, mock_request, mock_find):
        """Test 2: Page not in sync state, found by parent-scoped search."""
        # Setup: No sync state entry, but page exists under parent
        mock_find.return_value = '12345'
        
        # Mock: GET page to get version
        mock_response = Mock()
        mock_response.json.return_value = {'version': {'number': 3}}
        mock_request.return_value = mock_response
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>Test</p>',
            content_hash='abc123',
            parent_id='67890',
            sync_state_entry=None,
            previous_content_hash=None
        )
        
        # Verify
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'found')
        mock_find.assert_called_once_with('Test Page', parent_id='67890')
    
    @patch.object(ConfluenceSync, 'find_page_by_title')
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_03_page_not_found_creates_new(self, mock_request, mock_find):
        """Test 3: Page not found anywhere - creates new page."""
        # Setup: No sync state, no page found
        mock_find.return_value = None
        
        # Mock: POST to create new page
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': '99999',
            'version': {'number': 1}
        }
        mock_request.return_value = mock_response
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>Test</p>',
            content_hash='abc123',
            parent_id='67890',
            sync_state_entry=None,
            previous_content_hash=None
        )
        
        # Verify
        self.assertEqual(page_id, '99999')
        self.assertEqual(status, 'created')
        self.assertEqual(version, 1)
        # Verify POST was called
        call_args = mock_request.call_args
        self.assertEqual(call_args[0][0], 'POST')
        self.assertEqual(call_args[0][1], '/content')
    
    @patch.object(ConfluenceSync, 'find_page_by_title_space_wide')
    @patch.object(ConfluenceSync, 'find_page_by_title')
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_04_already_exists_space_wide_search_succeeds(self, mock_request, mock_find, mock_space_wide):
        """Test 4: Page exists but 'already exists' error - space-wide search succeeds."""
        # Setup: Creation fails with "already exists", space-wide search finds it
        mock_find.return_value = None  # Not found under parent
        
        # Mock: POST fails with "already exists"
        mock_post_error = Mock()
        mock_post_error.response.status_code = 400
        mock_post_error.response.json.return_value = {
            'message': 'A page with this title already exists'
        }
        from requests.exceptions import HTTPError
        mock_request.side_effect = [
            HTTPError(response=mock_post_error.response, request=Mock()),
            Mock(json=lambda: {'version': {'number': 2}, 'body': {'storage': {'value': '<p>Old</p>'}}, 'ancestors': [{'id': '11111'}]}),  # GET current page
            Mock(json=lambda: {'id': '12345', 'version': {'number': 3}})  # PUT update
        ]
        
        # Mock: Space-wide search finds page
        mock_space_wide.return_value = ('12345', '11111')
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>New</p>',
            content_hash='newhash',
            parent_id='67890',
            sync_state_entry=None,
            previous_content_hash=None
        )
        
        # Verify
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'updated')
        mock_space_wide.assert_called_once()
    
    @patch.object(ConfluenceSync, 'find_page_by_title_space_wide')
    @patch.object(ConfluenceSync, 'find_page_by_title')
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_05_already_exists_space_wide_search_fails(self, mock_request, mock_find, mock_space_wide):
        """Test 5: Page exists but 'already exists' error - space-wide search fails."""
        # Setup: Creation fails, space-wide search also fails
        mock_find.return_value = None
        mock_space_wide.return_value = None
        
        # Mock: POST fails with "already exists"
        mock_post_error = Mock()
        mock_post_error.response.status_code = 400
        mock_post_error.response.json.return_value = {
            'message': 'A page with this title already exists'
        }
        from requests.exceptions import HTTPError
        mock_request.side_effect = HTTPError(response=mock_post_error.response, request=Mock())
        
        # Execute & Verify
        with self.assertRaises(DuplicateTitleError):
            self.confluence.find_or_create_page(
                file_path='test/file.md',
                title='Test Page',
                storage_format='<p>Test</p>',
                content_hash='abc123',
                parent_id='67890',
                sync_state_entry=None,
                previous_content_hash=None
            )
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_06_directory_page_creation_with_hierarchy(self, mock_request):
        """Test 6: Directory page creation with proper parent hierarchy."""
        # Setup: Directory page with parent
        sync_state_entry = None
        
        # Mock: POST to create directory page
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': 'dir123',
            'version': {'number': 1}
        }
        mock_request.return_value = mock_response
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='folder1/folder2',
            title='Folder 2',
            storage_format='<p>Directory content</p>',
            content_hash='dirhash',
            parent_id='dir1',  # Parent directory page ID
            sync_state_entry=sync_state_entry,
            previous_content_hash=None
        )
        
        # Verify
        self.assertEqual(page_id, 'dir123')
        self.assertEqual(status, 'created')
        # Verify ancestors were set correctly
        call_args = mock_request.call_args
        self.assertIn('ancestors', call_args[1]['json'])
        self.assertEqual(call_args[1]['json']['ancestors'], [{'id': 'dir1'}])
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_07_never_returns_none_for_skipped(self, mock_request):
        """Test 7: Never returns (None, 'skipped', ...) - always returns valid page_id."""
        # Setup: Page in sync state, content unchanged
        sync_state_entry = {
            'page_id': '12345',
            'content_hash': 'abc123',
            'parent_id': '67890',
            'version': 5
        }
        
        # Mock: GET page to verify it exists
        mock_response = Mock()
        mock_response.json.return_value = {
            'version': {'number': 5},
            'body': {'storage': {'value': '<p>Test</p>'}},
            'ancestors': [{'id': '67890'}],
            'title': 'Test Page'
        }
        mock_request.return_value = mock_response
        
        # Execute
        page_id, status, version = self.confluence.find_or_create_page(
            file_path='test/file.md',
            title='Test Page',
            storage_format='<p>Test</p>',
            content_hash='abc123',
            parent_id='67890',
            sync_state_entry=sync_state_entry,
            previous_content_hash='abc123',
            previous_parent_id='67890'
        )
        
        # Verify: page_id is never None, even when skipped
        self.assertIsNotNone(page_id)
        self.assertEqual(page_id, '12345')
        self.assertEqual(status, 'skipped')
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_08_parent_page_not_found_error(self, mock_request):
        """Test 8: Parent page not found - raises ParentPageNotFoundError."""
        # Setup: Try to create page under non-existent parent
        mock_post_error = Mock()
        mock_post_error.response.status_code = 404
        mock_post_error.response.json.return_value = {
            'message': 'Parent page does not exist'
        }
        from requests.exceptions import HTTPError
        mock_request.side_effect = HTTPError(response=mock_post_error.response, request=Mock())
        
        # Execute & Verify
        with self.assertRaises(ParentPageNotFoundError):
            self.confluence.find_or_create_page(
                file_path='test/file.md',
                title='Test Page',
                storage_format='<p>Test</p>',
                content_hash='abc123',
                parent_id='nonexistent',
                sync_state_entry=None,
                previous_content_hash=None
            )
    
    @patch.object(ConfluenceSync, 'find_page_by_title')
    def test_lookup_09_find_page_by_title_requires_parent_id(self, mock_find):
        """Test 9: find_page_by_title() requires parent_id - returns None without it."""
        # Execute: Call without parent_id
        result = self.confluence.find_page_by_title('Test Page', parent_id=None)
        
        # Verify: Returns None (doesn't search space-wide)
        self.assertIsNone(result)
        mock_find.assert_not_called()  # Method returns early, doesn't make API call
    
    @patch.object(ConfluenceSync, '_make_request')
    def test_lookup_10_space_wide_search_warning(self, mock_request):
        """Test 10: Space-wide search logs warning when used."""
        # Setup: Space-wide search finds page
        mock_response = Mock()
        mock_response.json.return_value = {
            'results': [{'id': '12345', 'ancestors': [{'id': '11111'}]}]
        }
        mock_request.return_value = mock_response
        
        # Execute with capture of print output
        import io
        import contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = self.confluence.find_page_by_title_space_wide('Test Page', expected_parent_id='67890')
        
        output = f.getvalue()
        
        # Verify: Warning message appears
        self.assertIn('WARNING', output)
        self.assertIn('space-wide search', output.lower())
        self.assertIsNotNone(result)
        self.assertEqual(result[0], '12345')


if __name__ == '__main__':
    unittest.main()
