#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d} arguments{:s}".format(len(argv) - 1,
          "." if len(argv) == 1 else ":"))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
