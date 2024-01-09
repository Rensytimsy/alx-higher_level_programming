#!/bin/usr/python3
"""The function below append a string to a file"""


def append_write(filename="", text=""):
    """The code below appends the strinr to a file"""
    with open(filename, mode="a", encoding="utf-8") as new_file:
        return new_file.write(text)
