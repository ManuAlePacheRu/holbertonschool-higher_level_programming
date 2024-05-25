#!/usr/bin/python3    # This line is called a shebang. It tells the system this script should be run with Python3.
"""
Rectangle  class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        def width(self, value):
            """
            Set the width of the rectangle.

            Args:
                value (int): The width value to set.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
            """

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        def height(self, value):
            """
            Set the height of the rectangle.

            Args:
                value (int): The height value to set.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
            """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
