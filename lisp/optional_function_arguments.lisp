#!/usr/bin/clisp
;;;; use of optional arguments in lisp functions


;; use the '&optional' symbol to denote all following args as optional args

(defun list_available(a b &optional c d) "demonstrates use of"
       (write (list a b c d)))

(terpri)



(write-line "Calling with all four args")
(list_available 1 2 3 4)


(terpri)


;; when you call the above function with only two args, the remaining values are null.
(write-line "Calling with only two args")
(list_available 1 2)




;; Now i'm goint to create a less-than-practical example that uses optional arguments

(defun average_numbers(a b &optional c d e f g h i j k) "Averages a list of numbers"
       (defvar list0 (list a b c d e f g h i j k))
       (terpri)
       (format t "list0 contains the items: ~a ~%" list0)
       (defvar count0 (list-length list0))
       (format t "There are ~d items in the list~%" count0))


(average_numbers 13 15 16 17 20 21)























