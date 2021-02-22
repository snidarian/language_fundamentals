#! /usr/bin/python3

from colorama import init
from colorama import Fore, Back, Style

# List of available formatting constants:
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

# VERY USEFUL
# init()function accepts kwarg 'autoreset=True' which returns terminal text output to normal immediately after print statement
# by defaul autoreset is set to False unless otherwise specified
init(autoreset=True)

# change regular foreground text color
print(Fore.RED + 'some red text')
# notice the below print statement also produces red text without being explicitly asked
print("also red text")

# colors text background
print(Back.GREEN + 'and with a green background')

# change to black text backgroun
print(Back.BLACK + "Now with a black background")

# dim text
print(Style.DIM + 'and in dim text')

# RESET_ALL method of Style resets all affected text to termianl defaults
# Style.RESET_ALL resets foreground, background, and brightness. Colorama will perform this reset automatically on program exit.
print(Style.RESET_ALL)

print("Now the text is back to normal.")


# demonstration of colorizing the same line with different colors
print(Fore.CYAN + "Some cyan text and" + Fore.BLUE + " now some BLUE text." + Fore.GREEN + " And now some green text.")


# You can use colorama with for loops to make rainbow colored strings
string = "This is a multicolored output string!"

r = True
w = False
b = False
for x in string:
    if (r == True):
        print(Fore.RED + str(x), end='')
        r = False
        w = True
        continue
    if (w == True):
        print(Fore.WHITE + str(x), end='')
        w = False
        b = True
        continue
    if (b == True):
        print(Fore.BLUE + str(x), end='')
        b = False
        r = True
        continue

print("")


# Will continue to add to this file in the future if I find a greater use for Colorama module than at the present moment
