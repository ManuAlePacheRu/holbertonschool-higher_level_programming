#!/usr/bin/python3

"""
    A class called BaseGeometry with an area method
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def __init__(self, width, height):
        """
            Check withd and heigth
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
