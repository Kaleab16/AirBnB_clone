#!/usr/bin/python3
"""Tests for the FileStorage class."""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def test_instance(self):
        """Test that FileStorage can be instantiated."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
