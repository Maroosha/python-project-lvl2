"""
Read a file.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3

from pathlib import Path


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
    Get file format.

    Parameters:
        filepath: path to the file.

    Returns:
        file format as an uppercase string.
    """
    return Path(filepath).suffix.strip('.').upper()
