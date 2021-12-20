"""Formatter for comparing two files."""

# !usr/bin/env/python3

from collections import OrderedDict
from gendiff.formatters.engine import get_ordered_dictionary
from gendiff.formatters.engine import KEYWORDS_CONVERSION


def check_value_complexity(value):
    """
    Check whether value is complex.

    Parameters:
        value: value to be checked.

    Returns:
        '[complex value]' if value is a dictionary
        or json-style value if it not.
    """
    if isinstance(value, dict):
        return '[complex value]'
    return convert_keyword(value)


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
    return f'\'{value}\'' if isinstance(value, str) else value


def get_status_dict(dictionary):
    """
    Get a dict of dictionary keys statuses.

    Parameters:
        dictionary: check keys of this dictionary.

    Returns:
        dictionary of keys statuses:
        'not updated': key-value pair not updated,
        'updated': key-value pair updated
        'added': key-value pair added,
        'removed': key-value pair removed.
    """
    status_dict = OrderedDict()
    for key in dictionary:
        if key.startswith('  '):
            status_dict[key[2:]] = 'not updated'
        elif key.startswith('- ') and key[2:] in status_dict:
            status_dict[key[2:]] = 'updated'
        elif key.startswith('+ ') and key[2:] in status_dict:
            status_dict[key[2:]] = 'updated'
        elif key.startswith('- ') and key[2:] not in status_dict:
            status_dict[key[2:]] = 'removed'
        else:
            status_dict[key[2:]] = 'added'
    return status_dict


def get_message(dictionary, key, status, path):
    """
    Get a log message.

    Parameters:
        dictionary: sorted difference dictionary,
        key: key of a dictionary
        status: status of a key in a dictionary,
        path: path to a value.

    Returns:
        log message.
    """
    if status == 'updated':
        old_value = check_value_complexity(dictionary['- ' + key])
        new_value = check_value_complexity(dictionary['+ ' + key])
        return f"Property '{path}' was updated. From {old_value} to {new_value}"
    if status == 'added':
        new_value = check_value_complexity(dictionary['+ ' + key])
        return f'Property \'{path}\' was added with value: {new_value}'
    return f'Property \'{path}\' was removed'


def format_plain(difference):
    """
    Introduce output in plain format.

    Parameters:
        difference: dictionary of differences btw two files.

    Returns:
        difference in plain format.
    """
    sorted_dict = get_ordered_dictionary(difference)
    log = []

    def walk(dictionary, path=''):
        """
        Walk through status dictionary.

        Parameters:
            dictionary: sorted dictionary,
            path: path to the given key.
        """
        status_dict = get_status_dict(dictionary)
        for key, value in status_dict.items():
            path += f'{key}'
            if value == 'not updated':
                if isinstance(dictionary['  ' + key], dict):
                    walk(dictionary['  ' + key], path + '.')
                path = path[:-len(key)]  # do nothing
            else:
                status = value
                message = get_message(dictionary, key, status, path)
                log.append(message)
                path = path[:-len(key)]

    walk(sorted_dict)
    return '\n'.join(log)
