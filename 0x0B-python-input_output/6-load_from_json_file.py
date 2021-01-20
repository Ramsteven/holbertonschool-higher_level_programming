#!/usr/bin/python
import json
""" module load from json"""


def load_from_json_file(filename):
    """ method load from """
    with open(filename, mode="r", encoding="utf-8") as file_name:
        content = file_name.read()
        return (json.loads(content))
