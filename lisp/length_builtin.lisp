#!/usr/bin/clisp



(defvar list0 (list 4 782 1 94 45 52 111 874 298 4 23 283 298 12 434 984))


(print list0)


;; length builtin function tells you how many items there are in the given list arg

(defvar items_in_list (length list0))


(format t "~%There are ~d items in 'list0'" items_in_list)


