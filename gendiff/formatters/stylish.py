"""Formatter for comparing two files."""

# !usr/bin/env/python3

import json
from collections import OrderedDict


def sort_keys(keys):
    """
    Sort keys of a dictionary by sign and in alphabetical order.

    Parameters:
        keys: collection to be sorted.

    Returns:
        list of sorted keys.
    """
    sorted_keys = sorted(keys)
    for index, value in enumerate(sorted_keys):
        if not value[0].startswith('- ') and not value[0].startswith('+ '):
            sorted_keys[index] = ('  ' + value[0], value[1])
    sorted_keys.sort(key=lambda x: x[0], reverse=True)  # sort by sign
    sorted_keys.sort(key=lambda x: x[0][2:])  # sort in alph. order
    return sorted_keys


def get_ordered_dictionary(dictionary):
    """
    Order a dictionary in correspondence to the preferred output.

    Parameters:
        dictionary: dictionary to be ordered.

    Returns:
        ordered dictionary.
    """
    ordered_dict = OrderedDict()
    for key, value in sort_keys(dictionary.items()):
        if isinstance(value, dict):
            ordered_dict[key] = get_ordered_dictionary(value)
        else:
            ordered_dict[key] = value
    return ordered_dict


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
