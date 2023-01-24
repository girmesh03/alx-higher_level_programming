#!/usr/bin/python3
"""defines a square by: (based on 1-square.py)."""


class Square:
    """This is a constructor for the Square class
    which initializes the size instance attribute and
    raises an exception if the size is not an integer
    or if the size is less than 0"""

    # def __init__(self, size=0):
    #     self.__size = size
    #     if type(self.__size) is not int:
    #         raise TypeError("size must be an integer")
    #     elif self.__size < 0:
    #         raise ValueError("size must be >= 0")

    # def __init__(self, size=0):
    #     self.__size = size
    #     if type(size) is not int:
    #         raise TypeError("size must be an integer")
    #     if size < 0:
    #         raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
