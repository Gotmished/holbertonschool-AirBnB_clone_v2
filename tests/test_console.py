#!/usr/bin/python3
"""Test file for console module"""

import pycodestyle
import unittest
import inspect


class TestDocsConsole(unittest.TestCase):
    """Tests for presence of console module documentation"""

    def test_pycode_class(self):
        """Checks that console complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks that test_console complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
