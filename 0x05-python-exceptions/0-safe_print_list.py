#!/usr/bin/ptyhon3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="\n" if i == x - 1 else ""
                  ,sep="")
        return (x)
    except IndexError as err:
        print("\n{}".format(err))
        raise

