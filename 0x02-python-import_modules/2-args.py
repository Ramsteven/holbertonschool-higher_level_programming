#!/usr/bin/python3

if __name__ == "__main__":
    import sys

arguments = (len(sys.argv))

if (arguments == 1):
    print("0 arguments:")
else:
    if (arguments == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arguments - 1))
    for i in range(1, arguments):
        print("{:d}: {}".format(i, sys.argv[i]))
