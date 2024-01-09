#!/usr/bin/python3
"""The function returns string to json object"""
import json


def from_json_string(my_str):
    """To return string to object we use the json.loads() method """
    return json.loads(my_str)
