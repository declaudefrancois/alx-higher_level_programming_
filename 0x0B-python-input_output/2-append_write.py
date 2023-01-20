#!/usr/bin/python3
"""
    2. Append to a file.
"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file (UTF8)
        and returns the number of characters added.

        Args:
            filename (str): The file's path.
            text (str): The text to append.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
