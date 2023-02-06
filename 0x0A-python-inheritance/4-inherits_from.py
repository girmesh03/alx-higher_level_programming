#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class;
otherwise False."""


def inherits_from(obj, a_class):
    """check if obj is an instance of a class that inherited from a_class

    Args:
        obj (object): object to check
        a_class (class): class to check against

    Returns:
        True if obj is an instance of a class that inherited from a_class;
        otherwise False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
