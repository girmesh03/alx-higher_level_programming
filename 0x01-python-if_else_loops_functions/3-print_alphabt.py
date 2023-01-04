#!/usr/bin/python3

# write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.
# except for 'q' and 'e'

for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end="")
