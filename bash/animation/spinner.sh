#! /bin/bash                                                                                             


spinner=( \|0\|oooo o\|0\|ooo oo\|0\|oo ooo\|0\|o oooo\|0\| )


spin()
{
    # equivalent to "while True" - loop until interupted                                                 
    while [ 1 ]
    do
        for i in "${spinner[@]}"
        do
            echo -ne "\r$i"
            sleep 0.2
        done
    done

}



spin


