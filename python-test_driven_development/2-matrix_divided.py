#!/usr/bin/python3
def matrix_divided(matrix, div):
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
            if not len(row) == len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
         raise TypeError("div must be a number")
    if div == 0:
         raise ZeroDivisionError("division by zero")
    
    # result = list(map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
    # return result

    primera_lista = []

    for row in matrix:
        segunda_lista = []
        for elem in row:
            segunda_lista.append(round(elem / div, 2))
        primera_lista.append(segunda_lista)

    return primera_lista
