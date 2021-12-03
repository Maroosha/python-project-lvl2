"""
Compare two files with one another.

Acceptable file formats: .JSON, .YAML, .YML
"""

# !/usr/bin/env python3


from gendiff.file_parser import parse_file
import types

JSON_TO_PYTHON = types.MappingProxyType({
    'True': 'true',
    'False': 'false',
    'None': 'null',
})


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
            intersection_dictionary['  ' + key] = data1[key]
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


def compare_data(filepath1, filepath2):
    """
    Compare data from two .json files.

    Parameters:
        filepath1: path to file1,
        filepath2: path to file2.

    Returns:
        dictionary of compared data.
    """
    file1_data, file2_data = parse_file(filepath1), parse_file(filepath2)
    difference = {}
    difference.update(get_data_intersection(file1_data, file2_data))
    difference.update(get_data_difference(file1_data, file2_data, '-'))
    difference.update(get_data_difference(file2_data, file1_data, '+'))
    return difference


def get_non_python_style_difference_dict(filepath1, filepath2):
    """
    Change Python-style vars to JSON-/YAML-style vars.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference dictionary with JSON-stule vars.
    """
    difference = compare_data(filepath1, filepath2)
    for key, value in difference.items():
        if str(value) in JSON_TO_PYTHON:
            difference[key] = JSON_TO_PYTHON[str(value)]
    return difference


def generate_diff(filepath1, filepath2):
    """
    Generate difference btw data in file1 and file2 as a str.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference as a string.
    """
    diff = get_non_python_style_difference_dict(filepath1, filepath2)
    diff_keys = list(diff.keys())
    diff_keys.sort(key=lambda x: x[0], reverse=True)  # sort by sign
    diff_keys.sort(key=lambda x: x[2])  # sort in alphabetical order
    answer = '{'
    for key in diff_keys:
        answer += f'\n  {key}: {diff[key]}'
    return answer + '\n}'
