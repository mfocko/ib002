(setq org-publish-project-alist
      '(("org"
         :base-directory "~/git/xfocko/ib002"
         :publishing-function org-html-publish-to-html
         :publishing-directory "~/git/xfocko/ib002"
         :recursive t
         :section-numbers nil
         :with-toc 2
         :html-preamble t

         ;; use for deployment
         :html-head "<link rel=\"stylesheet\"
                  href=\"https://fi.muni.cz/~xfocko/ib002/css/org.css\" type=\"text/css\"/>"
         :html-link-home "https://fi.muni.cz/~xfocko/ib002/"

         ;; use for local testing
         ;; :html-head "<link rel=\"stylesheet\"
         ;;          href=\"/css/org.css\" type=\"text/css\"/>"
         ;; :html-link-home "/"
         ))
      )
