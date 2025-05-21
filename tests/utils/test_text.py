# tests/utils/test_text.py
"""Tests for text utility functions."""
import unittest
from utils.text import normalize_text

class TestNormalizeText(unittest.TestCase):
    """Test cases for the normalize_text function."""

    def test_lowercase(self):
        """Test that text is converted to lowercase."""
        self.assertEqual(normalize_text("HELLO"), "hello")
        self.assertEqual(normalize_text("Hello World"), "hello world")

    def test_strip_whitespace(self):
        """Test that whitespace is stripped."""
        self.assertEqual(normalize_text("  hello  "), "hello")
        self.assertEqual(normalize_text("\n\thello\n\t"), "hello")

    def test_remove_punctuation(self):
        """Test that punctuation is removed."""
        self.assertEqual(normalize_text("hello!"), "hello")
        self.assertEqual(normalize_text("hello, world!"), "hello world")
        self.assertEqual(normalize_text("hello-world"), "hello world")
        self.assertEqual(normalize_text("h.e.l.l.o"), "h e l l o")

    def test_combined_normalization(self):
        """Test combined normalization of text."""
        self.assertEqual(normalize_text("  HELLO, World! "), "hello world")
        self.assertEqual(normalize_text("What's UP?"), "whats up")
        self.assertEqual(normalize_text("  This-is, a. TEST!  "), "this is a test")


if __name__ == "__main__":
    unittest.main()