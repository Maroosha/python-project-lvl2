"""
Read a file.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3


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


def get_format(filepath):
    """
    Get file format (JSON or YAML).

    Parameters:
        filepath: path to the file.

    Returns:
        file format as a string.
    """
    return 'JSON' if filepath[-5:].upper() == '.JSON' else 'YAML'
