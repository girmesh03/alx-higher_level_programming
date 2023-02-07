#!/usr/bin/python3
"""A module that contains a function that
appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file

    Args:
        filename (str): The name of the file to append to
        text (str): The string to append to the file

    Returns:
        The number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
