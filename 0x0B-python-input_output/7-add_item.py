#!/usr/bin/python3
"""
adds argv to a list
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    x = load_from_json_file(filename)
except FileNotFoundError:
    x = []

save_to_json_file(x + argv[1:], filename)
