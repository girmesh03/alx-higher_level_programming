#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer with "{:d}".format()"""
    # import sys module
    import sys
    # try to print the integer
    try:
        # print the integer
        print("{:d}".format(value))
        # return True
        return True
        # get exception as e
    except Exception as e:
        # print the exception to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # return False
        return False
