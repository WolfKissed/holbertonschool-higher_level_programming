#!/usr/bin/python3
"""
append
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
