#!/usr/bin/env wish




grid [label .labelName -text "Click button to generate event." -textvariable var0 -background grey -foreground orange -height 10 -width 35 -relief ridge -borderwidth 5]

grid [button .button1 -text "Button 1" -font {Helvetica -12 bold} -height 3 -command "set var0 \"mark 1\"" -background green -foreground red -relief ridge -borderwidth 5 -width 35]

grid [button .button2 -text "Button 2" -font {Helvetica -12 bold} -height 3 -command "set var0 \"mark 2\"" -background blue -foreground yellow -relief ridge -borderwidth 5 -width 35]

grid [button .reset -text "Reset" -font {Helvetica -12 bold} -height 5 -command "set var0 \"Click button to generate event.\"" -background grey -foreground orange -relief ridge -borderwidth 5 -width 35]









