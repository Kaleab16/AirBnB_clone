#!/usr/bin/python3
"""Tests for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City."""

    def test_id(self):
        """Test that City has a string id."""
        city = City()
        self.assertIsInstance(city.id, str)


if __name__ == "__main__":
    unittest.main()
