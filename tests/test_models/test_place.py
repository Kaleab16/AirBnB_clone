#!/usr/bin/python3
"""Tests for the Place class."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def test_id(self):
        """Test that Place has a string id."""
        place = Place()
        self.assertIsInstance(place.id, str)


if __name__ == "__main__":
    unittest.main()
