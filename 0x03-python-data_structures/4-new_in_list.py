#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cpy = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        my_list_cpy[idx] = element

    return my_list_cpy
