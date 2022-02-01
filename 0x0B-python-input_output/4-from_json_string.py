#!/usr/bin/python3
"""convert from JSON """
import json


def from_json_string(my_str):
    """
    Return a python object represented by a JSON string
    """
    return json.loads(my_str)
