#!/usr/bin/python3
import unittest
import os


class BaseTestCase(unittest.TestCase):
    """
        Base test case to define some common
        actions.
    """
    def setUp(self):
        """
            Deletes all files prevouisly
            generated before starting each test.
        """
        files = [
            "Rectangle.json",
            "Square.json",
            "Rectangle.csv",
            "Square.csv",
        ]
        for f in files:
            if os.path.exists(f):
                os.remove(f)

