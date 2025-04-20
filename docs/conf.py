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
    'pointsize': '11pt',  # Font size
    'geometry': r'\usepackage{geometry}\geometry{margin=1in}',  # Margins
    'preamble': r'''
        \usepackage{times}  % Use Times font (or comment out for Computer Modern)
        \usepackage{tocloft}  % For table of contents customization
        \cftsetindents{section}{1em}{2em}  % Adjust TOC indentation
        \cftsetindents{subsection}{3em}{3em}

        \usepackage{booktabs}  % for better looking tables
\usepackage{array}     % for extended column formatting
\usepackage{geometry}  % optional: to control page margins

\newcommand{\teamtable}{%
    \begin{titlepage}
        \centering
        \vspace*{2cm}
        {\sffamily
        {\Large\bfseries Team Members \par}
        \vspace{1.5cm}
        \renewcommand{\arraystretch}{1.4}  % More vertical space between rows
        \setlength{\tabcolsep}{12pt}       % More horizontal padding in cells
        \begin{tabular}{>{\raggedright\arraybackslash}p{7cm} >{\centering\arraybackslash}p{5cm}}
            \toprule
            \textbf{Name} & \textbf{ID -- Section} \\
            \midrule
            Shams El-Din Mohamed Abdel-Monem & 2101442 -- S3 \\
            Ahmed Said Sayed & 2101546 -- S3 \\
            Abdelrahman Sherif Hassan & 2100735 -- S3 \\
            Mahmoud Essam Noureldin & 2001393 -- S2 \\
            Yousef Mahmoud Mohamed & 2100994 -- S3 \\
            Mohamed Hussien Mansour Sayed & 2100919 -- S4 \\
            Omar Tamer Mohamed & 2100528 -- S3 \\
            Youssof Waleed Fathi & 2101734 -- S3 \\
            Fares Khalaf Salman Sultan & 2101371 -- S3 \\
            Kareem Gaber El Halaby & 2101545 -- S3 \\
            \bottomrule
        \end{tabular}
        }
        \vfill
    \end{titlepage}
}

    ''',
    # Remove extra Sphinx styling
    'sphinxsetup': '',
    # Ensure table of contents is included
    'tableofcontents': r'\teamtable\tableofcontents\newpage',
}

latex_theme = 'howto'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
