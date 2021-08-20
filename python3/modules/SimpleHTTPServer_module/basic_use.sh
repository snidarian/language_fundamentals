#!/usr/bin/bash



# Run a simple http server in a directory with the following command
# the default port for this command is 8000 but 80 is the standard HTTP port
# note: running the python interpreter with the -m option allows you to run modules as scripts.
python -m SimpleHTTPServer 80


# You should see an output like this:
# Serving HTTP on 0.0.0.0 port 80 ...


# The directory that the command was run from now becomes the root directory of the server


# Now you can interract with the server from another device on the network
# Use the wget command to send a GET request to the server for one of the files

wget http://192.168.1.160/work_log.txt


# On the serverside console you should see an output like this:
# 192.168.1.160 - - [20/Aug/2021 13:15:23] "GET /work_log.txt HTTP/1.1" 200 -
























