#!/usr/bin/python3

"""
squareeeee
"""


class Square:
    """
    Clase que define un cuadrado.

    Atributos privados de instancia:
        __size: tamaño del cuadrado

    Métodos:
        __init__(self, size): Constructor.
        area(self): Calcula el área del cuadrado.
    """

    def __init__(self, size=0):
        """
        Constructor de la clase Square.

        Parámetros:
            size (int): Tamaño del cuadrado.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Obtiene el tamaño del cuadrado.

        Retorna:
            int: Tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Establece el tamaño del cuadrado.

        Parámetros:
            value (int): Nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula el área del cuadrado.

        Retorna:
            int: Área del cuadrado.
        """
        area = self.__size * self.__size
        return area
