#!/usr/bin/python3
"""
read
"""


def read_file(filename=""):
    """
    reading a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
