"""Formatter for comparing two files."""

# !usr/bin/env/python3

import json
from gendiff.formatters.engine import get_ordered_dictionary


def format_stylish(dictionary):
    """
    Get a dictionary in stylish format.

    Parameters:
        dictionary: dictionary of compared data.

    Returns:
        formatted data as a string.
    """
    sorted_dict = get_ordered_dictionary(dictionary)
    json_dict = json.dumps(sorted_dict, indent=4, separators=('', ': '))
    sorted_string = [i for i in json_dict if i != '"']
    for index, value in enumerate(sorted_string):
        if value == '}':
            sorted_string[index] = '  }'
    answer, index = [], 0
    while index < len(sorted_string):
        if sorted_string[index] == '\n':
            answer.append(sorted_string[index])
            index += 3
        else:
            answer.append(sorted_string[index])
            index += 1
    answer[-1] = '\n}'
    string_answer = ''.join(answer)
    return string_answer
