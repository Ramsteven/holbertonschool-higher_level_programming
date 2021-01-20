#!/usr/bin/python3
""" module append write"""


def append_write(filename="", text=""):
    """ function apend write """
    with open(filename, mode="a", encoding="utf-8") as file_name:
        file_name.write(text)
    return len(text)
