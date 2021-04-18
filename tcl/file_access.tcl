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






# a call to open returns a file indentifier
set file_identifier [open file.txt]

puts "$file_identifier"



