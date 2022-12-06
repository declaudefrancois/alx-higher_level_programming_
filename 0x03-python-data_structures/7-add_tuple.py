#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_list = [0, 0]
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    for i in range(2):
        t_list[i] += tuple_a[i] if a_len - 1 >= i else 0
        t_list[i] += tuple_b[i] if b_len - 1 >= i else 0

    return (tuple(t_list))
