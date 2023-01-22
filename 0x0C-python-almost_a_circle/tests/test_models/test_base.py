#!/usr/bin/python3
"""
    Base class tests.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
        Base class TestCase.
    """
    def test_id_set(self):
        """
            When a new Base class instance is created, its
            value should always be set to an int.
        """
        b1 = Base(99)
        self.assertEqual(b1.id, 99)

        b2 = Base()
        self.assertIsInstance(b2.id, int)

    def test_id_increment(self):
        """
            Ids should be incremented when attributed by the
            class.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_to_json_string(self):
        """
            Should return the JSON of a list of dict.
        """
        r1 = Rectangle(10, 4, 8, 6, 1)

        json_dict = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(Base.to_json_string(None), "[]")
        res = '[{"id": 1, "width": 10, "height": 4, "x": 8, "y": 6}]'
        self.assertEqual(json_dict, res)

    def test_save_to_file(self):
        """
            Should write the JSON representation of list to a file.
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
    
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 2, 2, 2)
        l_r = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), Base.to_json_string(l_r))
