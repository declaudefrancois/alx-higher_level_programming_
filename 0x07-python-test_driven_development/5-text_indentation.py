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
    str_r = text
    for c in ['.', '?', ':']:
        items = str_r.split(c)
        strs = []
        for i in range(len(items)):
            if i == len(items) - 1:
                strs.append(items[i].strip())
            else:
                strs.append("{}{}".format(items[i].strip(), c))
        str_r = "\n\n".join(strs)

    print(str_r, end="")
