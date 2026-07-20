# Paper

LaTeX source for the manuscript *Discrete-Time Quantum Walks on Möbius Graphs: Topological Robustness Under Non-Orientability*.

## Files

- `paper.tex` — Manuscript source. Currently in REVTeX 4.2 (`pra` style) — adapt the documentclass if targeting a different venue:
  - **Phys. Rev. A / Phys. Rev. Research:** keep as is (`revtex4-2`, `pra` or `prresearch`).
  - **Quantum** (`quantumarticle.cls`): replace the documentclass line and adjust the title block. Quantum's class is on CTAN.
  - **J. Phys. A: Math. Theor.** (`iopart.cls`): switch documentclass.
  - **Quantum Information Processing** (Springer `svjour3.cls`): switch documentclass and bibliography style.
- `refs.bib` — BibTeX bibliography (14 references).

## Compile

```bash
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

Or with `latexmk`:
```bash
latexmk -pdf paper.tex
```

Figures live in `../notebook/figures/`; the `\includegraphics` paths in the manuscript reference them as `../notebook/figures/<name>.png`. To create a standalone arXiv tarball, copy the figures into the paper directory and update paths.

## Status

Draft v1.0 (2026-05-16). Authors should:
1. Review the manuscript end-to-end for correctness.
2. Adjust author affiliations and email addresses.
3. Choose target journal and update the documentclass.
4. Verify all citations resolve (Dai 2012 in particular may need a corrected reference).
5. Sign off and submit.
