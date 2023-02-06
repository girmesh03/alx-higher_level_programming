#!/usr/bin/python3

"""Defines a function that adds a new attribute
to an object if it’s possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it’s possible.

    Args:
        obj (object): object to add attribute to
        name (str): name of attribute
        value (object): value of attribute

    Raises:
        TypeError: if the object can’t have new attribute added
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
