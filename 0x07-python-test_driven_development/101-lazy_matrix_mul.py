#!/usr/bin/python3
from numpy import matmul

"""
    Matrix multiplication with
    numpy.
"""

def lazy_matrix_mul(m_a, m_b):
    """
        Mutliplies two matrix using numpy.

        Args:
            m_a(list(list(int|float))): First matrix.
            m_b(list(list(int|float))): First matrix.

        Returns:
            list(list(in|float)): m_a * m_b.
    """
    return matmul(m_a, m_b)
