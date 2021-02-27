#!/usr/bin/bash


first=$1
second=$2
third=$3

k1="of mark 1"
k2="of mark 2"
k3="of mark 3"
k4="of mark4"



if [ $first == "mark1" ]; then
    echo "1st level $k1"
    if [ $second == "mark1" ]; then
	echo "2nd level $k1"
	if [ $third == "mark1" ]; then
	    echo "3rd level $k1"
	fi
    fi
fi


if [ $first == "mark2" ]; then
    echo "1st level $k2"
    if [ $second == "mark2" ]; then
	echo "2nd level $k2"
	if [ $third == "mark2" ]; then
	    echo "3rd level $k2"
	fi
    fi
fi


if [ $first == "mark3" ]; then
    echo "1st level $k3"
    if [ $second == "mark3" ]; then
	echo "2nd level $k3"
	if [ $third == "mark3" ]; then
	    echo "3rd level $k3"
	fi
    fi
fi
    

if [ $first == "mark4" ]; then
    echo "1st level $k4"
    if [ $second == "mark4" ]; then
	echo "2nd level $k4"
	if [ $third == "mark4" ]; then
	    echo "3rd level $k4"
	fi
    fi
fi
    



















