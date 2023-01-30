#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_index = 0
    while text_index < len(text) and text[text_index] == ' ':
        text_index += 1

    while text_index < len(text):
        print(text[text_index], end="")
        if text[text_index] == '\n' or text[text_index] in '.?:':
            if text[text_index] in '.?:':
                print('\n')
            text_index += 1
            while text_index < len(text) and text[text_index] == ' ':
                text_index += 1
            continue
        text_index += 1
