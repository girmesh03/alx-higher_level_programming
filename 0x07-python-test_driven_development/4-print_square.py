#!/usr/bin/python3
"""Defines a print_square function."""


def print_square(size):
    """A function that prints a square of '#' based on the given size.
    Args:
        size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer,
        TypeError: If size is a float and is less than 0,
        ValueError: If size is less than 0.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if size == 0:
        return

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
