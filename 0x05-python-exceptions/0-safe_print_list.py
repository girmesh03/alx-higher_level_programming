#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    # counter for number of elements to return
    counter = 0

    # loop through the list
    for index in range(x):
        # try printing elements
        try:
            # print elements on the same line
            print(my_list[index], end="")
            # update counter
            counter += 1
        # except break
        except IndexError:
            break
    # print a newline
    print()
    # return number of elements to print
    return counter
