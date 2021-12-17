"""Formatter for comparing two files."""

# !usr/bin/env/python3

import json
from gendiff.formatters.engine import get_ordered_dictionary


def format_stylish(dictionary):
    """
    Format a dictionary into preferred output.

    Parameters:
        dictionary: dictionary of compared data.

    Returns:
        formatted data as a string.
    """
    sorted_dict = get_ordered_dictionary(dictionary)
    json_dict = json.dumps(sorted_dict, indent=4, separators=('', ': '))
    answer = [i for i in json_dict if i != '"']
    for index, value in enumerate(answer):
        if value == '}':
            answer[index] = '  }'
    answer[-1] = '}'
    return ''.join(answer)
