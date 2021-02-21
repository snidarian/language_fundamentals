#! /usr/bin/bash


# C style bash for loop
for ((i = 0 ; i < 10 ; i++)); do
	echo "Hello Friend"
done


# loop in range
for i in {1..10}; do
	echo "Hello Friend"
done

# Iterative loop
for i in /var/*; do
	echo $i 
done

# while loop
num=1
while [ $num -le 10 ]; do
	echo $(($num * 3))
	num=$(($num+1))
done

# until loop
num=1
until [ $num -gt 10 ]; do
	echo $(($num * 3))
	num=$(($num+1))
done


# Looping through the contents of an array
prime=(2 3 5 7 11 13 17 19 23 29)
for i in "${prime[@]}"; do
	echo $i
done 


# C style for loop with a conditional break statement
for ((i=1;i<=10;i++)); do
	echo $i
	if [ $i -eq 3 ]; then
		break
	fi
done

# C style for loop demonstrating the use of 'continue' statement
for ((i=0;i<=10;i++)); do
	if [ $(($i % 2)) -ne 1 ]; then
		continue
	fi
	echo $i
done
