#!/usr/bin/python3
# Write a program that prints the numbers from 0 to 99.

for i in range(0, 100):
    if i < 10:
        print("0{:d}, ".format(i), end="")
    elif i == 99:
        print("{:d}".format(i))
    else:
        print("{:d}, ".format(i), end="")
