#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    # Initialize a new list
    new_list = []
    # Loop through the list
    for i in range(list_length):
        # Try to divide the values
        try:
            # Divide the values
            new_list.append(my_list_1[i] / my_list_2[i])
            # If TypeError, return 0
        except TypeError:
            # print "wrong type"
            print("wrong type")
            # return 0
            new_list.append(0)
            # If ZeroDivisionError, return 0
        except ZeroDivisionError:
            # print "division by 0"
            print("division by 0")
            # return 0
            new_list.append(0)
            # If IndexError, return 0
        except IndexError:
            # print "out of range"
            print("out of range")
            # return 0
            new_list.append(0)
            # If any other exception, return 0
        finally:
            # continue to the next iteration
            continue
    # return the new list
    return new_list
