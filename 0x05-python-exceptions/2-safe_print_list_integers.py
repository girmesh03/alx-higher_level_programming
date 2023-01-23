#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    # Initialize a counter
    counter = 0
    # Loop through the list
    for i in range(x):
        # Try to print the value
        try:
            # print the value if it is an integer
            print("{:d}".format(my_list[i]), end="")
            # Increment the counter
            counter += 1
            # If ValueError or TypeError, return False
        except (ValueError, TypeError):
            # return False
            continue
    # print a new line
    print()
    # return the counter
    return counter
