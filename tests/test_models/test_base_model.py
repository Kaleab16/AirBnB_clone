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

    def test_unique_ids(self):
        """Test that each instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        """Test created_at."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test the string representation."""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)

    def test_save(self):
        """Test that save updates updated_at."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict."""
        obj = BaseModel()
        obj.name = "test"
        obj.my_number = 42

        data = obj.to_dict()

        self.assertEqual(data["name"], "test")
        self.assertEqual(data["my_number"], 42)
        self.assertEqual(data["id"], obj.id)
        self.assertEqual(data["__class__"], "BaseModel")

        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

        self.assertEqual(
            data["created_at"],
            obj.created_at.isoformat()
        )
        self.assertEqual(
            data["updated_at"],
            obj.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()
