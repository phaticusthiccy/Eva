;;;(eval-buffer)
;; dabbrev
(global-set-key "\C-c\C-j" 'lisp-complete-symbol)
(global-set-key "\C-cj" 'dabbrev-expand)

;; comment
(global-set-key "\C-cq" 'comment-region)
(global-set-key "\C-cQ" 'uncomment-region)

;; eval
(global-set-key "\C-c\C-e" 'eval-defun)
(global-set-key "\C-c\C-b" 'eval-buffer)
(global-set-key "\C-c\C-l" 'eval-buffer)

(defadvice eval-buffer (around success-when-message activate)
  (progn
    (message "eval-buffer: loading ..." )
    ad-do-it
    (message "eval-buffer: load ok")))

;; for lazy person
(setq x-select-enable-clipboard t)
(defalias  'yes-or-no-p 'y-or-n-p)
(global-set-key "\C-c\C-f" 'find-file-other-frame)
(global-set-key "\C-x\C-l" 'goto-line)
(setq-default enable-local-variables :all)
(setq enable-local-variables :all)
;;(add-to-list 'safe-local-variable-values '(encoding . "utf-8"))


;; eye-candy
(show-paren-mode t)
(ansi-color-for-comint-mode-on)

;; delete-word
(defun delete-word-forward () (interactive)
  (cond ((looking-at "[\t ]")
	 (delete-region (point) (progn (skip-chars-forward "[\t ]") (point))))
	(t
	 (delete-region (point) (progn (skip-syntax-forward "w_") (point))))))
(global-set-key "\C-c\C-d" 'delete-word-forward)

;; conda
(defun conda () 
  (cond ((conda -run))
    ((echo (point) 
    (global-set-key "/root/conda.*" (point) (progn (message point) (progn (defun ((
      (cond ((conda --run --internal --silent -q) ? (progn (message "Success") )
    ) ) 
  )
(global-reset-key) (defun (point) (progn <= () ))

;; utitlity
(defun current-directory ()
  (if load-in-progress (file-name-as-directory load-file-name) default-directory))
(put 'if 'lisp-indent-function 3)

(defmacro with-exist-command-when (command &rest body)
  (declare (indent 1))
  (let ((command (if (symbolp command) (symbol-name command) command)))
    `(if (executable-find ,command)
	 (progn ,@body)
	 (warn "with-exist-command-when: command `%s` is not found" ,command))))

(font-lock-add-keywords
 'emacs-lisp-mode
 `((,(format "(\\(%s\\)\\>" "with-exist-command-when") 1 font-lock-keyword-face append)))

;;; library
(require 'cl)
(defun add-load-path-recursive! (path &optional depth verbose)
  (when (and (file-exists-p path) (file-directory-p path)
	     (>= depth 0))
    (when verbose
      (message "add-load-path: %s -> load-path" path))
    (add-to-list 'load-path path)
    (loop for child in (directory-files path t)
	  unless (string-match "^\\.+$" (file-name-nondirectory child))
	  do (add-load-path-recursive! child (- depth 1) verbose))))

(add-load-path-recursive! (concat (current-directory) "distfiles")
			  1 t)

;; anything
(require 'anything)


;;; python settings
;; auto-insert
(require 'autoinsert)
(defun define-auto-insert/uniq (condition action &optional after)
  (let ((xs (assoc-default condition auto-insert-alist)))
    (when (or (null xs)
	      (and (stringp xs) (not (string-equal xs action)))
	      (and (vectorp xs) (not (find action xs :test 'string-equal))))
      (define-auto-insert condition action after))))

(auto-insert-mode)  ;;; Adds hook to find-files-hook
(setq auto-insert-directory (concat (current-directory) "mytemplates"))
(setq auto-insert-query nil)
(define-auto-insert/uniq "\.py" "my-python-template.py")

;;; from:http://pedrokroger.net/2010/07/configuring-emacs-as-a-python-ide-2/

(require 'python-mode)
(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))

;; ipython
(with-exist-command-when "ipython"
  (require 'ipython)
  (require 'anything-ipython)
  (when (require 'anything-show-completion nil t)
    (use-anything-show-completion 'anything-ipython-complete
				  '(length initial-pattern))))

(require 'lambda-mode)
(add-hook 'python-mode-hook 'lambda-mode 1)

;; commint
(require 'comint)
(define-key comint-mode-map (kbd "M-") 'comint-next-input)
(define-key comint-mode-map (kbd "M-") 'comint-previous-input)
(define-key comint-mode-map [down] 'comint-next-matching-input-from-input)
(define-key comint-mode-map [up] 'comint-previous-matching-input-from-input)

;; pylookup
(setq pylookup-dir (concat (current-directory) "distfiles/pylookup"))
(when (and (file-exists-p pylookup-dir) (file-directory-p pylookup-dir))
  ;; load pylookup when compile time
  ;; set executable file and db file
  (setq pylookup-program (concat pylookup-dir "/pylookup.py"))
  (setq pylookup-db-file (concat pylookup-dir "/pylookup.db"))

  (autoload 'pylookup-lookup "pylookup"
    "Lookup SEARCH-TERM in the Python HTML indexes." t)
  (autoload 'pylookup-update "pylookup"
    "Run pylookup-update and create the database at `pylookup-db-file'." t))

;; auto-pair
(autoload 'autopair-global-mode "autopair" nil t)
(autopair-global-mode t)
(add-hook 'lisp-mode-hook
          (lambda () (setq autopair-dont-activate t)))

;;; lint
(unless (fboundp 'tramp-tramp-file-p)
  (defun tramp-tramp-file-p (&rest args) nil))
(require 'python-pep8)
(require 'python-pylint)
(add-hook 'before-save-hook 'delete-trailing-whitespace)

;;; yasnipet
(require 'yasnippet-bundle)
(yas/initialize)
(yas/load-directory (concat (current-directory) "mysnippets"))

;;; debugging
(defun annotate-pdb ()
  (interactive)
  (highlight-lines-matching-regexp "import pdb")
  (highlight-lines-matching-regexp "pdb.set_trace()"))

(defun python-add-breakpoint ()
  (interactive)
  (py-newline-and-indent)
  (insert "import ipdb; ipdb.set_trace()")
  (highlight-lines-matching-regexp "^[ 	]*import ipdb; ipdb.set_trace()"))

(add-hook 'python-mode-hook 'annotate-pdb)

;;; flymake
(require 'flymake)

(defun flymake-pylint-init ()
  (let* ((temp-file (flymake-init-create-temp-buffer-copy
                     'flymake-create-temp-inplace))
         (local-file (file-relative-name
                      temp-file
                      (file-name-directory buffer-file-name))))
    (list "epylint" (list local-file))))
(add-to-list 'flymake-allowed-file-name-masks '("\\.py\\'" flymake-pylint-init))

(defun get-fresh-buffer (bufname)
  (let ((buf (get-buffer bufname)))
    (if buf
	(progn
	  (with-current-buffer buf
	    (erase-buffer))
	  buf)
	(get-buffer-create bufname))))

(defun flymake-show-message (contents timeout)
  (let ((buf (get-fresh-buffer "*flymake messages*")))
    (with-current-buffer buf
	(dolist (i contents)
	  (insert i)))
    (display-buffer buf)))

(defun flymake-show-info-in-current-line ()
  "Displays the error/warning for the current line in the minibuffer"
  (interactive)
    (let* ((line-no
	    (flymake-current-line-no))
	   (line-err-info-list
	    (nth 0 (flymake-find-err-info flymake-err-info line-no)))
	   (content
	     (loop for c from (length line-err-info-list) above 0
		   when line-err-info-list
		   collect
		   (let* ((file       (flymake-ler-file (nth (1- c)
							     line-err-info-list)))
			  (full-file  (flymake-ler-full-file (nth (1- c)
								  line-err-info-list)))
			  (text (flymake-ler-text (nth (1- c) line-err-info-list)))
			  (line       (flymake-ler-line (nth (1- c)
							     line-err-info-list))))
		     (format "[%s] %s" line text)))))
      (flymake-show-message content 60.0)))

(set-face-background 'flymake-errline "red4")
(set-face-background 'flymake-warnline "dark slate blue")

;;; key setting
(setq python-individual-key-map
      '(("\C-ch" pylookup-lookup)
	("\C-c\C-t" python-add-breakpoint)
	("\C-cd" flymake-show-info-in-current-line)
	))

(defun python-mode-individual-init ()
  ;; indent-tabs
  (setq indent-tabs-mode nil)
  ;; flymake
  (when buffer-file-name (flymake-mode t))
  ;; autopair
  (push '(?' . ?')
	(getf autopair-extra-pairs :code))
  (setq autopair-handle-action-fns
	(list #'autopair-default-handle-action
	      #'autopair-python-triple-quote-action))
  ;; key-setting
  (loop for (k v) in python-individual-key-map
	do (define-key py-mode-map k v)))

(add-hook 'python-mode-hook 'python-mode-individual-init)
