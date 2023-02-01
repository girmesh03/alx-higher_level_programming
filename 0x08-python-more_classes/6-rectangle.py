#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 5-rectangle.py)"""


class Rectangle:
    """A class Rectangle that defines a rectangle by: 
    (based on 5-rectangle.py)"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height: 
        def __init__(self, width=0, height=0):"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property def width(self): to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter def width(self, value): to set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property def height(self): to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter def height(self, value): to set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method: def area(self): 
        that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method: def perimeter(self): 
        that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print() and str() should print the rectangle 
        with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n")
                * self.__height)[:-1]

    def __repr__(self):
        """repr() should return a string representation 
        of the rectangle to be able to recreate a new 
        instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message Bye rectangle... 
        (with ... being 3 dots not ellipsis) when an instance of Rectangle 
        is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
