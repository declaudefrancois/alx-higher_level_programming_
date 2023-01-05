#!/usr/bin/python3
c = 0
def magic_string():
    global c
    c += 1
    return ", ".join(["BestSchool" for i in range(c)])
