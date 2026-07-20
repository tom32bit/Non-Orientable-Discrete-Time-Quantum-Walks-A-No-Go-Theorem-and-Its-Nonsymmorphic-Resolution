# Chiral Geometry from Particle Physics → Option B Target

**Date:** 2026-05-16
**Purpose:** Cross-checked literature analysis of chiral geometry in fundamental particle physics to identify the right candidate for Option B's walker construction.

---

## Summary of finding

The Möbius topological insulator (MTI) framework of **Shiozaki, Sato, and Gomi (Phys. Rev. B 91, 155120, 2015; arXiv:1502.03265)** provides the precise mathematical setting we have been groping toward. The MTI is a $\mathbb{Z}_2$-classified topological phase protected by **nonsymmorphic chiral symmetry** ($k$-dependent chirality with $\Gamma(k+2\pi) = -\Gamma(k)$ in 1D, or analogously projective translational symmetry / glide reflection in higher dimensions). This was historically remarkable because it was the **first** $\mathbb{Z}_2$ topological phase protected by purely unitary symmetries — no anti-unitary time-reversal required.

The Floquet version of MTIs has been studied very recently in the **Hamiltonian-driven** setting (Zhou-Zhang-Pan, PRB 2025; arXiv:2506.01401), using time-periodic quenches to a static MTI model. They demonstrate Möbius-twisted edge bands at quasi-energies 0 and $\pi$.

**The DTQW realization of MTIs is not in the literature** as far as we have surveyed. This is the natural Option B target.

---

## The chiral-geometry-in-particle-physics chain of reasoning

### Step 1: Chiral symmetry in DTQW comes from chirality in Dirac-like physics

The standard chiral symmetry $\Gamma U \Gamma = U^{-1}$ in chiral DTQW (Option A) is the discrete-Floquet analogue of $\gamma^5$ chirality in continuum Dirac theory. The two chiral subspaces ($\Gamma = \pm 1$) play the role of left/right Weyl fermions.

In our Option A walker, $\Gamma = \sigma_x$ in the symmetric time frame; the integer winding number $\nu \in \mathbb{Z}$ corresponds to the integer-valued Wilczek-Zee Berry phase of the symmetric Floquet operator.

### Step 2: Z_2 refinements of integer chiral classifications come from additional symmetries

The Altland-Zirnbauer tenfold-way classification (see Kitaev periodic table, Wikipedia "Periodic table of topological insulators and topological superconductors") gives:

| Class | Chiral | TRS | PHS | 1D | 2D |
|---|---|---|---|---|---|
| A | — | — | — | 0 | $\mathbb{Z}$ |
| AIII | $\Gamma$ | — | — | $\mathbb{Z}$ | 0 |
| AI | — | $T^2 = +1$ | — | 0 | 0 |
| BDI | $\Gamma$ | $T^2 = +1$ | $C^2 = +1$ | $\mathbb{Z}$ | 0 |
| D | — | — | $C^2 = +1$ | $\mathbb{Z}_2$ | $\mathbb{Z}$ |
| DIII | $\Gamma$ | $T^2 = -1$ | $C^2 = +1$ | **$\mathbb{Z}_2$** | $\mathbb{Z}_2$ |
| AII | — | $T^2 = -1$ | — | 0 | $\mathbb{Z}_2$ |
| CII | $\Gamma$ | $T^2 = -1$ | $C^2 = -1$ | **$\mathbb{Z}_2$** | 0 |
| C | — | — | $C^2 = -1$ | 0 | $\mathbb{Z}$ |
| CI | $\Gamma$ | $T^2 = +1$ | $C^2 = -1$ | 0 | 0 |

The 1D $\mathbb{Z}_2$ classes are **DIII and CII**: both require chiral + an anti-unitary $T^2 = -1$ symmetry.

### Step 3: Kitagawa et al. 2010 demonstrated all ten classes can be realized in DTQW

Reference: Kitagawa, Rudner, Berg, Demler, Phys. Rev. A **82**, 033429 (2010), arXiv:1003.1729.

Cross-checked verbatim from the paper: "We further present a time-reversal-invariant 2D DTQW with $T^2 = -1$, which can realize the quantum spin Hall (QSH) phase." This is **class AII** in 2D, $\mathbb{Z}_2$.

Their construction:
- 2D DTQW with a **doubled coin** of dimension 4 (two flavors A and B, each with 2 coin states)
- $U_{\rm TRI} = \mathrm{diag}(U_A, U_B)$ block-diagonal in the flavor index
- Time-reversal acts as $T = \tau_y \otimes \sigma_y K$ or similar (the standard $T^2 = -1$ operator on a tensor product)

So class AII in 2D **is** in the literature for DTQW. By analogous "doubling" constructions, the other $\mathbb{Z}_2$ classes (DIII, CII in 1D) should be realizable too — but Kitagawa et al. focused on 2D class AII (QSH).

### Step 4: Z_2 protected by UNITARY symmetries — the Möbius topological insulator

**Reference:** Shiozaki, Sato, Gomi, arXiv:1502.03265 (Phys. Rev. B 91, 155120, 2015). Title: "$\mathbb{Z}_2$-topology in nonsymmorphic crystalline insulators: Möbius twist in surface states."

Cross-checked verbatim from the abstract: *"Here we report the first-known $\mathbb{Z}_2$ topological phase protected by only unitary symmetries. We show that the presence of a nonsymmorphic space group symmetry opens a possibility to realize $\mathbb{Z}_2$ topological phases without assuming any anti-unitary symmetry."*

Their 1D Hamiltonian (verbatim from the paper):
$$H_{1D}(k) = \begin{pmatrix} x(k) & -i\,y(k)\,e^{-ik/2} \\ i\,y(k)\,e^{ik/2} & -x(k) \end{pmatrix},$$
with real functions $x(k), y(k)$. The factors $e^{\pm ik/2}$ are the nonsymmorphic / glide structure: they represent a half-translation in real space. The chiral symmetry $\Gamma_{1D}(k)$ is **$k$-dependent** ("nonsymmorphic chiral symmetry"), and it satisfies $\Gamma(k + 2\pi) = -\Gamma(k)$ (anti-periodic in the BZ).

This makes the Brillouin zone effectively a **Möbius band** rather than a circle: the Hamiltonian returns to itself only after going around twice ($k \to k + 4\pi$). The $\mathbb{Z}_2$ invariant counts whether this Möbius topology is non-trivial.

In 2D and 3D, the construction is extended by combining $H_{1D}$ with additional momentum directions; the protecting symmetry becomes a **glide reflection** (a non-symmorphic spatial symmetry combining reflection with half-translation).

### Step 5: Floquet realization (Hamiltonian-driven) of MTIs

**Reference:** Zhou, Zhang, Pan, arXiv:2506.01401 (Phys. Rev. B 2025). "Floquet Möbius topological insulators."

Cross-checked from the paper PDF: they use **time-periodic quenches to an existing static MTI model** to realize Floquet MTIs. The walker is not a coined DTQW — it is a periodically driven tight-binding Hamiltonian.

Their result: Möbius-twisted edge bands at quasi-energies 0 and $\pi$, characterized by a pair of generalized winding numbers, $\mathbb{Z} \times \mathbb{Z}$ classification.

Cross-checked keyword searches in their PDF:
- "discrete-time quantum walk": **0 occurrences**
- "DTQW": **0 occurrences**
- "quantum walk": **1 occurrence** (passing reference)
- "split-step": **0 occurrences**
- "coin": **0 occurrences**
- "projective translation": 4 occurrences (their main protecting symmetry)
- "glide": 1 occurrence
- "nonsymmorphic": 3 occurrences
- "Shiozaki": 1 occurrence (citation)

**Conclusion:** The Floquet MTI paper does not address DTQW. The DTQW realization is open.

### Step 6: Pin structures and the connection to non-orientable surfaces

In differential geometry, **Pin structures** are the lifts of $O(n)$ frame bundles to $\mathrm{Pin}(n)$ — the analogue of Spin structures on non-orientable manifolds. The Möbius band has TWO Pin structures:

- **Pin$^+$:** $\Sigma^2 = +1$ (orientation-reversal squares to identity).
- **Pin$^-$:** $\Sigma^2 = -1$ (orientation-reversal squares to $-1$, like a Kramers fermion).

Cross-check via Wikipedia "Pin group" and "Spin structure": Pin$^+$/Pin$^-$ correspond to two distinct double covers of $O(n)$; in physics, they classify possible fermionic boundary conditions on non-orientable surfaces. Pin$^-$ is associated with time-reversal $T^2 = -1$ (Kramers pair structure).

For our walker: Option A's canonical deck $\Sigma = -\mathbb{I}$ satisfies $\Sigma^2 = +\mathbb{I}$ — Pin$^+$. A non-canonical deck with $\Sigma^2 = -\mathbb{I}$ (e.g., $\Sigma = i\sigma_y$) would be Pin$^-$ — the Kramers-fermion structure.

The Shiozaki MTI does **not** use a Pin$^-$ structure directly — it uses nonsymmorphic crystalline symmetry. The Pin$^-$ route gives class AII / DIII via $T^2 = -1$; the nonsymmorphic route gives the same $\mathbb{Z}_2$ classification via unitary glide instead.

---

## Cross-checked, validated conclusion: Option B target

**Option B should be the DTQW realization of the Möbius topological insulator (Shiozaki-Sato-Gomi 2015).**

This is concrete, well-motivated, has well-defined precedents, and is genuinely open in the DTQW context:
- Static MTI: Shiozaki-Sato-Gomi 2015 (cited reference).
- Hamiltonian-Floquet MTI: Zhou-Zhang-Pan 2025 (cited reference).
- **DTQW realization: not in the literature.** This is Option B's target.

### Walker construction (concrete plan)

The MTI's 1D Hamiltonian has a $2 \times 2$ structure with $k$-dependent glide chirality. A DTQW realization requires:

1. **Doubled unit cell:** position lattice with two sublattices per unit cell (call them $A$ and $B$).
2. **Coin:** standard $\mathbb{C}^2$ spin space.
3. **Total internal state:** sublattice $\otimes$ spin = $\mathbb{C}^4$.
4. **Nonsymmorphic chiral symmetry:** $\Gamma_{\rm NS} = \tau_x \otimes \sigma_x$ combined with a half-translation, where $\tau_x$ exchanges sublattices A and B and $\sigma_x$ flips coin states.
5. **Walker dynamics:** a generalized split-step with sublattice-dependent shifts and rotations that preserve the nonsymmorphic chiral symmetry.

This is essentially the **doubled-coin walker** (Candidate B in the previous Option B spec) but with a specific structure inherited from Shiozaki-Sato-Gomi 2015. The novelty is the explicit DTQW formulation; the topological framework is borrowed from prior work.

### Z_2 invariant for the DTQW MTI

To be derived during Option B execution. The static MTI invariant (Shiozaki et al. 2015, supplementary) is defined via Wilson loops / nonsymmorphic-symmetry-graded winding. The DTQW analogue should follow by Hamiltonian mapping: define an effective Hamiltonian $H_{\rm eff}(k) = i \log U(k)$ and compute the static MTI invariant on $H_{\rm eff}$. This is exactly what is done in Asbóth-Edge / Cedzich for chiral DTQW topology.

### What is genuinely new

1. **First DTQW realization of an MTI.** Provides a discrete-time-walk platform for the nonsymmorphic-chiral $\mathbb{Z}_2$ phase.
2. **Walker-specific signatures.** Möbius-twisted edge bands at quasi-energies 0 and $\pi$ would manifest as long-time dynamical features absent in Hamiltonian-Floquet realizations.
3. **Connection to Option A.** The Option A walker is the "trivial" case where the nonsymmorphic chiral symmetry collapses to ordinary chirality; Option B's walker is the non-trivial extension.

### Risks

- **Construction must respect a SPECIFIC nonsymmorphic chiral symmetry** matching Shiozaki et al.'s $\Gamma(k+2\pi) = -\Gamma(k)$. Naively doubling the unit cell will not give this — we showed in `_OB_alternating_check.py` that simple alternating-angle constructions fail.
- **Z_2 invariant computation** requires careful Wilson-loop machinery. The Cedzich et al. (2018) classification of symmetric DTQW may already cover this case; literature check needed.
- **Tony Stark / Endgame branding** continues to be a hazard. The Möbius framing is now legitimate (we are realizing a published MTI in DTQW form), but the project should be pitched as "DTQW realization of nonsymmorphic chiral $\mathbb{Z}_2$ topology" — that is what reviewers will care about, not the M\"obius name.

### Mandatory next steps before any code

1. **Read Shiozaki-Sato-Gomi 2015 in detail** — specifically the supplementary material with the explicit Z_2 invariant formula.
2. **Read Cedzich et al. 2018 (the topological classification of 1D symmetric DTQW)** to check whether they have already considered this symmetry class explicitly.
3. **Re-run the literature pre-emption search** with the specific query terms "DTQW + nonsymmorphic" and "DTQW + glide reflection" and "DTQW + Möbius topological insulator."

If after step 3 the DTQW realization of MTIs is still open, **Option B is on solid ground and the spec can be updated to target it concretely**.

---

## Validation status of cited references

| Reference | Title verified? | Abstract verified? | Key claims cross-checked? |
|---|---|---|---|
| Kitagawa et al. 2010 (arXiv:1003.1729, PRA 82 033429) | ✓ | ✓ | ✓ (DTQW realizes all 10 classes; 2D AII construction with $T^2 = -1$) |
| Shiozaki-Sato-Gomi 2015 (arXiv:1502.03265) | ✓ | ✓ | ✓ ($\mathbb{Z}_2$ via unitary symmetry; explicit 1D Hamiltonian; glide reflection in 2D/3D) |
| Zhou-Zhang-Pan 2025 (arXiv:2506.01401, PRB 2025) | ✓ | ✓ | ✓ (Hamiltonian-Floquet only; NO DTQW content per keyword search of the PDF) |
| Cedzich et al. 2018 (arXiv:1611.04439, Quantum 2 95) | ✓ | ✓ | ✓ (Class DIII fully covered with explicit $\mathbb{Z}_2$ invariant formulas; NO nonsymmorphic / glide / Möbius content) |
| **Mochizuki-Bessho-Sato-Obuse 2020 (PRB 102, 035418, arXiv:2004.09332)** | ✓ | ✓ | ✓ (**DTQW with time-glide symmetry: significant pre-emption of Option B's general framework**) |
| Altland-Zirnbauer tenfold way (Wikipedia + standard physics) | ✓ | n/a | ✓ |
| Pin structures / Pin$^\pm$ (standard differential geometry, Wikipedia) | ✓ | n/a | ✓ |

---

## Pre-emption alert: Mochizuki et al. 2020

The paper **"Topological Quantum Walk with Discrete Time-Glide Symmetry"** by Mochizuki, Bessho, Sato, Obuse (PRB 102, 035418, 2020; arXiv:2004.09332) is a substantial pre-emption of the Option B framework.

Cross-checked verbatim from the abstract: *"Regarding each constituent unitary operator as a discrete time step, we formulate discrete space-time symmetry in quantum walks and evaluate the corresponding symmetry protected topological phases. In particular, we study chiral and/or time-glide symmetric topological quantum walks in this formalism."*

Key observations from PDF cross-check:
- "time-glide": 91 occurrences (their central concept)
- "Möbius": 0 occurrences
- "Shiozaki": 1 occurrence (citation, not central)
- "nonsymmorphic": 0 occurrences
- 2D concrete example (not 1D)

**What this means for Option B:**

The general framework of "DTQW with glide symmetry → Z_2 topology" is **in the literature** (Mochizuki et al. 2020). What they cover:
- Discrete space-time symmetries in DTQW (general formalism)
- Chiral + time-glide symmetry → Z_2 topological classification
- Concrete 2D example with anomalous edge states

What remains potentially open (narrower niche, less novel):
- **1D space-glide** DTQW (their 2D example is time-glide; the 1D analogue is not explicitly developed)
- Explicit connection to **Shiozaki-Sato-Gomi 2015 Möbius topological insulator** framework (the Möbius/nonsymmorphic terminology is not central in Mochizuki et al.)
- DTQW realization of the **Floquet Möbius TI** (Zhou-Zhang-Pan 2025) — provides a discrete-walk analogue of the Hamiltonian-Floquet construction

The pre-emption is partial, not total. A focused Option B contribution would specialize Mochizuki et al.'s framework to 1D space-glide and Möbius geometry, with explicit identification of the Shiozaki-Sato-Gomi invariant. This is **incremental**, not groundbreaking.

---

## Revised honest assessment

After cross-checking the chiral-geometry literature, Option B sits in a more crowded space than initially hoped:

1. **The chiral DTQW tenfold-way classification (including 1D class DIII Z_2)** is fully covered by Cedzich et al. 2018.
2. **The general DTQW + glide-symmetry → Z_2 framework** is established by Mochizuki et al. 2020.
3. **The Möbius topological insulator framework** is established statically (Shiozaki-Sato-Gomi 2015) and in Hamiltonian-Floquet realization (Zhou-Zhang-Pan 2025).

The niche for Option B is narrow:
- 1D space-glide DTQW realization of MTIs, with explicit identification of the Shiozaki invariant.
- Connection to Möbius geometry that goes beyond what Mochizuki et al. 2020 stated.
- Walker-specific dynamical signatures (return amplitude, etc.) not covered in static or Hamiltonian-Floquet treatments.

This is a publishable but **incremental** contribution. Realistic venue: *Phys. Rev. Research*, *J. Phys. A*, *Quantum Inf. Process.*, not *Quantum* or *PRX Quantum*.

### Recommendation

Two paths forward:

**Path X (continue Option B with eyes open):** Specialize Mochizuki et al. 2020's framework to 1D space-glide, connect explicitly to Shiozaki MTI, build the walker, compute the Z_2 invariant, write a paper. Realistic timeline: 3-6 months. Realistic outcome: a modest-impact methods/extension paper.

**Path Y (close Option B):** Recognize that the literature has filled in most of the territory we hoped to claim. Submit Option A's characterization paper as the project's main deliverable. Note Option B's prior art in the discussion section. Move on to a different research line.

The decision is the user's. Both paths are honest. Path X is incremental but legitimate; Path Y is cleanest if the user judges that Option B's niche is too narrow to justify the time investment.

---

*End of chiral-geometry analysis. References to be cited in any Option B work; pre-emption status documented for transparency.*
