#!/usr/bin/python3
"""
This is the module for
    add_integer

"""


def print_square(size):
    """
    function that divides all elements of a matrix
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
