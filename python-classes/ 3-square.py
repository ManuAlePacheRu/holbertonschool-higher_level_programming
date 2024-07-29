"""
square class
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

    def area(self):
        """
        Calcula el área del cuadrado.

        Retorna:
            int: Área del cuadrado.
        """
        area = self.__size * self.__size
        return area
