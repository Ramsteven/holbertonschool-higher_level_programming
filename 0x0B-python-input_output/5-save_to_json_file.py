#!/usr/bin/python3
"""module to object to text"""
import json


def save_to_json_file(my_obj, filename):
    """ function object to string """
    file_new = json.dumps(my_obj)

    with open(filename, mode='w', encoding="utf-8") as file_name:
        file_name.write(file_new)
