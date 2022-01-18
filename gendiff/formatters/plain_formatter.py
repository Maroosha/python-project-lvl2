"""Plain formatter for comparing two files."""

# !usr/bin/env/python3

from gendiff.formatters.keywords import KEYWORDS_CONVERSION


LOG_MESSAGES = {
    'added': "Property '{path}' was added with value: {new_value}",
    'removed': "Property '{path}' was removed",
    'changed': "Property '{path}' was updated. From {old_value} to {new_value}",
}


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


def get_message(status, path, old_value, new_value):
    """
    Get a log message.

    Parameters:
        status: status of a key-value pair,
        path: path to the parameter (key),
        old_value: old value if any,
        new_value: new value if any.

    Returns:
        log message as a string.
    """
    if status == 'changed':
        return LOG_MESSAGES[status].format(
            path=path,
            old_value=old_value,
            new_value=new_value,
        )
    if status == 'added':
        return LOG_MESSAGES[status].format(path=path, new_value=new_value)
    if status == 'removed':
        return LOG_MESSAGES[status].format(path=path)


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
        if status == 'changed':
            old_value = check_value_complexity(value.get('old value'))
            new_value = check_value_complexity(value.get('new value'))
            message = get_message(status, path, old_value, new_value)
            log.append(message)
        elif status == 'added':
            new_value = check_value_complexity(status_dict.get('value'))
            message = get_message(status, path, None, new_value)
            log.append(message)
        elif status == 'removed':
            message = get_message(status, path, None, None)
            log.append(message)
        elif status == 'nested':
            log.append(format_plain(value, path))
    return '\n'.join(log)
