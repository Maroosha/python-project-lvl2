"""
Compare two files with one another.

Acceptable file formats: .JSON, .YAML, .YML
"""

from gendiff.compare_data import get_compared_data
from gendiff.data_parser import parse
from gendiff.file_reader import get_raw_data, get_format
from gendiff.formatters.formatter import format_diff


def generate_diff(filepath1, filepath2, formatter='stylish'):
    """
    Generate difference btw data in file1 and file2 as a str.

    Parameters:
        filepath1: path to the first file,
        filepath2: path to the second file.

    Returns:
        difference as a string.
    """
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(get_raw_data(filepath1), format1)
    data2 = parse(get_raw_data(filepath2), format2)
    diff = get_compared_data(data1, data2)
    return format_diff(diff, formatter)
