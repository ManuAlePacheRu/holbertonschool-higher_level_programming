#!/usr/bin/python3
"""
This module make an addition
"""


def add_integer(a, b=98):
    """
    This function adds two numbers, `a` and `b`.
    `b` is optional and defaults to 98 if not provided.
    Both `a` and `b` should be integers or floats.
    If they are floats, they are converted to integers.
    If they are not integers or floats, a TypeError is raised.
    """
    if type(a) is float:
        a = int(a)
    """
    If 'a' is a float, convert it to an integer
    """
    if type(b) is float:
        b = int(b)
    """
    If 'b' is a float, convert it to an integer
    """
    if type(a) is not int:
        raise TypeError("a must be an integer")
    """
    If 'b' is not an integer after the conversion, raise a TypeError
    """
    if type(b) is not int:
        raise TypeError("b must be an integer")
    """
    If 'b' is not an integer after the conversion, raise a TypeError
    """
    return a + b
    """
    Return the sum of a + b
    """
