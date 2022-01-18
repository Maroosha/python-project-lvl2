"""Stylish formatter for comparing two files."""

# !usr/bin/env/python3

from gendiff.formatters.keywords import KEYWORDS_CONVERSION
from typing import Dict
import types

INDENT = '    '
STATUS_KEYSWORDS = types.MappingProxyType({
    'unchanged': '    ',
    'added': '  + ',
    'removed': '  - ',
})


def convert_keyword(value):
    """
    Convert a value from Python- to JSON/YAML-style.

    Parameters:
        value: value to be converted.

    Returns:
        value in a JSON/YAML-style.
    """
    if str(value) in KEYWORDS_CONVERSION:
        return KEYWORDS_CONVERSION[str(value)]
    return value


def get_lines(value, diff_depth):
    """
    Get lines per value to be inserted into the final output.

    Parameters:
        value: value to be checked,
        diff_depth: depth of a key-value pair inside diff.

    Returns:
        line for a final output.
    """
    if not isinstance(value, Dict):
        return convert_keyword(value)
    output = ['{']
    tab = INDENT * diff_depth
    ending = f'{tab}}}'
    for key_, value_ in value.items():
        if isinstance(value_, Dict):
            line = f'{tab}{INDENT}{key_}: {get_lines(value_, diff_depth+1)}'
            output.append(line)
        else:
            line = f'{tab}{INDENT}{key_}: {get_lines(value_, diff_depth)}'
            output.append(line)
    output.extend([ending])
    return '\n'.join(output)


def get_almost_stylish_output(diff, diff_depth):
    """
    Get the output in almost stylish format (without outer brackets).

    Parameters:
        diff: dictionary of differences btw two files,
        diff_depth: depth of a key-value pair inside diff.

    Returns:
        output in an almost stylish format.
    """
    output = []
    tab = INDENT * diff_depth
    for key, status_dict in diff.items():
        status = status_dict.get('status')
        value = status_dict.get('value')
        if status == 'nested':
            output_key = f'{tab}{INDENT}{key}: '\
                f'{{\n{get_almost_stylish_output(value, diff_depth+1)}'
            output_value = f'{tab}{INDENT}}}'
            output.extend([output_key, output_value])
        elif status == 'changed':
            old_value = value.get('old value')
            new_value = value.get('new value')
            output_key = f'{tab}{STATUS_KEYSWORDS["removed"]}{key}: '\
                f'{get_lines(old_value, diff_depth+1)}'
            output_value = f'{tab}{STATUS_KEYSWORDS["added"]}{key}: '\
                f'{get_lines(new_value, diff_depth+1)}'
            output.extend([output_key, output_value])
        else:  # unchanged
            output_line = f'{tab}{STATUS_KEYSWORDS[status]}{key}: '\
                f'{get_lines(value, diff_depth+1)}'
            output.append(output_line)
    return '\n'.join(output)


def format_stylish(diff):
    """
    Get a dictionary in stylish format.

    Parameters:
        diff: dictionary of compared data.

    Returns:
        difference in stylish format.
    """
    final_output = ['{', get_almost_stylish_output(diff, diff_depth=0), '}']
    return '\n'.join(final_output)
