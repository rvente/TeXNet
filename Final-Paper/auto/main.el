(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "english") ("csquotes" "autostyle") ("biblatex" "backend=biber" "style=alphabetic" "citestyle=authoryear")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "lmodern"
    "amssymb"
    "amsmath"
    "longtable"
    "booktabs"
    "comment"
    "pdfpages"
    "inputenc"
    "babel"
    "csquotes"
    "biblatex")
   (TeX-add-symbols
    "KaTeX"
    "TeXNet")
   (LaTeX-add-bibliographies))
 :latex)

