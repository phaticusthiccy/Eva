;;; The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
;;; The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
;;; Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
;;; All such material is used with the permission of the owner.
;;; All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
;;; All Rights Reserved.


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
