#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

list_t = [1, 2, "H", 9]
print_reversed_list_integer(list_t)

list = None
print_reversed_list_integer(list)

list = [1, 2, 3]
print_reversed_list_integer(list)

list = [1]
print_reversed_list_integer(list)

list = []
print_reversed_list_integer(list)

