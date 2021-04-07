#!/usr/bin/env wish



grid [label .label0 -text "widget text" -textvariable var0 -background grey -relief ridge -borderwidth 5 -width 40 -foreground orange]
grid [text .text0 -width 30 -height 15 -relief ridge -borderwidth 5 -background grey -foreground orange -padx 5]
.text0 insert 1.0 "Example text\nThis is a body of example text"
grid [entry .entry0 -text "Entry widget" -relief ridge -borderwidth 10]
grid [message .message0 -background grey -foreground orange -text "message text" -padx 5 -width 100]
grid [button .button0 -text "Button text" -command "set var0 \"button 1 clicked\""]














