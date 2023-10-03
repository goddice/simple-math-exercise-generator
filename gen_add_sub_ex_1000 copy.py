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

sub_history = []
add_history = []

def pick_add_numbers():
    a = random.randint(1, 999)
    b = random.randint(1, 999)
    enc = a * 10000 + b
    while enc in add_history:
        a = random.randint(1, 999)
        b = random.randint(1, 999)
        enc = a * 10000 + b
    add_history.append(enc)
    return a, b

def pick_sub_numbers():
    a = random.randint(10, 999)
    b = random.randint(1, a - 1)
    enc = a * 10000 + b
    while enc in sub_history:
        a = random.randint(10, 999)
        b = random.randint(1, a - 1)
        enc = a * 10000 + b
    sub_history.append(enc)
    return a, b

def generate_page(op):
    page = ""
    items_per_row = 7
    for i in range(6):
        for j in range(items_per_row):
            if op == "sub":
                a, b = pick_sub_numbers()
            if op == "add":
                a, b = pick_add_numbers()
            page += f"\op{op}[resultstyle=\color{{white}},carrystyle=\color{{white}}]{{{a}}}{{{b}}}\quad\quad"
            if j < items_per_row - 1:
                page += "\n"
            else:
                page += "\\\\\\\\\n\n"
    return page

with open("practice.tex", "w+") as f:
    f.write(f"{latex_header}\n")
    for _ in range(6):
            f.write(f'{generate_page("add")}\n')
            f.write(f'{generate_page("sub")}\n')
    f.write(f"{latex_tailer}\n")