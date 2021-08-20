#!/usr/bin/bash                                                                                      


# груди                                                                                              
spin_array0=( o0 0o o0 0o )
# Switching x's                                                                                      
spin_array1=( Xxxxx xXxxx xxXxx xxxXx xxxxX )
# coin flip                                                                                          
spin_array2=( - \\ \| / )

i=0

while [ 1 ]; do
    for((i=0;i<=3;i++))
    do
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} "
        echo -ne "${spin_array2[$i]} \r"
        sleep 0.2
    done
done


