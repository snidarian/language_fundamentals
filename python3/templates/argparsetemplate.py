# Template for quickly inserting argparse into new program

import argparse

parser = argparse.ArgumentParser(description='program description here.')

args = parser.add_argument("-single", "--double", help="help message", type=float)


args = parser.parse_args()




