

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 1:
        if len(args) == 2:
            print("{0:d} argument:".format(len(args) - 1))
        else:
            print("{0:d} arguments:".format(len(args) - 1))
        for i in range(len(args) - 1):
            print("{0:d}: {1:s}".format(i + 1, args[i + 1]))
    else:
        print("{0:d} arguments.".format(len(args) - 1))
