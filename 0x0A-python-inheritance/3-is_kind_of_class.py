#!/usr/bin/python3
"""The function below checks if object is equal to a_class value"""
def is_kind_of_class(obj, a_class):
    """If the ob is equal to a _class value we return True else False"""
    if isinstance(obj, a_class):
        return True
    return False
