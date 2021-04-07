#!/usr/bin/tclsh

# OPERATORS in tcl


# ARITHMETIC OPERATORS

set a 15
set b 20

# ADDITION
puts [expr $a + $b]
# SUBTRACTION
puts [expr $a - $b]
# MULTIPLICATION
puts [expr $a * $b]
# DIVISION
puts [expr $a / $b]
# MODULUS/REMAINDER
puts [expr $a % $b]

puts "RELAIONAL OPERATORS"

# RELATIONAL OPERATORS

# EQUAL TO
# '=='
if { $a == 15 } {
    puts "a is equal to 15"
}

# NOT EQUAL
# '!='
if { $b != 19 } {
    puts "b is not equal to 19"
}

# GREATER THAN
# '>'

if { $a > 2 } {
    puts "a is greater than 2"
}

# LESS THAN
# '<'

if { $b < 50 } {
    puts "b is less than 50"
}


# GREATER OR EQUAL
# >=
if { $a >= 15 } {
    puts "a is greater than or equal to 15"
}


# LESSER OR EQUAL
# <=
if { $a <= 45 } {
    puts "a is lesser than or equal to 45"
}

puts "LOGICAL OPERATORS"
# LOGICAL OPERATORS

# "AND"
# &&

if { $a == 15 && $b == 20 } {
    puts "a is equal to 15 and b is equal to 20"
}


# "OR"
# ||

if { $a > 13 || $b >= 45 } {
    puts "a is greater than 20 OR b is greater or equal to 45"
}


# "NOT"
# !
# if conditional true, makes it false and vice versa
if {! ($a == 45) } {
    puts "not statement"
}


# TERNARY OPERATORS



    











