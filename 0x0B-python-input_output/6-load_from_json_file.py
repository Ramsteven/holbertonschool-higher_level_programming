#!/usr/bin/python
""" module load from json"""


def load_from_json_file(filename):
    """ method load from jsonfile"""
    import json
    with open(filename, encoding="utf-8") as file_name:
        return json.load(file_name)
