#!/usr/bin/python3
"""A module that defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """This functions prints My name is <first name> <last name>
    and return nothing.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
