#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = 0
    sign = sys.argv[2]

    if sign == "+":
        c = add(a, b)
    elif sign == "-":
        c = sub(a, b)
    elif sign == "*":
        c = mul(a, b)
    elif sign == "/":
        c = div(a, b)
    else:
        print("Unknown operator."
              " Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {:s} {:d} = {}".format(a, sign, b, c))
