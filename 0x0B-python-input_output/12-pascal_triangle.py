#!/usr/bin/python3
"""A module that defines a pascal's triangle function"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing the
    Pascal's triangle of n

    Args:
        n (int): The number of rows of the triangle

    Returns:
        A list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
