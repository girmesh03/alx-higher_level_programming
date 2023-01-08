#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass

    for value in reversed(my_list):
        print("{}".format(value))
