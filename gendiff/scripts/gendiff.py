"""Script for gendiff."""

# !usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.formatters.formats import STYLISH
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default=STYLISH,
        choice=[STYLISH, PLAIN],
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
