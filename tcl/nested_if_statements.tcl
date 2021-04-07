#!/usr/bin/tclsh

# like in all other programming languages, you can nest if statements in tcl
# one important syntax theme to keep in mind using control-flow in tcl is 'curly bracket placement'



set a 10
set b 20
set c 30
set d 40
set e 50


if { $a == 10 } {
    puts "1st"
    if { $b == 20 } {
	puts "2nd"
	if { $c == 30 } {
	    puts "3rd"
	    if { $d == 40 } {
		puts "4th"
		if { $e == 50 } {
		    puts "5th"
		}
	    }
	}
    }
}
















