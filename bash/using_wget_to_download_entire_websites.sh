#!/usr/bin/bash


# sometimes it's useful to download all the static content on a website for future review or use.
# You can use either the wget or the curl command for this (and I'm sure there are other commands too)

# Using wget:

wget  --recursive --domains example.com --page-requisites --html-extension --convert-links --no-clobber HTTPS://www.example.com/


# Here are the explanations of the above cli options for wget
# only above option that takes an argument is is --domains

# --recursive - recursively download all the directories and their child files and folders
# --domains [example.com] - Don't follow links outside outside "example.com"
# --page-requisites - get all the elements that compose the page (images, css etc..)
# --html-extension - save files with the .html extension
# --convert-links - convert links so that they work locally, off line
# --no-clobber - don't overwrite any existing files (Great in case download is interrupted and reresumed)













