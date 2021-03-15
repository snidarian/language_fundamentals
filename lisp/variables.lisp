#!/usr/bin/clisp
;;;; A lisp program demonstrating the basic use of variables



(defun add_variables() "this function adds a and b together"       
       (defvar a 50)
       (setq b 100)
       (print (+ a b))
       (terpri))




(defun print_strings(string_a string_b) "This function prints string a and string b"
       (write-line "the following is string a: ")
       (print string_a)
       (terpri)
       (write-line "The following is string b: ")
       (print string_b))




(add_variables)

(print_strings "hello" "how's it going?")






