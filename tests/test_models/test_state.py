#!/usr/bin/python3
"""Tests for the State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    def test_id(self):
        """Test that State has a string id."""
        state = State()
        self.assertIsInstance(state.id, str)


if __name__ == "__main__":
    unittest.main()
