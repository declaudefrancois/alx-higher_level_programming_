#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{:c}".format(ord(str[i]) - (ord('a') - ord('A'))
              if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')
              else ord(str[i])), end="")
    print("\n", end="")
