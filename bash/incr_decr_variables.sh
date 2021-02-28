#!/bin/bash


# There are a number of ways to increment and decrement variables in bash



I=1
V=5
X=10
L=50
C=100

# incrementation

I=$((I+1))

echo "$I"

let "V=V+1"

echo "$V"

# decrementation

I=$((i-1))

echo "$I"

let "V=V-1"

echo "$V"



# until loop illustrating the use of incrementing and decrementing

until [ $L -eq 0 ]
do
    echo "L = $L"
    # two steps forward one step back
    ((L=L+1))
    echo "L = $L"
    ((L=L-2))
done



# Using the incrementation and decrementation operators


# increment operator:
((I+=1))
echo "$I"

# decrement operator:
((C-=1))
echo "$C"



# While loop using the decrement operator


while [ $C -gt 50 ]
do
    echo "C = $C"
    ((C-=2))
done




# C-style increment and decrement operators in BASH

# Just like in C, ++ and -- operators can be used to increment and decrement a variable

# the distinction between postfixing and prefixin ++ or -- is much the same as it is in C.

# postfixing returns the value before it is incremented or decremented
# prefixing returns the value after it is incremented or decremented


# increment
((i++))
((++i))

let "i++"
let "++i"

# decrement
((i--))
((--i))

let "i--"
let "--i"


# postfix
x=5
y=$((x++))
echo x: $x
echo y: $y

# prefix
x=5
y=$((++x))
echo x: $x
echo y: $y












