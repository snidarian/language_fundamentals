#!/usr/bin/tclsh


# A namespace is a container for setting identifiers that can be used to group variables and procedures.
# before namespaces there was single global scope; Now with namespaces, we have additional partitions of global scope.



namespace eval MyMath {
    # create a variable inside the namespace
    variable myResult
}


# create procedures in the namespace
proc MyMath::Add {a b } {
    set ::MyMath::myResult [expr $a + $b]
}

MyMath::Add 10 25


puts $::MyMath::myResult



# Nested namespaces
# tcl allows the nesting of namespaces.

namespace eval MyMath {
   # Create a variable inside the namespace
   variable myResult
}

namespace eval extendedMath {
   # Create a variable inside the namespace
   namespace eval MyMath {
      # Create a variable inside the namespace
      variable myResult
   }
}
set ::MyMath::myResult "test1"
puts $::MyMath::myResult
set ::extendedMath::MyMath::myResult "test2"
puts $::extendedMath::MyMath::myResult











