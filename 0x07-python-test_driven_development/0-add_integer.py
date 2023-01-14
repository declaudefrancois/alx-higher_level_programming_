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
    if type(a) not in [int, float] or a in [float('NaN'), None]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b in [float('NaN'), None]:
        raise TypeError("b must be an integer")

    if (a == float('inf') and b == -float('inf')
       or b == float('inf') and a == -float('inf')):
        return float('NaN')
    if abs(a) == float('inf') and b != -float('inf'):
        return a
    if abs(b) == float('inf') and a != -float('inf'):
        return b
    if a == float('inf') and b == float('inf'):
        return a

    return (int(a) + int(b))
