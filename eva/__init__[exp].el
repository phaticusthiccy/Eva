
;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(defconst jem-version "1.0.5" "Jem version")
(defconst jem-emacs-min-version "24.3" "Minimum required Emacs version")
(defconst jem-start-time (current-time))

(defconst jem-load-paths '("jem"
                           "jem/libs"
                           "third-party"
                           "third-party/use-package"))

(if (version<= emacs-version jem-emacs-min-version)
    (message (concat "jem> Jem requires Emacs >= %s. "
                     "Your current Emacs version is %s.")
             jem-emacs-min-version emacs-version)

  (set-default-font "Operator Mono XLight 12")

  (eval-and-compile
    (mapc #'(lambda (path)
              (add-to-list 'load-path
                           (expand-file-name path user-emacs-directory)))
          jem-load-paths))
  (add-to-list 'custom-theme-load-path (expand-file-name "third-party/themes"
                                                         user-emacs-directory))

  (require 'jem-lib)
  (jem-init)
  (load-theme 'zenburn t))
