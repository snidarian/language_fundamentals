#! /usr/bin/clisp


(defvar a (read))

;;; (if (condition) (if condition True) (else condition))
(if (= a 15) (format t "~% a is 15") (format t "~% a is not 15"))

(if (= a 20) (format t "~% A is 20") (format t "~% a is not 20"))

(if (= a 30) (format t "~% a is 30") (format t "~% a is not 30"))

(if (= a 40) (format t "~% a is 40") (format t "~% a is not 40"))

(if (= a 50) (format t "~% a is 50") (format t "~% a is not 50"))

(if (= a 60) (format t "~% a is 60") (format t "~% a is not 60"))

(if (< a 100) (format t "~% a < 100") (format t "~% a > 100"))

(if (< a 1000) (format t "~% a < 1000") (format t "~% a > 1000"))


(format t "~% a = ~d" a)




