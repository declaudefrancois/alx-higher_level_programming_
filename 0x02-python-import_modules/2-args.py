#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d} argument{:s}{:s}".format(len(argv) - 1,
          "" if len(argv) == 2 else "s",
          "." if len(argv) == 1 else ":"))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
