#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for item in my_list:
        bool_list.append(item % 2 == 0)
    return (bool_list)
