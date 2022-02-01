"Format a difference dict."

# !/usr/bin/env python3

from gendiff.formatters.json import format_json
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def format_diff(diff, formatter):
    """
    Get a difference dict in one of three formats:
    stylish, plain or json.

    Parameters:
        diff: difference dict,
        format: stylish/plain/json.

    Returns:
    difference dict in one of three preferred formats.
    """
    if formatter == 'json':
        return format_json(diff)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'stylish':
        return format_stylish(diff)
    raise Exception('Invalid format. Try "json", "plain" or "stylish" instead.')
