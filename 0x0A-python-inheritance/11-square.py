#!/usr/bin/python3

"""Defines a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the informal string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
