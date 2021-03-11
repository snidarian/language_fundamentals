#!/usr/bin/bash



coinflip_sequence=( / - \\ \| )



while [ 1 ]; do
    for((i=0;i<=3;i++)); do
	echo -ne "${coinflip_sequence[$i]}"
	echo -ne "\b"
	sleep .1
    done
echo -ne " "
done


























