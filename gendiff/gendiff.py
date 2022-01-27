"""
Compare two files with one another.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3

from typing import Dict
from gendiff.parser.data_parser import parse
from gendiff.parser.file_reader import get_raw_data, get_format
from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def get_compared_data(data1, data2):
    """
    Compare data from two files.

    Parameters:
        data1: data from the first file,
        data2: data from the second file
        (both are represented as dicts).

    Returns:
        dictionary of compared data.
        Structure of a difference pair:
        {
            type: nested/changed/unchanged/added/removed,
            value: {
                [old_value:] some_value,
                [new_value: if any,]
            }
        }
    """
    data_difference = {}
    keys1, keys2 = set(data1.keys()), set(data2.keys())
    key_union = sorted(keys1 | keys2)
    for key in key_union:
        if key not in data1 and key in data2:
            data_difference[key] = {
                'type': 'added',
                'value': data2[key],
            }
        elif key in data1 and key not in data2:
            data_difference[key] = {
                'type': 'removed',
                'value': data1[key],
            }
        elif data1[key] == data2[key]:
            data_difference[key] = {
                'type': 'unchanged',
                'value': data1[key],
            }
        elif isinstance(data1[key], Dict) and isinstance(data2[key], Dict):
            data_difference[key] = {
                'type': 'nested',
                'value': get_compared_data(data1[key], data2[key]),
            }
        else:  # data1[key] != data2[key]
            data_difference[key] = {
                'type': 'changed',
                'value': {
                    'old value': data1[key],
                    'new value': data2[key],
                },
            }
    return data_difference


def generate_diff(filepath1, filepath2, formatter='stylish'):
    """
    Generate difference btw data in file1 and file2 as a str.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference as a string.
    """
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(get_raw_data(filepath1), format1)
    data2 = parse(get_raw_data(filepath2), format2)
    diff = get_compared_data(data1, data2)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'json':
        return format_json(diff)
    return format_stylish(diff)
