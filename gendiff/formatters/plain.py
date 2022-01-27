"""Plain formatter for comparing two files."""

# !usr/bin/env/python3

import json
import types


LOG_MESSAGES = types.MappingProxyType({
    'added': "Property '{path}' was added with value: {new_value}",
    'removed': "Property '{path}' was removed",
    'changed': "Property '{path}' was updated. From {old_value} to {new_value}",
})


def check_value_complexity(value):
    """
    Check whether a value is complex.

    Parameters:
        value: value to be checked.

    Returns:
        '[complex value]' if value is a dictionary
        or json-style value if it not.
    """
    if isinstance(value, dict):
        return '[complex value]'
    return stringify_value(value)


def stringify_value(value):
    """
    Convert a value from Python- to JSON/YAML-style.

    Parameters:
        value: value to be converted.

    Returns:
        value in a JSON/YAML-style.
    """
    if value is None or isinstance(value, bool):
        return json.dumps(value)
    return f"'{value}'" if isinstance(value, str) else value


def get_path(parent, key):
    """
    Get a log path for a given parameter.

    Parameters:
        parent: parameter name at a higher nesting lvl,
        key: parameter name.

    Returns:
        path as a str.
    """
    if parent:
        return parent + f'.{key}'
    return f'{key}'


def get_logline(status_dict, value, type_, path):
    """
    Get a logline.

    Parameters:
        status_dict: dictionary of types and values
        for a current (sub)dict,
        value: given value,
        type_: type of a key-value pair,
        path: path to the parameter (key).

    Returns:
        logline as a list with a single string.
    """
    log_line = []
    if type_ == 'changed':
        old_value = check_value_complexity(value.get('old value'))
        new_value = check_value_complexity(value.get('new value'))
        message = LOG_MESSAGES[type_].format(
            path=path,
            old_value=old_value,
            new_value=new_value,
        )
        log_line.append(message)
    elif type_ == 'added':
        new_value = check_value_complexity(status_dict.get('value'))
        message = LOG_MESSAGES[type_].format(path=path, new_value=new_value)
        log_line.append(message)
    elif type_ == 'removed':
        message = LOG_MESSAGES[type_].format(path=path)
        log_line.append(message)
    elif type_ == 'nested':
        log_line.append(format_plain(value, path))
    return log_line


def format_plain(diff, parent=None):
    """
    Introduce output in plain format.

    Parameters:
        diff: dictionary of differences btw two files.

    Returns:
        difference in plain format.
    """
    log = []
    for key, status_dict in diff.items():
        path = get_path(parent, key)
        type_ = status_dict.get('type')
        value = status_dict.get('value')
        logline = get_logline(status_dict, value, type_, path)
        log.extend(logline)
    return '\n'.join(log)
