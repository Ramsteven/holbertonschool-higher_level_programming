#!/usr/bin/python3
"""module to json string"""
import json
from io import StringIO


def from_json_string(my_str):
    """ function json to string """
    io = StringIO(my_str)
    return json.load(io)
