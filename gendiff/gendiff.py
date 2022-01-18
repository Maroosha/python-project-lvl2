"""
Compare two files with one another.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3

from typing import Dict, OrderedDict
from gendiff.file_parser import get_raw_data, parse_file
from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.stylish_formatter import format_stylish
from gendiff.formatters.plain_formatter import format_plain


def get_status_dictionary(keys, data, status):
    """
    Get a dictionary of statuses for a current (sub)dict.

    Parameters:
        keys: keys of a dict,
        data: data from a file,
        status: status of a key-value pair.

    Returns:
        status dictionary.
    """
    status_dictionary = {}
    for key in keys:
        status_dictionary[key] = {
            'status': status,
            'value': data.get(key),
        }
    return status_dictionary


def get_data_intersection(data1, data2):
    """
    Get instersecting data from two data files.

    Parameters:
        data1: data from the first file as a dict,
        data2: data from the second file as a dict.

    Returns:
        list of intersected keys.
    """
    return list(data1.keys() & data2.keys())


def get_data_difference(data1, data2):
    """
    Get data that differs between two data files.

    Parameters:
        data1: data from the first file as a dict,
        data2: data from the second file as a dict.

    Returns:
        list of differing keys.
    """
    return list(data1.keys() - data2.keys())


def get_local_difference_pair(key, value1, value2):
    """
    Get a key-value pair for the local_difference dict.

    Parameters:
        key: key from data1 and data2,
        value1: value from data1,
        value2: value from data2.

    Returns:
        local_difference dict with a single key-value pair.
    """
    local_difference_pair = {}
    if isinstance(value1, Dict) and isinstance(value2, Dict):
        local_difference_pair[key] = {
            'status': 'nested',
            'value': compare_data(value1, value2),
        }
    elif value1 == value2:
        local_difference_pair[key] = {
            'status': 'unchanged',
            'value': value1,
        }
    else:
        local_difference_pair[key] = {
            'status': 'changed',
            'value': {
                'old value': value1,
                'new value': value2,
            },
        }
    return local_difference_pair


def analyze_interseting_keys(intersecting_keys, data1, data2):
    """
    Build a status dictionary for intersecting keys.

    Parameters:
        intersecting keys: keys that intersect in data1 & data2,
        data1: data from the first file,
        data2: data from the second file.

    Returns:
       status dict for intersecting keys.
    """
    local_difference = {}
    for key in intersecting_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        local_difference_pair = get_local_difference_pair(
            key,
            value1,
            value2,
        )
        local_difference.update(local_difference_pair)
    return local_difference


def compare_data(data1, data2):
    """
    Compare data from two files.

    Parameters:
        data1: data from the first file,
        data2: data from the second file.

    Returns:
        ordered dict of compared data.
    """
    difference_dictionary = {}
    intersecting_keys = get_data_intersection(data1, data2)
    added_keys = get_data_difference(data2, data1)
    removed_keys = get_data_difference(data1, data2)

    intersection_statuses = analyze_interseting_keys(
        intersecting_keys,
        data1,
        data2,
    )
    added_keys_statuses = get_status_dictionary(
        added_keys,
        data2,
        'added',
    )
    removed_keys_statuses = get_status_dictionary(
        removed_keys,
        data1,
        'removed',
    )

    difference_dictionary.update(added_keys_statuses)
    difference_dictionary.update(removed_keys_statuses)
    difference_dictionary.update(intersection_statuses)

    return OrderedDict(sorted(difference_dictionary.items()))


def generate_diff(filepath1, filepath2, formatter='stylish'):
    """
    Generate difference btw data in file1 and file2 as a str.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference as a string.
    """
    data1 = parse_file(filepath1, get_raw_data(filepath1))
    data2 = parse_file(filepath2, get_raw_data(filepath2))
    diff = compare_data(data1, data2)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'json':
        return format_json(diff)
    return format_stylish(diff)
