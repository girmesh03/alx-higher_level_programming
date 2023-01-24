#!/usr/bin/python3
"""A class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """This class raises an exception if the size is not an integer,
        if the size is less than 0, calculates the area of the square,
        setter, getter, and print method"""

    # This is a constructor for the Square class
    def __init__(self, size=0):
        # initialize the private instance attribute size
        self.__size = size

    # getter method for size
    @property
    def size(self):
        return self.__size

    # setter method for size
    @size.setter
    def size(self, value):
        # if type of size is not an integer raise a TypeError exception
        if type(value) is not int:
            raise TypeError("size must be an integer")
            # if size is less than 0 raise a ValueError exception
        elif value < 0:
            raise ValueError("size must be >= 0")
            # otherwise set the private instance attribute size
        else:
            self.__size = value

    # This is a public instance method that returns the current square area
    def area(self):
        return self.__size * self.__size

    # This is a public instance method that prints the "#" character
    # if the size is not 0, otherwise print an empty line
    def my_print(self):
        # if size is 0 print an empty line
        if self.__size == 0:
            print()
        else:  # otherwise print the "#" character
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
