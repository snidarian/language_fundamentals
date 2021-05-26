#!/usr/bin/python3

import wikipedia


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

return_random_pages(3)

