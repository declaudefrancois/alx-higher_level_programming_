#!/usr/bin/python3
def pow(a, b):
    aTob = a

    if b == 0:
        return 1
    if b < 0:
        return 1 / pow(a, -1 * b)
    for i in range(1, b):
        aTob *= a

    return aTob
