#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = [i * 0 for i in range(list_length)]
    for i in range(list_length):
        try:
            res[i] = div(my_list_1[i], my_list_2[i])
        except IndexError:
            print("out of range")
    return (res)


def div(a, b):
    res = 0
    try:
        if type(a) != int or type(b) != int:
            print("wrong type")
            res = 0
        else:
            res = a / b
    except ZeroDivisionError:
        print("division by 0")
        res = 0
    finally:
        return (res)
