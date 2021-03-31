#!/usr/bin/python3



# Basic style format of a try-except statement


# The variable x doesnt exist in this program so when you try to print it, it throws an error

#print(x)
# OUTPUT: NameError: variable x is not defined.


# This is where a try except statement might come in handy

try:
    print(x)
except NameError:
    print("Variable X is not defined")

# and now the program can run and terminate successfully with an exit code status of 0.


# You can link multiple except errors clauses together like so:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except ValueError:
    print("This would occur x is an integer and you're trying to print is inside a string")
except:
    print("This is a generic catch-all except option if you don't name and 'error type'")


# This is how exception are handled in python















