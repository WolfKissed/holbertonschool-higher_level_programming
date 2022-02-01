#!/usr/bin/python3
"""load object from JSON file """
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    """
    with open(filename, encoding="UTF8") as Myfile:
        return json.load(Myfile))
