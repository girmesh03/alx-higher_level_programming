#!/usr/bin/python3

# Write a program that prints all possible different combinations of two digits.

for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", ")
print("{:d}{:d}".format(i, j))
