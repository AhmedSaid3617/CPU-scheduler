# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CPU Scheduler Simulator'
copyright = '2025, Shams El-Din Mohamed, Ahmed Saeed'
author = 'Shams El-Din Mohamed, Ahmed Saeed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# LaTeX-specific settings
latex_engine = 'pdflatex'  # Use pdflatex for PDF generation
latex_elements = {
    'papersize': 'a4paper',  # Or 'letterpaper' for US standard
    'pointsize': '11pt',     # Font size
    'geometry': r'\usepackage{geometry}\geometry{margin=1in}',  # Margins
    'preamble': r'''
        \usepackage{titling}  % Better title control
        \usepackage{tocloft}  % Customize TOC
        \setlength{\cftsecnumdepth}{2}  % Number sections in TOC
        \setlength{\cftsubsecnumdepth}{1}  % Number subsections
    ''',
    'maketitle': r'''
        \begin{titlepage}
            \centering
            \vspace*{2cm}
            {\Huge \textbf{\thetitle}} \\[1cm]
            {\Large \theauthor} \\[0.5cm]
            {\large School Code: CS1234} \\[0.5cm]
            {\large Spring 2025} \\
            \vfill
            {\large Instructor: Dr. Jane Doe}
        \end{titlepage}
    ''',
    'tableofcontents': r'\tableofcontents\newpage',  # TOC on its own page
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
