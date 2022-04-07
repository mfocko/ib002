(setq org-publish-project-alist
      '(("org"
         :base-directory "~/git/xfocko/ib002"
         :publishing-function org-html-publish-to-html
         :publishing-directory "~/git/xfocko/ib002"
         :recursive t
         :section-numbers nil
         :with-toc 2
         :html-head "<link rel=\"stylesheet\"
                  href=\"/css/org.css\" type=\"text/css\"/>"
         :html-preamble t
         :html-link-home "/"
         ))
      )
