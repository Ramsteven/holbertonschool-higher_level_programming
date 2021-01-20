#!/usr/bin/python3
"""function read file """


def read_file(filename=""):
    """ function that read a file close stream object automatically"""
    with open(filename, encoding="utf-8") as file_name:
        content = file_name.read()
        print(content, end="")
