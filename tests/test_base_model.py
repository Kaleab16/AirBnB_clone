#!/usr/bin/python3
"""Tests for BaseModel."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel."""

    def test_id(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_created_at(self):
        """Test created_at."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict."""
        obj = BaseModel()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
