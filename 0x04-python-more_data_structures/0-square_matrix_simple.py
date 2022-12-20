#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx = []
    for mx1 in matrix:
        mx.append([n ** 2 for n in mx1])
    return (mx)
