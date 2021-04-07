#!/usr/bin/tclsh

# interesting points of departure from other languages
# 1. The conditional statements are houses in curly brackets
# 2. the opening curly brace of the block statement MUST remain on the same line as the 'if' keyword
# 3. else statement must begin after closing curly brace of 'if' statement block


set a 77



if { $a < 50 } {
    puts "a < 50"
} elseif { $a < 75 } {
    puts "a < 75"
} elseif { $a == 76 } {
    puts "a == 76"
} elseif { $a > 76 && $a < 78 } {
    puts "a is more than 76 and less than 78"
} elseif { $a > 79 || $a > 80 } {
    puts "a is more than 79 or more than 80"
} else {
    puts "else statement block runs"
}






