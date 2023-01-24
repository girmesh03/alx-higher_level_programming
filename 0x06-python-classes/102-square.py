#!/usr/bin/python3
"""A class which compare 2 squares"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """A constructor for the Square class"""
        self.__size = size

    @property
    def size(self):
        """A getter for the Square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the Square class"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A method to calculate the area of a square"""
        return self.__size * self.__size

    def __lt__(self, other):
        """A method to compare 2 squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """A method to compare 2 squares"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """A method to compare 2 squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """A method to compare 2 squares"""
        return self.area() != other.area()

    def __gt__(self, other):
        """A method to compare 2 squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """A method to compare 2 squares"""
        return self.area() >= other.area()
