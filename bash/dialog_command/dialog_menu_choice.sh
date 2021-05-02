#!/usr/bin/bash


# store the result of the menu-choice in a variable and specify --stoud double flag
choice=$(dialog --stdout --menu ".bashrc or .zshrc?" 10 30 2 bash .bashrc zsh .zshrc)


# exit code
echo "$?"
# the choice should show here
echo "$choice"







