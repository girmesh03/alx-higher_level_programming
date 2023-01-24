#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    # Initialize a new list and index
    new_list = []
    index = 0
    # Loop through the list
    while index < list_length:
        # Try to divide the values
        try:
            # Divide the values and append to new list
            new_list.append(my_list_1[index] / my_list_2[index])
            # If TypeError, do the following
        except TypeError:
            # print "wrong type"
            print("wrong type")
            # append 0 to the new list
            new_list.append(0)
            # If ZeroDivisionError, do the following
        except ZeroDivisionError:
            # print "division by 0"
            print("division by 0")
            # append 0 to the new list
            new_list.append(0)
            # If IndexError, do the following
        except IndexError:
            # print "out of range"
            print("out of range")
            # append 0 to the new list
            new_list.append(0)
            # whatever happens, do the following
        finally:
            # increment the index
            index += 1
    # return the new list
    return new_list
