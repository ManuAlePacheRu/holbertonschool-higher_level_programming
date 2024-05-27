#!/usr/bin/python3
"""Convert a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: A Python object representing the JSON string.

    Raises:
        ValueError: If the input string is not valid JSON.
    """
    return json.loads(my_str)
