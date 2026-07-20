# Validation Log — Unified Paper Restart (2026-07-19)

Per the restart directive: **nothing inherited from the Option A / Option B phase
was taken as ground truth.** Every load-bearing claim was re-derived or
re-verified with independent code (`code/part1_validation/validate_part1.py`,
written from scratch — no code shared with the legacy notebook), and every new
Part II claim was built with adversarial checks (collapse tests) designed to
kill it. This file records what was questioned, what survived, what was
corrected, and what was discovered in the process.

## Part I claims (inherited) — all re-verified independently

| Claim | Re-check | Outcome |
|---|---|---|
| Unitarity of split-step walkers, both BCs | fresh implementation, L ∈ {7,50} | PASS, err ~2e-16 |
| Canonical-deck proposition (Σ ∈ {±𝕀}) | commutant of {σy, σz} computed as a linear system | PASS, nullity 1 (scalars) |
| Möbius spectrum = Bloch at half-odd-integer momenta | direct diagonalisation vs analytic Bloch, L ∈ {31,50} | PASS, err ≤ 3e-15 |
| Chiral symmetry Γ = σx in symmetric frame, both BCs | operator identity | PASS, err ≤ 6e-17 |
| T-D4 winding equality (cyl = Möb = ν∞) | independent H_eff route (no legacy formulas), 5 interior points × L ∈ {5,8,16,50} | PASS |
| T-D4 documented L=4 aliasing exception | reproduced | PASS |
| T-D7 Möbius ladder spectrum formula | direct graph diagonalisation, L ∈ {6,11,20} | PASS, err ≤ 7e-15 |

**Corrections / sharpenings found:**

1. **Winding sign convention.** The legacy docs' winding values are opposite in
   sign to the convention used here (their −1 = our +1). The *equality* claims
   are unaffected. The unified paper fixes one convention and states it.
2. **Canonical-deck proposition wording.** The old statement required Σ to
   commute with R(θ) "for all θ"; only fixed generic angles are ever used. The
   commutant of a single generic rotation already equals the commutant of σy,
   so the proposition holds pointwise for generic (θ₁, θ₂), with exceptions
   only at the measure-zero special angles. The unified paper states it this
   way (Part I, Proposition 1).

## Part II claims (new) — adversarial checks and live corrections

1. **First construction collapsed — caught by design.** The initial
   half-protocol used the *full* spin-dependent shift; the no-collapse tests
   (E1f/E1g) found a 4-dimensional commutant. Diagnosis: displacement-parity
   argument — U = ΓF†Γ⁻¹F with all-odd-parity F factors conserves the
   sublattice grading. Promoted to a design lemma (partial shifts are
   necessary); split-step F passes all tests (commutant = scalars, no constant
   chiral operator). *This is exactly the failure mode of the two 2026-05
   Option B candidates, now understood structurally.*
2. **First invariant proposal was wrong — caught by probe.** The naive
   MTI-style sign pair sgn d(0)·sgn d(2π) is identically +1 because
   d(2π) = conj(d(0)) is an algebraic identity, not independent data. The
   correct invariant is the relative half-zone winding parity ζ = n mod 2
   (P2 §5). Quantization then verified to ≤ 3e-15 over the full scanned grid.
3. **Protection scope tested.** ζ remains exactly quantized when coin phases
   break the reality symmetry — the invariant needs glide-chirality only
   (stronger claim, matching the "Z2 from unitary symmetries alone" narrative).
4. **Control-experiment artifact caught.** The first domain-wall control used
   the hyper-symmetric point (−π/2, −π/2) and showed spurious near-pinned
   quadruplets. A generic trivial control shows zero in-gap wall modes. The
   published control uses the generic point.
5. **Boundary-alignment audit.** Every ζ jump on the 61×61 phase-diagram grid
   sits on a step whose bulk-gap floor is ≤ 0.005; there are zero ζ jumps
   across well-gapped steps.

## Revision round (2026-07-20, internal review)

An internal review ran three adversarial numerical tests against the draft
and found two substantive flaws; the full 10-item revision list was then
executed:

1. **Theorem 4 overclaim [FIXED].** Absolute ζ shown frame-relative (an
   admissible gauge with det g± = ±e^{ik/2} shifts n by −1 at every
   parameter point). Theorem restated: canonical-frame ζ + walk-independent
   frame shifts + intrinsic Δζ, with proof of all three parts.
2. **Wall-pinning misattribution [FIXED].** Mechanism identified and
   demonstrated (E7a): reality/PHS K pins (real disorder, even global at
   W = 0.3, keeps deviation 2–5e-5; complex phase disorder unpins →1e-2);
   glide Δζ dictates existence. Defect section rewritten around this.
3. Prop 1 necessity proven (Fourier-coefficient commutant argument, V7:
   joint commutant dim 1 at three generic angle pairs, decomposition error
   ≤ 1e-16).
4. Inter-wall hybridization: ξ = 1.41 cells, r = −0.999994 over six
   decades; the s ≳ 30 upturn identified as the tanh-profile tail floor
   (~1e-8), NOT second-wall hybridization (would be ~1e-15) — corrected
   in figure and text before it could mislead.
5. Second β-slice (0.4, 1.3), 41×41: both classes, zero audit violations,
   quantization 1.7e-15 (E8b).
6. Reality-broken family scan (E8a): quantization 5.6e-16 over 51 gapped
   points (glide-only protection at scale); ζ₀ = ζπ persists ⇒ identity is
   not a K-consequence.
7. S_π optimization (E7c): 0.034 → 0.140 (wall cell) → 0.624 (±2 cells).
8. Part I compressed; abstract 218 words; Rydberg claim tempered with
   tolerance budget; bibliography verified against the published record
   (chen2020 = Zhao–Huang–Yang confirmed; dai2012 = JPA 45, 285301;
   li2015 authors corrected to Li–Mc Gettrick–Zhang–Zhang, pages added;
   higuchi2025 = Higuchi–Segawa; unused matsubara1955 removed).
9. Manuscript validation: mechanical checker
   (`code/part1_validation/check_manuscript.py`) — balanced environments,
   22/22 citations resolved, all \ref labels defined, all figure files
   present, math delimiters balanced, single intentional TODO (author
   email) — PASS; content audit — every review item present, every
   numerical claim in the text cross-checked against measured outputs —
   PASS. (pdflatex unavailable on this machine; compile check deferred.)

## Open items carried into the paper as such (not overclaimed)

- ζ₀ = ζπ at all sampled points: stated as an observation + conjecture.
- Wall modes appear only at ε = π: bulk–defect correspondence for glide-chiral
  unitaries left open.
- Completeness of the ℤ₂ classification: to be settled against Cedzich-type
  index theory; flagged in the discussion.
