#!/usr/bin/python3
"""A class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """This class raises an exception if the size is not an integer,
    if the size is less than 0, and calculates the area of the square"""

    # This is a constructor for the Square class
    def __init__(self, size=0):
        # if type of size is not an integer raise a TypeError exception
        if type(size) is not int:
            raise TypeError("size must be an integer")
            # if size is less than 0 raise a ValueError exception
        elif size < 0:
            raise ValueError("size must be >= 0")
            # otherwise set the private instance attribute size
        else:
            self.__size = size

    # This is a public instance method that returns the current square area
    def area(self):
        return self.__size * self.__size
