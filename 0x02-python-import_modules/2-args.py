#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)

    if num_args == 1:
        print("{} arguments.".format(num_args - 1))
    else:
        print("{} arguments:".format(num_args - 1))
        for index in range(1, num_args):
            print("{} {}:".format(index, sys.argv[index]))
