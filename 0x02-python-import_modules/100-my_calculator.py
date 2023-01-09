#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    if len(args) != 4:
        print("Usage: {0:s} <a> <operator> <b>".format(args[0]))
        exit(1)
    if args[2] != "+" and args[2] != "-" and args[2] != "*" and args[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a, b = int(args[1]), int(args[3])
    if args[2] == "+":
        print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    elif args[2] == "-":
        print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
    elif args[2] == "*":
        print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
    else:
        print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
