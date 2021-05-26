#!/usr/bin/python3
# Command line program that returns the result of a wikipedia search


import wikipedia
import argparse
from colorama import Fore, Style


# Argparse takes care of the arguments passed to the program
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--search-term", help="Search term string", type=str, default="Wikipedia")

args = parser.parse_args()


# Checks whether of not you might have mispelled search term
spellcheck = wikipedia.suggest(args.search_term) # returns None if no search suggestion is found
if spellcheck != None:
    print(f"Did you by chance mean '{spellcheck}'?")
else:
    pass

try:
    result = wikipedia.page(args.search_term)
    print(result.summary)
except:
    print("Some sort of error encountered")







