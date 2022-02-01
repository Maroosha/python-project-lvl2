"""
Parse data.
"""

# !/usr/bin/env python3


import json
import yaml


def parse(raw_data, format_):
    """
    Parse data.

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
