# PROJECT_INSTRUCTIONS.md
# LaTeX Exam Summary — General Guide

This file defines the structure, style rules, and workflow for producing
a LaTeX exam summary for any university course. Follow it exactly when
generating each `.tex` file so the whole document stays consistent.

---

## 1. Project Structure

```
project/
├── main.tex                  # Master file — inputs all lecture/part files
├── PROJECT_INSTRUCTIONS.md   # This file
├── images/
│   └── slides/
│       ├── lecture_1/        # slide_001.png, slide_007.png, ...
│       ├── lecture_2/
│       └── ...
├── lecture1_notes.tex
├── lecture2_notes.tex
└── ...
```

- One `.tex` file per lecture or thematic block.
- All files are `\input{}`-ed from `main.tex`; they contain **no preamble**.
- Images live under `images/slides/lecture_X/` and are named `slide_NNN.png`
  where `NNN` is the **zero-padded PDF page index** (not the printed slide number).

---

## 2. main.tex Template

```latex
\documentclass{article}
\usepackage[english]{babel}
\usepackage[utf8x]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage[colorlinks=true, allcolors=black]{hyperref}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{xcolor}
\usepackage{roboto}
\usepackage{float}
\usepackage{titling}
\usepackage{blindtext}
\usepackage{titlesec}
\usepackage[square,sort,comma,numbers]{natbib}
\usepackage{tikz}
\usepackage{geometry}
\usepackage{sectsty}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{listings}
\usepackage{multicol}
\usepackage{wrapfig}
\usepackage{enumitem}
\usepackage{ragged2e}
\usepackage{changepage}
\usepackage{siunitx}

\definecolor{tudelftdarkblue}{RGB}{12,35,64}
\definecolor{tudelftcyan}{RGB}{0,166,214}
\definecolor{tudelftblue}{RGB}{0,118,194}

\geometry{a4paper, margin=2cm}
\allsectionsfont{\color{black}}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\sectionfont{\fontfamily{RobotoSlab-TLF}\selectfont}
\setlength\parindent{0pt}
\usepackage{setspace}

\begin{document}
\thispagestyle{empty}
\newpage
\setcounter{page}{1}

\input{lecture1_notes}
\newpage
\input{lecture2_notes}
% add further lectures here

\end{document}
```

---

## 3. Individual Lecture File — Style Rules

### 3.1 Header

Every file starts with a `\section` stating the lecture number and topic.
Follow it immediately with a short introductory paragraph (2–4 sentences)
that names the key concepts covered and, for oral exams, flags which
topics are especially likely to be examined.

```latex
\section{Lecture 3 -- Topic Name Here}

These notes cover ... (brief scope sentence). The key concepts are
X, Y, and Z. % For oral exams: flag high-priority topics here.
```

### 3.2 Subsections

Use `\subsection*{}` for major topics and `\subsubsection*{}` for
sub-topics. Always use the starred form (no numbering).

```latex
\subsection*{Topic Name}

\subsubsection*{Sub-topic Name}
```

### 3.3 Paragraph breaks

Separate paragraphs with `\\` followed by **two blank lines**:

```latex
First paragraph text ends here.\\


Second paragraph starts here.
```

Do **not** use `\par`, `\vspace`, or empty lines alone.

### 3.4 Equations

Use `equation` for single equations and `align` for multi-line derivations.
Box key final results with `\boxed{}`. Use `\emph{}` for first introduction
of a term.

```latex
The governing relation is
\begin{equation}
    \boxed{K = M_\infty \tau.}
\end{equation}

For multi-line derivations:
\begin{align}
    A &= B + C, \\
    D &= E.
\end{align}
```

### 3.5 Figures (slide images)

Include only the most important slides — those that show a diagram,
graph, or result that would be hard to convey in text alone.

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{images/slides/lecture_X/slide_NNN.png}
    \caption{Brief description of what the slide shows (slide NNN).}
\end{figure}
```

- Width is typically `0.65`–`0.85\textwidth` depending on content.
- Caption always ends with `(slide NNN)` so the source is traceable.
- For side-by-side slides use `subcaption` / `minipage`.

### 3.6 Lists

Use `itemize` for unordered and `enumerate` for ordered lists.
Each item should be at least one full sentence.

```latex
\begin{itemize}
    \item First point, explained in full.
    \item Second point.
\end{itemize}
```

### 3.7 Tables

Use `booktabs` for clean tables. Always include a caption above the table.

```latex
\begin{table}[H]
    \centering
    \caption{Caption goes above the table.}
    \begin{tabular}{lll}
        \toprule
        Column A & Column B & Column C \\
        \midrule
        ...      & ...      & ...      \\
        \bottomrule
    \end{tabular}
\end{table}
```

### 3.8 Oral-exam callouts

For oral exams, flag high-priority topics with a bold note inline:

```latex
\textbf{Exam note:} This derivation is frequently asked; know the
three key assumptions and the final result by heart.\\
```

For written exams, this callout can be omitted or rephrased as a
reminder of what is typically tested in problem sets.

### 3.9 Closing recap

End every lecture file with a `\subsection*{Recap}` that summarises
the main takeaways in 4–8 sentences of dense prose (no bullet points).
This mirrors the "Recap of Part X" sections that make the notes
self-contained for last-minute revision.

```latex
\subsection*{Recap}

Lecture X introduced ... The central result is ... This connects
to ... and is important because ...
```

---

## 4. Content Guidelines

| Guideline | Rule |
|-----------|------|
| **Depth** | Summarise, do not transcribe. One paragraph per major idea. |
| **Derivations** | Include key steps only; skip routine algebra unless the method itself is examinable. |
| **Definitions** | Define every symbol the first time it appears. |
| **Examples** | Omit worked examples and practice questions from the source material unless the method they demonstrate is unique. |
| **Notation** | Match the lecture notation exactly (no reformulation). |
| **Images** | Only slides that add value beyond the text (diagrams, graphs, summary tables). Aim for 2–4 per lecture. |
| **Length** | Target 1–2 compiled pages per lecture hour of material. |

---

## 5. Exam-Type Adaptations

### Oral exam
- Open every section with a brief motivation: *why* this topic matters.
- Flag the 2–3 questions most likely to be asked at the start of each subsection.
- Include key derivation steps (the examiner may ask you to reproduce them).
- The closing recap is especially important — it is the "spoken answer" skeleton.

### Written exam
- Prioritise formulas, scaling laws, and result tables over conceptual discussion.
- Include more worked-example structure where problem-solving steps are examinable.
- Skip the oral-exam callout blocks; add formula boxes instead.

---

## 6. Image Extraction

Images are extracted from the PDF lecture slides using a Python script.
The script uses **PDF page indices** (0-based or 1-based depending on
configuration — check your script), not printed slide numbers.

After writing a `.tex` file, provide a comma-separated list of the
page indices needed, e.g.:

```
Slides needed: 36, 42, 55, 61, 78
```

Run the extraction script once per lecture and drop the resulting
`.png` files into the correct `images/slides/lecture_X/` folder
before compiling in Overleaf.

---

## 7. Per-Lecture Checklist

Before finalising each `.tex` file:

- [ ] `\section` title matches lecture number and topic from the source PDF.
- [ ] Introductory paragraph names all key concepts.
- [ ] All symbols defined on first use.
- [ ] Key results are `\boxed{}`.
- [ ] Paragraph breaks use `\\` + two blank lines.
- [ ] Every `\includegraphics` path matches `images/slides/lecture_X/slide_NNN.png`.
- [ ] Figure captions end with `(slide NNN)`.
- [ ] Exam callouts present (oral) or formula boxes present (written).
- [ ] No `\usepackage`, `\documentclass`, or `\begin{document}` in the file.
- [ ] Closing `\subsection*{Recap}` present.
- [ ] Comma-separated slide index list provided for image extraction.
- [ ] File added to `\input{}` list in `main.tex`.

---

## 8. Canonical Prompt

Use this prompt verbatim for each new lecture. Attach the PDF of the
lecture notes as a file. No further instructions are needed.

> *Write a LaTeX lecture notes file for this lecture.
> Follow the style in PROJECT_INSTRUCTIONS.md.*

Infer the lecture number, topic, and exam type from the PDF itself —
do not specify them manually.
