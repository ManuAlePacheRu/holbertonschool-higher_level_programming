#!/usr/bin/python3

"""Convert CSV file to JSON format"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file to JSON format.

    Args:
        filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if conversion is successful, otherwise False.
    """
    with open(filename, 'a+', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_json = json.dumps(list(csv_reader), indent=4)

    with open('data.json', 'w') as json_file:
        json_file.write(data_json)

    return True