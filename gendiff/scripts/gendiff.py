# !usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Generate diff')

# positional args
parser.add_argument('first_file')
parser.add_argument('second_file')
# optional args

args = parser.parse_args()


def main():
    pass


if '__name__' == '__main__':
    main()
