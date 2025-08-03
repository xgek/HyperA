# test_aiartist.py
"""
Tests for AIArtist module.
"""

import unittest
from aiartist import AIArtist

class TestAIArtist(unittest.TestCase):
    """Test cases for AIArtist class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIArtist()
        self.assertIsInstance(instance, AIArtist)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIArtist()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
