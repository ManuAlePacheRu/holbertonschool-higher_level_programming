#!/usr/bin/python3
"""
This is a function that write text to a file.
"""


def write_file(filename="", text=""):
    """
    Write text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, mode="w", encoding="utf-8") as writefile:
        return writefile.write(text)
