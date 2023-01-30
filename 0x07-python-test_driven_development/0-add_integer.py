#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """ adds 2 integers
        Args:
            a (int): first integer
            b (int): second integer.
        Returns:
            int: sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return int(a) + int(b)
