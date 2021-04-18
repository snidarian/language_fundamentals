#!/usr/bin/tclsh

# exec command spawns a subprocess.


# set a variable to the command substitution of exec on a linux command
set returnvar [exec ls]

# The normal output of ls is added to this command
puts $returnvar










