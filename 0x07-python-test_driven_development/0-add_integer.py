#!/usr/bin/python3
"""
This is the module for
    add_integer
"""


def add_integer(a, b=98):
    """
        add_integer' that add two number
    """
    handle_a = isinstance(a, (int, float))
    handle_b = isinstance(b, (int, float))
    if handle_a is False or handle_b is False:
        raise TypeError("{} must be an integer"
                        .format("a" if handle_a is False else "b"))
    else:
        return int(a) + int(b)
