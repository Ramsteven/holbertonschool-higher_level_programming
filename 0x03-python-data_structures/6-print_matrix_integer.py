#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        space = ""
        for number in x:
            print("{:s}{:d}".format(space, number), end="")
            space = " "
        print()
