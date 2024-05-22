#!/usr/bin/python3
"""
This is a method that aplies a tab to a text when it find [".", "?", ":"]
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print()
            print()
    else:
        print(i, end="")
