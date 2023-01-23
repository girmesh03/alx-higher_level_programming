#!/usr/bin/python3
def safe_function(fct, *args):
    """executes a function safely"""
    # try to execute the function
    try:
        # return the result of the function
        return fct(*args)
        # get exception as e
    except Exception as e:
        # import sys module
        import sys
        # print the exception to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # return None
        return None
