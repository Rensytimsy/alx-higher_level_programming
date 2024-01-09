#!/usr/bin/python3
"""Below is a function that adds text to a file"""


def write_file(filename="", text=""):
    """The code below adds some string to a file """
    with open(filename, mode="w", encoding="utf-8") as new_file:
        return new_file.write(text)
