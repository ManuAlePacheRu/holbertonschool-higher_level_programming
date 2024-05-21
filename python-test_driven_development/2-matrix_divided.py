#!/usr/bin/python3
"""
This module divide a list elements for certain number.
"""


def matrix_divided(matrix, div):
    """
    The module take a matrix and divide it for the given number give in
    the 'div' variable.
    """
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
            """
            If 'elem' is not int or float raise a type error.
            """
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        """
        If every row is not of the same size rise a type error.
        """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """
    If div is not int or float raise an error.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """
    If div is 0 raise a ZeroDivisionError.
    """
    primera_lista = []
    for row in matrix:
        segunda_lista = []
        for elem in row:
            segunda_lista.append(round(elem / div, 2))
        primera_lista.append(segunda_lista)
    """
    This part of the code make the division and round the numbers,
    after that it add it to the list and add the second list to the first one
    to complete the matrix.
    """
    return primera_lista
