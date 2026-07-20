# Unified Research Specification

**Paper:** *Non-Orientable Discrete-Time Quantum Walks: A No-Go Theorem and Its
Nonsymmorphic Resolution*
**Authors:** S. M. Yousuf Iqbal Tomal, Abdullah Al Shafin
**Spec version:** 2.0 (2026-07-19). Supersedes `archive/` specs of both former
options; the two former projects are now Parts I and II of one paper.

---

## 1. Thesis (one paragraph)

The Möbius twist cannot be put into a chiral split-step DTQW through the
boundary condition: the only deck operators compatible with the standard walker
are scalars, and the scalar twist leaves the topological classification
untouched at every size above an O(1) aliasing threshold (**Part I — no-go**,
proven + machine-verified). The twist can, however, be put into the *symmetry
algebra*: replacing the involutive coin chirality σx by a **glide-chiral**
operator Γ = (one-site translation)·σx with Γ(k)² = e^{-ik}𝕀 makes the
symmetry's eigenbundle a **Möbius bundle over the Brillouin zone**, and the
walker family U = ΓF†Γ⁻¹F carries a gap-resolved **ℤ₂ invariant** ζ (relative
half-zone winding parity of det H₊₋) protected by this unitary symmetry alone,
with π-pinned domain-wall modes and a walk-native dynamical detector
(**Part II — resolution**, constructed + machine-verified). Together:
non-orientability is topologically inert in real space but topologically
active in momentum space — the no-go and its unique escape route.

## 2. Deliverables and status

| ID | Deliverable | Status |
|---|---|---|
| D1 | Part I re-validation suite (independent code) | DONE — `code/part1_validation/validate_part1.py`, all PASS |
| D2 | Part I theory (T-D1…T-D7, inherited, re-verified) | DONE — `theory/part1_no_go/` |
| D3 | Part II construction theorem + parity lemma + invariant | DONE — `theory/part2_nonsymmorphic/P2_construction_and_invariant.md` |
| D4 | Part II library + E1 checks | DONE — `code/part2_spaceglide/` |
| D5 | E2 bands/winding figure; E3 phase diagram; E4 walls; E5 bridge; E6 dynamics | DONE — `code/figures/E*.png` + npz |
| D6 | Refreshed lit check | DONE — `docs/lit_check_2026-07-19.md` |
| D7 | Unified manuscript | REVISED v2 — `paper/main.tex` (post-review; all 10 review items executed 2026-07-20, mechanical + content audits pass) |
| D8 | Internal review + revision round | DONE — E7/E8 experiments, `check_manuscript.py`, logged in `docs/VALIDATION_LOG.md` |
| D9 | Open-problem section backlog (below) | ONGOING |

## 3. Definitions locked (conventions)

- Split-step: U = S↓ R(θ₂) S↑ R(θ₁); rotations R(θ) = e^{-iθσy/2};
  symmetric frame splits R(θ₁). Winding orientation as in
  `validate_part1.py` (opposite sign to the 2026-05 docs — see VALIDATION_LOG).
- Part II cell: (A↑, A↓, B↑, B↓); Bloch gauge |k,s,c⟩ ∝ Σₙ e^{ikn}|2n+s, c⟩.
- Glide Γ(k) = t(k)⊗σx, t(k) = [[0, e^{-ik}],[1,0]].
- Half-protocol F(k) = S↓(k) Rc(β) S↑(k) Rc(α), partial shifts, sublattice
  coin angles α=(αA,αB), β=(βA,βB).
- Invariant ζ per gap: P2 §5. Phase-diagram slice for the paper:
  (αA, αB) ∈ [−π,π]², (βA,βB) = (−1.24,−1.39).
- Representative points: ζ=1: (2.0944, 2.7227, −1.24, −1.39);
  ζ=0: (2.0944, 1.1519, −1.24, −1.39).

## 4. Claims discipline

Claimed as theorems: construction theorem; parity lemma; ζ well-definedness
and gap-closing protection. Claimed as machine-verified numerics: everything in
P2 §6 table. Explicitly NOT claimed (open, stated as such in the paper):
ζ₀=ζπ identity; π-only wall-mode correspondence; classification completeness.

## 5. Roadmap after the draft

1. Author review of the manuscript; fix affiliation/email placeholders.
2. Re-run `docs/lit_check` queries; then arXiv (quant-ph, cross-list
   cond-mat.mes-hall).
3. Target venue: Physical Review B or Physical Review Research (PRR preferred:
   construction + numerics + open theory items fit its format).
4. Follow-up project (separate): projective-symmetry-protected gate protection
   using this walker as the platform (the 2026-05-16 "Option B of the deep
   analysis"); the S_π detector and wall modes are the starting resources.
5. Optional strengthening if a referee asks: entanglement-spectrum probe of
   the ℤ₂; richer F families to decouple ζ₀ from ζπ; K-theory classification.

## 6. Reproduction

- Part I: `python code/part1_validation/validate_part1.py` (~20 s).
- Part II checks: `python code/part2_spaceglide/e1_construction_checks.py` (~5 s).
- Phase diagram: `python code/part2_spaceglide/run_phase_diagram.py` (~3 min).
- Figures 2, 4: `run_bands_figure.py`, `run_walls_and_bridge.py` (~4 min).
Requirements: numpy, scipy, matplotlib (see `requirements.txt`).
