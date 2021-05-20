#!/usr/bin/bash
# Getting opt strings is an important part of any sophisticated multiuse/versatile bash script
# in emacs you can create a getopts skeleton structure with 'C-c C-o'
# Emacs does really make using getops very very easy, i recommend it.

# options that are to be followed by a colon ':' are expected to have an argument and the arguments value will be initialized to $name variable

# A colon begins the list of possible flag option arguments
# place a colon after each flag argument that is in turn to have it's on argument.

while getopts :uelf: OPT; do
    case $OPT in
	u|+u)
	    echo "arguement: $OPT"
	    ;;
	e|+e)
	    echo "arguement: $OPT"	    
	    ;;
	l|+l)
	    echo "arguement: $OPT"	    
	    ;;
	f|+f)
	    echo "file named: $OPTARG"
	    ;;
	*)
	    echo "usage: ${0##*/} [+-uelf ARG} [--] ARGS..."
	    exit 2
    esac
done
shift $(( OPTIND - 1 ))
OPTIND=1







