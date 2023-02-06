#!/usr/bin/python3

"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified
    class; otherwise False.

    Args:
        obj (object): object to check
        a_class (class): class to check against

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    return type(obj) == a_class
