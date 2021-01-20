#!/usr/bin/python
""" module load_from_json_file"""


def load_from_json_file(filename):
    """ 
    method load_from_json_file
    """
    import json
    with open(filename, encoding="UTF-8") as file_name:
        return json.load(file_name)
