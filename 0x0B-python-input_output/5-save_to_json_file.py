#!/usr/bin/python3
"""A module that defines a save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (object): The object to write to the file
        filename (str): The name of the file to write to
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
