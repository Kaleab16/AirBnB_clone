#!/usr/bin/python3
"""Tests for the Amenity class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def test_id(self):
        """Test that Amenity has a string id."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)


if __name__ == "__main__":
    unittest.main()
