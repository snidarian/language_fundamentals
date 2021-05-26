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
parser = argparse.ArgumentParser(description="Command line Wikipedia Utility. Returns summary paragraph by default. Enclose multi-word search terms in a pair of double quotes")

parser.add_argument("query", help="Search term string", type=str, nargs='?', default='wikipedia')
parser.add_argument("--html", help="Get full page html", action='store_true')
parser.add_argument("-c", "--all-page-content", help="Returns page plain text", action='store_true')
parser.add_argument("-r", "--random", help="Random article integer argument", type=int, default=3)

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
        print("This is a catchall error message; Investigate further")


def return_page_plain_text(search_term):
    try:
        page = wikipedia.WikipediaPage(title=search_term)
        content = page.content
        print(content)
    except wikipedia.exceptions.PageError:
        print(f"PageError: '{search_term}' does not match any pages. Try again.")
        # if page not found calls suggest_term() function to suggest an orthographically similar page title
        suggest_term()
    except:
        print("catchall error message; Investigate further")


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

# return quantity of random page summaries (10 max)
def return_random_pages(quantity):
    random_results = wikipedia.random(pages=quantity)
    print(random_results)
    for term in random_results:
        # retrieve page content summary
        page = wikipedia.page(title=term)
        uppercased_term = term.upper()
        print("---------------------------------------------------------", end="\n")
        print(str(uppercased_term), end="\n\n")
        print(page.summary)
        print("---------------------------------------------------------", end="\n\n")


def return_page_html(term):
    if args.html:
        print("printing html to page")
        html = wikipedia.WikipediaPage(title=term).html()
        return(html)


# Main Function
def main():
    if args.random:
        print("mark0")
    elif args.all_page_content:
        return_page_plain_text(args.query)
    elif args.html:
        html = return_page_html(args.query)
        print(html)
    else:
        make_page_search(args.query)


# #################################################
# EXECUTIONS

if __name__ == "__main__":
    main()







