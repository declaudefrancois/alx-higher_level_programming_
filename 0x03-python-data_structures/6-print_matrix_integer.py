#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m1 in matrix:
        for idx, item in enumerate(m1):
            print("{:d}".format(item), end="" if idx == len(m1) - 1 else " ")
        print("")
