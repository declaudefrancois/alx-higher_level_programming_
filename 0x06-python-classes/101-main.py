#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

my_square = Square(4, (4, 0))
print(my_square)

my_square = Square(4, (4, 4))
print(my_square)

my_square = Square(0, (10, 10))
print(my_square)
