#!/usr/bin/python3
"""__init__
start method
Atributtes:
__size (int): The size of square (private attribute).
"""


class Square:  # Define the class Square
    def __init__(self, size=0):  # Initialization method with a parameter
        """
        Args:
        __size (int): The size of square (private attribute)
        """
        if not isinstance(size, int):  # Check if size is an integer
            raise TypeError("size must be an integer")  # If not an integer.
        elif size < 0:  # If size is an integer, less than 0.
            raise ValueError("size must be >= 0")  # If it's less than 0.
        else:
            self.__size = size  # If size is an integer.
