#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv)
    add = 0

    for i in range(1, size):
        add += int(sys.argv[i])

    print("{:d}".format(add))
