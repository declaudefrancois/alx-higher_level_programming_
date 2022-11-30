#!/usr/bin/python3
def islower(c):
    return ((ord(c) >= ord('a') and ord(c) <= ord('z')) or
            (ord(c) >= ord('0') and ord(c) <= ord('9')))
