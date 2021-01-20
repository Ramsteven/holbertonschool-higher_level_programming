#!/usr/bin/python3
"""function write file """


def write_file(filename="", text=""):
    """ function that write a file close stream object automatically"""
    with open(filename, mode='w', encoding="utf-8") as file_name:
        file_name.write(text)
    return len(text)
