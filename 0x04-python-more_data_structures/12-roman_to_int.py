#!/usr/bin/python3
_roman_to_int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500
}


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    num = 0
    _str = list(reversed(roman_string))
    for idx, k in enumerate(_str):
        if k in _roman_to_int:
            if idx > 0:
                if _roman_to_int[_str[idx - 1]] > _roman_to_int[k]:
                    num -= _roman_to_int[k]
                else:
                    num += _roman_to_int[k]
            else:
                num += _roman_to_int[k]

    return (num)
