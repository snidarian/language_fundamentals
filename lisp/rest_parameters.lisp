#!/usr/bin/clisp

;;;; REST PARAMETERS

;; Sometimes functions need to take an variable quantity of arguments.
;; You use rest parameters in a function using the '&rest' symbol.


;; The argument values stored in 'values' variable will be in the form of a list
(defun print_members (a b &rest values) "Displays the values in list0"
       (defvar list0 (list a b values))
       (print list0))



;;(print_members 1 2 3 4 5 6 7 8 9 10)


;; Now for a practical example..

;; The below function finds the average of the arguments provided to it

(defun get_average (&rest values) "Gets and returns average of all arguments values"
       (defvar integer-list values)
       (defvar total 0.0)
       (defvar count (list-length values))
       (format t "Argc = ~d" count)
       (defvar average 0.0)
       (loop for loopvar in values
	     do (setf total (+ total loopvar))
	     )
       (setf average (/ total count)))


;; Remember that in LISP the last line of a function is returned by default.
(print (get_average 5 5.74 6 7 5 5 5 5 172))





