#!/usr/bin/python3
"""
    Add module.
    This module contains a simple function for adding
    two numbers.
"""


def add_integer(a, b=98):
    """ Adds two numbers of type inf or float.

    Args:
        a(Union[int, float]): The first number.
        b(Union[int, float]): The second number.

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        Union[int, float]: the result of a + b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
