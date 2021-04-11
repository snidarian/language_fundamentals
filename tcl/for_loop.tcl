#!/usr/bin/tclsh

# demonstrating the syntax of for loops in tcl


for {set a 1} {$a < 10} {incr a} {
    puts "a = $a";
}
