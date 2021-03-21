#!/usr/bin/clisp
;;;; type-of builtin function allows you to return the data type of a given variable (or struct if you used defstruct)

;; string
(defvar a "stringy McString")
;; single float
(defvar b 45.25)
;; integer
(defvar c 72)
;; symbol
(defvar d 'symbol)
;; NULL - basically a symbolic constant for false or nothing
(defvar e nil)

(print (type-of a))
(print (type-of b))
(print (type-of c))
(print (type-of d))
(print (type-of e))

(setq x 10)
(setq y 34842398.28)
(setq ch nil)
(setq n 123.59)
(setq bg 11.0e+4)
(setq r 124/2)

(print (type-of x))
(print (type-of y))
(print (type-of ch))
(print (type-of n))
(print (type-of bg))
(print (type-of r))


