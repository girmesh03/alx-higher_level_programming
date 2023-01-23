#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    # Try to print the value
    try:
        # print the value if it is an integer
        print("{:d}".format(value))
        # return True if successful
        return True
        # If ValueError or TypeError, return False
    except (ValueError, TypeError):
        # return False
        return False
