# test_bigone.py
"""
Tests for BigONE module.
"""

import unittest
from bigone import BigONE

class TestBigONE(unittest.TestCase):
    """Test cases for BigONE class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BigONE()
        self.assertIsInstance(instance, BigONE)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BigONE()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
