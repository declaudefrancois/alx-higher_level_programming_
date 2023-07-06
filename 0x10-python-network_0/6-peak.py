#!/usr/bin/python3
"""Find a peak in a list of integers.
"""


def find_peak(list_int):
    """Find a peak in list_int.

       Params:
            list_int(list): A list of integers.
    """
    limit = 1 + len(list_int) / 2
    i = 0
    peak = None
    while i < limit and limit > 1:
        low = list_int[i]
        high = list_int[-i - 1]
        if peak is None:
            peak = low if low >= high else high
        else:
            if low >= high and low > peak:
                peak = low
            elif high >= low and high > peak:
                peak = high
        i += 1
    return peak
