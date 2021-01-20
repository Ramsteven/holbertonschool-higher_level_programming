#!/usr/bin/python
""" module load from json"""
import json


def load_from_json_file(filename):
    """ method load from """
    with open(filename, mode="r", encoding="utf-8") as file_name:
        return json.load(file_name)
