#! /usr/bin/bash

# script demonstrates finding substring in string


string=$1
substring=$2

echo "String = $string"
echo "substring = $substring"


if [[ $string == *"$substring"* ]]; then
    echo "Substring in string"
else
    echo "Substring not in string"
fi




















