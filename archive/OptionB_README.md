# Option B — Intrinsic M\"obius Walker

**Status:** **Open research problem.** Two candidate walker constructions investigated on 2026-05-16; both failed sanity checks. Spec revised to honest open-problem framing.

## Current state

- `research_spec.md` — canonical project specification (revised v1.1). Documents failed candidates, lists remaining candidates, proposes a phased research plan with explicit decision points.
- `_OB_sanity_check.py` — Candidate Failure 1: $U_{\text{sym}}$ on a $2L$-cylinder with $D = T^L \otimes \sigma_x$ as a "new" chiral symmetry. Collapses to Option A (cylinder + M\"obius direct sum) under the $T^L$-eigenspace decomposition. Windings identical in both sectors — no $\mathbb{Z}_2$ refinement.
- `_OB_alternating_check.py` — Candidate Failure 2: Alternating-angle walker on $2L$-cylinder. Has neither $D$ as unitary symmetry nor as chiral symmetry; not a meaningful "intrinsic M\"obius" construction.

## Next concrete step

**Literature analysis completed 2026-05-16** in `chiral_geometry_analysis.md`. Key finding: the conceptual territory Option B was aiming for is partially pre-empted by Mochizuki-Bessho-Sato-Obuse 2020 (PRB 102, 035418), which establishes DTQW with glide symmetry → $\mathbb{Z}_2$ topology. The remaining niche (1D space-glide DTQW as a Möbius topological insulator analog of Shiozaki-Sato-Gomi 2015) is publishable but **incremental**, not groundbreaking.

## Two paths forward

**Path X (continue Option B with eyes open).** Specialize Mochizuki 2020's framework to 1D space-glide on a Möbius graph, connect to Shiozaki MTI, compute the Z_2 invariant, write a methods/extension paper. Timeline: 3-6 months. Likely venue: *Phys. Rev. Research*, *J. Phys. A*, *Quantum Inf. Process.*

**Path Y (close Option B).** Acknowledge the literature has filled the territory. Submit Option A's characterization paper as the project's main deliverable; note Option B's prior art in the discussion. Move on.

The decision is the user's. Both are honest research conclusions.

## Why this is open vs why it's bounded

The two naive constructions (`_OB_sanity_check.py`, `_OB_alternating_check.py`) failed for structural reasons. The chiral-geometry literature analysis identifies the correct construction direction (specialization of Mochizuki et al. 2020) but also documents the substantial pre-emption.

If Path X is chosen, the spec's "candidate constructions" should be replaced by the Mochizuki-template, with explicit references to Shiozaki-Sato-Gomi 2015 and Zhou-Zhang-Pan 2025.

If Path Y is chosen, Option B closes with the chiral-geometry analysis as its only artifact — a useful reference document for any future work in this direction.

## Files

- `research_spec.md` — Original (now superseded) project specification. Records the early failed-candidate findings.
- `chiral_geometry_analysis.md` — First-pass literature cross-check; identified the partial pre-emption by Mochizuki et al. 2020.
- `projective_symmetry_deep_analysis.md` — **Current canonical document.** Skeptical re-analysis at user request, identifying three remaining open territories (Brillouin Klein bottle DTQW; projective-symmetry-protected DTQW gates; Klein-bottle search). Detailed novelty/risk matrix and recommendation.
- `_OB_sanity_check.py`, `_OB_alternating_check.py` — Sanity check scripts documenting the failed candidates.
