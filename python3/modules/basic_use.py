#!/usr/bin/bash


# Using the python interpreter command with the -m option allows us to run a module as a script...
# python -m [module_name]


# I wasn't able to use this module with python3 interpreter so I think it's just for python2



# specify the port that the HTTP server will listen and run on
# note that the default port is port 8000 which is NOT the default HTTP or HTTPS port.
python -m SimpleHTTPServer 80


# you should get output like this:

# Serving HTTP on 0.0.0.0 port 80 ...
# 192.168.1.160 - - [20/Aug/2021 13:15:23] "GET /work_log.txt HTTP/1.1" 200 -



# The directory you ran the command from is not the root directory of the server.



# now you can interract with hosted files and directories in the root folder like so:

wget http://192.168.1.160/work_log.txt






















