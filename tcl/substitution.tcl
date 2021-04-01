#!/usr/bin/tclsh


if 0 {
    In tcl square brackets are used for command substitution.
    See the below example. The Bash equivalent would be:
    echo `expr 1 + 6 + 9`
}

# Command substitution in tcl
puts [expr 1 + 6 + 9]



# Variable substitution in tcl

# Set variable 'a'
set a 147

# Variable substitution of variable 'a'
puts $a


