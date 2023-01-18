#!/usr/bin/python3
"""
    Rectangle class test.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Rectangle test Case.
    """

    def test_should_inherit_base(self):
        """
            Instance of Rectangle should be Base
        """
        b1 = Rectangle(10, 12)
        self.assertIsInstance(b1, Rectangle)

    def test_all_atttribute_set(self):
        """
            Attributes should be set correctly and accessible.
        """
        w = 4
        h = 8
        x = 12
        y = 24
        id = 12

        r1 = Rectangle(w, h, x, y, id)
        self.assertEqual(r1.width, w)
        self.assertEqual(r1.height, h)
        self.assertEqual(r1.x, x)
        self.assertEqual(r1.y, y)
        self.assertEqual(r1.id, id)

    def test_raise_typerErrors(self):
        """
            Should raise a TypeError if user is
            trying to set a non int value.
        """
        with self.assertRaises(TypeError) as ctx:
            Rectangle("10", 10, 1, 2)

        e = ctx.exception
        self.assertIsInstance(e, TypeError)
        self.assertEqual("{}".format(e), "width must be an integer")

        with self.assertRaises(TypeError) as ctx:
            Rectangle(12, [], 1, 2)

        e = ctx.exception
        self.assertIsInstance(e, TypeError)
        self.assertEqual("{}".format(e), "height must be an integer")
 
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 12, 12, [], 2)
        self.assertRaises(TypeError, "y must be an integer",
                               Rectangle, 12, 12, 14, "2")

    def test_raise_value_errors(self):
        """
            should raise if width <= 0 or height <= 0 or x < 0 or y < 0
        """
        gt_err = "{} must be > 0"
        gte_err = "{} must be >= 0"
        self.assertRaisesRegex(ValueError, "must be >= 0",
                          Rectangle, 1, 1, -1, -4)
        self.assertRaisesRegex(ValueError, "must be >= 0",
                          Rectangle, 1, 1, 1, -4)

        self.assertRaisesRegex(ValueError, "must be > 0",
                          Rectangle, -1, 1, 1, -4)
        self.assertRaisesRegex(ValueError, "must be > 0",
                          Rectangle, 1, 0, 1, 45)

    def test_required_positional_args(self):
        """
            Width and height are required.
        """
        err = ("TypeError: __init__() missing 2 "
               "required positional arguments: "
               "'width' and 'height'")
        self.assertRaises(TypeError, err,
                          Rectangle)

    def test_rectangle_are(self):
        """
            Area calculation shoudl be correct.
        """
        r1 = Rectangle(4, 4)
        self.assertEqual(r1.area(), 16)

        r2 = Rectangle(23, 3)
        self.assertEqual(r2.area(), 69)
