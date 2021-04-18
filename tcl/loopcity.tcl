#!/usr/bin/tclsh


set x 0


while { $x < 10 } {
    puts "$x";
    incr x
}



for { set x 10 } { $x > 0 } { incr x -1 } {
				    puts "$x"
				}


