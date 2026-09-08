#!/usr/bin/python3
"""Tests for the Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    def test_id(self):
        """Test that Review has a string id."""
        review = Review()
        self.assertIsInstance(review.id, str)


if __name__ == "__main__":
    unittest.main()
