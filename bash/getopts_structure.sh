#!/usr/bin/bash
# Getting opt strings is an important part of any sophisticated multiuse/versatile bash script
# in emacs you can create a getopts skeleton structure with 'C-c C-o'


while getopts :uertloEF OPT; do
    case $OPT in
	u|+u)
	    echo "argument chosen: u"
	    ;;
	e|+e)
	    echo "argument chosen: e"	    
	    ;;
	r|+r)
	    echo "argument chosen: r"	    
	    ;;
	t|+t)
	    echo "argument chosen: t"	    
	    ;;
	l|+l)
	    echo "argument chosen: l"	    
	    ;;
	o|+o)
	    echo "argument chosen: o"	    
	    ;;
	E|+E)
	    echo "argument chosen: E"	    
	    ;;
	F|+F)
	    echo "argument chosen: F"	    
	    ;;
	*)
	    echo "usage: ${0##*/} [+-uertloEF} [--] ARGS..."
	    exit 2
    esac
done
shift $(( OPTIND - 1 ))
OPTIND=1







