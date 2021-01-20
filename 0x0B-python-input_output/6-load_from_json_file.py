#!/usr/bin/python
""" module load_from_json_file"""


def load_from_json_file(filename):
    """ 
    method load_from_json_file
    """
    content = ""
    import json
    with open(filename, 'r', encoding="UTF-8") as file_name:
        content = file_name.read()

    return json.loads(content)
