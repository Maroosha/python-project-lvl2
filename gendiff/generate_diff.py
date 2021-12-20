"""
Compare two files with one another.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3

from gendiff.file_parser import parse_file
from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.stylish_formatter import format_stylish
from gendiff.formatters.plain_formatter import format_plain


def is_flat(filepath):
    """Check if the file data is flat or nested.

    Parameters:
        filepath: path to the file.

    Returns:
        True if data is a flat dictionary, False if nested.
    """
    data = parse_file(filepath)
    for _, value in data.items():
        if isinstance(value, dict):
            return False
    return True


def get_data_intersection(data1, data2):
    """
    Get instersecting data from two data files.

    Parameters:
        data1: data from the first file as a dict,
        data2: data from the second file as a dict,

    Returns:
        dictionary with intersected data.
    """
    intersection_dictionary = {}
    keys1, keys2 = data1.keys(), data2.keys()
    data_intersection = keys1 & keys2
    for key in data_intersection:
        if data1[key] == data2[key]:
            intersection_dictionary[key] = data1[key]
        else:
            intersection_dictionary['- ' + key] = data1[key]  # file1
            intersection_dictionary['+ ' + key] = data2[key]  # file2
    return intersection_dictionary


def get_data_difference(data1, data2, prefix):
    """
    Get data that differs from two data files.

    Parameters:
        data1: data from the first file as a dict,
        data2: data from the second file as a dict,
        prefix: '+' changed in file2; '-' removed from file2.

    Returns:
        dictionary with differing data.
    """
    difference_dictionary = {}
    keys1, keys2 = data1.keys(), data2.keys()
    data_difference = keys1 - keys2
    for key in data_difference:
        difference_dictionary[prefix + ' ' + key] = data1[key]
    return difference_dictionary


def compare_flat_data(data1, data2):
    """
    Compare data from two files with flat dicts.

    Parameters:
        filepath1: path to file1,
        filepath2: path to file2.

    Returns:
        dictionary of compared data.
    """
    difference = {}
    difference.update(get_data_intersection(data1, data2))
    difference.update(get_data_difference(data1, data2, '-'))
    difference.update(get_data_difference(data2, data1, '+'))
    return difference


def compare_nested_data(data1, data2):
    """
    Compare data from two nested files.

    Parameters:
        filepath1: path to the first file.
        filepath2: path to the second file.

    Returns:
        dictionary of compared data.
    """
    difference = {}
    keys_union = data1.keys() | data2.keys()
    for key in keys_union:
        if key in data1 and key not in data2:
            difference['- ' + key] = data1[key]
        if key not in data1 and key in data2:
            difference['+ ' + key] = data2[key]
        elif key in data1 and key in data2:
            difference.update(recurse_through_value(key, data1, data2))
    return difference


def recurse_through_value(parent, dict1, dict2):
    """
    Recurse though a nested dictionary.

    Parameters:
        parent: key of a dictionary.
        dict1: subdictionary from the first file
        dict2: subdictionary from the second file

    Returns:
        local difference.
    """
    local_difference = {parent: {}}
    child1, child2 = dict1[parent], dict2[parent]
    if not isinstance(child1, dict) or not isinstance(child2, dict):
        parent_child1 = {parent: child1}
        parent_child2 = {parent: child2}
        local_difference.update(
            compare_flat_data(parent_child1, parent_child2)
        )
        local_difference = {
            k: v for k, v in local_difference.items() if v != {}
        }
    else:
        intersecting_keys = child1.keys() & child2.keys()
        xor_keys = child1.keys() ^ child2.keys()
        for key in intersecting_keys:
            ans = recurse_through_value(key, child1, child2)
            local_difference[parent].update(ans)
        for key in xor_keys:
            if key in child1:
                local_difference[parent].update({'- ' + key: child1[key]})
            elif key in child2:
                local_difference[parent].update({'+ ' + key: child2[key]})
    return local_difference


def generate_diff(filepath1, filepath2, formatter='stylish'):
    """
    Generate difference btw data in file1 and file2 as a str.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference as a string.
    """
    data1, data2 = parse_file(filepath1), parse_file(filepath2)
    if is_flat(filepath1) and is_flat(filepath2):
        diff = compare_flat_data(data1, data2)
    else:
        diff = compare_nested_data(data1, data2)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'json':
        return format_json(diff)
    return format_stylish(diff)
