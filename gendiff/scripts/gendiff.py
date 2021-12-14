"""Script for gendiff."""

# !usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.formatters.formats import STYLISH
import argparse

parser = argparse.ArgumentParser(description='Generate diff')

# positional args
parser.add_argument('first_file')
parser.add_argument('second_file')
# optional args
parser.add_argument(
    '-f', '--format',
    default=STYLISH,
    help='set format of output (default: stylish)'
)

args = parser.parse_args()


def main():
    return generate_diff(args.first_file, args.second_file)


if '__name__' == '__main__':
    main()
