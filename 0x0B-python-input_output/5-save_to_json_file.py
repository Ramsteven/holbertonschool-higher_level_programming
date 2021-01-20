#!/usr/bin/python3
"""module to object to text"""
import json


def save_to_json_file(my_obj, filename):
    """ function object to string """
    with open(filename, mode='w', encoding="utf-8") as file_name:
        file_new = json.dumps(my_obj)
        file_name.write(file_new)
