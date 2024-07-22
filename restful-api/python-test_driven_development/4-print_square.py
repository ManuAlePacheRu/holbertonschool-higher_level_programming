#!/usr/bin/python3
""" This module prints a square made of # """


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
