# Discrete-Time Quantum Walks on Möbius Graphs

**Paper:** *Discrete-Time Quantum Walks on Möbius Graphs: Topological Robustness Under Non-Orientability*
**Authors:** S. M. Yousuf Iqbal Tomal, Abdullah Al Shafin
**Status:** Manuscript draft v1.0; ready for author review and journal submission.
**License:** MIT (see `LICENSE`)

This repository is the code companion and theory archive for the paper. It contains the full numerical pipeline, the theorem proofs, the manuscript source, and the supporting project documentation.

---

## Headline claim

**For the canonical Möbius quantum walker with deck operator $\Sigma = -\mathbb{I}_d$, the chiral DTQW topological classification is identical to that of the cylinder walker at every system size above an aliasing threshold.** Spectral signatures of non-orientability scale as $\pi/L$ and vanish asymptotically. A structural distinction does persist in the rung-antisymmetric sector of the Möbius ladder adjacency operator, where the twist enters as an anti-periodic boundary condition; this manifests in the Szegedy walker spectrum.

This is, fundamentally, a **negative result paper** with a few clean structural observations. The dramatic $\mathbb{Z} \to \mathbb{Z}_2$ topological reduction one might expect from non-orientability does **not** occur for the canonical walker. The non-canonical (intrinsic) Möbius walker, with deck operators that mix coin states, is the natural setting where richer non-orientable physics might live; see Option B (separate folder/repo) for that follow-up project.

---

## What's in the box

### `paper/`

The LaTeX manuscript.

- `paper.tex` — REVTeX 4.2 source, ~12 pages compiled.
- `refs.bib` — 14-entry BibTeX bibliography.
- `README.md` — compile instructions and journal-class notes.

### `notebook/`

The numerical pipeline.

- `mobius_dtqw_simulator.ipynb` — Self-contained Jupyter notebook. Executes the entire experiment suite (N0–N7) end-to-end in ≲ 1 minute on a 2024-era laptop CPU. Generates all 8 figures used in the paper.
- `figures/` — Pre-rendered PNGs of all figures, sufficient for paper compilation without re-running the notebook.

### `theory/`

Detailed theorem proofs (Markdown).

- `T-D1_walk_operators.md` — Explicit walk operators (cylinder + Möbius) for split-step, Hadamard, three-state Grover, Szegedy. Bloch decomposition and bulk dispersion derived.
- `T-D3_chiral_symmetry.md` — Chiral symmetry operator $\Gamma = \sigma_x$ in the symmetric time frame.
- `T-D4_winding_equality.md` — Theorem: $\nu^{\text{cyl}}_L = \nu^{\text{Möb}}_L$ off phase boundaries.
- `T-D5_edge_modes.md` — Cut-walker edge modes (corollary of T-D4 + Asbóth–Edge 2015).
- `T-D6_universality.md` — Half-odd-integer signature is protocol-independent (corollary).
- `T-D7_mobius_ladder_spectrum.md` — Theorem: Möbius ladder adjacency spectrum decomposition.

### `docs/`

Project metadata.

- `mobius_dtqw_research_spec.md` — Master specification, revision history v1.0 through v1.6.
- `lit_check_2026-05-07.md` — Literature pre-emption check (verdict: PROCEED, no overlap found).
- `The 3 Angles.md` — Record of the three QC/QI directions considered during scoping (DTQW, holonomic gate, surface code).

### Top-level

- `LICENSE` — MIT.
- `requirements.txt` — NumPy ≥ 1.24, SciPy ≥ 1.10, matplotlib ≥ 3.7, jupyter, nbformat.
- `.gitignore` — standard Python/Jupyter exclusions.

---

## Reproducing the results

### Locally

```bash
git clone <repo>
cd Option_A_chiral_DTQW_mobius
pip install -r requirements.txt
jupyter notebook notebook/mobius_dtqw_simulator.ipynb
```

"Restart & Run All". Total runtime: ~6 seconds to ~1 minute depending on hardware. All 8 figures land in `notebook/figures/`.

### On Kaggle

1. Create a new Kaggle notebook.
2. Upload `notebook/mobius_dtqw_simulator.ipynb`.
3. Run all cells. Figures appear inline and are saved to `/kaggle/working/` for download.

No datasets, no GPU. Free tier sufficient.

---

## Test summary

The notebook's §2 sanity tests verify (all PASS at machine precision):

- **Unitarity** of all four walk operators across cylinder and Möbius BCs, $L \in \{50, 100\}$. Error ~$10^{-17}$.
- **Möbius boundary** $T_{\text{Möb}}^L = -\mathbb{I}_L$ for $L \in \{10, 50, 100\}$. Error exactly 0.
- **Bloch–position consistency** at $L \in \{50, 100\}$. Error ~$10^{-15}$.

Independent theorem validations are documented in each T-D markdown file's §8 block, with paste-ready code snippets.

---

## Headline experimental table

| Experiment | Spec ref | Outcome |
|---|---|---|
| N0 | spec §6.8 | Reproduces Asbóth–Edge cylinder phase diagram (4 boundary lines). |
| N1 (T1) | spec §6.1 | Half-odd-integer momentum quantization on Möbius confirmed. |
| N2 (T2) | spec §6.2 | TRIM-mediated phase transitions absent on Möbius. Max gap difference $\approx \pi/L$. |
| N3 | spec §6.3 | Standard chiral-DTQW edge modes (T-D5 corollary). |
| N4 | spec §6.4 | Deck-phase signature in return amplitude; max $|\Delta\mathcal{A}| \approx 0.18$ at $T \approx L$. |
| N5+N6 (T4) | spec §6.5–6.6 | Hadamard and Grover walkers confirm protocol-independence. |
| N7 (T5) | spec §6.7 | $M_L$ rung-antisymmetric sector at half-odd-integer momentum; analytical match to $5 \times 10^{-15}$. |

---

## Honest framing

The authors adopted the following honest framing during the 2026-05-16 review:

- The results show that **non-orientability has limited topological consequence for chiral DTQW**.
- The main quantitative observable distinctions are finite-size ($\pi/L$ shifts) that vanish asymptotically.
- The Szegedy walker on the Möbius ladder is the only setting where a non-vanishing structural distinction persists, and even that is partly a known property of Möbius ladders in graph theory.
- The paper's value is in **precise characterization** and a clean **negative-result theorem** (T-D4), not in discovering dramatic new physics.

The natural follow-up (Option B) is to investigate non-canonical deck operators ($\Sigma = \sigma_x$ etc.) with modified walker structure. That work is in a separate folder/repo.

---

## Citation

If you use this code or build on the results, please cite:

```bibtex
@article{tomal_shafin_mobius_dtqw,
  author = {Tomal, S. M. Yousuf Iqbal and Shafin, Abdullah Al},
  title  = {Discrete-Time Quantum Walks on M\"obius Graphs:
            Topological Robustness Under Non-Orientability},
  year   = {2026},
  note   = {Manuscript in preparation. Code: this repository.},
}
```

Update the `note` field once the paper is published or posted to arXiv.
