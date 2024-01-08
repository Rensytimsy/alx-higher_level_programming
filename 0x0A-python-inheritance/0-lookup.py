#!/usr/bin/python3
"""Below is a function that prints the attributes and methods present in a class"""


def lookup(obj):
    """Return a list of properties and instances present"""
    return(dir(obj))
