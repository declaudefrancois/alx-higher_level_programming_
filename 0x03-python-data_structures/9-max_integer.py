#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    my_list.sort()
    my_list.reverse()
    return (my_list[0])
