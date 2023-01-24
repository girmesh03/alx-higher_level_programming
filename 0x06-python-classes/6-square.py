#!/usr/bin/python3
"""A class Square that defines a square by: (based on 5-square.py)"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        # initialize the private instance attribute size
        self.__size = size
        # initialize the private instance attribute position
        self.__position = position

    # getter method for size
    @property
    def size(self):
        return self.__size

    # setter method for size
    @property
    def position(self):
        return self.__position

    # setter method for size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # setter method for position
    @position.setter
    def position(self, value):
        # if value not satisfied the following conditions
        # raise a TypeError exception
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        # otherwise set the private instance attribute position
        self.__position = value

    # This is a public instance method that returns the current square area
    def area(self):
        return self.__size * self.__size

    # This is a public instance method that prints the square
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
