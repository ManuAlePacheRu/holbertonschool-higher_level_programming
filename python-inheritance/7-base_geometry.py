#!/usr/bin/python3

"""
    A class called BaseGeometry with an area method
"""


class BaseGeometry:
    """
        Class with an area method
    """

    def area(self):
        """
            Exeption raised
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Check if value is a num and if it is greater than cero
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
