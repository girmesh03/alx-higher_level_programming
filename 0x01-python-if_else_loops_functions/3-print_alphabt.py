#!/usr/bin/python3

# write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.
# except for 'q' and 'e'

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
