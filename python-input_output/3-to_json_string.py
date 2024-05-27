#!/usr/bin/python3
import json
"""
Convert a Python object to a JSON string.
"""


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON representation of the input Python object.

    Raises:
        TypeError: If the input object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
