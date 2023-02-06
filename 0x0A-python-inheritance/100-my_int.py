#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Represent a MyInt object."""

    def __eq__(self, other):
        """Return True if self is not equal to other."""
        return self.real != other

    def __ne__(self, other):
        """Return True if self is equal to other."""
        return self.real == other
