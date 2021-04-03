#!/usr/bin/tclsh



# variable typing is dynamic and automatic
# setting a variable

set variable_name 10
puts $variable_name


# As "variable_name" exists right now, it is a string
# but when we use it to make an arithmetic expression
# the value "10" as a string is automaticall converted
# to an integer by the interpreter.

puts [expr $variable_name + 147 - 72]


# In tcl variables are given no starting value and must
# be initialized by giving them a value before they are used.



# Set a variable to the value of a string with "" or {}
set double_quotes_var "string"
set double_braces_var {string}

puts "$double_braces_var , $double_quotes_var"



# Variables are dynamically typed in tcl
# so variable data types are changed automatically

set dynamic_variable 10

puts [expr $dynamic_variable + 50]

set $dynamic_variable "string value"










