#!/usr/bin/python
import json
""" module load from json"""


def load_from_json_file(filename):
    """ method load from jsonfile"""
    with open(filename, encoding="utf-8") as file_name:
        return json.loads(file_name)
