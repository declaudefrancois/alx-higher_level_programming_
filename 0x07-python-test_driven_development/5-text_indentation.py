#!/usr/bin/python3
"""
    text_indentation function module.
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after
        each of these characters: ., ? and :

        Args:
            text (str): The text to indent.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="\n\n")
        else:
            print(text[i], end="")
