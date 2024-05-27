#!/usr/bin/python3
"""Write an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a JSON file.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None

    Raises:
        IOError: If the file cannot be opened or written to.
    """
    with open(filename, 'w', encoding="utf-8") as filewrite:
        json.dump(my_obj, filewrite)
