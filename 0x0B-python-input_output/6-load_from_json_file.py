#!/usr/bin/python3
"""Ths function below should create an object to a file"""
import json


def load_from_json_file(filename):
    """The function below should add the object to a file"""
    with open(filename) as file_to_add:
        return json.load(file_to_add)
