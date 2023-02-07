#!/usr/bin/python3
"""A module that defines a 4-from_json_string.py function"""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): The JSON string to convert to an object

    Returns:
        The object represented by the JSON string
    """
    return json.loads(my_str)
