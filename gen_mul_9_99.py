import random

latex_header = r"""\documentclass[12pt,letterpaper, onecolumn]{exam}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[lmargin=71pt, tmargin=1.2in]{geometry}  %For centering solution box
\usepackage{setspace}
\usepackage{xcolor}% http://ctan.org/pkg/xcolor
\usepackage{xlop}% http://ctan.org/pkg/xlop

% \chead{\hline} % Un-comment to draw line below header
\thispagestyle{empty}   %For removing header/footer from page 1

\begin{document}

\doublespacing
\setlength{\parindent}{0pt}"""

latex_tailer = r"""\end{document}"""

mul_history = []

def pick_mul_numbers():
    a = random.randint(2, 99)
    b = random.randint(2, 9)
    enc = a * 10000 + b
    while enc in mul_history:
        a = random.randint(2, 99)
        b = random.randint(2, 9)
        enc = a * 10000 + b
    mul_history.append(enc)
    return a, b

def generate_page(op):
    page = ""
    items_per_row = 8
    for i in range(6):
        for j in range(items_per_row):
            a, b = pick_mul_numbers()
            page += f"\op{op}[resultstyle=\color{{white}},carrystyle=\color{{white}}]{{{a}}}{{{b}}}\quad\quad"
            if j < items_per_row - 1:
                page += "\n"
            else:
                page += "\\\\\\\\\n\n"
    return page

with open("practice.tex", "w+") as f:
    f.write(f"{latex_header}\n")
    for _ in range(4):
            f.write(f'{generate_page("mul")}\n')
    f.write(f"{latex_tailer}\n")