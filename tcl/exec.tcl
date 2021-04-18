#!/usr/bin/tclsh

# exec command spawns a subprocess.
# This doc-file exhibits some of the uses of the exec command.

# a simple way to use the exec command is to use it in a command substitution and
# and assign a variable (using set) to the result of the command substitution.


# set a variable to the command substitution of exec on a linux command
set lsvar [exec ls]

# The normal output of ls is added to this command
puts $lsvar


# The output of cat used on a file in the current directory
set catvar [exec cat file.txt]

# print the output
puts $catvar



# Create a file in the current directory with the touch command
exec touch example_file.txt


# removes the file just created form the current directory 
exec rm example_file.txt


# cd is a builtin command in tcl!! You can change directories with the script.
cd ~

set lshome [exec ls]

puts $lshome


# list the contents of the root directory
set lsroot [exec ls /]

puts $lsroot



