#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
            Should return None if len(list) == 0
        """
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """
            Should return None if no args given.
        """
        self.assertIsNone(max_integer())

    def test_correct_result(self):
        """
            Should return the max integer in a list.
        """
        list_t = [1, 5, 6, 78, 56, 0]
        self.assertEqual(max_integer(list_t), 78)

        list_t = [1, 1, 5, 78965, 452, 99999]
        self.assertEqual(max_integer(list_t), 99999)

        list_t = [19.5, 4, 6, 8, -float('inf')]
        self.assertEqual(max_integer(list_t), 19.5)

        list_t = [19.5, 4, 6, 8, float('inf')]
        self.assertEqual(max_integer(list_t), float('inf'))

        list_t = ["a", "t", "z"]
        self.assertEqual(max_integer(list_t), "z")

        list_t = [7]
        self.assertEqual(max_integer(list_t), 7)

    def test_raises_error(self):
        """
            Should raise errors if successive list element
            are not int or float.
        """
        list_t = [99, "a", [1], float('inf')]
        self.assertRaises(TypeError, max_integer, list_t)

        list_t = [99, "a", [1], float('inf')]
        self.assertRaises(TypeError, max_integer, list_t)

        list_t = ["b", "a", "z", []]
        self.assertRaises(TypeError, max_integer, list_t)
