# Möbius Quantum Walk: Topological Signatures of Non-Orientable Floquet Geometry

**Research Project Specification — Finalized**

| Field | Value |
|---|---|
| Authors | S. M. Yousuf Iqbal Tomal, Abdullah Al Shafin |
| Status | Pre-implementation. Spec lock pending the day-1 literature pre-emption check (Part 9). |
| Date | 2026-05-07 |
| Replaces | `mobius_latent_space_complete.md` (classical-ML/VAE framing, deprecated 2026-05-07) |
| Project domain | Computational quantum information |
| Working mode | Duo, no advisor, simulator-only |

---

## 0. Document Purpose and Authority

This is the canonical specification for the project. Subsequent code, drafts, notes, and notebooks defer to this document on:

- Scope and exclusions
- Exact walk-operator definitions and notation
- Theorem statements (what the paper is claiming)
- Numerical experiment specifications
- Work breakdown between the two authors
- Risk register and mitigations
- Literature pre-emption protocol and pivot conditions
- Submission strategy

Where the document hedges (e.g., "T2 form to be determined by Phase A of the literature check"), the hedge is intentional: the spec records what is known *now* and what is to be resolved *during* the work, without pretending false certainty.

This document is detailed and deliberately long-form. Treat it as a project bible, not a paper outline. The paper outline is a separate artifact, derived from this spec near submission.

---

## 1. Executive Summary

### 1.1 Thesis (one paragraph)

A discrete-time quantum walk (DTQW) defined on a Möbius ribbon graph — i.e., a one-dimensional position circle of length $L$ with a non-orientable boundary identification implemented as a deck operator $\Sigma$ acting on the coin Hilbert space — exhibits Floquet-spectral and topological-phase-diagram signatures that are not realizable on any orientable graph in the same coin/protocol class. The paper establishes these signatures as theorems for the canonical chiral split-step DTQW (Kitagawa et al. 2010), demonstrates protocol-independence numerically across Hadamard and three-state walks, and contrasts the chiral-Floquet results against the coinless Szegedy walk on the same Möbius graph to show that spatial non-orientability and chiral protection are *independent* contributors to the resulting ℤ₂ structure.

### 1.2 Key claims (target theorems and demonstrations)

- **T1 (Spectrum, theorem):** Half-odd-integer crystal-momentum quantization of the Möbius DTQW vs. integer quantization on the cylinder.
- **T2 (Phase-diagram modification, theorem + numerics):** Topological phase boundaries of the chiral-symmetric split-step DTQW on Möbius differ from cylinder in a specific, computable way involving the time-reversal-invariant momenta (TRIMs) $k = 0, \pi$, which are absent from the Möbius spectrum. Whether this constitutes a strict ℤ × ℤ → ℤ₂ reduction or a milder TRIM-exclusion effect is a research question to be settled (Section 5.2).
- **T3 (Boundary modes, numerics + sketch):** A finite Möbius walker with hard-wall cuts hosts edge-localized zero-quasi-energy modes whose count tracks the bulk topological invariant, with bulk-edge correspondence reformulated for the half-odd-integer momentum lattice.
- **T4 (Universality, numerics):** T1 and the qualitative phase-diagram modifications of T2 are not artifacts of the split-step protocol; they hold for Hadamard and three-state walks under the same deck operator.
- **T5 (Contrast, theorem + numerics):** The Szegedy walk on the Möbius graph inherits the half-odd-integer signature *without* a chiral-symmetry-protected reduction, evidencing that the half-odd-integer spectrum is a property of spatial non-orientability alone, separable from the chiral invariant.

### 1.3 Target venue

| Tier | Venue | Fit |
|---|---|---|
| Primary | *Quantum* (Verein zur Förderung) | Open access, strong topological-walks community, accepts focused method/theory papers with clean numerics. |
| Primary | *Phys. Rev. Research* | Broader scope, fast turnaround, expects numerical rigor. |
| Secondary | *Phys. Rev. A* | Traditional QI venue; conservative reviewers may object to ML-adjacent framing — keep framing physics-first. |
| Secondary | *J. Phys. A: Math. Theor.* | Math-physics-leaning; favors clean theorem-centric papers. |
| Stretch | *PRX Quantum* | Only if T2 lands as a strict ℤ × ℤ → ℤ₂ reduction with a clean proof. |
| Backup (lower) | *Quantum Information Processing* | Reliable Q1 backup. |

### 1.4 Working mode

Two parallel work tracks (theory, numerics), running concurrently from spec lock. Joint anchors at: (a) spec lock after literature check, (b) spectrum cross-check, (c) draft merge. **No phases.** If one track stalls, the other continues. Authorship and credit conventions per Section 11.

---

## 2. Background, Pivot, and What This Project Is Not

### 2.1 Project genealogy

The project began as a classical-ML investigation: encoding data on a Möbius strip in $\mathbb{R}^4$ via the fiber-bundle map $\varphi(s,t) = (\cos s, \sin s, t\cos\frac{s}{2}, t\sin\frac{s}{2})$, with downstream applications in topology-constrained VAEs, deck-augmentation, and AI-side topics. That body of work is preserved in the project's git history (commit prior to 2026-05-07) but is **not** the basis of this paper. The user's stated intent was always quantum computing / quantum information; the classical-ML scoping was a misdirection corrected in the 2026-05-07 working session.

### 2.2 Why a quantum walk on a Möbius graph

The Möbius strip is the simplest non-trivial principal $\mathbb{Z}_2$-bundle. In the QC/QI domain, $\mathbb{Z}_2$ structure is fundamental to: spin-½ / SU(2) double cover, fermion parity, time-reversal $T^2 = \pm 1$, particle-hole symmetry $C^2 = 1$, $\pi$-Berry phases, Floquet $\pi$-modes, and topological invariants in symmetry classes D and BDI. A discrete-time quantum walk on a Möbius graph is the *minimal* setting that:

(a) places a $\mathbb{Z}_2$ topological constraint into a unitary quantum dynamical system,
(b) is exactly simulable on a laptop ($L \le 200$ sites, dim $\le 1000$), and
(c) connects to a literature with established topological-classification machinery (Kitagawa 2010, Asbóth–Edge 2015, Cedzich et al.).

We are *not* claiming the Möbius walk is a universal QC primitive or a hardware proposal. We are claiming it is a tractable model where non-orientability produces theorem-level consequences in unitary dynamics — a "minimal classifying space" demonstration for $\mathbb{Z}_2$-Floquet phenomena.

### 2.3 What this project is explicitly not

- **Not** a quantum-walk algorithm paper (no claim of algorithmic speedup).
- **Not** a hardware proposal (no implementation in photonic/ion-trap/circuit hardware).
- **Not** a continuous-time quantum walk (CTQW) paper. CTQW on Möbius is a separate project — different topological framework (Berry curvature of band structure rather than Floquet winding). Mentioned in Discussion only.
- **Not** a classical-ML latent-space paper. The original `mobius_latent_space_complete.md` framing is permanently retired.
- **Not** a quantum-error-correction paper. Möbius surface codes are interesting; that's a follow-up project.
- **Not** the same as the Tomal & Shafin metric-preserving-autoencoder line (arXiv:2512.15801). No autoencoders, no learning, no fidelity-preserving constructions in this project.

---

## 3. Mathematical Setup

### 3.1 The Möbius graph

Let $L \in \mathbb{Z}_{\ge 4}$, with parity preferences for $L$ noted per experiment in Part 6.

**Position space:** $\mathcal{P}_L = \mathbb{Z}/L\mathbb{Z} = \{0, 1, \dots, L-1\}$, identified with vertices on a circle.

**Coin space:** $\mathcal{C}_d = \mathbb{C}^d$, with $d = 2$ for split-step, Hadamard; $d = 3$ for the Grover coin walk.

**Walker Hilbert space (coined walkers):** $\mathcal{H}_L = \ell^2(\mathcal{P}_L) \otimes \mathcal{C}_d$, of complex dimension $Ld$.

**Cylinder graph $\mathcal{G}_L^{\text{cyl}}$:** position lives on $\mathbb{Z}/L\mathbb{Z}$ with periodic boundary $\psi(x+L, c) = \psi(x, c)$. This is the standard reference.

**Möbius graph $\mathcal{G}_L^{\text{Möb}}$ (coined walkers):** position lives on $\mathbb{Z}/L\mathbb{Z}$ with twisted boundary $\psi(x+L, c) = \Sigma\,\psi(x, c)$, where $\Sigma$ is the **deck operator on coin** — a unitary on $\mathcal{C}_d$ with $\Sigma^2 = \mathbb{I}_d$. For coined walkers the two graphs share the same vertex set and Hilbert space, differing only in the boundary identification encoded in the walk operator.

**Möbius ladder graph $M_L$ (coinless walkers; for Szegedy contrast).** Because the Szegedy walk is coinless, the deck-operator-on-coin construction does not apply: a coinless walker on a 1D position circle cannot distinguish cylinder from Möbius. For the Szegedy contrast (T5) we instead use the **Möbius ladder** $M_L$, a standard graph-theoretic object:
- Vertex set: $V(M_L) = \{(x, r) : x \in \mathbb{Z}/L\mathbb{Z},\ r \in \{0, 1\}\}$ — two rows of $L$ vertices, total $|V| = 2L$.
- Edges (in-row): $(x, r) \sim (x+1, r)$ for $x \in \{0, 1, \dots, L-2\}$, $r \in \{0, 1\}$.
- Edges (rung): $(x, 0) \sim (x, 1)$ for all $x$.
- Möbius identification (twisted boundary): $(L-1, 0) \sim (0, 1)$ and $(L-1, 1) \sim (0, 0)$.

Result: a 3-regular non-orientable graph. The cylinder counterpart is the prism graph $Y_L$, identical except the boundary identifications are $(L-1, r) \sim (0, r)$ (untwisted). Adjacency matrices differ between $M_L$ and $Y_L$, so the Szegedy walker on each is distinct.

**Notation convention.** Throughout this document, $\mathcal{G}_L^{\text{Möb}}$ refers to the coined-walker Möbius graph (1D + coin twist). $M_L$ refers to the Möbius ladder graph (2L-vertex graph for coinless walkers). The two are different objects with different roles; do not conflate them.

### 3.2 The deck operator $\Sigma$ — choice and consequences

**This is the most subtle modeling choice in the project.** Different choices of $\Sigma$ give *different* Möbius walkers, with *different* topological structure. The choice is not unique and the project must commit to one (with justification) and at most one variant for follow-up.

**Constraint for the quotient construction.** If we want the Möbius walker to be the restriction of a $2L$-cylinder walker to the deck-invariant subspace (a clean and standard construction), then $\Sigma$ must commute with the cylinder walk operator. For the standard split-step DTQW with coin rotations $R(\theta) = \exp(-i\theta\sigma_y/2)$ and the spin-dependent shift, the only $\Sigma$ commuting with both factors is $\Sigma \propto \mathbb{I}$, i.e., **$\Sigma = -\mathbb{I}$** (anti-periodic boundary, the only non-trivial choice up to phase).

**Stronger Möbius structure (intrinsic walker).** If we want $\Sigma$ to be a non-trivial coin operator (e.g., $\Sigma = \sigma_x$), the walker is *not* a quotient of a cylinder walker. It is intrinsically Möbius, with the deck operator applied at the seam — but the standard "spin-dependent shift" then has unitarity issues at the seam (collisions between R-coin wraparound flipped to L-coin and the existing L-coin trajectory). A consistent intrinsic walker requires modifying the shift structure as well, giving a fundamentally different walk.

**Project commitment:** The **canonical Möbius walker for this paper uses $\Sigma = -\mathbb{I}$** — anti-periodic boundary, the quotient-construction-compatible choice. All theorem proofs and primary numerical results are stated for this canonical walker. The intrinsic walker with $\Sigma = \sigma_x$ is mentioned in Section 6.2 as a possible follow-up project but is **not** part of the paper.

**Cautions on this choice (read carefully):**

- $\Sigma = -\mathbb{I}$ is a global phase $-1$ on coin. This is the *minimal* deck operator and gives a Möbius BC equivalent to anti-periodicity. It is non-trivial topologically (one full loop ≠ identity), but it does not mix coin states.
- Because $\Sigma$ commutes with all coin operations, the chiral symmetry $\Gamma$ of the cylinder walker lifts trivially to Möbius. This means **there is no $\Gamma$-multivaluedness** on Möbius. Earlier informal discussion in this project's correspondence speculated about a clean ℤ × ℤ → ℤ₂ reduction via $\Gamma$ multivaluedness; that mechanism does not apply for the canonical walker. The actual T2 mechanism (TRIM-exclusion) is detailed in Section 5.2.
- The "clean ℤ × ℤ → ℤ₂ reduction" is **not promised** by this spec. T2 is an open research question with three possible outcomes: (a) phase-boundary modification only (modest result, still publishable), (b) genuine ℤ × ℤ → ℤ₂ reduction via a different mechanism (winding-integral discretization on the half-odd-integer momentum lattice), (c) no topological consequence beyond T1 (worst case, paper still survives on T1+T3+T4+T5).

### 3.3 Cylinder reference

For every Möbius construction below, a cylinder counterpart is defined by replacing $\Sigma$ with $\mathbb{I}$ (periodic boundary). The cylinder walker is the published baseline; we reproduce known cylinder results numerically before claiming any Möbius result. No exceptions.

---

## 4. Walk Operators — Exact Specifications

### 4.1 Notation

| Symbol | Meaning |
|---|---|
| $\|x, c\rangle$ | Walker state at position $x$, coin $c$. $x \in \mathbb{Z}/L\mathbb{Z}$, $c \in \{R, L\}$ (or $c \in \{0, +, -\}$ for three-state). |
| $\sigma_x, \sigma_y, \sigma_z$ | Pauli matrices in the $\{\|R\rangle, \|L\rangle\}$ basis. $\|R\rangle = (1, 0)^T$, $\|L\rangle = (0, 1)^T$. |
| $R(\theta)$ | Coin rotation $e^{-i\theta\sigma_y/2}$. Real-valued matrix. |
| $H$ | Hadamard coin $\frac{1}{\sqrt 2}\begin{pmatrix}1 & 1\\1 & -1\end{pmatrix}$. |
| $S_+, S_-$ | Spin-dependent shifts (defined below). |
| $T$ | Position translation $T\|x\rangle = \|x+1\rangle$ (mod $L$). |
| $\Sigma$ | Deck operator on coin. Canonical choice: $\Sigma = -\mathbb{I}_d$. |
| $\Gamma$ | Chiral symmetry operator (when present). |
| $U^{\text{cyl}}, U^{\text{Möb}}$ | Walk operators on cylinder, Möbius. |

All position arithmetic is mod $L$ on cylinder, and on Möbius with the boundary-condition phase $-1$ applied to the coin component when crossing the seam $x = L-1 \to x = 0$ (or $x = 0 \to x = L-1$ for left-shifts).

### 4.2 Split-step DTQW (canonical, $d = 2$)

**Coin rotations:**
$$R(\theta) = e^{-i\theta\sigma_y/2} = \begin{pmatrix}\cos(\theta/2) & -\sin(\theta/2)\\ \sin(\theta/2) & \cos(\theta/2)\end{pmatrix}$$

**Spin-dependent shifts on cylinder:**
$$S_+ = T \otimes |R\rangle\langle R| + \mathbb{I} \otimes |L\rangle\langle L|, \qquad S_- = \mathbb{I} \otimes |R\rangle\langle R| + T^{-1} \otimes |L\rangle\langle L|$$

In words: $S_+$ shifts R-movers right by one and leaves L-movers stationary; $S_-$ leaves R-movers stationary and shifts L-movers left by one. This is the Kitagawa et al. 2010 split-step convention.

**Cylinder walk:** $U^{\text{cyl}}_{ss}(\theta_1, \theta_2) := S_- \, R(\theta_2) \, S_+ \, R(\theta_1)$.

**Möbius walk (canonical, $\Sigma = -\mathbb{I}$):** Identical operator form; the difference enters via the boundary condition imposed on $\mathcal{H}_L$:
$$\psi(x+L, c) = -\psi(x, c) \text{ for all } c.$$

Equivalently: realize the Möbius walker as the cylinder walker on a $2L$-position lattice, restricted to the anti-periodic subspace $\{\psi : \psi(x+L) = -\psi(x)\}$. This subspace has dimension $2L \cdot d / 2 = Ld$, matching the Möbius Hilbert space.

**Chiral symmetry.** The standard split-step DTQW satisfies $\Gamma U^{\text{cyl}}_{ss}(\theta_1, \theta_2) \Gamma^\dagger = (U^{\text{cyl}}_{ss})^\dagger$ for an appropriate $\Gamma$ (typically a position-independent coin operator; the explicit form depends on protocol convention and is to be derived during Theory track day 1). The chiral symmetry persists on the Möbius walker for $\Sigma = -\mathbb{I}$ since $\Sigma$ commutes with $\Gamma$.

### 4.3 Hadamard DTQW ($d = 2$, simpler)

**Coin:** $H$ (constant, no parameters).

**Walk:** $U^{\text{cyl}}_H = (S_+ S_-^\dagger) \, (\mathbb{I} \otimes H) = S_{HW} \, (\mathbb{I} \otimes H)$, where $S_{HW} = S_+ S_-^\dagger$ is the standard Hadamard-walk shift moving R-movers right and L-movers left in one step:
$$S_{HW} = T \otimes |R\rangle\langle R| + T^{-1} \otimes |L\rangle\langle L|.$$

**Möbius:** Same operator form, anti-periodic BC.

This walker has *no continuous parameters* — the topological structure (if any) is fixed. Its role in the paper is universality demonstration (T4): a different protocol exhibiting the same spectrum signatures.

### 4.4 Three-state Grover walk ($d = 3$)

**Coin:** Grover diffusion $G_3 = \frac{2}{3}J_3 - \mathbb{I}_3$, where $J_3$ is the all-ones $3\times 3$ matrix.

**Coin basis:** $\{|0\rangle, |+\rangle, |-\rangle\}$ — stay, right, left.

**Shift:** $S_3 = \mathbb{I}\otimes|0\rangle\langle 0| + T\otimes|+\rangle\langle+| + T^{-1}\otimes|-\rangle\langle-|$.

**Walk:** $U^{\text{cyl}}_3 = S_3 (\mathbb{I} \otimes G_3)$.

**Möbius:** Same form, anti-periodic BC ($\Sigma = -\mathbb{I}_3$).

This walker has a richer coin space ($d = 3$) and is the third protocol for the universality check.

### 4.5 Szegedy walk on Möbius ladder graph (contrast, coinless)

The Szegedy walk is the quantization of a classical Markov chain on a graph. Because Szegedy is coinless, it operates on the **Möbius ladder graph $M_L$** defined in §3.1, not on the coined-walker Möbius graph $\mathcal{G}_L^{\text{Möb}}$.

**Underlying classical chain:** uniform random walk on $M_L$ — each vertex transitions with equal probability $1/3$ to each of its three neighbors (in-row neighbor on each side, rung partner). Transition matrix $P$ is the doubly-stochastic adjacency-normalized matrix of $M_L$.

**Hilbert space:** $\mathbb{C}^{V \times V}$ restricted to the edge subspace, equivalently $\mathbb{C}^{|\vec{E}|}$ where $|\vec{E}|$ is the number of directed edges. $M_L$ has $3L$ undirected edges, hence $|\vec{E}| = 6L$.

**Walk:** $U^{\text{Sze}}_{M_L} = S \cdot (2\Pi_P - \mathbb{I})$, where $\Pi_P = \sum_v |\pi_v\rangle\langle\pi_v|$ is the projector onto the span of "outgoing" superposition states $|\pi_v\rangle = \sum_w \sqrt{P_{vw}}\,|v\rangle|w\rangle$, and $S$ is the swap operator on edge labels: $S|v\rangle|w\rangle = |w\rangle|v\rangle$.

**Cylinder counterpart:** identical construction on the prism graph $Y_L$ (untwisted boundary) — gives $U^{\text{Sze}}_{Y_L}$ as the comparison Szegedy walker.

The Szegedy walk has no coin space — the Möbius geometry enters entirely through the difference between adjacency matrices of $M_L$ and $Y_L$. It is the "minimum-coin" comparison for T5.

### 4.6 Cross-protocol notational consistency

All four walks are parameterized so the cylinder vs. Möbius distinction lies *entirely* in the boundary condition. No protocol uses position-dependent operators that smell of the boundary. This ensures the comparison is clean and the Möbius effect cannot be confused with a difference in protocol structure.

---

## 5. Theorems (Targets) and Proof Sketches

The five claims below are the paper's core. Each is stated as a target (what we hope to prove), a proof strategy (how we would prove it), and a difficulty assessment. Numerical demonstrations are in Part 6.

### 5.1 T1 — Spectrum (theorem)

**Statement.** Let $U^{\text{Möb}}_{ss}(\theta_1, \theta_2)$ be the Möbius split-step DTQW with $\Sigma = -\mathbb{I}_2$ on $\mathcal{H}_L$. Its quasi-energy spectrum is
$$\{\,e^{-i\varepsilon^{\text{Möb}}_n(\theta_1, \theta_2)}\,\}_{n=0}^{2L-1}, \quad \varepsilon^{\text{Möb}}_n(\theta_1, \theta_2) = \pm\varepsilon\!\left(\theta_1, \theta_2;\, k_n^{\text{Möb}}\right), \quad k_n^{\text{Möb}} = \frac{(2n+1)\pi}{L},$$
where $\varepsilon(\theta_1, \theta_2; k)$ is the bulk dispersion of the cylinder split-step DTQW. The cylinder counterpart has $k_n^{\text{cyl}} = 2\pi n / L$, integer-quantized.

**Consequence.** The TRIMs $k = 0$ and $k = \pi$ (when $L$ is even) are present in the cylinder spectrum but **absent from the Möbius spectrum** for all $L$.

**Proof strategy.** Bloch–Floquet decomposition. The cylinder walker on a $2L$-position lattice is translation-invariant, hence diagonalizes in momentum space with $k \in \frac{2\pi}{2L}\mathbb{Z}/2\pi\mathbb{Z}$, i.e., $k \in \{0, \pi/L, 2\pi/L, \dots, (2L-1)\pi/L\}$. Restriction to the anti-periodic subspace $\psi(x+L) = -\psi(x)$ projects to states satisfying $e^{ikL} = -1$, i.e., $k \in \{(2n+1)\pi/L : n = 0, \dots, L-1\}$. The bulk dispersion $\varepsilon(\theta_1, \theta_2; k)$ is unchanged. ∎

**Difficulty:** Low. Standard Bloch–Floquet exercise with a twisted BC. One page of derivation in the paper.

### 5.2 T2 — Phase diagram modification (theorem + numerics; *open form*)

**Background.** The cylinder split-step chiral DTQW has $(\theta_1, \theta_2) \in [0, \pi]^2$ phase diagram with phases labeled by $(w_+, w_-) \in \mathbb{Z}^2$ winding numbers in chiral subspaces. Phase boundaries occur where the bulk gap closes — i.e., where $\varepsilon(\theta_1, \theta_2; k) = 0$ or $\pi$ for some $k$ in the Brillouin zone. Asbóth–Edge (PRB 91, 2015) showed gap closings at the TRIMs $k = 0, \pi$ are responsible for specific transitions.

**Target statement.** On the Möbius walker, gap closings can only occur at the half-odd-integer momenta. In the thermodynamic limit $L \to \infty$, the BZ becomes continuous and the difference vanishes; at finite $L$, certain TRIM-localized gap closings are absent. The paper claims: for $L$ in a regime where this matters, the topological phase boundary in $(\theta_1, \theta_2)$ space is a measurably modified set.

**Open question — three possible refinements (research outcome of the project):**

(a) **TRIM-exclusion only (modest):** Phase boundaries shift by $O(1/L)$ from the cylinder result. Still a clean theorem; less dramatic than ℤ × ℤ → ℤ₂.

(b) **Winding-integer reduction (strong):** The winding-number formula evaluated as a Riemann sum over half-odd-integer momenta yields a different integer than the cylinder sum, mod 2 — giving an effective ℤ × ℤ → ℤ₂ reduction. This is the most striking outcome but is *not promised* by this spec.

(c) **No topological reduction (weakest):** T1 holds, but the topological invariant computed on Möbius equals the cylinder one in the thermodynamic limit. The paper's contribution is then T1 + T3 + T4 + T5 (still publishable; the project is robust to this outcome).

**Proof strategy.** Compute the winding-number integral $w_\pm = \frac{1}{2\pi}\oint_{BZ} dk\,\partial_k \phi_\pm(k)$ for the chiral subspaces, on cylinder (continuous BZ) and Möbius (half-odd-integer-quantized BZ). Compare. The discrepancy, if any, is the T2 result.

**Difficulty:** Medium-high. The integral form is standard; the discrete vs. continuous comparison and the resulting integer/parity result are the substance.

**Caution:** Resolution of which of (a), (b), (c) holds is itself a research outcome and should not be promised in advance. Section 7's work plan includes a checkpoint where T2's form is committed before the proof structure is written.

### 5.3 T3 — Boundary modes on a cut walker (conditional on T2 outcome)

**Caveat (read first).** With the canonical $\Sigma = -\mathbb{I}$, the closed Möbius walker has uniform anti-periodic BC; there is no localized seam. Cutting the walker open at $x = 0$ and $x = L-1$ produces a finite open chain whose physical Hamiltonian is identical to a cut cylinder. T3 therefore has Möbius-specific content **only if T2 lands as 5.2-b** (the genuine ℤ × ℤ → ℤ₂ topological reduction); otherwise T3 reduces to a corollary of standard chiral-DTQW edge-mode counting (Asbóth–Edge 2015) with no Möbius-specific signature.

**Statement (conditional on T2 yielding 5.2-b).** Let $w_{\text{Möb}} \in \mathbb{Z}_2$ be the reduced topological invariant of the closed Möbius walker. On a finite open chain whose bulk parameters $(\theta_1, \theta_2)$ correspond to a topologically non-trivial Möbius phase ($w_{\text{Möb}} = 1$), there exist edge-localized zero-quasi-energy modes at both hard walls. The mode count differs from the cut-cylinder case in the parameter regime where $(w_+^{\text{cyl}}, w_-^{\text{cyl}})$ on cylinder gives a different $\mathbb{Z}_2$ parity than $w_{\text{Möb}}$.

**Statement (conditional on T2 yielding 5.2-a or 5.2-c).** T3 collapses to standard chiral-DTQW bulk-edge correspondence on the cut walker (Asbóth–Edge). The cut Möbius walker and cut cylinder walker yield the same edge-mode counts in the thermodynamic limit; finite-size differences exist due to the half-odd-integer momentum quantization of the closed walker but vanish for $L \to \infty$ on an open chain (which has no closed BC).

**Proof strategy.** Standard transfer-matrix construction adapted from Asbóth–Edge. Conditional content depends on T2's bulk invariant.

**Difficulty:** Medium. The numerical experiment N3 is well-defined regardless of T2's outcome; only the *interpretation* is conditional. If T2 is unfavorable, T3 may be folded into a single paragraph rather than a section.

### 5.4 T4 — Universality across coined Floquet protocols (numerics + sketch)

**Statement.** T1 holds for any coined DTQW (Hadamard, three-state Grover, generic split-step variants) on the Möbius graph with $\Sigma = -\mathbb{I}$. The qualitative phase-diagram modifications of T2 hold across the protocol class.

**Argument:** The half-odd-integer momentum quantization is a property of the boundary condition, not the walk operator. Any coined Floquet walk on the same Hilbert space inherits the BC. The protocol-independent statement follows by Bloch–Floquet for each walker.

**Difficulty:** Low (sketch); the *demonstration* requires running each walker and confirming.

### 5.5 T5 — Szegedy contrast on Möbius ladder vs. prism graph

**Statement.** The Szegedy walk on the Möbius ladder graph $M_L$ has a quasi-energy spectrum distinguishable from the Szegedy walk on the prism graph $Y_L$ (cylinder counterpart). Specifically, the spectrum of $U^{\text{Sze}}_{M_L}$ contains modes traceable to the twisted-boundary structure of $M_L$'s adjacency matrix that are absent from $U^{\text{Sze}}_{Y_L}$. The signature does **not** require any chiral symmetry on the walker; the spectral distinction is induced purely by spatial non-orientability of the underlying graph.

**Proof strategy.** Direct spectral comparison: diagonalize $U^{\text{Sze}}_{M_L}$ and $U^{\text{Sze}}_{Y_L}$, identify the modes specific to each. Use the symmetry decomposition of $M_L$ (which has $\mathbb{Z}_2$ rung-swap symmetry coupled with a half-period rotation) to derive the spectral split analytically.

**Difficulty:** Low. Both graphs have published spectra in the algebraic graph theory literature; Szegedy quantization is a mechanical step on each.

**Role in the paper.** T5 establishes the structural separation: spatial non-orientability (graph topology) and chiral protection (coin-space symmetry) are *independent* contributors to ℤ₂ structure in Floquet walks. This separation is the paper's core conceptual contribution beyond the individual claims T1–T4.

### 5.6 The story arc

**Two effects, cleanly separated by walker choice:**
- *Spatial non-orientability* contributes the half-odd-integer spectrum (T1, T5).
- *Spatial non-orientability + chiral protection* together produce the ℤ₂ topological structure (T2, T3, T4).

This separation is the paper's structural contribution.

---

## 6. Numerical Experiments

All experiments run on a laptop. NumPy/SciPy first; JAX port deferred. Sizes $L \in \{50, 100, 200\}$ unless noted. Every experiment has a cylinder counterpart run as a sanity baseline before any Möbius result is reported.

### 6.1 N1 — Spectrum visualization (matches T1)

**Setup:** $U^{\text{Möb}}_{ss}(\theta_1, \theta_2)$ for fixed $(\theta_1, \theta_2) = (\pi/3, \pi/4)$ (off-resonant, gapped phase). $L = 50, 100, 200$.

**Procedure:** Diagonalize $U^{\text{Möb}}$. Plot eigenvalues on the unit circle. Plot quasi-energy bands $\varepsilon(k)$ vs. $k$, with momentum sampling $k = 2\pi m/L$ on cylinder and $k = (2m+1)\pi/L$ on Möbius.

**Expected result:** Möbius eigenvalues sit at half-odd-integer momenta on the cylinder dispersion curve, missing the integer-momentum points.

**Figure:** 1 figure, 2 subplots (cylinder vs. Möbius spectrum, side by side).

### 6.2 N2 — Phase diagram (matches T2)

**Setup:** Sweep $(\theta_1, \theta_2) \in [0, \pi]^2$ on a $51 \times 51$ grid. For each grid point, compute the chiral winding number(s) $(w_+, w_-)$ for cylinder and Möbius walkers. $L = 100$.

**Procedure:** Use the Asbóth–Edge winding formula adapted to discrete momentum sums. Color the $(\theta_1, \theta_2)$ plane by phase label.

**Expected result:** Phase boundaries differ between cylinder and Möbius. Specific transitions absent on Möbius (those mediated by $k = 0, \pi$ gap closings).

**Figure:** 1 figure, 2 subplots (cylinder phase diagram, Möbius phase diagram). Plus a difference plot highlighting the boundary shifts.

### 6.3 N3 — Edge modes on cut Möbius (matches T3)

**Setup:** $U^{\text{Möb}}_{ss}$ with hard-wall boundaries at $x = 0, L-1$. Choose $(\theta_1, \theta_2)$ in two phases — one with bulk winding $w = 0$, one with $w = 1$. $L = 100$.

**Procedure:** Diagonalize. Identify zero-quasi-energy modes. Plot their position-density profile.

**Expected result:** Edge-localized zero modes in the $w = 1$ phase, no zero modes in the $w = 0$ phase. Mode count tracks $|w|$.

**Figure:** 1 figure, 2 subplots (mode density in trivial vs. topological phase).

### 6.4 N4 — Return-amplitude topological signature

**Setup:** Initial state $|x_0 = 0, R\rangle$. Evolve under $U^{\text{Möb}}_{ss}$ for $T$ steps. Measure return amplitude $\mathcal{A}(T) = \langle x_0, R | U^T | x_0, R\rangle$.

**Procedure:** Compute $\mathcal{A}(L)$ vs. $\mathcal{A}(2L)$. Compare with cylinder.

**Expected result:** Cylinder has $\mathcal{A}^{\text{cyl}}(L) = \mathcal{A}^{\text{cyl}}(2L)$ up to dispersion; Möbius has a sign-flip-like signature in $\mathcal{A}(L)$ relative to $\mathcal{A}(2L)$ traceable to the anti-periodic BC.

**Figure:** 1 figure, 4 subplots ($|\mathcal{A}(T)|$ for cylinder, Möbius, $T$ from 0 to $4L$).

### 6.5 N5 — Hadamard universality (matches T4)

**Setup:** Hadamard walker (Section 4.3) on cylinder and Möbius. $L = 100$.

**Procedure:** Spectrum (matches N1 for Hadamard), and a single phase-diagram-equivalent plot (Hadamard has no continuous parameters, so this is a "yes/no" test of the spectrum signature).

**Expected result:** Half-odd-integer spectrum on Möbius Hadamard.

**Figure:** 1 figure, 2 subplots.

### 6.6 N6 — Three-state Grover universality (matches T4)

**Setup:** Grover walker (Section 4.4). $L = 100$.

**Procedure:** Spectrum on cylinder and Möbius. (No phase diagram — Grover walker has no parameters.)

**Expected result:** Half-odd-integer spectrum on Möbius Grover, with $d = 3$ coin space giving three bands per momentum.

**Figure:** 1 figure, 2 subplots.

### 6.7 N7 — Szegedy contrast on Möbius ladder vs. prism graph (matches T5)

**Setup:** Szegedy walks $U^{\text{Sze}}_{M_L}$ and $U^{\text{Sze}}_{Y_L}$ on the Möbius ladder $M_L$ and prism graph $Y_L$ respectively. $L = 50, 100$.

**Procedure:** Diagonalize both walk operators. Identify spectral differences: which eigenvalues are present in $M_L$ but not $Y_L$, and vice versa. Compute mixing times and hitting times. Use symmetry decomposition (rung-swap × position-rotation) to label eigenmodes.

**Expected result:** Spectrum of $M_L$ Szegedy contains modes traceable to the twisted boundary; symmetry-decomposed eigenvalues differ from $Y_L$. *No* chiral-symmetry-protected topological invariant (Szegedy is coinless, no chirality).

**Figure:** 1 figure, 2-3 subplots (cylinder spectrum, Möbius ladder spectrum, difference plot or symmetry-decomposed eigenvalue table).

### 6.8 N0 — Sanity baseline (mandatory before any other experiment)

**Reproduce known cylinder results from Kitagawa et al. 2010 and Asbóth–Edge 2015.** Specifically:

- Cylinder split-step phase diagram matching Asbóth–Edge Fig. 2.
- Zero-mode count matching their Eq. (37) for finite chains.

**Pass threshold:** Phase-diagram match to within boundary thickness < 0.02 in $(\theta_1, \theta_2)$ units. Zero-mode count exactly matches.

**This is a hard gate.** No Möbius result is reported until N0 passes.

### 6.9 Reproducibility, code organization, and figures

**Code:** GitHub repository, MIT license, single source of truth.
**Structure:**
```
mobius_dtqw/
  walkers/             # WalkProtocol classes (Split, Hadamard, Grover, Szegedy)
  topology/            # boundary conditions (Cylinder, Möbius), shift operators
  observables/         # spectrum, winding, return amplitude, edge modes
  experiments/         # N0..N7 reproduction scripts
  notebooks/           # one notebook per figure
  tests/               # pytest covering protocol unitarity, BC consistency, baseline reproduction
  README.md
```

**Reproducibility commitment:** every figure in the paper is generated by exactly one notebook. Every notebook runs in < 5 minutes on a laptop. No `if __name__ == "__main__"` files generating figures.

**Test suite (mandatory before paper submission):**
- $U^{\text{cyl}}, U^{\text{Möb}}$ unitary to relative error $< 10^{-12}$.
- BC implemented correctly: $\psi(x+L) = -\psi(x)$ for Möbius, $+\psi(x)$ for cylinder, verified by direct application.
- Cylinder spectrum reproduces Kitagawa 2010 Fig. 1 to relative error $< 10^{-10}$.
- Sum of squared eigenstate components = 1 (exact).

---

## 7. Work Plan — Parallel Tracks

Two tracks. Concurrent. No phases. Joint anchors at three milestones.

### 7.1 Theory track

Owner: one person (suggested: whoever has stronger background in topology / band structure / Bloch–Floquet).

**Deliverables (flat checklist):**

- [ ] T-D1. Write explicit walk operators $U^{\text{cyl}}_{ss}, U^{\text{Möb}}_{ss}$ in position+coin form with all conventions fixed. Output: typeset LaTeX section.
- [ ] T-D2. Bloch–Floquet derivation for both walkers; derive bulk dispersion $\varepsilon(\theta_1, \theta_2; k)$. Output: T1 proof.
- [ ] T-D3. Identify the chiral symmetry $\Gamma$ of the cylinder split-step DTQW; verify it persists on Möbius (it should, since $\Gamma$ commutes with $\Sigma = -\mathbb{I}$).
- [ ] T-D4. Compute the winding-number integrals on cylinder and Möbius; commit to T2 form (a/b/c per Section 5.2). This is the critical decision point.
- [ ] T-D5. Construct edge zero-modes on a cut Möbius walker (T3 sketch).
- [ ] T-D6. Universality argument (T4 sketch).
- [ ] T-D7. Szegedy walker spectral analysis (T5).
- [ ] T-D8. Write paper sections §2 (background), §3 (model), §4 (theorems and proofs), §6 (Szegedy contrast), §7 (discussion).

**Suggested order of T-D items:** T-D1 → T-D2 → T-D3 → T-D5 → (T-D4 in parallel with N2) → T-D6 → T-D7 → T-D8. T-D4 is gated on N2's numerical winding-number sweep telling us which T2 form to commit to.

### 7.2 Numerics track

Owner: the other person.

**Deliverables (flat checklist):**

- [ ] N-D1. Build core walker simulator. NumPy/SciPy. Modular: graph topology (cylinder/Möbius/cut) is a parameter, walk protocol (split/Hadamard/Grover/Szegedy) is a parameter. Comprehensive test suite.
- [ ] N-D2. Pass N0 sanity baseline.
- [ ] N-D3. Run N1 (spectrum). Generate Figure 1.
- [ ] N-D4. Run N2 (phase diagram). Generate Figure 2 + difference plot. **Report findings to Theory track to inform T-D4.**
- [ ] N-D5. Run N3 (edge modes). Generate Figure 3.
- [ ] N-D6. Run N4 (return amplitude). Generate Figure 4.
- [ ] N-D7. Run N5, N6 (universality). Generate Figures 5, 6.
- [ ] N-D8. Run N7 (Szegedy contrast). Generate Figure 7.
- [ ] N-D9. Code release: clean repo, README, license, reproducibility notebook.
- [ ] N-D10. Write paper section §5 (numerics) plus figure captions.

### 7.3 Joint anchors (three checkpoints, no fixed schedule)

**Anchor 1 — Spec lock.** Both authors review this document; sign off on operator definitions, theorem statements, and numerical experiment specs. Possible amendments: choice of $\Sigma$ (default $-\mathbb{I}$ unless literature check forces a pivot), scope inclusions/exclusions. Once signed, this document becomes immutable for the project's duration; later amendments require an explicit revision history at the bottom.

**Anchor 2 — Spectrum cross-check.** Numerics track reproduces the analytical T1 spectrum from Theory track to relative error $< 10^{-10}$. *Both* tracks must agree before either commits to downstream work. If disagreement: stop both tracks, debug the inconsistency.

**Anchor 3 — Draft merge.** Both tracks have complete drafts of their assigned sections. Review and merge into single paper. Joint authorship of §1 (intro) and §7 (discussion).

### 7.4 Joint work outside the tracks

- Bibliography curation (both authors).
- Response to reviewers (both authors).
- Submission, formatting, code release coordination (both authors).
- Tony Stark / Endgame Möbius motivation (omit from the paper text; this is a private joke).

---

## 8. Risks and Cautions — Comprehensive Register

This section is exhaustive. Read before committing time.

### 8.1 Project-level risks

**R1 — Literature pre-emption.** The single highest risk. If a published paper covers (a) the Möbius split-step DTQW spectrum *and* (b) the topological phase-diagram modification, this project is dead. Mitigation: Section 9 protocol, with a hard-stop pivot to Angle 2 (Möbius holonomic ℤ₂ gate) or Angle 3 (Möbius surface code) if pre-empted. Conduct the pre-emption check before writing any code.

**R2 — Scope creep.** The temptation to add the intrinsic Möbius walker ($\Sigma = \sigma_x$), CTQW, multi-walker walks, anyonic walks, etc. is significant. Mitigation: this spec is the scope. Additions require an explicit amendment to Anchor 1 with both authors' written agreement.

**R3 — T2 worst-case (5.2-c).** If T2 has no topological consequence beyond TRIM exclusion, the paper still survives on T1 + T3 + T4 + T5 but loses one of its "headline" claims. Reframe accordingly. This is *not* a project killer.

**R4 — Authorship friction.** Duo without advisor; unclear authorship-order norms. Mitigation: agree in advance — primary author = whoever owns more deliverables (likely whoever owns the harder track), corresponding author = same. Both authors have equal contribution in spirit. Document this in Section 11 below.

### 8.2 Mathematical-subtlety risks

**M1 — Deck operator choice.** Section 3.2 commits to $\Sigma = -\mathbb{I}$. If during the literature check we find precedent or a strong physical argument for $\Sigma = \sigma_x$ or other non-trivial choices, the spec may need amendment. Document the reasoning.

**M2 — Chiral symmetry on Möbius.** With $\Sigma = -\mathbb{I}$, the chiral symmetry persists trivially. But the *winding-number integral* on the half-odd-integer momentum lattice may yield a different value than on the integer lattice (T2-b possibility). The discretization-vs.-continuous-BZ subtlety is the technical heart of T2. If we get this wrong, T2 collapses to T2-c.

**M3 — Parity of $L$.** The half-odd-integer momentum set $\{(2n+1)\pi/L\}$ behaves differently for even $L$ vs. odd $L$:
- Even $L$: $\pi$ is a TRIM on cylinder but absent on Möbius.
- Odd $L$: $\pi$ is *also* absent from cylinder spectrum (since $\pi = (2 \cdot L/2)\pi/L$ requires $L$ even); both cylinder and Möbius miss it.
- Always: $k = 0$ is on cylinder, off Möbius.
Mitigation: report results for $L$ even and odd separately; the differences are part of the physics, not a bug.

**M4 — "Seam" terminology.** With $\Sigma = -\mathbb{I}$, the boundary identification is uniform — there is no localized "seam" in the same sense as a Möbius strip embedded in $\mathbb{R}^3$. Edge modes (T3) live on hard-wall cuts, not on the seam. *Avoid the word "seam" in the paper unless explicitly defining it as the BC location.*

**M5 — Bulk-edge correspondence on Möbius.** Standard bulk-edge correspondence assumes a band structure with continuous BZ. On Möbius with finite $L$ the BZ is a discrete set; the correspondence is recovered in the thermodynamic limit. For T3, work at $L \ge 100$ to be safely in the asymptotic regime, and explicitly check finite-size scaling.

### 8.3 Numerical-pitfall risks

**N-R1 — Floating-point eigenvalue degeneracies.** Quasi-energy bands at $\pm\varepsilon$ can be near-degenerate; numerical diagonalization may give noisy eigenvectors. Mitigation: use `scipy.linalg.eig` with explicit reordering by chiral subspace; verify results against `numpy.linalg.eig` and the analytical formula from T1.

**N-R2 — Phase-diagram pixel artifacts.** The phase-diagram Figure 2 may show "transitions" that are pixelation artifacts. Mitigation: subsample at higher resolution along boundary lines; verify using the analytical gap-closing condition derived in T-D4.

**N-R3 — Winding-number sign convention.** The chiral winding number depends on convention ($\Gamma = \sigma_x$ vs. $\sigma_y$, sign of integration direction, etc.). Mitigation: pick one convention, stated explicitly in §3 of the paper, and verify against published cylinder reference numerics (N0).

**N-R4 — Edge-mode count ambiguity.** Zero-quasi-energy modes can be at $\varepsilon = 0$ or $\varepsilon = \pi$ (both are "zeros" on the unit circle in DTQW). Standard chiral DTQW topology uses *both* and the count is $w$ at $\varepsilon = 0$ plus $w$ at $\varepsilon = \pi$. Confusing the two halves the apparent count. Mitigation: report zero-modes separately at $\varepsilon = 0$ and $\varepsilon = \pi$.

**N-R5 — Szegedy vs. coined walk dimensions.** Szegedy walks live on a different Hilbert space ($\mathbb{C}^{|E|}$, edge-based). Don't compare Szegedy spectra directly to coined walk spectra without dimensional matching.

### 8.4 Reviewer-pushback risks

**P1 — "Why Möbius and not just anti-periodic BC?"** The two are equivalent for $\Sigma = -\mathbb{I}$. We must argue the *physical* / *geometric* significance of the Möbius framing — namely, that the anti-periodic BC arises here as the deck operator of a non-trivial principal $\mathbb{Z}_2$-bundle, not as an ad-hoc boundary choice. This connects to fermionic boundary conditions, the $\mathbb{Z}_2$ holonomy structure of the bundle, and the broader story of non-orientable manifolds in QC/QI. Frame the paper this way from §1.

**P2 — "Anti-periodic BC has been studied in DTQW already."** Possible. The literature check must turn up any such precedent. If found: the project's contribution must focus on the *topological invariant* angle (T2, T3) rather than spectrum (T1), and explicitly cite/distinguish from prior work.

**P3 — "What's new beyond Asbóth–Edge?"** Asbóth–Edge (PRB 91, 2015) classified chiral-DTQW topology on cylinders and lines. Our contribution: same classification on a non-orientable graph, with explicit phase-boundary modifications. Frame as a "non-orientable extension" of their work — they will likely be reviewers; cite carefully and respectfully.

**P4 — "Numerics-only paper without a strong theorem."** If T2 lands as 5.2-c (no real topological reduction), the paper is at risk of being characterized as numerical exploration. Mitigation: ensure T1 and T5 have crisp analytical statements with proofs. Even in the worst T2 outcome, the paper has two theorems (T1, T5) plus three numerical demonstrations (T3, T4, plus the phase-diagram boundary shifts).

### 8.5 Process risks specific to a duo without advisor

**D1 — No external sanity check.** Without an advisor, mistakes propagate. Mitigation: Anchor 2 (spectrum cross-check) is a hard gate. If the two tracks disagree, stop and debug. Use referee-style internal review at Anchor 3.

**D2 — Tunnel vision.** Both authors may converge on a single interpretation that's wrong. Mitigation: at Anchor 1 and Anchor 3, each author writes a one-page "if I were a hostile reviewer" critique. Both critiques are addressed before submission.

**D3 — Workload imbalance.** Theory track is bursty (long thinking, occasional outputs); Numerics track is steady. Mitigation: don't measure progress by hours; measure by deliverables completed (the checklists in §7.1, §7.2). Re-balance at Anchor 2 if one track has fallen >2 deliverables behind.

**D4 — Submission deadline pressure.** Unbounded scope + duo + no advisor = risk of indefinite extension. Mitigation: declare a target submission window before Anchor 2 (suggested: 4-5 months from spec lock). If at Anchor 3 the paper is short of all five claims, submit the partial result rather than indefinitely extending.

---

## 9. Literature Pre-emption Protocol

**Mandatory before any code is written.** Allocate one focused afternoon (4-6 hours, both authors) to this check.

### 9.1 Search queries

Run on Google Scholar, arXiv, ADS, and Semantic Scholar:

1. `quantum walk Möbius`
2. `DTQW Möbius`
3. `quantum walk non-orientable`
4. `quantum walk anti-periodic boundary`
5. `quantum walk twisted boundary topological`
6. `Floquet topological walk Möbius`
7. `Szegedy walk Möbius`
8. `Szegedy walk non-orientable graph`

For each query, scan the first 30 results. Read abstracts of any relevant hits.

### 9.2 Citation traversal

Forward-cite the following base papers (look at all subsequent papers citing them):

- Kitagawa, Rudner, Berg, Refael, Demler, *Phys. Rev. A* **82**, 033429 (2010).
- Asbóth, Edge, *Phys. Rev. B* **91**, 195442 (2015).
- Cedzich, Geib, Grünbaum, Stahl, Velázquez, Werner, Werner, *Quantum* **2**, 95 (2018) — chiral DTQW indices.
- Higashikawa, Nakagawa, Ueda, *Phys. Rev. Lett.* **123**, 066403 (2019) — Floquet topological insulators in non-Hermitian systems.
- Rakovszky, Asbóth, *Phys. Rev. A* **92**, 052311 (2015).

Look for any title or abstract mentioning "Möbius," "non-orientable," "anti-periodic," or "twisted."

### 9.3 Hard-stop conditions

If the literature check finds:

- A paper deriving the half-odd-integer spectrum (T1) **and** a phase-diagram or topological-invariant modification (T2) for any chiral DTQW on a Möbius / non-orientable graph: **project pivots to Angle 2 (Möbius holonomic ℤ₂ gate)** or **Angle 3 (Möbius surface code)** from the prior session's discussion. Do not proceed with the current scope.
- A paper deriving T1 alone for any DTQW on a non-orientable graph: **project narrows scope to T2-T5**, citing the prior work for T1. The paper is shorter but still novel.
- A paper deriving the equivalent of T1 for Szegedy walks on non-orientable graphs: **drop T5, focus on T1-T4 only.**
- Nothing matching the project's claims: **proceed as specified.**

### 9.4 Deliverable

A short written summary (1-2 pages, plain Markdown) of the literature-check findings, signed off by both authors. This summary is committed to the project repo as `lit_check_2026-MM-DD.md`. It includes: queries run, key papers found, hard-stop verdict, and (if pivoting) the new scope.

---

## 10. Submission Strategy

### 10.1 Target ordering

1. *Quantum* (primary). Open access; topology + walks community is concentrated there. Editorial process is community-style; expect 2-3 reviewers, 6-10 weeks first decision.
2. *Phys. Rev. Research* (primary alternative). Faster, broader, expects strong numerics.
3. *Phys. Rev. A* (secondary). Standard Q1, conservative reviewers.
4. *J. Phys. A* (secondary). Math-physics-leaning; pitch the paper with theorems first if submitting here.
5. *Quantum Information Processing* (backup).

### 10.2 Pre-submission steps

- Two weeks before submission: full internal review (each author writes hostile-reviewer critique; both critiques addressed).
- One week before: code release with frozen tag matching the submitted paper version.
- Day of: arXiv preprint posted simultaneously with journal submission.

### 10.3 If desk-rejected

If desk-rejected at Quantum or PRR, examine the rejection reason carefully. Common reasons and responses:

- "Out of scope" → resubmit to PRA.
- "Insufficient novelty" → reframe with deeper engagement with cited work; resubmit.
- "Numerical results without strong theorem" → if T2 was 5.2-c, consider strengthening with extra analytical work before resubmitting.

### 10.4 Authorship

To be agreed at Anchor 1 and committed to a private memo:

- Order: by track ownership (suggested: heavier track owner first).
- Both equal-contribution if appropriate.
- Corresponding author: matches first author or explicitly designated.

---

## 11. Code, Reproducibility, and Open Science

### 11.1 Repository

`github.com/<owner>/mobius-dtqw` (public, MIT license, created at Anchor 1).

### 11.2 Stack

- Python 3.11+
- NumPy / SciPy (primary)
- Matplotlib (figures; one figure per notebook)
- pytest (test suite)
- JAX (optional, deferred port)

### 11.3 Reproducibility commitments

- Every figure in the paper generated by exactly one notebook; notebook runs in $< 5$ minutes on a 2024-era laptop.
- All randomness seeded; seeds documented.
- Test suite runs in $< 1$ minute; all tests pass on Python 3.11 and 3.12.
- README contains: install instructions, single-command "reproduce all figures" script, link to arXiv preprint, citation block.

### 11.4 What we are *not* releasing

- Hardware schematics (none).
- Trained ML models (none — there are no ML models in this project).
- Datasets (none — all data is generated from analytic walker definitions).

---

## 12. Glossary

| Term | Definition |
|---|---|
| DTQW | Discrete-time quantum walk. A unitary $U$ acting on $\ell^2(\text{vertices}) \otimes \mathcal{C}_d$. |
| Coin space | The internal $d$-dim Hilbert space carried by the walker; for split-step $d=2$. |
| Coin operator | A unitary $C$ acting only on the coin space. Mixes coin states without moving the walker. |
| Shift | A unitary that translates the walker's position conditioned on the coin state. |
| Cylinder graph | $L$-vertex circle with periodic identification $\psi(x+L) = \psi(x)$. |
| Möbius graph | $L$-vertex circle with twisted identification $\psi(x+L, c) = \Sigma\,\psi(x, c)$. Canonical: $\Sigma = -\mathbb{I}$. |
| Deck operator | $\Sigma$, the unitary on coin space implementing the Möbius identification. Project canonical: $\Sigma = -\mathbb{I}$. |
| Quasi-energy | $\varepsilon$ such that $e^{-i\varepsilon}$ is an eigenvalue of $U$. Defined modulo $2\pi$. |
| TRIM | Time-reversal invariant momentum. In 1D BZ, $k = 0$ and $k = \pi$. |
| Chiral symmetry | $\Gamma U \Gamma^{-1} = U^{-1}$ for some unitary involution $\Gamma$. |
| Winding number | $w = \frac{1}{2\pi}\oint dk\,\partial_k\phi(k)$, integer-valued for chiral systems with gapped bulk. |
| Bulk-edge correspondence | Theorem: number of edge modes = bulk topological invariant. |
| Anchor | A joint checkpoint between the two work tracks. Three anchors total (Section 7.3). |
| Pre-emption | A published paper that already establishes the project's claims; triggers pivot per Section 9.3. |

---

## 13. Key References (preliminary)

Full bibliography to be assembled at draft stage. Below is the spine:

- T. Kitagawa, M. S. Rudner, E. Berg, G. Refael, E. Demler, *Phys. Rev. A* **82**, 033429 (2010). [Foundational DTQW + Floquet topology.]
- J. K. Asbóth, J. M. Edge, *Phys. Rev. B* **91**, 195442 (2015). [Bulk-edge for chiral DTQW.]
- C. Cedzich, T. Geib, F. A. Grünbaum, C. Stahl, L. Velázquez, A. H. Werner, R. F. Werner, *Quantum* **2**, 95 (2018). [Chiral DTQW indices.]
- M. S. Rudner, N. H. Lindner, E. Berg, M. Levin, *Phys. Rev. X* **3**, 031005 (2013). [Anomalous Floquet edge states; broader Floquet topology context.]
- T. Rakovszky, J. K. Asbóth, *Phys. Rev. A* **92**, 052311 (2015). [Edge states in chiral DTQW.]
- M. Szegedy, *Proc. FOCS* (2004). [Szegedy walks.]
- A. Y. Kitaev, *Ann. Phys.* **303**, 2 (2003). [Topological codes; mentioned only for the Möbius surface code follow-up.]
- A. Hatcher, *Algebraic Topology* (2002). [For Möbius bundle, $w_1$, $\mathbb{Z}_2$ holonomy reference.]

---

## 14. Document Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial finalized spec. Replaces `mobius_latent_space_complete.md`. Pivot from classical-ML to QC/QI; canonical walker fixed at $\Sigma = -\mathbb{I}$ split-step DTQW. T2 form left open per Section 5.2. Pre-implementation: literature check pending per Section 9. |
| 1.1 | 2026-05-07 | Literature pre-emption check completed (`lit_check_2026-05-07.md`). Verdict: PROCEED AS SPECIFIED. No DTQW + non-orientable + chiral-Floquet topology paper found. Mandatory citations identified (Beugeling 2014; Quelle 2014 SSC; Moradi & Annabestani 2017; Dai 2012; Delanty & Steel 2012; Li 2015; Higuchi 2025). New caution noted: arXiv:2506.01401 ("Floquet Möbius topological insulators") uses "Möbius" in band-structure sense, not physical-graph sense — disambiguation required in paper §1. Anchor 1 (spec lock) ready for both authors to sign off. |
| 1.2 | 2026-05-07 | Two pre-signoff fixes applied. (1) §3.1 + §4.5 + §6.7: Szegedy walk now uses the Möbius ladder graph $M_L$ (vs. prism graph $Y_L$ for the cylinder counterpart) — the bare 1D position circle has no Möbius structure for coinless walkers, so the comparison was ill-defined under v1.1. (2) §5.3 T3: reformulated as conditional on T2's outcome — with $\Sigma = -\mathbb{I}$ the closed walker has uniform anti-periodic BC (no localized seam), so a cut walker is identical to a cut cylinder unless T2 yields the strong topological-invariant reduction (5.2-b). T3's Möbius-specific content is now explicitly conditional. Numerical experiment N3 unchanged; only its interpretation is conditional. Spec ready for both-author sign-off. |
| 1.3 | 2026-05-16 | **T-D3 (chiral symmetry) delivered with full validation**: `T-D3_chiral_symmetry.md`. Derives parameter-dependent $\Gamma_{\text{asym}}(\theta_1) = \cos(\theta_1/2)\sigma_x + \sin(\theta_1/2)\sigma_z$ in the asymmetric Kitagawa frame, then changes to symmetric frame $U_{\text{sym}} = R(\theta_1/2)\,S_-\,R(\theta_2)\,S_+\,R(\theta_1/2)$ where $\Gamma_{\text{sym}} = \sigma_x$ (parameter-independent). All five validations §8.1–§8.5 PASS at machine precision (max err 5e-17). **T2 resolved as 5.2-a**: cylinder and Möbius discrete winding numbers are *identical* across a 40×40 parameter grid at L=50 ($\max\|\Delta\nu\|=0$). The TRIM-exclusion shifts phase-boundary locations by $O(1/L)$ but does not change the integer invariant. Paper's strongest claims are now T1, N4, T5; T2/T3/T4 are supporting roles with this finite-$L$ winding-equality as T-D4's main analytical target. T-D4 task narrows from "compute possibly-different windings" to "prove the windings are equal for all $L$, $(\theta_1, \theta_2)$ off boundaries." Spec §5.3 (T3) caveat about 5.2-b conditional content now confirmed null. |
| 1.4 | 2026-05-16 | **T-D4 (winding-equality theorem) delivered with full validation**: `T-D4_winding_equality.md`. Theorem statement (§2.1): for $(\theta_1, \theta_2)$ off all four cylinder phase-boundary lines, there exists $L_0(\theta_1, \theta_2)$ such that $\nu^{\text{cyl}}_L = \nu^{\text{Möb}}_L = \nu^\infty$ for all $L \geq L_0$. Proof (§4 lemmas + §5): three-step homotopy argument — (i) discrete winding equals continuous winding under no-aliasing, (ii) aliasing threshold $L_0 < \infty$ exists on the open phase region, (iii) cylinder lattice $K(0)$ and Möbius lattice $K(\pi)$ are connected by a continuous lattice-translation path that preserves the integer winding. Validation §8.1–§8.3 executed: all PASS. Empirical $L_0 \in \{4, 5\}$ for tested interior points; one aliasing case found at $L=4$ for $(\pi/3, \pi/4)$ Möbius (resolves at $L \geq 5$). **T2 form 5.2-a is now rigorously locked.** T3 simplifies to a corollary of standard Asbóth–Edge 2015 (cut walker is identical to cut cylinder). Paper headline structure unchanged: T1, T5, N4 plus T-D4 as a clean theoretical theorem stating the negative result. Next deliverables: T-D7 (Möbius ladder spectrum proof, low-hanging since N7 already validates), T-D5/T-D6 (now corollary-level), N-D9 (code release), N-D10 (paper §5 writeup). |
| 1.5 | 2026-05-16 | **T-D7 (Möbius ladder spectrum theorem) delivered with full validation**: `T-D7_mobius_ladder_spectrum.md`. Theorems 2.1 and 2.2: $\mathrm{spec}(A_{Y_L}) = \{2\cos(2\pi n/L) \pm 1\}$ and $\mathrm{spec}(A_{M_L}) = \{2\cos(2\pi n/L) + 1\} \cup \{2\cos((2n+1)\pi/L) - 1\}$. Proof via rung-swap symmetry $\tau$ decomposing $\mathcal{H} = V_+ \oplus V_-$ (§3); explicit action $A_{M_L}\|_{V_+} = A_{C_L} + \mathbb{I}_L$ (§4), $A_{M_L}\|_{V_-} = \tilde{A}_{C_L} - \mathbb{I}_L$ where $\tilde{A}_{C_L}$ is the anti-periodic cycle adjacency (§5). Explicit eigenvector catalog (§6). Three validations §8.1–§8.3 PASS at machine precision: $[\tau, A] = 0$ exact; block-diagonal V_± spectra match formulas to 2e-15; explicit eigenvectors diagonalize A to 3e-15. **T5 (Szegedy contrast) paper paragraph written (§7.3).** Structural mechanism: Möbius non-orientability acts as anti-periodic BC in the rung-antisymmetric sector of $A_{M_L}$ — entirely independent of any coin or chiral structure. With T-D4 (chiral integer winding robust under cylinder→Möbius) and T-D7 (Möbius adjacency spectrum reduction in $V_-$), the paper's two-effect claim is fully formalized: spatial non-orientability and chiral protection are independent ingredients of ℤ₂ structure in Floquet walks. Theory track is essentially complete; T-D5 and T-D6 reduce to one-paragraph corollaries. Remaining: N-D9 (code release), N-D10 (paper §5 writeup). |
| 1.6 | 2026-05-16 | **T-D5, T-D6 (corollary writeups) and N-D9 (code release) delivered.** T-D5 (`T-D5_edge_modes.md`): cut Möbius walker is identical to cut cylinder walker for $\Sigma=-\mathbb{I}$; edge modes follow standard Asbóth–Edge bulk-edge correspondence. Two-sentence proof, paper paragraph ready. T-D6 (`T-D6_universality.md`): half-odd-integer spectrum signature is protocol-independent (split-step, Hadamard, Grover all confirm). Quotient-construction argument from T-D1 §3.3 generalizes to any translation-invariant coined Floquet walker. Paper paragraph ready. N-D9 (code release artifacts): `README.md` (project overview, run instructions, citation block, results table), `LICENSE` (MIT), `requirements.txt` (NumPy/SciPy/matplotlib/jupyter/nbformat), `.gitignore`. Repository is now ready for the user to push to GitHub. Theory track complete (T-D1, T-D3, T-D4, T-D5, T-D6, T-D7). Numerics track complete except for N-D10 (paper §5 writeup). |
| 1.7 | 2026-05-16 | **Honest re-audit after pushback on optimism + figure inspection.** Noted that cylinder and Möbius results "look identical" in the figures, prompting a pushback on the overly-positive framing. Audit findings: (a) code is correct, no bugs; (b) numerical differences ARE real but scale as $\pi/L$ — vanish asymptotically; (c) several figures fail to convey the differences because the spectra are visually overlapping at $L=50$; (d) the paper's contribution is a precise *characterization* with a clean negative-result theorem (T-D4), not a discovery of dramatic non-orientable Floquet topology. **Project reframed accordingly.** User chose **Option A** (submit honest characterization paper to modest Q1/Q2 venue) for current project, with Option B (intrinsic Möbius walker, non-canonical deck) as separate follow-up. |
| 1.8 | 2026-05-16 | **Folder restructured for two-option workflow.** All Option A artifacts moved into `Option_A_chiral_DTQW_mobius/` (GitHub-ready), organized into `paper/`, `notebook/`, `theory/`, `docs/`. Option B placeholder folder created at `Option_B_intrinsic_mobius_walker/` with planning document (no implementation yet). Top-level project folder now contains only the two Option folders. **Paper draft v1.0 written** (`paper/paper.tex`, ~700 lines REVTeX, projected 18–22 pages) with full proofs of T1, chiral symmetry, T-D4 winding equality (three lemmas + main proof), and T-D7 ladder spectrum decomposition. Supporting `refs.bib` with 16 entries. Unicode characters replaced with LaTeX escapes for compilation compatibility. Paper expanded substantially after user note that v0.5 draft was "very very short" — now contains §I Introduction (literature positioning), §II Model (with canonical-deck proposition proved), §III Theorems (with full proofs), §IV Numerical Results (per-experiment subsections, table of scaling data), §V Discussion (mechanism for null result, comparison with Beugeling/Quelle/Morais Smith and Moradi/Annabestani, outlook including Option B preview, honest framing note), three appendices (Bloch matrix calculation, time-frame change derivation, eigenvector catalog). Ready for author review and journal submission. |

Future revisions append rows. This is the canonical changelog for the spec; do not amend without recording here.

---

## 15. Sign-Off Block

Anchor 1 (spec lock) is signed off when both authors record their names below with the date.

| Author | Date | Status |
|---|---|---|
| S. M. Yousuf Iqbal Tomal | _____ | _____ |
| Abdullah Al Shafin | _____ | _____ |

Once both rows are filled, the spec becomes immutable for the project's duration. Subsequent amendments require an explicit revision history entry above and a re-sign by both authors.

---

*End of finalized research project specification.*
