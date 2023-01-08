#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0

    if my_list == list():
        return None

    for index in range(len(my_list)):
        if my_list[index] > biggest:
            biggest = my_list[index]
    return biggest
