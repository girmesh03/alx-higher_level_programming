#!/usr/bin/python3
"""A module that contains a function that returns the dictionary
description with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """A function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): The object to get the dictionary description
        for JSON serialization.

    Returns:
        The dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
    """
    return obj.__dict__
