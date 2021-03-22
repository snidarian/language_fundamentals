#!/usr/bin/clisp


;; load ltk wrapper library for tcl gui toolkit
(load "ltk")

;; Change into ltk package
(in-package :ltk)


;; function that defines the gui
(defun hello-1()
  (with-ltk ()
	    (let ((b (make-instance 'button
				    :master nil
				    :text "Click here"
				    :command (lambda ()
					       (format t "Hello, world. Button was pressed.~&")))))
	      (pack b))))




;; function call to hello world gui
(hello-1)








