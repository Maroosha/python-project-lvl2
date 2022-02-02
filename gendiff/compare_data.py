"Compare data btw two files."

from typing import Dict


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
