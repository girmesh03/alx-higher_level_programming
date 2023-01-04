#!/usr/bin/python3

# write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.
# except for 'q' and 'e'

for character in range(97, 123):
    if chr(character) != 'q' and chr(character) != 'e':
        print("{}".format(chr(character)), end="")
