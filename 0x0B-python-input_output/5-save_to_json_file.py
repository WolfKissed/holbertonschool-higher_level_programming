#!/usr/bin/python3
"""save text to json file """
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file using JSON representation
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
