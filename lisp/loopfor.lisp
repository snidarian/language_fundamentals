#! /usr/bin/clisp


(defvar a (list 1 2 3 4 5 6 7 8 9 10))


;; looping through the items in a list
(loop for loopvar in a
      do (print loopvar))

(terpri)

;; looping through symbolic values
(loop for x in '(black green white red orange blue)
      do (format t "~s, " x))

(terpri)

;; looping through an integer range
(loop for x from 15 to 20
      do (print x))

(terpri)

;; looping through an integer range and only printing odd numbers
;; if can also be written thusly 'if(condition)' as a side-note

(loop for x from 1 to 20
      do (if (oddp x) (print x)))

(terpri)
