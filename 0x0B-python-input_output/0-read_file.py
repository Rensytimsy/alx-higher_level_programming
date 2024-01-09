#!/usr/bin/python3
"""Below are instructions to open a file"""


def read_file(filename=""):
    """openning a file using with"""
    with open(filename, mode="r", encoding="utf-8") as new_file:
        print(new_file.read(), end="")
