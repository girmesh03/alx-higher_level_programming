#!/usr/bin/python3

"""
Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is <= 0.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is <= 0.
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the x coordinate of the rectangle.

        Args:
            x (int): The x coordinate of the rectangle.

        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is < 0.
        """

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the y coordinate of the rectangle.

        Args:
            y (int): The y coordinate of the rectangle.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is < 0.
        """

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the # character to stdout."""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        list_attributes = ["id", "width", "height", "x", "y"]
        to_dict = {}
        for attr in list_attributes:
            to_dict[attr] = getattr(self, attr)

        return to_dict
