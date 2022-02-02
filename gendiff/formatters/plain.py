"""Plain formatter for comparing two files."""

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


def get_log(diff, parent):
    """
    Get a log of messages for plain representation.

    Parameters:
        diff: dictionary of differences btw two files,
        parent: current parameter.

    Returns:
        log for plain representation.
    """
    log = []
    for key, status_dict in diff.items():
        path = get_path(parent, key)
        type_ = status_dict.get('type')
        value = status_dict.get('value')
        if type_ == 'changed':
            old_value = check_value_complexity(value.get('old value'))
            new_value = check_value_complexity(value.get('new value'))
            message = LOG_MESSAGES[type_].format(
                path=path,
                old_value=old_value,
                new_value=new_value,
            )
            log.append(message)
        elif type_ == 'added':
            new_value = check_value_complexity(status_dict.get('value'))
            message = LOG_MESSAGES[type_].format(path=path, new_value=new_value)
            log.append(message)
        elif type_ == 'removed':
            message = LOG_MESSAGES[type_].format(path=path)
            log.append(message)
        elif type_ == 'nested':
            log.append(get_log(value, path))
    return '\n'.join(log)


def format_plain(diff):
    """
    Introduce output in plain format.

    Parameters:
        diff: dictionary of differences btw two files.

    Returns:
        difference in plain format.
    """
    return get_log(diff, parent='')
