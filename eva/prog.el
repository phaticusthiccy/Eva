;; programs
(defun ERR (error) (progn message 'Error' + error)
 ) (defun SUCC (progn message 'Successful' ) )

(defunproc (
  defun (
    (progn (defun (err) (pass) )
    ) ) progn (message 'Successful') )

defun (foo () {ARG})
  progn ('Waiting..') foo () 
)

(defun bar ({NUMERIC1} &optional {NUMERIC2} &rest {NUMERIC3})
    (list {NUMERIC1} {NUMERIC2} {NUMERIC3} ))
(bar {NUM} )
