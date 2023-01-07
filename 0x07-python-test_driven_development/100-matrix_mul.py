#!/usr/bin/python3
"""
    contains a function that multiplies
    2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
        Multiplies 2 matrices.

        Args:
            m_a (list(list(int|float))): The first matrix.
            m_b (list(list(int|float))): The second matrix.

        Returns:
            list(list(int|float)): m_a * m_b

        Raises:
            TypeError: if m_a or m_b is not a list or
                if m_a or m_b is not a list of lists or
                if m_a or m_b is not a rectangle
                (all ‘rows’ should be of the same size) or
                if one element of those list of lists is
                not an integer or a float

            ValueError: if m_a or m_b is empty
                (it means: = [] or = [[]]) or
                If m_a and m_b can’t be multiplied.
    """
    validate_mx(m_a, "m_a")
    validate_mx(m_b, "m_b")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rows = len(m_a)
    cols = len(m_b[0])
    n = len(m_a[0])

    result = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = sum([m_a[i][k] * m_b[k][j] for k in range(n)])

    return result


def validate_mx(m, name):
    """
       if m, matrix of name name is invalid,
       raise error.
    """
    msgs = [
            "{} must be a list",
            "{} must be a list of lists",
            "{} can't be empty",
            "each row of {} must be of the same size",
            "{} should contain only integers or floats"]

    if type(m) is not list:
        raise TypeError(msgs[0].format(name))
    if len(m) == 0:
        raise TypeError(msgs[2].format(name))

    if not all(type(row) is list for row in m):
        raise TypeError(msgs[1].format(name))

    if len(m) == 1 and len(m[0]) == 0:
        raise TypeError(msgs[2].format(name))

    if not all(type(cell) in [int, float]
               for cell in [i for row in m for i in row]):
        raise TypeError(msgs[4].format(name))

    if not all(len(row) == len(m[0]) for row in m):
        raise TypeError(msgs[3].format(name))
