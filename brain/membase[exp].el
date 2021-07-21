;; https://github.com/alk/elisp-regex-dsl
(require 'regex-dsl)
;;; http://cvs.savannah.gnu.org/viewvc/*checkout*/emacs/lisp/json.el?root=emacs
(require 'json)

(setq *alk-membase-default-host* "Administrator:asdasd@lh:9000")
(setq *alk-membase-host-split-re* (redsl-to-regexp '(concat (line-begin)
                                                            (\? (concat (cap-group (literal ".*?"))
                                                                        (\? (concat ":" (cap-group (literal ".*?"))))
                                                                        "@"))
                                                            (cap-group (literal ".*?"))
                                                            (\? (concat ":" (cap-group (+ (char-set "0-9")))))
                                                            (line-end))))

;; (save-match-data
;;   (let ((*alk-membase-default-host* "aasd@asd:11"))
;;     (string-match *alk-membase-host-split-re* *alk-membase-default-host*)
;;     (list (match-string 1 *alk-membase-default-host*)
;;           (match-string 2 *alk-membase-default-host*)
;;           (match-string 3 *alk-membase-default-host*))))

(defun alk-membase-read-host ()
  (let ((value (read-from-minibuffer (concat "host (" *alk-membase-default-host* "): ") nil nil nil nil *alk-membase-default-host*))
        (username "Administrator")
        (password "adsasd"))
    (when (equal value "")
      (setq value *alk-membase-default-host*))
    value
    (save-match-data
      (string-match *alk-membase-host-split-re* value)
      (let ((username (or (match-string 1 value) username))
            (password (or (match-string 2 value) password))
            (host (match-string 3 value))
            (port (or (match-string 4 value) "8091")))
        (list username password host port)))))

;; (alk-membase-read-host)

(defun alk-with-output-in-buffer (fun &rest call-process-args)
  (with-temp-buffer
    (let ((status (apply #'call-process
                         (car call-process-args)
                         ""
                         (list (current-buffer) nil)
                         nil
                         (cdr call-process-args))))
      (if (eql status 0)
          (funcall fun)
        (message "%s exited with status %d" (car call-process-args) status)
        nil))))

;; (alk-with-output-in-buffer #'(lambda () (buffer-string)) "wget" "-O-" "-q" "--user=Administrator" "--password=asdasd" "http://lh:9000/pools/default")

(defun alk-membase-grab-node-and-cookie (username password host port)
  ;; (message "grabbing cookie from: %S\n" (list username password host port))
  (let* ((json (alk-with-output-in-buffer #'(lambda ()
                                              ;; (message "raw output: %S\n" (buffer-string))
                                              (beginning-of-buffer)
                                              (json-read))
                                          "wget" "-O-" "-q"
                                          (concat "--header=Authorization: Basic "
                                                  (base64-encode-string (concat username ":" password)))
                                          (concat "http://" host ":" port "/pools/default")))
         (nodes (assoc 'nodes json))
         (first-node (elt (cdr nodes) 0))
         (cookie (cdr (assoc 'otpCookie first-node)))
         (otp-node (cdr (assoc 'otpNode first-node))))
    (message "cookie and node: %S\n" (list cookie otp-node))
    (list otp-node cookie)))

(defun alk-membase-setup-distel (username password host port)
  (interactive (alk-membase-read-host))
  (let* ((rv (alk-membase-grab-node-and-cookie username password host port))
         (otp-node (car rv))
         (otp-cookie (cadr rv)))
    (message "cookie and node: %S\n" (list otp-cookie otp-node))
    (setq derl-cookie otp-cookie)
    (setq erl-nodename-cache (intern otp-node))
    (setq distel-modeline-node otp-node)
    (force-mode-line-update)))

;; (call-interactively 'alk-membase-setup-distel)

(defun alk-membase-shell (username password host port)
  (interactive (alk-membase-read-host))
  (let* ((rv (alk-membase-grab-node-and-cookie username password host port))
         (otp-node (car rv))
         (otp-cookie (cadr rv)))
    (message "cookie and node: %S\n" (list otp-cookie otp-node))
    (unless (and otp-node otp-cookie)
      (error "Failed to grap node name and cookie"))
    (let ((inferior-erlang-machine-options `("-setcookie" ,otp-cookie
                                             "-name" "membasectl@127.0.0.1" "-hidden"
                                             ,@inferior-erlang-machine-options)))
      (run-erlang)
      (let ((proc (get-buffer-process (current-buffer))))
        (comint-send-string proc (format "net_kernel:set_net_ticktime(rpc:call('%s', net_kernel, get_net_ticktime, [])).\n" otp-node))
        (sleep-for 0.1)
        (comint-send-string proc "")
        (sleep-for 0.1)
        (comint-send-string proc (concat "r '" otp-node "'\n"))
        (sleep-for 0.1)
        (comint-send-string proc (concat "c 2\n"))))))
