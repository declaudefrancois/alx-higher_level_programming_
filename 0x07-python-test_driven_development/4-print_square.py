#!/usr/bin/python3
"""
    This module contains a single
    function that print a square.
"""


def print_square(size):
    """
        Prints a square with the character #.

        Args:
            size (int): The length of a side.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
