#!/usr/bin/python -B

import argparse

parser = argparse.ArgumentParser(
  description='This program demonstrates how to use argparse',
  formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('-f', '--float', type=float, required=False, default=0.0,
                    help="A floating point parameter")
parser.add_argument('-i', '--integer', type=int, required=True, default=10,
                    help="An integer parameter")
parser.add_argument('-b', '--boolean',
                    action='store_true', required=False, default=False,
                    help="A boolean parameter")
args = parser.parse_args()


print('args.float = ', args.float)
print('args.integer = ', args.integer)
print('args.boolean = ', args.boolean)
