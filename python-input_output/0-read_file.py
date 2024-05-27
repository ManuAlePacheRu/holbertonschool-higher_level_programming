#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
