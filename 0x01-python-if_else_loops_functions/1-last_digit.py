#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(str(number)[-1])
print("Last digit of {:d} is {:d}".format(number, lastDigit), end = " ")
print(f"and is greater than 5" if lastDigit > 5 else
       "and is less than 6 and not 0" if lastDigit < 6 and lastDigit != 0 else
       "and is 0")
