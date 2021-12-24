"""
Parse a file.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3


import json
import yaml


def get_raw_data(filepath):
    """
    Get raw data from a file.

    Parameters:
        filepath: path to file.

    Returns:
        raw data.
    """
    with open(filepath) as file:
        return file.read()


def parse_file(filepath, file_data):
    """
    Parse a file.

    Parameters:
        filepath: path to the file.
        file_data: raw data from the file.

    Returns:
        data as a dictionary if file format is correct;
        Exception if file format is invalid.
    """
    if filepath[-5:].upper() == '.JSON':
        return json.loads(file_data)
    if filepath[-4:].upper() == '.YML' or filepath[-5:].upper() == '.YAML':
        return yaml.safe_load(file_data)
    raise Exception('Invalid file format.')
