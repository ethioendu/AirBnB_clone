#!/usr/bin/python3
"""test for console
"""
import unittest
import sys
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting
    """

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help message
    """

    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting
    """

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

if __name__ == '__main__':
    unittest.main()
