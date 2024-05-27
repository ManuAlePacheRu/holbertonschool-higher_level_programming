#!/usr/bin/python3
"""Function that read and print file content"""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, 'r', encoding="utf-8") as fileread:
        print(fileread.read(), end='')
