#!/usr/bin/python3
"""json object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    my_obj has a json file
    which should first be converted to a string
    and then write it to a file
    filename is the file to write our object in string form
    """
    with open(filename, mode="w", encoding="utf-8") as new_file:
        file_to_add = json.dumps(my_obj)
        return new_file.write(file_to_add)
