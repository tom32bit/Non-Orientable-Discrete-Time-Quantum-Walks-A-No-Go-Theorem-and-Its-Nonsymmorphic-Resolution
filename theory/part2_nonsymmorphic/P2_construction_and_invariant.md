# P2 — The Space-Glide Walker: Construction, Möbius Bundle, and ℤ₂ Invariant

**Project:** Non-orientable DTQW — unified paper, Part II
**Status:** v1.0, 2026-07-19. All claims cross-validated numerically (see `code/part2_spaceglide/e1_construction_checks.py` and the experiment scripts).

---

## §1. Setting and definitions

Lattice: sites $x \in \mathbb{Z}$ (finite: even ring of $2N_c$ sites), two-site unit cell — sublattice $A$ = even sites, $B$ = odd sites. Coin space $\mathbb{C}^2$. Cell-internal space $\mathbb{C}^4$ ordered $(A\uparrow, A\downarrow, B\uparrow, B\downarrow)$.

**Glide-chiral operator.**
$$\Gamma \;=\; T_1 \cdot (\mathbb{I}_{\rm pos} \otimes \sigma_x),$$
where $T_1$ translates every amplitude by **one site** (half a unit cell). In the periodic Bloch gauge ($|k,s,c\rangle \propto \sum_n e^{ikn}\,|x = 2n+s,\,c\rangle$):
$$\Gamma(k) = t(k) \otimes \sigma_x, \qquad t(k) = \begin{pmatrix} 0 & e^{-ik} \\ 1 & 0\end{pmatrix},$$
$$\boxed{\;\Gamma(k)^2 = e^{-ik}\,\mathbb{I}_4\;}$$
— a **projective** (nonsymmorphic) relation: $\Gamma$ squares to the full cell translation, not the identity. Its eigenvalues $\pm e^{-ik/2}$ are $4\pi$-periodic and **exchange** under $k \to k + 2\pi$.

**The Möbius bundle.** The $\Gamma(k)$-eigenbasis, chosen smoothly,
- $+e^{-ik/2}$ sector: $u_1 = v_+ \otimes |+\rangle$, $u_2 = v_- \otimes |-\rangle$,
- $-e^{-ik/2}$ sector: $u_3 = v_+ \otimes |-\rangle$, $u_4 = v_- \otimes |+\rangle$,

with $v_\pm(k) = (\pm e^{-ik/2}, 1)/\sqrt{2}$ and $\sigma_x |\pm\rangle = \pm|\pm\rangle$, satisfies
$$V(k + 2\pi) = V(k) \cdot X, \qquad X = \text{(sector swap)}.$$
The eigenbundle over the Brillouin circle is **the Möbius bundle**: it closes only after two trips around the zone. *(Verified: E1h, intra-sector residue ≤ 1e-16.)*

This is the precise sense in which the paper's arc closes: Part I proves the Möbius twist placed in the **boundary condition** (real space) is topologically inert; here the twist reappears, irremovably, in the **symmetry algebra** (momentum space).

---

## §2. The construction theorem

**Theorem (glide-chiral walkers from arbitrary half-protocols).**
Let $F$ be any unitary, local, cell-periodic operator ("half-protocol"), and let
$$U \;=\; \Gamma\, F^\dagger\, \Gamma^{-1}\, F.$$
Then $U$ is unitary, local, $2\pi$-periodic in $k$, and satisfies the **glide-chiral symmetry**
$$\Gamma\, U\, \Gamma^{-1} = U^\dagger .$$

*Proof.* Unitarity and locality are clear ($\Gamma$ is a shift composed with a coin flip; conjugation by it preserves locality). For the symmetry, work at fixed $k$ where $\Gamma^2 = e^{-ik}\mathbb{I}$ is a scalar $s$; scalars commute with everything:
$$\Gamma U \Gamma^{-1} = \Gamma^2 F^\dagger \Gamma^{-1} F \Gamma^{-1}
= s\, F^\dagger \Gamma^{-1} F \Gamma^{-1}
= F^\dagger (s\,\Gamma^{-1}) F \Gamma^{-1}
= F^\dagger \Gamma F \Gamma^{-1} = U^\dagger,$$
using $s\,\Gamma^{-1} = \Gamma$. Periodicity: $\Gamma(k+2\pi) = -\Gamma(k)$ in the smooth (4π-periodic) picture, and the two sign flips cancel in $U$; in the periodic gauge, $\Gamma(k)$ itself is $2\pi$-periodic. In real space the identity holds provided $[F, T_2] = 0$ (cell periodicity), since $\Gamma^2 = T_2$. ∎

*(Verified: E1c, error ≤ 3e-16, Bloch and real space.)*

This is the glide analogue of the ordinary symmetric-timeframe trick $U_{\rm sym} = \Gamma_0 F^\dagger \Gamma_0 F$ with $\Gamma_0 = \sigma_x$: the entire chiral DTQW toolbox generalises by replacing the involutive coin chirality with the projective glide.

**Second frame.** $U' = F\,\Gamma F^\dagger \Gamma^{-1}$ is glide-chiral by the same argument; it is the analogue of the second symmetric timeframe of Asbóth–Obuse.

---

## §3. The sublattice-parity obstruction (design lemma)

**Lemma.** If every term of $F$ displaces by an **odd** number of sites (e.g. $F$ built from full spin-dependent shifts, where both spin components move by exactly one site), then every term of $U = \Gamma F^\dagger \Gamma^{-1} F$ displaces by an even number of sites, so $U$ conserves the sublattice grading and decomposes as $U_A \oplus U_B$ — two decoupled 2-band walkers. The glide-chiral structure is then unitarily removable (the walker "collapses").

*Proof sketch.* Displacement parity is multiplicative along operator products; $F, F^\dagger, \Gamma, \Gamma^{-1}$ contribute odd+odd+odd+odd = even for every term. An even-displacement operator maps each sublattice to itself. ∎

**Consequence.** A non-collapsing glide-chiral walker **requires partial (split-step) shifts** — factors of mixed displacement parity, e.g. $S_\uparrow$ (spin-up moves one site, spin-down rests). This was discovered as a live failure: the first implementation used the full shift and produced a 4-dimensional commutant (E1f/E1g failure); the split-step form
$$F(k) = S_\downarrow(k)\, R_c(\beta)\, S_\uparrow(k)\, R_c(\alpha),$$
with sublattice-dependent coin angles $\alpha = (\alpha_A, \alpha_B)$, $\beta = (\beta_A, \beta_B)$, passes all no-collapse tests:

- no $k$-independent chiral operator exists (solution space dimension 0),
- the commutant of $\{U(k)\}$ is the scalars (dimension 1).

*(Verified: E1f, E1g.)*

---

## §4. Block structure and the determinant function

Glide-chirality of $U$ gives $\Gamma H \Gamma^{-1} = -H$ for the effective Hamiltonian $H(k) = i\log U(k)$ (branch cut in a chosen spectral gap). In the twisted basis, with $\Gamma_{\rm diag} = {\rm diag}(\mu, \mu, -\mu, -\mu)$, $\mu = e^{-ik/2}$:
$$H_{++} = H_{--} = 0, \qquad H = \begin{pmatrix} 0 & D(k) \\ D(k)^\dagger & 0\end{pmatrix}, \qquad d(k) := \det D(k).$$
*(Verified: E1e, diagonal leak ≤ 1e-15.)*

**Möbius constraint.** From $V(k+2\pi) = V(k)X$ and $H(k+2\pi) = H(k)$:
$$\boxed{\;d(k + 2\pi) = \overline{d(k)}\;}$$
*(Verified: E1h, relative error ≤ 1e-15.)* With real coins there is additionally $d(-k) = \overline{d(k)}$, pinning $d(0), d(2\pi) \in \mathbb{R}$; this reality is **not** required for the invariant below.

---

## §5. The ℤ₂ invariant

**Definition.** Assume both quasienergy gaps (at $\varepsilon = 0$ and $\pi$) are open, so $d(k) \neq 0$ for the appropriate branch. Lift $\theta(k) = \arg d(k)$ continuously over $[0, 2\pi]$. The constraint $d(2\pi) = \overline{d(0)}$ forces
$$\theta(2\pi) = -\theta(0) + 2\pi n, \qquad n \in \mathbb{Z}.$$
A change of the initial branch $\theta(0) \to \theta(0) + 2\pi m$ shifts $n \to n + 2m$. Hence
$$\boxed{\;\zeta = n \bmod 2 \in \{0, 1\}\;}$$
is well defined. Two invariants $(\zeta_0, \zeta_\pi)$ arise from the two branch cuts (gap 0 via cut at $\pi$, gap $\pi$ via cut at 0).

**Quantization and protection.** $n$ can change only when $d(k_*) = 0$ for some $k_* \in [0, 2\pi]$ — a bulk gap closing. No symmetry beyond glide-chirality is used. *(Verified: quantization error ≤ 3e-15 across a 61×61 phase-diagram grid; quantization survives complex coin phases that break the coins' reality.)*

**Why the total doubled-zone winding carries nothing.** The constraint makes the winding over $[2\pi, 4\pi]$ cancel that over $[0, 2\pi]$; the total is always zero. The invariant is the *relative* half-zone datum $n$, exactly parallel to the Möbius-topological-insulator index of Shiozaki–Sato–Gomi.

---

## §6. Numerical results (experiment log)

| Exp | Statement | Result |
|---|---|---|
| E1 | Construction checks + no-collapse | all pass (see §2, §3) |
| E2 | Bulk bands + winding data at representative $\zeta = 0, 1$ points | figure `E2_bands_and_winding.png`; $\zeta=1$: $d(0)=d(2\pi)=-2.79$ pinned real, half-turn sweep |
| E3 | Phase diagram, slice $(\alpha_A, \alpha_B) \in [-\pi,\pi]^2$, $(\beta_A,\beta_B)=(-1.24,-1.39)$, 61×61 | both classes present; every $\zeta$ jump sits on a step with bulk-gap floor ≤ 0.005; zero jumps across well-gapped steps |
| E4 | Domain walls, $\Delta\zeta = 1$ vs $\Delta\zeta = 0$ ring (60 cells) | $\Delta\zeta=1$: **one mode per wall pinned at $\varepsilon = \pi$** (to 1e-5–8e-5, robust under wall width 2→5); $\Delta\zeta=0$ generic control: zero in-gap wall modes |
| E5 | Canonical (scalar) cell twist on the glide walker | spectrum = Bloch at half-odd-integer momenta to 3e-15; glide-chirality intact — Part I's mechanism carries verbatim and remains inert |
| E6 | Staggered return amplitude $S_\pi(T)$ at a wall | topological wall → 0.034 (converged plateau = π-mode weight); control → 0 (power-law decay) |

**Status after the 2026-07-20 internal review and revision round** (see
`docs/VALIDATION_LOG.md` and experiments E7/E8):

1. **[RESOLVED — reformulated]** The *absolute* ζ is frame-relative: an
   admissible eigenbasis change with $\det g_\pm = \pm e^{ik/2}$ shifts $n$
   by −1 at every parameter point (verified). The invariant is defined in the
   canonical frame; the frame shift is walk-independent, so **differences
   Δζ are intrinsic**. Theorem restated accordingly in the manuscript
   (Thm 4 (i)–(iii)).
2. **[RESOLVED — mechanism identified]** Wall-mode π-pinning is enforced by
   the walker's **reality** (antiunitary PHS $K$, $K^2=+1$: real $U$ ⇒
   spectrum symmetric under ε → −ε ⇒ an unpaired localized mode is pinned at
   ε ∈ {0, π}); the glide ℤ₂ mismatch Δζ dictates the mode's **existence**.
   Verified (E7a): real angle disorder (even global, W ≤ 0.3) keeps deviation
   at the hybridization floor 2–5e-5; complex phase disorder unpins linearly
   (→1e-2 at W = 0.3). Inter-wall hybridization: δ ∝ e^{−s/ξ}, ξ = 1.41
   cells, r = −0.999994 over six decades, floored at ~1e-8 by the tanh-wall
   profile tails (E7b).
3. **[SHARPENED]** $\zeta_0 = \zeta_\pi$ at every sampled point *including*
   the reality-broken family (E8a, 51 gapped points, quantization 6e-16) —
   the identity is not a consequence of $K$; conjectured structural to the
   two-coin-layer family. **Still open** whether richer $F$ splits it.
4. **[UNCHANGED — open]** Bulk–defect correspondence theorem and full
   index-theoretic classification (vs. Cedzich et al.) remain open; evidence
   is numerical. Second slice audit (E8b, β = (0.4, 1.3), 41×41) confirms
   genericity of the phase-diagram findings.
5. **[NEW]** Prop 1 (Part I) upgraded: necessity now proven via the
   Fourier-coefficient argument (V7): $[\Sigma, U(k)] = 0\ \forall k$ ⟺
   $\Sigma$ commutes with each of $c_-, c_0, c_+$ ⟹ $[\Sigma, R_1] = 0$ and
   $[\Sigma, \sigma_z] = 0$ ⟹ Σ scalar.
6. **[NEW]** $S_\pi$ signal optimization (E7c): baseline single-site state
   0.034; optimal wall-cell state 0.140; optimal ±2-cell state 0.624.

---

## §7. Relation to prior art (what is new)

- **Shiozaki–Sato–Gomi 2015**: static Hamiltonian MTI, $\mathbb{Z}_2$ by unitary nonsymmorphic symmetry. *Here:* Floquet-unitary/DTQW realization, invariant defined directly on the walk operator, with walk-native dynamical detection ($S_\pi$).
- **Mochizuki et al. 2020**: DTQW with **time**-glide symmetry (2D example). *Here:* **space**-glide in 1D; different symmetry axis; explicit Möbius-bundle formulation and MTI-style half-zone invariant; general construction recipe $U = \Gamma F^\dagger \Gamma^{-1} F$ for arbitrary $F$.
- **Zhou–Zhang–Pan 2025**: Hamiltonian-Floquet MTI via quenches. *Here:* strictly coined DTQW; single ℤ₂ with π-pinned wall doublet rather than $\mathbb{Z}\times\mathbb{Z}$ edge-band windings.
- **Part I (this project)**: the no-go motivates the construction — the *unique* way to put the Möbius twist into a split-step DTQW with the standard coin toolbox is through the glide algebra, and then it is topological.
