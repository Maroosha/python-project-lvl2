"""Compare two .json files with one another."""

# !/usr/bin/env python3


import json
import types

JSON_TO_PYTHON = types.MappingProxyType({
    'True': 'true',
    'False': 'false',
    'None': 'null',
})


def get_dicts(filepath):
    """
    Get data from a .json file.

    Parameters:
        filepath: .json file path.

    Returns:
        data as a dictionary.
    """
    return json.load(open(filepath))


def compare_data(filepath1, filepath2):
    """
    Compare data from two .json files.

    Parameters:
        filepath1: path to file1,
        filepath2: path to file2.

    Returns:
        dictionary of compared data.
    """
    file1_data, file2_data = get_dicts(filepath1), get_dicts(filepath2)
    difference = {}

    def get_data_intersection():
        """Get data that instersects in two .json files."""
        file1_keys, file2_keys = file1_data.keys(), file2_data.keys()
        keys_intersection = file1_keys & file2_keys
        for key in keys_intersection:
            if file1_data[key] == file2_data[key]:
                difference['  ' + key] = file1_data[key]
            else:
                difference['- ' + key] = file1_data[key]  # file1
                difference['+ ' + key] = file2_data[key]  # file2

    def get_data_difference(data1, data2, prefix):
        """
        Get data that differs in two .json files.

        Parameters:
            data1: data from the first file as a dict,
            data2: data from the second file as a dict,
            prefix: '+' changed in file2; '-' removed from file2.
        """
        keys1, keys2 = data1.keys(), data2.keys()
        data_difference = keys1 - keys2
        for key in data_difference:
            difference[prefix + ' ' + key] = data1[key]

    get_data_intersection()
    get_data_difference(file1_data, file2_data, '-')
    get_data_difference(file2_data, file1_data, '+')
    return difference


def get_json_style_difference_dict(filepath1, filepath2):
    """
    Change Python-style vars to JSON-style vars.

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
    diff = get_json_style_difference_dict(filepath1, filepath2)
    diff_keys = list(diff.keys())
    diff_keys.sort(key=lambda x: x[0], reverse=True)  # sort by sign
    diff_keys.sort(key=lambda x: x[2])  # sort in alphabetical order
    answer = '{'
    for key in diff_keys:
        answer += f'\n  {key}: {diff[key]}'
    return answer + '\n}'
