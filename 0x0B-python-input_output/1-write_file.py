#!/usr/bin/python3
"""
    1. Write to a file
"""


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8) and
        returns the number of characters written.

        Args:
            filename (str): The file path.
            text (str): The text to write.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
