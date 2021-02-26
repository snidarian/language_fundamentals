#! /usr/bin/clisp
;;;; Illustrating the do construct


;; The initial values of each variable is evaluated and bound to the respective variable.
;;The updated value in each clause corresponds to an optional update statement that specifies how the values of the variables will be updated with each iteration.

;;After each iteration, the test is evaluated, and if it returns a non-nil or true, the return-value is evaluated and returned.

;;The last s-expression(s) is optional. If present, they are executed after every iteration, until the test value returns true.


(do ((x 0 (+ 2 x))
   (y 20 ( - y 2)))
   ((= x y)(- x y))
   (format t "~% x = ~d  y = ~d" x y)
)















