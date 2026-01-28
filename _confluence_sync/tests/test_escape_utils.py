#!/usr/bin/env python3
"""
Unit tests for XML escaping utilities.
"""

import unittest
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from content_preparer import escape_xml, escape_title_for_confluence


class TestEscapeUtils(unittest.TestCase):
    """Test XML escaping functions."""
    
    def test_escape_ampersand(self):
        """Should escape ampersand."""
        text = "A & B"
        result = escape_xml(text)
        self.assertEqual(result, "A &amp; B")
    
    def test_escape_angle_brackets(self):
        """Should escape angle brackets."""
        text = "<code>test</code>"
        result = escape_xml(text)
        self.assertEqual(result, "&lt;code&gt;test&lt;/code&gt;")
    
    def test_escape_quotes(self):
        """Should escape quotes."""
        text = 'He said "Hello" and \'Hi\''
        result = escape_xml(text)
        self.assertEqual(result, 'He said &quot;Hello&quot; and &apos;Hi&apos;')
    
    def test_escape_combined_special_chars(self):
        """Should escape all special characters."""
        text = '<test attr="value" & more>'
        result = escape_xml(text)
        self.assertIn('&lt;', result)
        self.assertIn('&quot;', result)
        self.assertIn('&amp;', result)
        self.assertIn('&gt;', result)
    
    def test_escape_already_escaped_content(self):
        """Should double-escape already escaped content."""
        text = "&amp;"
        result = escape_xml(text)
        self.assertEqual(result, "&amp;amp;")
    
    def test_escape_empty_string(self):
        """Should handle empty string."""
        result = escape_xml("")
        self.assertEqual(result, "")
    
    def test_escape_title_for_confluence(self):
        """Should escape and strip title."""
        title = '  <Test> & "More"  '
        result = escape_title_for_confluence(title)
        self.assertEqual(result, "&lt;Test&gt; &amp; &quot;More&quot;")


if __name__ == '__main__':
    unittest.main()
