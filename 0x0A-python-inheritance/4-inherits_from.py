#!/usr/bin/python3
"""The function checks if the obj is a subclass and if it can return a bool"""


def inherits_from(obj, a_class):
    """Below is the conditional rendering"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
