#!/usr/bin/python3

"""
    Method to check if a object is from a same class
"""


def is_same_class(obj, a_class):
    """
        Method Definition
    """
    if type(obj) is a_class:
        return True
    else:
        return False
