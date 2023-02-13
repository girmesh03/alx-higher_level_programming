#!/usr/bin/python3
"""A Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.width = size
        self.height = size

    def __str__(self):
        """Return a string representation of a rectangle instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the attributes of a Square instance."""
        if args is not None and len(args) != 0:
            list_attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list_attributes[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of a Square instance."""
        list_attributes = ["id", "size", "x", "y"]
        to_dict = {}

        for attribute in list_attributes:
            if attribute == "size":
                to_dict[attribute] = getattr(self, "width")
            else:
                to_dict[attribute] = getattr(self, attribute)

        return to_dict
