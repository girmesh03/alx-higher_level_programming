#!/usr/bin/ptyhon3

"""Module 1-rectangle - Defines Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Raises:
            TypeError: if width or height are not integers
            ValueError: if width or height are less than 0
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
