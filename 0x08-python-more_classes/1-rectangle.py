#!/usr/bin/ptyhon3
"""Module 1-rectangle - Defines Rectangle class"""


class Rectangle:
    """A class Rectangle that defines a rectangle
    by: (based on 0-rectangle.py)

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle

    Raises:
        TypeError: if width or height are not integers
        ValueError: if width or height are less than 0
    """

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
