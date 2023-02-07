#!/usr/bin/python3
"""A module that defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file to read from

    Returns:
        The object represented by the JSON string
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
