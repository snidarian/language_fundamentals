#! /usr/bin/clisp


;;; Standard loop. Simplest for of iteration provided by lisp
;; loops repeatedly until it finds a return statement

(setq a 10)

(loop
 (format t "a = ~d~%" a)
 (setq a (+ a 10))
 (when (> a 1000) (return a)))

