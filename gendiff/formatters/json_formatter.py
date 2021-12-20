"""Formatter for comparing two files."""

# !usr/bin/env/python3

import json
from gendiff.formatters.engine import get_ordered_dictionary


def format_json(dictionary):
    """
    Format a dictionary: json style.

    Parameters:
        dictionary: dictionary of compared data.

    Returns:
        formatted data in json format.
    """
    sorted_dict = get_ordered_dictionary(dictionary)
    return json.dumps(sorted_dict)
