#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = abs(number) % 10

    print("{:d}".format(lastDigit), end="")
    return lastDigit
