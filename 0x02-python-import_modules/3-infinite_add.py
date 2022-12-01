#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    def add_recursive(a, i):
        """Recursively adds numbers in the list a.

        Args:
            a: a list of integers.
            i: the index of the first item to sum.

        Returns:
            sum of all items of a.
        """
        if i >= len(a):
            return (0)

        return (int(a[i]) if i == len(argv) else
                int(a[i]) + add_recursive(a, i + 1))

    print("{:d}".format(add_recursive(argv, 1)))
