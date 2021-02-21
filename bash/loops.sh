#! /usr/bin/bash


for ((i = 0 ; i < 10 ; i++)); do
	echo "Hello Friend"
done



for i in {1..10}; do
	echo "Hello Friend"
done



for i in /var/*; do
	echo $i 
done



num=1
while [ $num -le 10 ]; do
	echo $(($num * 3))
	num=$(($num+1))
done


num=1
until [ $num -gt 10 ]; do
	echo $(($num * 3))
	num=$(($num+1))
done



prime=(2 3 5 7 11 13 17 19 23 29)
for i in "${prime[@]}"; do
	echo $i
done 




for ((i=1;i<=10;i++)); do
	echo $i
	if [ $i -eq 3 ]; then
		break
	fi
done


for ((i=0;i<=10;i++)); do
	if [ $(($i % 2)) -ne 1 ]; then
		continue
	fi
	echo $i
done
