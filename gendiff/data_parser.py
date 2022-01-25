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


def parse(raw_data, format_):
    """
    Parse a file.

    Parameters:
        file_data: raw data from the file,
        format_: file format.

    Returns:
        data as a dictionary if file format is correct;
        Exception if file format is invalid.
    """
    if format_ == 'JSON':
        return json.loads(raw_data)
    if format_ == 'YAML':
        return yaml.safe_load(raw_data)
    raise Exception('Invalid file format.')
