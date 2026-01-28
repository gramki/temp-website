#!/usr/bin/env python3
"""
Unit tests for content signature computation.
"""

import unittest
from pathlib import Path
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from sync_state import compute_content_signature


class TestContentSignature(unittest.TestCase):
    """Test content signature computation."""
    
    def test_signature_same_content_same_hash(self):
        """Same content should produce same signature."""
        content1 = "# Title\n\nSome content here."
        content2 = "# Title\n\nSome content here."
        
        sig1 = compute_content_signature(content1)
        sig2 = compute_content_signature(content2)
        
        self.assertEqual(sig1, sig2)
    
    def test_signature_different_content_different_hash(self):
        """Different content should produce different signatures."""
        content1 = "# Title\n\nSome content here."
        content2 = "# Different Title\n\nDifferent content."
        
        sig1 = compute_content_signature(content1)
        sig2 = compute_content_signature(content2)
        
        self.assertNotEqual(sig1, sig2)
    
    def test_signature_ignores_whitespace_changes(self):
        """Signature should be based on structure, not whitespace."""
        content1 = "# Title\n\nSome content."
        content2 = "# Title\n\n  Some content.  "
        
        sig1 = compute_content_signature(content1)
        sig2 = compute_content_signature(content2)
        
        # Note: Current implementation uses first 500 chars, so minor whitespace changes
        # might still produce same signature if structure is same
        # This test documents current behavior
        self.assertEqual(sig1, sig2)
    
    def test_signature_detects_structural_changes(self):
        """Signature should detect changes in heading structure."""
        content1 = "# Title\n\nContent."
        content2 = "# Title\n## Subtitle\n\nContent."
        
        sig1 = compute_content_signature(content1)
        sig2 = compute_content_signature(content2)
        
        self.assertNotEqual(sig1, sig2)
    
    def test_signature_with_empty_content(self):
        """Empty content should produce a signature."""
        content = ""
        sig = compute_content_signature(content)
        self.assertIsNotNone(sig)
        self.assertEqual(len(sig), 16)  # Short hash is 16 chars


if __name__ == '__main__':
    unittest.main()
