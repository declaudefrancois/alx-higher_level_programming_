#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for c in my_string:
        if ord(c) != ord('c') and ord(c) != ord('C'):
            str += c
    return str
