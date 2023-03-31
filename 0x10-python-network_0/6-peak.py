#!/usr/bin/python3
"""Peak finder module.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    sorted_list = sorted(list_of_integers)
    return sorted_list[-1] if len(sorted_list) > 0 else None
