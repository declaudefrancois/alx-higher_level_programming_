#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx = []
    for i, mx1 in enumerate(matrix):
        mx[i] = []
        for j, item in enumerate(matrix[i]):
            mx[i][j] = item ** 2
    return (mx)
