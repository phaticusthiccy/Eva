;;; The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
;;; The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
;;; Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
;;; All such material is used with the permission of the owner.
;;; All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
;;; All Rights Reserved.

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
