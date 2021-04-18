#!/usr/bin/tclsh



# to read an already existing file
# open file.txt r

# # # open file for reading and writing - file must already exist
# open file.txt r


# # open file for writing; create it if it doesnt already exist
# open file.txt w


# # open file for writing. The file must already exist
# open file.txt a

# # open file for writing. creates file if not already existing.
# open file.txt a+

#set lsvar [exec ls]
#puts $lsvar



# a call to open returns a file indentifier
set file_identifier [open file.txt]
puts "$file_identifier"
close $file_identifier

# ----------------------------------------------------------------------------------------------

# These are the accessmode symbols. The determine the purpose and abilities you gain in accessing a given file.
# they are the following: r, w, a, r+, w+, a+

# r and r+ can only open already created files
# r is for reading only and r+ is for reading and writing.

# w and w+ are for reading and writing. Creates a file if it does not yet exist.
# w and w+ truncates a file if it already exists

# a and a+ both are for appending to a file.
# a - the file must already exist
# a+ - opens file for reading and writing. creates file if non-existant. appends to end if you write

# ----------------------------------------------------------------------------------------------

# writing to a file
set file_object [open "file.txt" a]

# puts command is used to write to an open file
# notice how I had to escape out the [] brackets below even in a quoted string
puts $file_object "using file_object returned from \[open filename\] use puts command"

close $file_object

# cats the current content of the file after we've appended to it
set catvar [exec cat file.txt]

puts $catvar


# reading a file

set file_object [open "file.txt" w+]
puts $file_object "this is what I've wrote to this file"
close $file_object

# get file object from return of open command with r access mode
set file_object [open "file.txt" r]

# create a variable and set it to the return of read command on file_object
set file_data [read $file_object]

# print the data from the file object
puts "This is the file data: $file_data"

# to close a file use the 'close' keyword with the filename as its arguement
















