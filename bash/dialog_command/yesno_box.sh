#!/usr/bin/bash                                                                  



dialog --title "Confirmation" --yesno "Are you sure?" 10 40

# variable set equal to exit status of dialog command
var=$?

echo "exit code = $var"

# clear the gui after its usefulness elapses
clear


# the exit code value is used to determine which option was selected by the user.
if [ $var -eq 0 ]; then
    echo "you said yes"
else
    echo "you said no"
fi

# sleep to show the feedback was recieved and noted
sleep 2

clear
