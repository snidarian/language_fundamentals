#!/usr/bin/bash                                                                  



dialog --title "Confirmation" --yesno "Are you sure?" 10 40

var=$?

echo "exit code = $var"

# the exit code value is used to determined which option was selected by the user.
if [ $var -eq 0 ]; then
    echo "you said yes"
else
    echo "you said no"
fi


