#!/usr/bin/python3

# write a program that prints the ASCII alphabet,
# in lowercase, except for 'q' and 'e' not followed by a new line.

for character in range(97, 123):
    if chr(character) != 'q' and chr(character) != 'e':
        print("{}".format(chr(character)), end="")
