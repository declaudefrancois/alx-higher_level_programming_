#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul


print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2, 3]], [[3, 4], [5, 6], [5, 6]]))
print(matrix_mul([[1, 2], [0, 0]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2, 8], [7, 2, 5.6], [1, 1, 1]], [[3, 4, 4], [5, 6, 4], [7, 8, 9]]))
