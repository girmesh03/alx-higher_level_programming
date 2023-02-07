#!/usr/bin/python3
"""A module that contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file

    Args:
        filename (str): The name of the file to write to
        text (str): The string to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
