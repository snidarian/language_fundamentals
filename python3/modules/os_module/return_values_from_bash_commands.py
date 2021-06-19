#!/usr/bin/python3


import os


# you can get a return value from a bash command with the .popen() and .read() methods


return_value = os.popen('ls ~').read()


# in this example the results of the ls command are returned separated by '\n' newline characters
print(return_value)

















