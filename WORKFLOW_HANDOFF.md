# WORKFLOW HANDOFF — AE4135 LaTeX Exam Summary

Use this file to resume the project in a new chat. Paste the
"Prompt to start the new chat" section at the bottom, and re-attach the
files listed there.

---

## 1. Goal

Build a LaTeX exam-summary document for **AE4135 Rotor / Wake Aerodynamics**
(TU Delft). For **each slide deck** I upload, Claude writes **one `.tex`
file** that follows `PROJECT_INSTRUCTIONS.md`. All `.tex` files are
`\input{}`-ed from a master `main.tex` and compiled in Overleaf.

## 2. Fixed decisions (do not re-ask these)

- **Exam type: WRITTEN.** Use the written-exam treatment: prioritise
  formulas, scaling laws and result tables; box key results with
  `\boxed{}`; use `booktabs` summary tables. **No oral-exam callouts**
  (no `\textbf{Exam note:}` blocks, no "why this matters" motivation).
- **One `.tex` file per uploaded slide deck.** A "combined" chapter deck
  contains several sub-units → put them in ONE file, with a `\subsection*`
  per sub-unit (and `\subsubsection*` below that).
- **File naming:** `lectureN_notes.tex` for Chapter N. The `\section`
  title reads `Chapter N -- <topic>`. Images go in
  `images/slides/lecture_N/`.
- Infer chapter number, topic and content from the PDF itself.

## 3. Style rules (from PROJECT_INSTRUCTIONS.md — apply every time)

- **No preamble** in the file (no `\documentclass`, `\usepackage`,
  `\begin{document}`). It is `\input{}`-ed into `main.tex`.
- Start with `\section{Chapter N -- ...}` + a short intro paragraph naming
  the key concepts (for the written exam, list the key formulas/results to
  have on hand instead of oral "flags").
- `\subsection*{}` / `\subsubsection*{}` (always starred / unnumbered).
- Paragraph breaks: `\\` followed by **two blank lines** (no `\par`,
  no `\vspace`).
- Equations: `equation` for single, `align` for multi-line; `\boxed{}`
  the key final results; `\emph{}` on first use of a term.
- Figures: `\begin{figure}[H] ... \includegraphics[width=0.65–0.85\textwidth]
  {images/slides/lecture_N/slide_NNN.png} ... \end{figure}`. Caption
  **always ends with `(slide NNN)`**. Use `subcaption`/`subfigure` for
  side-by-side images.
- Tables: `booktabs`, caption above.
- End every file with `\subsection*{Recap}` — 4–8 sentences of dense prose,
  no bullets.
- Aim ~2–4 figures per sub-unit; for a big combined chapter ~8–10 total,
  the ones that genuinely need a diagram (control volumes, velocity
  triangles, curves, flowcharts), not text-only slides.

## 4. Image extraction (the script + page indexing)

Script: `extract_slides (1).py` (PyMuPDF). Behaviour:
- `my_slides` takes **1-based PDF page numbers**.
- Output filename = the SAME 1-based number, zero-padded: `slide_NNN.png`.
- So: the number Claude reports, the number you paste into `my_slides`,
  and the number in the filename are **all the same 1-based PDF page
  index** — and that is also the number used in the `(slide NNN)` caption.

Per-deck run:
1. Set `pdf_file_path = "<deck>.pdf"`.
2. Set `my_slides = [ ...the list Claude gives... ]`.
3. Set `output_folder = "images/slides/lecture_N"` (matches the
   `\includegraphics` paths). (The script's example uses `"lecture_6"` —
   change it to the full `images/slides/lecture_N` path, or extract then
   move the PNGs there.)
4. Run, drop PNGs into `images/slides/lecture_N/`.
5. Add `\input{lectureN_notes}` to `main.tex`.

## 5. How Claude reads each deck (so figures are correct)

The deck PDF text often isn't in context. Claude should: extract the text
layer (`pdftotext`), map each PDF page to its leading text to get exact
page indices, then **rasterize the candidate figure pages** to confirm
they're visual and to caption them accurately.

## 6. Status

| Item | Status |
|------|--------|
| `lecture1_notes.tex` (Chapter 1) | **Done, but in OLD oral style** — needs redo to written treatment |
| `lecture2_notes.tex` (Chapter 2) | Done, written style |

**Slides already extracted:**
- Chapter 1: `8, 17, 19, 25, 28, 30, 32, 43, 48, 51`
- Chapter 2: `18, 61, 83, 84, 88, 89, 99, 106, 113`

**Chapter coverage so far:**
- Ch1 = actuator surface concept → action of forces on flow → wake states
  → annular streamtubes / blade element → solidity → performance
  coefficients (dimensional analysis, C_T, C_P, λ, J).
- Ch2 = actuator-disk momentum derivation → axial-disk performance
  (induction factor, C_T=4a(1−a), C_P=4a(1−a)², Betz 16/27) → BEM
  (annular balance, blade element, a/a' closure, Prandtl + Glauert
  corrections, algorithm) → rotors in yaw (momentum / Glauert /
  vortex-cylinder, skew angle).

## 7. Outstanding to-dos

1. **Redo `lecture1_notes.tex` in written style** (swap oral callouts for
   formula boxes / scaling-law emphasis). Keep the same slide list.
2. Process remaining decks (one `.tex` each). Uploads seen earlier that
   may still need doing — **check for duplication** with the combined
   Chapter 1/2 decks before writing, since some of these may be the
   individual source decks already covered:
   - `1_4_Introduction-Rotor_design.pdf`
   - `1_5_Introduction_Rotor_Coefficients_v2.pdf`
   - `2_1_2_From_momentum_to_vorticity-Actuator_disc_theory.pdf`
   - `2_2_1_BEM_theory.pdf`
   - `BEM_for_yawed_rotor.pdf`
   - `LECTURE_2_-_VAWTS.pdf`  (Vertical-Axis Wind Turbines — new content)
3. Build/maintain `main.tex` with the `\input{}` list once more chapters
   exist (template is in PROJECT_INSTRUCTIONS.md §2).

## 8. Practice exam (calibration)

The course has a written practice exam. Used to weight emphasis. Rough map
of question → where it's covered:
- Q1 root vortex (tip-speed ratio, circulation on disk/wake) → likely a
  later vorticity/lifting-line chapter.
- Q2 wake rotation speed at tip vortices, axial vs rotational wake velocity
  → **Ch2 BEM** (Ωr·2a' far wake, U∞(1−2a)).
- Q3 BEM vs Lifting-Line vortex model → **BEM in Ch2**; lifting-line not
  yet covered (expect later deck).
- Q4 two blade-performance tuning devices → not yet covered.
- Q5 2D unsteady airfoil, loads vs circulation, Helmholtz → later chapter.
- Q6 yaw misalignment (flow/loads/wake/C_P) → **Ch2 yaw module**.
- Q7 actuator disk with uniform normal force f_n (+ azimuthal f_azim):
  velocity/pressure/total-pressure along streamtube, vorticity, U/P/T as
  f(f_n) → **Ch2 actuator-disk + wake-rotation**.

Optional future deliverable: a separate study file mapping each exam
question to the relevant results, or worked-answer sketches.

---

## Prompt to start the new chat

> Continuing my AE4135 LaTeX exam-summary project. Read the attached
> `WORKFLOW_HANDOFF.md` — it has all the conventions and decisions
> (written-exam style, one `.tex` per deck, naming `lectureN_notes.tex`,
> images in `images/slides/lecture_N/`, 1-based slide numbering, etc.).
> Follow `PROJECT_INSTRUCTIONS.md` for style. I'm attaching the next slide
> deck — write its `.tex` file and give me the comma-separated slide list
> to extract. [If you also want it: "First, redo lecture1_notes.tex in
> written style."]

**Attach to the new chat:** `WORKFLOW_HANDOFF.md`, `PROJECT_INSTRUCTIONS.md`,
`extract_slides (1).py`, and the next deck PDF. (Re-attach
`lecture1_notes.tex` if you want it redone.)
