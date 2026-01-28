#!/usr/bin/env python3
"""
Unit tests for attachment handler.
"""

import unittest
from pathlib import Path
import sys
from unittest.mock import Mock, MagicMock, patch

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from attachment_handler import AttachmentHandler


class TestAttachmentHandler(unittest.TestCase):
    """Test attachment upload and image reference conversion."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_confluence = Mock()
        self.handler = AttachmentHandler(self.mock_confluence)
    
    def test_find_local_images(self):
        """Should find local image references in Markdown."""
        content = "![Alt text](./image.png)\n![Remote](https://example.com/img.jpg)"
        base_path = Path('/tmp/test.md')
        
        # Create a mock image file
        with patch('pathlib.Path.exists', return_value=True):
            with patch('pathlib.Path.is_file', return_value=True):
                images = self.handler.find_images_in_markdown(content, base_path)
                # Should find local image but not remote
                self.assertEqual(len(images), 1)
    
    def test_ignore_remote_images(self):
        """Should ignore remote HTTP/HTTPS image URLs."""
        content = "![Remote](https://example.com/img.jpg)"
        base_path = Path('/tmp/test.md')
        
        images = self.handler.find_images_in_markdown(content, base_path)
        
        self.assertEqual(len(images), 0)
    
    def test_ignore_data_urls(self):
        """Should ignore data URLs."""
        content = "![Data](data:image/png;base64,iVBORw0KGgo=)"
        base_path = Path('/tmp/test.md')
        
        images = self.handler.find_images_in_markdown(content, base_path)
        
        self.assertEqual(len(images), 0)
    
    @patch('attachment_handler.requests')
    def test_upload_attachment_success(self, mock_requests):
        """Should upload attachment successfully."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status = Mock()
        mock_requests.request.return_value = mock_response
        
        page_id = '123'
        file_path = Path('/tmp/test.png')
        
        with patch('pathlib.Path.exists', return_value=True):
            with patch('builtins.open', create=True):
                result = self.handler.upload_attachment(page_id, file_path)
                
                self.assertIsNotNone(result)
                self.assertEqual(result, 'test.png')
    
    @patch('attachment_handler.requests')
    def test_upload_attachment_failure(self, mock_requests):
        """Should handle upload failure gracefully."""
        mock_requests.request.side_effect = Exception("Upload failed")
        
        page_id = '123'
        file_path = Path('/tmp/test.png')
        
        with patch('pathlib.Path.exists', return_value=True):
            result = self.handler.upload_attachment(page_id, file_path)
            
            self.assertIsNone(result)
    
    def test_convert_img_to_confluence_macro(self):
        """Should convert img tags to Confluence image macros."""
        html = '<img src="test.png" alt="Test Image">'
        page_id = '123'
        
        # Mark attachment as uploaded
        self.handler.page_attachments[page_id] = ['test.png']
        
        result = self.handler.convert_image_references(html, page_id)
        
        self.assertIn('ac:image', result)
        self.assertIn('ri:attachment', result)
        self.assertIn('test.png', result)


if __name__ == '__main__':
    unittest.main()
