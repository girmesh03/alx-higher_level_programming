#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
            matrix (list): A list of lists of integers or floats.
            div (int or float): The number to divide the matrix by.
    Raises:
            TypeError: If the matrix is not a list of lists of integers \
                or floats.
            TypeError: If the matrix contains a row of different size.
            TypeError: If div is not an integer or float.
            ZeroDivisionError: If div is 0.
    Returns:
            A new matrix where each element is divided by div.
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float))
                for element in [item for row in matrix for item in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix \
                        (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
