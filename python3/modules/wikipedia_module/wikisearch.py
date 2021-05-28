#!/usr/bin/python3
# Command line program that returns the result of a wikipedia search
# supports searching in russian and english
# supports random page generation in English and Russian
# can dump full wiki page content or merely page summaries to stdout in Russian or English

import wikipedia
import argparse
from colorama import Fore, Style
import lxml

# ANSI Terminal color definitions
r = Fore.RED; w = Fore.WHITE; b = Fore.BLUE; g = Fore.GREEN; bl = Fore.BLACK 
m = Fore.MAGENTA; y = Fore.YELLOW; c = Fore.CYAN; reset = Fore.RESET

# Argparse sets up with global scope for greater ease
# Argparse takes care of the arguments passed to the program
parser = argparse.ArgumentParser(description="Command line Wikipedia Utility. Returns summary paragraph by default. Enclose multi-word search terms in a pair of double quotes")

parser.add_argument("query", help="Search term string", type=str, nargs='?', default='wikipedia')
parser.add_argument("--html", help="Get full page html", action='store_true')
parser.add_argument("-c", "--all-page-content", help="Returns page plain text", action='store_true')
parser.add_argument("-r", "--random", help="Random article integer argument", type=int)
parser.add_argument("-ru", "--russian", help="Sets language to Russian", action='store_true')

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
    except wikipedia.exceptions.DisambiguationError:
        print("The term you search lead to a disambiguation page..")
    except:
        print("Catch-all error message; Investigate further. VPN might be to blame")


def return_page_plain_text(search_term, russian_lang=False):
    # if russian_lang == True:
    #     wikipedia.set_lang('ru')
    try:
        page = wikipedia.WikipediaPage(title=search_term)
        content = page.content
        print(content)
    except wikipedia.exceptions.PageError:
        print(f"PageError: '{search_term}' does not match any pages. Try again.")
        # if page not found calls suggest_term() function to suggest an orthographically similar page title
        suggest_term()
    except wikipedia.exceptions.DisambiguationError:
        print(r + "DisambiguationError: Result resolves to a disambiguation page" + reset)
    except wikipedia.exceptions.HTTPTimeoutError:
        print(r + "HTTPTimeoutError: Request to mediawiki server has timed out" + reset)
    except:
        print(r + "catchall error message; Investigate further" + reset)


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
def return_random_pages(quantity=3):
    random_results = wikipedia.random(pages=quantity)
    for item in random_results:
        print(g + item + reset, end=", ")
    for term in random_results:
        print("")
        # retrieve page content summary
        try:
            page = wikipedia.page(title=term)
            uppercased_term = term.upper()
            print(m + "--------------------------------------------------------------------------" + reset, end="\n")
            print(y + str(uppercased_term) + reset, end="\n\n")
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError:
            print(r + "Page resolves to a disambiguation page" + reset)
        except wikipedia.exceptions.PageError:
            print(r + "Page error encountered" + reset)
        except:
            print(r + "Catch all error exception. Error coult be an HTTPTimeoutError" + reset)
    print("\n")


def return_page_html(term):
    if args.html:
        print("printing html to page")
        html = wikipedia.WikipediaPage(title=term).html()
        return(html)


# Main Function
def main():
    russian_lang = False
    # check if the query argument contains any russian letter
    for letter in [ # Vowels listed first so for-loop breaks sooner saving time
        'а', 'е', 'ё', 
        'и', 'о', 'у', 
        'ы', 'э', 'ю', 
        'я', 'б', 'в', 
        'г', 'д', 'ж', 
        'з', 'к', 'л', 
        'м', 'н', 'п', 
        'р', 'с', 'т', 
        'ф', 'х', 'ц', 
        'ч', 'ш', 'щ']:
        if letter in args.query:
            russian_lang = True
            break
    if russian_lang == True:
        wikipedia.set_lang('ru')
    else:
        wikipedia.set_lang('en')
    if args.random:
        if args.russian:
            wikipedia.set_lang('ru')
        else:
            wikipedia.set_lang('en')
        if args.random > 10:
            # asking for more than 10 random articles - (because api only supports requests for 10 random articles at a time)
            print(f"random articles is > 10... you asked for {args.random} articles")
            loaded_calls = (args.random // 10)
            for _ in range(loaded_calls):
                return_random_pages(10)
            # number of odd-extra times to call random function based on --random integer
            spare_calls = (args.random % 10)
            return_random_pages(spare_calls)
        else:
            # Asking for less than or equal to 10 random articles
            return_random_pages(args.random)
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







