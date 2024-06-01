#!/usr/bin/env python3

from json import dump, load


"""A basic serialization module."""


def serialize_and_save_to_file(data, filename):
    """Serialize data and save to a file."""
    with open(filename, 'w', encoding="UTF-8") as newfile1:
        dump(data, newfile1)


def load_and_deserialize(filename):
    """Load and deserialize data from a file."""
    with open(filename, 'r', encoding="utf-8") as newfile2:
        return load(newfile2)
