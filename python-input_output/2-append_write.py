#!/usr/bin/python3
"""
This Function append a given text to a file.
"""


def append_write(filename="", text=""):
    """
    Append text to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended to the file.

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, mode="a", encoding="utf-8") as writefile:
        return writefile.write(text)
