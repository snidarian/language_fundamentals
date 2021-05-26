#!/usr/bin/python3
# Command line program that returns the result of a wikipedia search


import wikipedia
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-s", help="Search term string")


result = wikipedia.page("Tibetan Book of the dead")

print(result.summary)








