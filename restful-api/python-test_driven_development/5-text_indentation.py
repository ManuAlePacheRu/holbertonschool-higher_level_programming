#!/usr/bin/python3
"""
This is a method that applies indentation to a text when it finds [".", "?", ":"]
"""


def text_indentation(text):
    """
    Apply indentation to text based on certain characters.

    Args:
        text (str): The input text to be indented.

    Raises:
        TypeError: If `text` is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print( i, end="")
        if i == "." or i == "?" or i == ":":
            print()
            print()
