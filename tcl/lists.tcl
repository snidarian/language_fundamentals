#!/usr/bin/tclsh



# Create a list using {} or ""

set list_braces {item1 item2 item3 item4 item5 item6}
set list_quotes "item1 item2 item3 item4 item5 item6"


# access list items with the lindex command
# index values start at zero like in other languages
puts [lindex $list_braces 2]; # accesses list-item 3

puts [lindex $list_quotes 5]; # accesses list-item 6













