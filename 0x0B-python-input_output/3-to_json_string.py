#!/usr/bin/python3
"""A module that contains a function that returns the JSON
representation of an object (string)"""

import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string)

    Args:
        my_obj (object): The object to convert to JSON

    Returns:
        The JSON representation of the object
    """
    return json.dumps(my_obj)
