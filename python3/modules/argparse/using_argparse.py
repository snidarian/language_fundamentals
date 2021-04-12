#! /usr/bin/python3


import argparse

parser = argparse.ArgumentParser(description='program description here.')

# positional arguments have one value to denote them, no second double flag.
args = parser.add_argument("name", help="Name given to program", type=str)
# Add an optional argument that defauls to a particular value is nothing is supplied to it.
args = parser.add_argument("greeting", help="Greeting supplied to program", nargs='?', type=str, default="good morning")

# below is an example of an optional argument.
args = parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")

# Adding unlimited amount of optional arguments? Use the nargs specifier when defining new argument with args.parser.add_argument([arg details])
# args = parser.add_argument("numbers", help="Numbers to be totaled", nargs="*", type=float)

# Below statement cements arguments and prepares them for use
args = parser.parse_args()


print(f"Hello, {args.name}. {args.greeting} to you!")
if args.verbose:
    print(f"and a merry {args.greeting} to you!")










