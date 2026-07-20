# T-D5 — Edge Modes on a Cut Walker (Corollary)

**Project:** Möbius Quantum Walk
**Deliverable:** T-D5 (Theory track; corollary of T-D4 + Asbóth–Edge 2015)
**Status:** Final v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.5, `T-D3_chiral_symmetry.md`, `T-D4_winding_equality.md`.

---

## §0. Purpose and Status

After T-D4 closed out T2 as form 5.2-a (winding integer robust under cylinder→Möbius), T-D5 reduces from a separate theorem with its own proof to a **two-sentence corollary**.

This document records the corollary and points to the relevant literature. The numerical experiment N3 in `mobius_dtqw_simulator.ipynb` provides direct visual confirmation.

---

## §1. The Corollary

**Setup.** Consider a finite open chain obtained from the canonical Möbius walker (spec §4.2, $\Sigma = -\mathbb{I}$) by removing the boundary identification — i.e., the shift operator's wraparound entry is set to zero. The resulting walker is identical (as a finite-dimensional unitary on $\mathbb{C}^L \otimes \mathbb{C}^2$) to the cut cylinder walker, because:

1. The wraparound entry of the shift carries the only place where cylinder and Möbius walkers differ (the sign $+1$ vs $-1$). When this entry is set to zero, both reduce to the same open-chain operator.
2. The Möbius BC is a property of the closed walker only; cutting destroys it.

**Corollary (T-D5).** *Edge modes on a cut Möbius walker are identical to edge modes on a cut cylinder walker. Bulk-edge correspondence is the standard chiral-DTQW result of Asbóth & Edge 2015: the number of zero-quasi-energy edge modes at each wall equals the bulk winding number $|\nu|$ at quasi-energy $\varepsilon = 0$ plus the bulk winding at $\varepsilon = \pi$.*

**Proof.** By the construction above, the cut walker's Hamiltonian is identical for cylinder and Möbius. The bulk topological invariant is the same in both cases (T-D4). Standard bulk-edge correspondence (Asbóth & Edge, *Phys. Rev. B* **91**, 195442, 2015) applies. ∎

---

## §2. Numerical evidence

`mobius_dtqw_simulator.ipynb` §6 (experiment N3) constructs the cut walker at $L = 80$, scans two parameter regions, and reports edge-mode counts. The figure shows the position density of the lowest-quasi-energy mode for each region.

Phase B at $(\pi/4, 2\pi/3)$: 2 near-zero modes localized at the chain ends — the standard topological edge-mode signature.
Phase A at $(\pi/4, \pi/3)$: many near-zero modes, but inspection of the position density shows them to be bulk-extended (small bulk gap at that parameter point), not edge-localized — consistent with the phase having $\nu = 0$.

The figure visually distinguishes the two scenarios; the precise counts depend on the choice of `eps_tol` and bulk gap size and should be interpreted via the position-density profile rather than the integer count alone.

---

## §3. Paper paragraph (ready to drop in)

> The Möbius walker's anti-periodic boundary condition affects the closed-system spectrum (half-odd-integer momentum quantization, T1) but does not enter the open-chain construction. A finite walker with hard-wall cuts has the same Hamiltonian on cylinder and Möbius, and hence the same edge-mode structure. Bulk-edge correspondence reduces to the standard chiral-DTQW result of Asbóth & Edge [PRB 91, 195442 (2015)]: zero-quasi-energy modes are localized at the walls in phases with non-trivial bulk winding number, with mode count tracking the bulk invariant. Möbius non-orientability does not modify this correspondence — consistent with the more general T-D4 winding-equality theorem.

---

## §4. Status

Theory track item T-D5 (spec §7.1) is closed by this corollary. No further proof needed.

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-16 | Reduced from separate theorem to corollary of T-D4 + Asbóth–Edge 2015. Two-sentence proof, paper paragraph ready. |
