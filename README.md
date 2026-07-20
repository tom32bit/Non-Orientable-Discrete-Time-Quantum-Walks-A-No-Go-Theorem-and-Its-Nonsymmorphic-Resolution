# Non-Orientable Discrete-Time Quantum Walks: A No-Go Theorem and Its Nonsymmorphic Resolution

**Authors:** S. M. Yousuf Iqbal Tomal, Abdullah Al Shafin
**Status:** unified manuscript draft + complete verified numerical pipeline (2026-07-19)
**License:** MIT

One paper, two movements:

- **Part I (no-go).** For the chiral split-step DTQW, the only Möbius deck
  operators compatible with the standard walker are scalars (Σ = ±𝕀), and the
  scalar twist is topologically inert: the winding classification is identical
  on cylinder and Möbius momentum lattices at every size above an O(1)
  aliasing threshold. Non-orientability, imposed through the boundary
  condition, does nothing topological.
- **Part II (resolution).** The twist survives in exactly one place: the
  symmetry algebra. The glide-chiral operator Γ = (one-site shift)·σx obeys
  Γ(k)² = e^{-ik}𝕀; its eigenbundle is a **Möbius bundle over the Brillouin
  zone**. Every local half-protocol F yields a glide-chiral walker
  U = ΓF†Γ⁻¹F carrying a ℤ₂ invariant ζ (relative half-zone winding parity)
  protected by this **unitary** symmetry alone — the DTQW realisation of the
  Möbius-topological-insulator mechanism — with π-pinned domain-wall modes and
  a dynamical detector (staggered return amplitude).

## Layout

```
paper/                      unified manuscript (REVTeX) + bibliography
theory/part1_no_go/         inherited theorem files T-D1..T-D7 (re-verified)
theory/part2_nonsymmorphic/ construction theorem, parity lemma, Z2 invariant
code/part1_validation/      independent re-validation suite for Part I
code/part2_spaceglide/      walker library + experiments E1..E6
code/figures/               generated figures + raw npz data
code/legacy_notebook/       original Option A notebook (archival, superseded)
docs/                       unified spec, validation log, lit checks, analyses
archive/                    former Option A paper, failed Option B candidates
```

## Reproduce everything

```bash
pip install -r requirements.txt
python code/part1_validation/validate_part1.py        # Part I: all claims, ~20 s
cd code/part2_spaceglide
python e1_construction_checks.py                      # Part II: E1 gate, ~5 s
python run_phase_diagram.py                           # E3 figure + npz, ~3 min
python run_bands_figure.py                            # E2 figure
python run_walls_and_bridge.py                        # E4/E5/E6 figure
```

Every figure in the paper regenerates from these scripts; every theorem cites
its verification block. See `docs/VALIDATION_LOG.md` for the skeptical-restart
audit (including two live corrections the checks caught: the sublattice-parity
collapse and the failed first invariant proposal).

## Provenance

This repository unifies and supersedes two earlier project lines ("Option A":
canonical Möbius DTQW characterisation; "Option B": intrinsic Möbius walker,
open problem). Their archived states are under `archive/` and `docs/archive/`.
The former Option A negative result is now Part I — the motivation engine for
Part II's construction — rather than a standalone paper.
