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
    a = random.randint(10, 35)
    b = random.randint(1, min(a - 1, 50 - a))
    enc = a * 100 + b
    while enc in add_history:
        a = random.randint(10, 35)
        b = random.randint(1, min(a - 1, 50 - a))
        enc = a * 100 + b
    add_history.append(enc)
    return a, b

def pick_sub_numbers():
    a = random.randint(10, 50)
    while (a % 10 == 9):
        a = random.randint(10, 50)
    b = random.randint((a % 10) + 1, 9)
    enc = a * 100 + b
    while enc in sub_history:
        a = random.randint(10, 50)
        while (a % 10 == 9):
            a = random.randint(10, 50)
        b = random.randint((a % 10) + 1, 9)
        enc = a * 100 + b
    sub_history.append(enc)
    return a, b

def generate_page(op):
    page = ""
    for i in range(6):
        for j in range(9):
            if op == "sub":
                a, b = pick_sub_numbers()
            if op == "add":
                a, b = pick_add_numbers()
            print(a, b)
            page += f"\op{op}[resultstyle=\color{{white}},carrystyle=\color{{white}}]{{{a}}}{{{b}}}\quad\quad"
            if j < 8:
                page += "\n"
            else:
                page += "\\\\\n\n"
    return page

with open("practice.tex", "w+") as f:
    f.write(f"{latex_header}\n")
    for i in range(2):
        f.write(f'{generate_page("sub")}\n')
    f.write(f"{latex_tailer}\n")