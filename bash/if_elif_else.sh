#!/usr/bin/bash


number="$1"


if [ $number -gt 1 ] && [ $number -lt 10 ]; then
    echo "number is greater than 1"
elif [ $number -gt 10 ] && [ $number -lt 100 ]; then
    echo "number is greater than 10"
elif [ $number -gt 100 ] && [ $number -lt 1000 ] ; then
    echo "number is greater than 100"
elif [ $number -gt 1000 ] && [ $number -lt 10000 ] ; then
    echo "number is greater than 1,000"
elif [ $number -gt 10000 ] && [ $number -lt 100000 ]; then
    echo "number is greater than 10,000"
elif [ $number -gt 100000 ] && [ $number -lt 1000000 ]; then
    echo "number is greater than 100,000"
elif [ $number -gt 1000000 ] && [ $number -lt 10000000 ] ; then
    echo "number is greater than 1,000,000"
else
    echo "number is greater than ONE BILLION"
fi










