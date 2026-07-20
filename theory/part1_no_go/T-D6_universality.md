# T-D6 — Universality of the Half-Odd-Integer Spectrum (Corollary)

**Project:** Möbius Quantum Walk
**Deliverable:** T-D6 (Theory track; corollary of T-D1 + the deck-operator structure)
**Status:** Final v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.5, `T-D1_walk_operators.md`.

---

## §0. Purpose and Status

T-D6 records the protocol-independence claim for T1 (half-odd-integer momentum quantization on Möbius) as a corollary of the deck-operator structure. The numerical confirmation is N5 (Hadamard) and N6 (three-state Grover) in `mobius_dtqw_simulator.ipynb`.

---

## §1. The Corollary

**Setup.** Let $U^{\text{cyl}}$ be any unitary on $\mathcal{H}_L = \ell^2(\mathbb{Z}/L\mathbb{Z}) \otimes \mathbb{C}^d$ that is:
1. Translation-invariant on the position circle, and
2. Periodic in position: $\psi(x+L, c) = \psi(x, c)$ in its domain Hilbert space.

The cylinder Bloch decomposition gives $U^{\text{cyl}}$ as a fiber bundle of $d \times d$ unitaries $U^{\text{cyl}}(k)$ over $k \in K^{\text{cyl}}_L = \{2\pi n/L : n = 0, \dots, L-1\}$.

The corresponding **Möbius walker** with canonical deck $\Sigma = -\mathbb{I}_d$ is the same operator family acting on the anti-periodic Hilbert space $\mathcal{H}_L^{\text{Möb}} = \{\psi : \psi(x+L, c) = -\psi(x, c)\}$. Its Bloch decomposition is the same family $U^{\text{Möb}}(k) = U^{\text{cyl}}(k)$ evaluated at $k \in K^{\text{Möb}}_L = \{(2n+1)\pi/L : n = 0, \dots, L-1\}$.

**Corollary (T-D6).** *The Möbius walker's quasi-energy spectrum is the cylinder bulk dispersion sampled at half-odd-integer crystal momenta, for any translation-invariant coined Floquet walker on $\mathcal{H}_L$ — including but not limited to split-step (T-D1 §2), Hadamard (T-D1 §4), and three-state Grover (T-D1 §5). The TRIMs $k = 0$ and $k = \pi$ are absent from the Möbius spectrum (and conditional on $L$ parity for $k = \pi$, per spec §8.M3).*

**Proof.** The deck operator $\Sigma = -\mathbb{I}_d$ commutes with all coin operations and with translation. The Möbius Hilbert space is the $-1$ eigenspace of the $2L$-cylinder deck operator $D = T^L \otimes \Sigma$; the walker on Möbius is the restriction of the cylinder walker (on a $2L$-periodic system) to this invariant subspace. Bloch decomposition selects the half-odd-integer momentum modes by the anti-periodic projection (T-D1 §3.3). This argument is independent of the walk operator's structure beyond translation invariance and acts identically on split-step, Hadamard, Grover, and any other translation-invariant coined Floquet walker. ∎

---

## §2. Numerical confirmation

Three walkers tested numerically in the notebook:

- **N1 (split-step DTQW, $L = 50$):** Möbius eigenvalues at half-odd-integer momenta confirmed; cylinder modes at $k = 0$ count = 1, Möbius count = 0.
- **N5 (Hadamard walker, $L = 50$):** Möbius spectrum shifted from cylinder, mean shift $0.0628 = \pi/L$.
- **N6 (three-state Grover walker, $L = 50$):** Möbius spectrum shifted from cylinder, mean shift $0.0419$.

All three confirm the corollary at machine precision (after the cylinder–position Bloch consistency tests in §2 of the notebook).

---

## §3. What the corollary doesn't say

T-D6 covers spectrum quantization. It does *not* automatically extend the topological-invariant claims (T2 / T-D4) across protocols — different walkers have different chiral symmetry structures and different winding-number classifications. T-D4's winding-equality theorem is for the split-step DTQW specifically; Hadamard and Grover walkers' topological invariants are simpler (Hadamard has no parameters, Grover-3 has a fixed structure), so cylinder–Möbius topological-invariant equality holds vacuously or by direct computation, but not via T-D4's machinery.

---

## §4. Paper paragraph (ready to drop in)

> The half-odd-integer crystal-momentum signature of the Möbius walker (T1) is a property of the anti-periodic boundary condition alone — implemented via the canonical deck operator $\Sigma = -\mathbb{I}_d$ — and applies to any translation-invariant coined Floquet walker on the Möbius graph. We verify this numerically for the split-step DTQW, the Hadamard walker, and the three-state Grover walker; all three exhibit the half-odd-integer momentum-quantization shift relative to their cylinder counterparts (Figures 1, 5, 6). The signature is protocol-independent; the topological invariants beyond T1 are protocol-specific.

---

## §5. Status

Theory track item T-D6 (spec §7.1) is closed by this corollary. No further proof needed.

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-16 | Reduced from separate theorem to one-paragraph corollary of T-D1 §3.3's quotient construction. Validated numerically by N1, N5, N6. Paper paragraph ready. |
