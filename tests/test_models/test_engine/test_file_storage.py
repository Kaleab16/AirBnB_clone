#!/usr/bin/python3
"""Tests for FileStorage."""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage."""

    def setUp(self):
        """Set up test storage."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage._FileStorage__objects = {}

    def test_file_path(self):
        """Test __file_path."""
        self.assertIsInstance(
            self.storage._FileStorage__file_path,
            str
        )

    def test_objects(self):
        """Test __objects."""
        self.assertIsInstance(
            self.storage._FileStorage__objects,
            dict
        )

    def test_all(self):
        """Test all()."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new()."""
        obj = BaseModel()
        self.storage.new(obj)

        key = "BaseModel.{}".format(obj.id)

        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], obj)

    def test_save(self):
        """Test save()."""
        obj = BaseModel()
        obj.name = "Test"
        self.storage.new(obj)
        self.storage.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as file:
            content = file.read()

        self.assertIn(obj.id, content)
        self.assertIn("Test", content)

    def test_reload(self):
        """Test reload()."""
        obj = BaseModel()
        obj.name = "Reload Test"
        self.storage.new(obj)
        self.storage.save()

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = "BaseModel.{}".format(obj.id)

        self.assertIn(key, self.storage.all())

        new_obj = self.storage.all()[key]

        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.name, "Reload Test")


if __name__ == "__main__":
    unittest.main()
