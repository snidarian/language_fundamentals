#!/usr/bin/clisp
;;;; How to define macros in LISP

;;; a macro is a function that takes an s-expression as arguments and returns a LISP form, which is then evaluated

;;; VERY IMPORTANT - in LISP no return statements are needed in functions or macros. The last statement in a macro or function is implicitly the return statement


;; ---------------------STRUCTURE---------------------------------
;; Structure of defining a macro
(defmacro macro-name (parameter-list)
"Optional documentation string."
(write-line "this is the body of the macro"))


;; ----------------------------------------------------------------
;; first example macro
(defmacro square(num)
  "Squares number provided as argument"
  (* num num))

(defvar x 30)

(print (type-of x))

;; execution - pass by value not by reference.
(print (square 15))

(terpri)

;; ----------------------------------------------------------------
;; second example macro
(defmacro twice(string)
  "prints given string arg twice"
  (format t "~a ~a ~%" string string))

;; execution
(twice "rainbow 6")


;; ----------------------------------------------------------------
;; third example macro
(defmacro sub-ninety(number)
  "subtracts 90 from given arg"
  (- number 90))


;; execution
(format t "(190 - 90) = ~a ~%" (sub-ninety 190))


;; ----------------------------------------------------------------
;; fourth example macro
(defmacro say-whatup(name)
  "Says whatup to given name argument"
  (format t "Hey whatup, ~a. ~%" name))

;; execution
(say-whatup "jerdann")

;; ----------------------------------------------------------------
;; fifth example macro

(defmacro set-to-10(number)
  "Sets given argument to 10"
  (setq number 10))

;; execution
(format t "The number 50 set to ~a ~%" (set-to-10 50))


;; ----------------------------------------------------------------
;; sixth example macro

(defmacro add-3-nums(number1 number2 number3)
  "Adds three number arguments together"
  (defvar result 0)
  (+ result (+ number1 number2 number3)))

;; execution
(format t "4 + 14 + 7 = ~a ~%" (print (add-3-nums 4 14 7))) ;; print here is unecessary
