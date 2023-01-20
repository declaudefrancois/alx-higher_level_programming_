#!/usr/bin/python3
"""
    read file module.
"""


def read_file(filename=""):
    """
        Reads a text file (UTF8) and prints it to stdout.

        Args:
            filename (str): the file path.
    """
    with open(filename, encoding="utf-8") as f_obj:
        for line in f_obj:
            print(line, end="")
