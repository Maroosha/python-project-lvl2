"""
Parse a file.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3


import json
import yaml
from yaml.loader import SafeLoader


def parse_file(filepath):
    """
    Parse a file.

    Parameters:
        filepath: file path.

    Returns:
        data as a dictionary if file format is correct;
        Exception if file format is invalid.
    """
    if filepath[-5:].upper() == '.JSON':
        return json.load(open(filepath))
    if filepath[-4:].upper() == '.YML' or filepath[-5:].upper() == '.YAML':
        with open(filepath) as file_:
            return yaml.load(file_, Loader=SafeLoader)
    raise Exception('Invalid file format.')
