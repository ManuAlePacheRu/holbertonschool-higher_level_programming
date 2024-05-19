#!/usr/bin/python3

"""
This module defines a class Square.

Attributes:
    __size (int): The size of the square (private attribute).
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
        """

        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is less than 0
        elif size < 0:
            raise ValueError("size must be >= 0")

        # If size is an integer and it's not less than 0, assign it to __size
        else:
            self.__size = size
