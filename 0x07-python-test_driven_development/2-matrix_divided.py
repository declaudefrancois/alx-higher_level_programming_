#!/usr/bin/python3
"""
    This modules contains a single function
    for operating division on a matrix
    elements.
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix (list of lists).

        Args:
            list (list(int)): a list of list of integers.
            div (int): divisor.

        Returns:
            list (list(int)): A matrix with all elements divided
                              by div.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(type(cell) == int or type(cell) == float
                for cell in [i for row in matrix for i in row])):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
