"""Script for gendiff."""

# !usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.formatters.formats import JSON, STYLISH, PLAIN
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default=STYLISH,
        choices=[JSON, PLAIN, STYLISH],
        help='set format of output (default: stylish)'
    )
    args = parser.parse_args()
    return generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    )


if '__name__' == '__main__':
    main()
