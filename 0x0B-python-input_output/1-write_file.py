#!/usr/bin/python3
"""
write
"""


def write_file(filename="", text=""):
    """
    write a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
