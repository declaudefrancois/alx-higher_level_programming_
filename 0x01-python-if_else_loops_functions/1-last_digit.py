#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10 * (-1 if number < 0 else 1)

print("Last digit of {:d} is {:d}".format(number, lastDigit), end=" ")
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
