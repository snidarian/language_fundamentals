#!/usr/bin/tclsh


set a 45

while {$a < 72} {
    puts "a = $a"
    set a [expr $a + 1]
}

puts "loop is terminated. a now equals $a"
