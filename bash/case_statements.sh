#!/bin/bash

# Each clause must be terminated by two semi-colons ';;'
# Each pattern terminates with a right perenthesis '('
# '|' pipe is used to create or equivalencies between case patterns as seen below

# setting a default case:
# '*' wildcard is commonly used as pattern to set a default case


case $1 in
    "hello")
	echo "mark 1"
	;;
    "hi"|"sup")
	echo "mark 2"
	;;
    "halo"|"guten tag")
	echo "mark 2.5"
	;;
    *)
	echo "mark 3"
	;;
esac



case $1 in
    "Iran"|"Persia")
	language="Farsi"
	;;
    "Somalia")
	language="Somali"
	;;
    "Russia"|"Russian Federation")
	language="Russian"
	;;
    "Azerbaijan")
	language="Azerbaijani"
	;;
    "China")
	language="Mandarin Chinese"
	;;
    "America")
	language="American English"
	;;
    "Nederlands")
	language="Dutch"
	;;
    *)
	echo "Error: Country not contained in database"
	exit 127
	;;
esac


echo "The language of $1 is $language"





