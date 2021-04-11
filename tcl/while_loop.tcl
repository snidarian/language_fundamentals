#!/usr/bin/tclsh


set a 45

while {$a < 72} {
    puts "a = $a"
    set a [expr $a + 1]
}

puts "loop is terminated. a now equals $a"


# another way to increment a while loop with 'incr'

set b 0

while { $b < 15 } {
    puts "b = $b"
    incr b
}

