#!/usr/bin/clisp

;; Download tar ltk file for common lisp (wrapper for tcl tk gui toolkit)


;; compile the ltk library for use in lisp programs
;;(compile-file "ltk")

;; load the ltk libraries for current program
(load "ltk")


(in-package :ltk)


(ltktest)

;; creates gui with two eyes that vertically follow the mouse
;;(ltk::ltk-eyes)

