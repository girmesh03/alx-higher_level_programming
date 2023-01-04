#!/usr/bin/python3

# Write a program that prints all numbers
# from 0 to 98 in decimal and in hexadecimal

for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i))
