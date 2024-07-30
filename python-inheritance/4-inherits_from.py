#!/usr/bin/python3

"""
    Check if inherits from a class
"""


def inherits_from(obj, a_class):
    """
        Returns if is a instance and if is not a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
