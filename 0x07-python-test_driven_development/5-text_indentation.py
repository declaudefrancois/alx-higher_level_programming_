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
    chars = ['.', '?', ':']
    for i in range(len(text)):
        if text[i] in chars:
            print(text[i], end="\n\n")
        else:
            if not (i > 0 and text[i - 1] in chars and
                    text[i] == ' '):
                print(text[i], end="", sep='')
