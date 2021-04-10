#!/usr/bin/tclsh

# below its not actually necessary to use quotation marks


set switchvar "string2"

switch $switchvar {
    "string0" {
	puts "it's string0"
    }
    "string1" {
	puts "it's sting1"
    }
    "string2" {
	puts "it's string2"
    }
    default {
	puts "none of the strings matched"
    }
}

