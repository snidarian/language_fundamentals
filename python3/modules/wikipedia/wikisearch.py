#!/usr/bin/python3
# Command line program that returns the result of a wikipedia search


import wikipedia
import argparse
from colorama import Fore, Style
import lxml

# ANSI Terminal color definitions
r = Fore.RED
w = Fore.WHITE
b = Fore.BLUE
g = Fore.GREEN
bl = Fore.BLACK
m = Fore.MAGENTA
y = Fore.YELLOW
c = Fore.CYAN
reset = Fore.RESET

# Argparse sets up with global scope for greater ease
# Argparse takes care of the arguments passed to the program
parser = argparse.ArgumentParser(description="Command line Wikipedia Utility. Returns summary paragraph by default")

parser.add_argument("query", help="Search term string", type=str, default="Wikipedia")
parser.add_argument("--html", help="Get full page html", action='store_true')

args = parser.parse_args()

# #####################################################################
# DEFINITIONS

def make_page_search(search_term):
    try:
        result = wikipedia.page(title=search_term, auto_suggest=False)
        print(result.summary)
    except wikipedia.exceptions.PageError:
        print(f"PageError: '{search_term}' does not match any pages. Try again.")
        # if page not found calls suggest_term() function to suggest an orthographically similar page title
        suggest_term()
    except:
        print("Some sort of other error occurred. You must be unlucky. This is a catchall error message; Investigate further")


def suggest_term():
    # Checks whether of not you might have mispelled search term
    spellcheck = wikipedia.suggest(args.search_term) # returns None if no search suggestion is found
    if spellcheck != None:
        confirm = input("Did you by chance mean '" + r + f"{spellcheck}" + reset + "'" + y + " (y/n)" + reset + "? ")
        confirm = confirm.lower()
        if confirm == "y":
            make_page_search(spellcheck)
        else:
            pass
    else:
        pass


def return_page_html(term):
    if args.html:
        print("printing html to page")
        html = wikipedia.WikipediaPage(title=term).html()
        return(html)


# Main Function
def main():
    make_page_search(args.query)
    if args.html:
        html = return_page_html(args.query)
        print(html)


# #################################################
# EXECUTIONS

if __name__ == "__main__":
    main()







