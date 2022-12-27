#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="\n" if i == x - 1 else "",
                  sep="")
            count += 1

        if x == 0:
            print("")
        return (count)
    except IndexError:
        print("")
        return (count)
