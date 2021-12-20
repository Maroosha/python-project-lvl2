"""Formatter for comparing two files."""

# !usr/bin/env/python3

import json
from gendiff.formatters.engine import get_ordered_dictionary


def format_closing_bracket(list_):
    """
    Format all the closing brackets: '}' -> '  }'.

    Parameters:
        list_: list to be processed.

    Returns:
        processed list with formatted brackets.
    """
    for index, value in enumerate(list_):
        if value == '}':
            list_[index] = '  }'
    return list_


def get_almost_stylish_output(list_):
    """
    Format the list into an almost stylish format.

    Parameters:
        list_: list to be processed.

    Returns:
        processed list in almost stylish format.
    """
    answer, index = [], 0
    while index < len(list_):
        if list_[index] == ' ' and list_[index + 1] == '\n':
            index += 1
        elif list_[index] == '\n':
            answer.append(list_[index])
            index += 3
        else:
            answer.append(list_[index])
            index += 1
    return answer


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
    result = format_closing_bracket([i for i in json_dict if i != '"'])
    answer = get_almost_stylish_output(result)
    answer[-1] = '\n}'
    return ''.join(answer)
