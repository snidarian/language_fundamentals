#!/usr/bin/env wish


# if -height and -width are not specified, they auto-calculated.
# setting -padx and -pady are sometimes prefereable


grid [label .labelName0 -background grey -foreground orange -text "This is a message describing some sort of important information\n that you need to regard based on a decision you just made in a tcl program" -pady 50 -padx 50 -relief ridge -borderwidth 8 -font {Helvetica -12 bold} -height 10 -justify center -textvariable var0]

#set var0 "test hello"


# The text to put in a label can be inserted into a variable like so:
set var1 "Example message notificaion. Watch out for _____ and _____ when _____ing"



# for some reason the below widget displays inside of the above widget. Not sure why but I'll learn
grid [label .labelName1 -textvariable var1 -borderwidth 10 -relief ridge]













