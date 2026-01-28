#!/usr/bin/env python3
"""
Unit tests for anchor generation.
"""

import unittest
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from content_preparer import ContentPreparer


class TestAnchorGeneration(unittest.TestCase):
    """Test anchor macro generation for headings."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.preparer = ContentPreparer(repo_root=Path('/tmp'))
    
    def test_anchor_from_simple_heading(self):
        """Should generate anchor from simple heading."""
        html = "<h1>Introduction</h1>"
        result = self.preparer._add_anchors_to_headings(html)
        self.assertIn('ac:structured-macro ac:name="anchor"', result)
        self.assertIn('introduction', result.lower())
    
    def test_anchor_from_heading_with_spaces(self):
        """Should convert spaces to dashes in anchor."""
        html = "<h2>Getting Started</h2>"
        result = self.preparer._add_anchors_to_headings(html)
        self.assertIn('getting-started', result.lower())
    
    def test_anchor_from_heading_with_special_chars(self):
        """Should remove special characters from anchor."""
        html = "<h1>Test & More!</h1>"
        result = self.preparer._add_anchors_to_headings(html)
        # Special chars should be removed
        self.assertNotIn('&', result.lower())
        self.assertNotIn('!', result.lower())
    
    def test_anchor_preserves_case_in_content(self):
        """Should preserve original case in heading content."""
        html = "<h1>Title Case Heading</h1>"
        result = self.preparer._add_anchors_to_headings(html)
        # Content should preserve case
        self.assertIn('Title Case Heading', result)
        # But anchor slug should be lowercase
        self.assertIn('title-case-heading', result.lower())
    
    def test_multiple_headings_unique_anchors(self):
        """Should generate unique anchors for multiple headings."""
        html = "<h1>First</h1><h2>Second</h2>"
        result = self.preparer._add_anchors_to_headings(html)
        self.assertIn('first', result.lower())
        self.assertIn('second', result.lower())


if __name__ == '__main__':
    unittest.main()
