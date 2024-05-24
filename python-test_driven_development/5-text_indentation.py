#!/usr/bin/python3
"""
This is a method that applies indentation to a text when it finds [".", "?", ":"]
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print( i, end="")
        if i == "." or i == "?" or i == ":":
            print()
            print()
  