#!/usr/bin/python3
"""A module that defines a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str): The name of the file
        search_string (str): The string to search for
        new_string (str): The string to insert after each line containing
        search_string
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + "\n")
