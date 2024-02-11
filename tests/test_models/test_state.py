#!/usr/bin/python3
"""test for state
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
