"""Json formatter for comparing two files."""

# !usr/bin/env/python3

import json


def format_json(diff):
    """
    Format a dictionary: json style.

    Parameters:
        diff: dictionary of compared data.

    Returns:
        formatted data in json format.
    """
    return json.dumps(diff)
