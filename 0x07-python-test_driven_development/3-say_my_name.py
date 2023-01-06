#!/usr/bin/python3
"""
    This module contains a single
    function say_may_name wich prints
    someone's name.
"""


def say_my_name(first_name, last_name=""):
    """
         Prints "My name is <first name> <last name>"

         Args:
            fist_name (str): First name to print.
            last_name (str): Lasg name to print.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
