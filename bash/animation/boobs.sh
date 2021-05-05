#! /usr/bin/bash


boob_array=( o0 0o )


while [ 1 ]; do
    for((i=0;i<=1;i++)); do
	echo -ne "${boob_array[$i]}\r"
	sleep 0.2
    done
done
















