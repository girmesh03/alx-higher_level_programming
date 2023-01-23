#!/usr/bin/python3
def magic_calculation(a, b):
    """performs a magic calculation"""
    # variable to store the result
    result = 0
    # loop through the range of a and b
    for i in range(1, 3):
        # try to add a and b
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        # if the addition fails, print "Too far" and break
        except:
            # result is sum of b and a
            result = b + a
            # break out of the loop
            break
    # return the result
    return result
