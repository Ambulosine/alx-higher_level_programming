#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args, res = sys.argv, 0
    for i in range(len(args) - 1):
        res += int(args[i + 1])

    print("{0:d}".format(res))
