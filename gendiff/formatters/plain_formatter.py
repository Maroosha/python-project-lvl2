"""Plain formatter for comparing two files."""

# !usr/bin/env/python3

from gendiff.formatters.keywords import KEYWORDS_CONVERSION
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


def get_logline(status_dict, value, status, path):
    """
    Get a logline.

    Parameters:
        status_dict: dictionary of statuses and values
        for a current (sub)dict,
        value: given value,
        status: status of a key-value pair,
        path: path to the parameter (key).

    Returns:
        logline as a list with a single string.
    """
    log_line = []
    if status == 'changed':
        old_value = check_value_complexity(value.get('old value'))
        new_value = check_value_complexity(value.get('new value'))
        message = LOG_MESSAGES[status].format(
            path=path,
            old_value=old_value,
            new_value=new_value,
        )
        log_line.append(message)
    elif status == 'added':
        new_value = check_value_complexity(status_dict.get('value'))
        message = LOG_MESSAGES[status].format(path=path, new_value=new_value)
        log_line.append(message)
    elif status == 'removed':
        message = LOG_MESSAGES[status].format(path=path)
        log_line.append(message)
    elif status == 'nested':
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
        status = status_dict.get('status')
        value = status_dict.get('value')
        logline = get_logline(status_dict, value, status, path)
        log.extend(logline)
    return '\n'.join(log)
