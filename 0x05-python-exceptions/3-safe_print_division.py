#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""
    # Try to divide a and b
    try:
        # Divide a and b
        result = a / b
        # If ZeroDivisionError, return None
    except ZeroDivisionError:
        # return None
        result = None
    # Print the result
    finally:
        print("Inside result: {}".format(result))
        # return the result
        return result
