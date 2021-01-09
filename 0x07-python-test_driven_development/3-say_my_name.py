#!/usr/bin/python3
"""
 This is the module for
    say_my_name

"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name
    """
    first = isinstance(first_name, str)
    last = isinstance(last_name, str)
    if first is False or last is False:
        raise TypeError("{} must be a string".format
                        ("first_name"if first is False else "last_name"))
    print("My name is {} {}".format(first_name, last_name))
