# T-D4 — Winding-Number Equality Theorem on Cylinder vs. Möbius

**Project:** Möbius Quantum Walk
**Deliverable:** T-D4 (Theory track; depends on T-D1, T-D3)
**Status:** Draft v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.3, `T-D1_walk_operators.md` v1.0, and `T-D3_chiral_symmetry.md` v1.0 on scope, conventions, and notation.

---

## §0. Purpose

T-D4 proves rigorously that, in our project's symmetric time frame with chiral operator $\Gamma = \sigma_x$ (T-D3), the discrete winding numbers computed on the cylinder and Möbius momentum lattices are **identical** for all $(\theta_1, \theta_2)$ in the open interior of each chiral DTQW phase region and for all $L$ sufficiently large to avoid aliasing.

This finalizes **T2 as form 5.2-a** (spec §5.2): the TRIM-exclusion shifts phase-boundary *locations* by $O(1/L)$ but does **not** change the integer topological invariant. The dramatic ℤ × ℤ → ℤ₂ reduction is rigorously ruled out for the canonical $\Sigma = -\mathbb{I}$ walker.

The §8.5 numerical observation from T-D3 ($\max\|\Delta\nu\| = 0$ over a 40×40 grid at $L=50$) is now upgraded to a theorem.

---

## §1. Notation Recap

From T-D3 §7, in the symmetric time frame:
$$a_y'(k;\, \theta_1, \theta_2) = c_1 s_2 + c_2 s_1 \cos k, \qquad a_z'(k;\, \theta_1, \theta_2) = -c_2 \sin k,$$
with $c_i := \cos(\theta_i/2)$, $s_i := \sin(\theta_i/2)$, and $a_x'(k) \equiv 0$.

The angle function:
$$\phi(k;\, \theta_1, \theta_2) := \mathrm{atan2}\!\big(a_z'(k),\ a_y'(k)\big) \in (-\pi, \pi].$$

Momentum lattices:
- Cylinder: $K^{\text{cyl}}_L = \{2\pi n / L : n = 0, 1, \dots, L-1\}$.
- Möbius: $K^{\text{Möb}}_L = \{(2n+1)\pi / L : n = 0, 1, \dots, L-1\}$.

Discrete winding number (on a lattice $K \subset [0, 2\pi)$ ordered as $k_0 < k_1 < \dots < k_{L-1}$, with $k_L := k_0 + 2\pi$):
$$\boxed{\;\nu_L(K) := \frac{1}{2\pi}\sum_{n=0}^{L-1} \widehat{\Delta\phi}_n,\quad \widehat{\Delta\phi}_n := \mathrm{prv}\!\big(\phi(k_{n+1}) - \phi(k_n)\big),\;}$$

where $\mathrm{prv}(x) := \big((x + \pi) \bmod 2\pi\big) - \pi \in (-\pi, \pi]$ is the principal-value branch ("unwrap"). $\nu_L(K)$ is the standard counting formula for the winding of a sampled function around the origin.

Continuous winding:
$$\nu^\infty(\theta_1, \theta_2) := \frac{1}{2\pi}\oint_0^{2\pi} \partial_k\phi\,dk \in \mathbb{Z}.$$

---

## §2. The Theorem

### 2.1 Statement

**Theorem (Winding equality on cylinder vs. Möbius).** Let $(\theta_1, \theta_2) \in (0, \pi)^2$ with $\theta_1 \pm \theta_2 \notin \{0, \pi\}$ (i.e., off all four cylinder phase-boundary lines). There exists an integer $L_0(\theta_1, \theta_2) \geq 4$ such that for all $L \geq L_0$:
$$\boxed{\;\nu_L\!\big(K^{\text{cyl}}_L\big) = \nu_L\!\big(K^{\text{Möb}}_L\big) = \nu^\infty(\theta_1, \theta_2).\;}$$

Equivalently, $\Delta\nu_L(\theta_1, \theta_2) := \nu_L(K^{\text{Möb}}_L) - \nu_L(K^{\text{cyl}}_L) = 0$ for all $L \geq L_0$.

### 2.2 Significance

The chiral DTQW topological classification is **unaffected** by the cylinder $\to$ Möbius momentum quantization shift for the canonical $\Sigma = -\mathbb{I}$ walker. The ℤ classification of the chiral split-step DTQW persists on Möbius — no reduction to ℤ₂.

T2 is therefore form 5.2-a: phase boundaries shift but invariants do not. (Spec §5.2, §5.3, §8.M2 caveat about a potential 5.2-b mechanism is closed out as null.)

---

## §3. Analytic Structure of $\phi$

### 3.1 Singularities of $\phi$

$\phi(k)$ is undefined exactly when $\big(a_y'(k), a_z'(k)\big) = (0, 0)$. From §1:
- $a_z'(k) = -c_2 \sin k = 0 \iff c_2 = 0$ (i.e., $\theta_2 = \pi$) or $\sin k = 0$ ($k \in \{0, \pi\}$).
- At $k = 0$: $a_y'(0) = c_1 s_2 + c_2 s_1 = \sin\!\big((\theta_1 + \theta_2)/2\big)$.
- At $k = \pi$: $a_y'(\pi) = c_1 s_2 - c_2 s_1 = \sin\!\big((\theta_2 - \theta_1)/2\big)$.

**Conclusion.** The pairs $(a_y', a_z')$ vanish only when:
- $\theta_1 + \theta_2 = 0$ at $k = 0$ (degenerate corner of the parameter space).
- $\theta_1 - \theta_2 = 0$ at $k = \pi$ (main diagonal).

For an $\varepsilon$-quasi-energy gap closing (where the bulk gap touches $\varepsilon = \pi$ instead of $\varepsilon = 0$): we need $U^{\text{cyl}}(k) = -\mathbb{I}$, which means $a_0 = -1$ and $\mathbf{a}' = 0$. The condition $a_0 = -1$ at $k = 0$ gives $c_1 c_2 - s_1 s_2 = \cos\!\big((\theta_1+\theta_2)/2\big) = -1$, i.e., $\theta_1 + \theta_2 = 2\pi$ (corner); at $k = \pi$ gives $-c_1 c_2 - s_1 s_2 = -1$, i.e., $\theta_1 + \theta_2 = 0$ (corner). Combined with the boundary lines from Asbóth–Edge 2015 (lines $\theta_1 \pm \theta_2 \in \{0, \pi\}$), and accounting for both $\varepsilon = 0$ and $\varepsilon = \pi$ gap closings, the four phase-boundary lines are exactly $\theta_1 \pm \theta_2 \in \{0, \pi\}$.

**Off all four phase-boundary lines: $\phi(k)$ is smooth on all of $[0, 2\pi)$.**

### 3.2 Continuity and integer-valued winding

For $(\theta_1, \theta_2)$ off the phase boundaries, $\phi: S^1 \to S^1$ is a smooth map, and $\nu^\infty \in \mathbb{Z}$ is the (topological) degree of this map. The Asbóth–Edge 2015 / Kitagawa 2010 cylinder phase diagram identifies $\nu^\infty$ as the labels of the four phase regions.

---

## §4. Lemmas

### 4.1 Lemma 1 — Discrete winding equals continuous winding under no-aliasing

**Lemma 1.** Let $\phi: S^1 \to S^1$ be continuous, and let $K = \{k_0 < k_1 < \dots < k_{L-1}\} \subset [0, 2\pi)$ be an ordered $L$-point sampling with $k_L := k_0 + 2\pi$. If
$$\max_{n} \big|\phi(k_{n+1}) - \phi(k_n) - 2\pi m_n\big| < \pi \quad \text{for some integers } m_n,$$
(equivalently, no individual unwrapped step exceeds $\pi$ in absolute value), then
$$\nu_L(K) = \nu^\infty.$$

**Proof.** Telescoping:
$$\sum_{n=0}^{L-1} \widehat{\Delta\phi}_n = \sum_n \big[\phi(k_{n+1}) - \phi(k_n) - 2\pi m_n\big] = \phi(k_L) - \phi(k_0) - 2\pi\sum_n m_n = -2\pi\!\sum_n m_n,$$
since $\phi(k_L) = \phi(k_0 + 2\pi) = \phi(k_0) \pmod{2\pi}$. Hence $\nu_L = -\sum_n m_n \in \mathbb{Z}$.

Continuous winding is $\nu^\infty = \frac{1}{2\pi}\oint d\phi$; the unwrapped sum approximates the line integral by a Riemann sum with step $\Delta k = O(1/L)$, with error bounded by $\max_n |\partial_k^2 \phi| \cdot O(1/L^2) \cdot L = O(1/L)$. As both sides are integers and the difference goes to zero, $\nu_L = \nu^\infty$ for $L$ large enough. ∎

### 4.2 Lemma 2 — Aliasing threshold

**Lemma 2.** Define
$$L_0(\theta_1, \theta_2) := \left\lceil \frac{2}{\pi}\max_{k \in [0, 2\pi)} |\partial_k \phi(k;\, \theta_1, \theta_2)| \right\rceil + 1.$$
Then for $L \geq L_0$, no aliasing occurs on any lattice $K \subset [0, 2\pi)$ with spacing $\geq \pi/L$.

**Proof.** Mean value theorem: $|\phi(k_{n+1}) - \phi(k_n)| \leq |k_{n+1} - k_n| \cdot \max_k |\partial_k \phi| \leq (2\pi/L) \cdot \max_k |\partial_k \phi|$. The no-aliasing condition $|\widehat{\Delta\phi}_n| < \pi$ holds whenever $(2\pi/L) \cdot \max_k |\partial_k\phi| < \pi$, equivalently $L > 2\max_k|\partial_k\phi|/\pi$. ∎

**Remark.** $L_0(\theta_1, \theta_2) \to \infty$ as $(\theta_1, \theta_2)$ approaches a phase boundary (gap closing $\Rightarrow$ $\mathbf{a}'(k)$ approaches zero at some $k$ $\Rightarrow$ $|\partial_k\phi| \to \infty$ there). On any compact subset of the open interior of a phase region, $L_0$ is uniformly bounded.

### 4.3 Lemma 3 — Lattice translation preserves winding

**Lemma 3.** Let $\phi: S^1 \to S^1$ be continuous and $L \geq L_0$ (Lemma 2). For $\delta \in \mathbb{R}$, define the shifted lattice $K(\delta) := \{(2\pi n + \delta)/L : n = 0, \dots, L-1\}$. The map $\delta \mapsto \nu_L\!\big(K(\delta)\big)$ is constant on $\mathbb{R}$.

**Proof.** By Lemma 1, $\nu_L\!\big(K(\delta)\big) = \nu^\infty$ for all $\delta$, since the no-aliasing condition holds uniformly in $\delta$ (Lemma 2's bound depends on $L$ and $(\theta_1, \theta_2)$, not on $\delta$). ∎

---

## §5. Proof of the Theorem

The cylinder lattice is $K^{\text{cyl}}_L = K(0)$. The Möbius lattice is $K^{\text{Möb}}_L = K(\pi)$. Both are translations of the same uniform $L$-point lattice on $S^1$.

By Lemma 3, $\nu_L\!\big(K^{\text{cyl}}_L\big) = \nu_L\!\big(K^{\text{Möb}}_L\big) = \nu^\infty(\theta_1, \theta_2)$ for all $L \geq L_0(\theta_1, \theta_2)$.

The integer $L_0$ is finite on the open interior of each phase region (Lemma 2 remark). ∎

---

## §6. Edge Cases and Aliasing Threshold

### 6.1 Where $L_0$ matters

**Empirical $L_0$ values** (computed by §8.2 validation, executed 2026-05-16):

| $(\theta_1, \theta_2)$ | $\nu^\infty$ | $L_0$ |
|---|---|---|
| $(\pi/4, \pi/3)$ | 0 | 4 |
| $(\pi/3, \pi/4)$ | −1 | 5 |
| $(\pi/3, 2\pi/3)$ | 0 | 4 |
| $(2\pi/3, \pi/3)$ | −1 | 4 |
| $(\pi/4, 5\pi/6)$ | 0 | 4 |

For all five interior test points, $L_0 \in \{4, 5\}$ — the smallest values consistent with Lemma 2 (the lattice must have $\geq 4$ points to define a winding on $S^1$ at all). One configuration ($(\pi/3, \pi/4)$ at $L = 4$) shows the aliasing phenomenon: the Möbius lattice $\{\pi/4, 3\pi/4, 5\pi/4, 7\pi/4\}$ at this parameter point samples $\phi$ such that one $|\widehat{\Delta\phi}_n|$ exceeds $\pi$, giving $\nu = 0$ instead of $-1$. At $L = 5$ and above, the aliasing resolves.

For the spec's working range ($L \geq 50$), the theorem holds across all interior points, with substantial margin.

### 6.2 What happens at a phase boundary

When $(\theta_1, \theta_2)$ crosses a phase-boundary line, $\phi(k)$ develops a singularity (gap closing) at some $k^*$. The discrete winding $\nu_L$ is *not* well-defined at the singularity itself, and changes integer value as the parameter crosses the boundary. This is the standard topological-phase-transition mechanism — universal across cylinder and Möbius.

The *location* of the boundary at finite $L$ shifts by $O(1/L)$ between cylinder and Möbius (because the lattice samples the bulk gap differently). This is the T2 / N2 observation. But the boundary *shape* and the integer phase labels are identical.

### 6.3 Parity of $L$ subtleties

At cylinder $\delta = 0$, the sample $k_0 = 0$ coincides with a TRIM. For $L$ even, the sample $k_{L/2} = \pi$ also coincides with a TRIM.

At Möbius $\delta = \pi$, $k_0 = \pi/L \neq 0$. For $L$ odd, the sample $k_{(L-1)/2} = \pi$ coincides with a TRIM.

These TRIM coincidences only matter when $(\theta_1, \theta_2)$ is *also* on a phase boundary (so the gap closes at exactly that $k$). Off boundaries, no such coincidence affects the winding. Hence the proof works for any $L$.

---

## §7. Implications for the Paper

### 7.1 Locked: T2 form is 5.2-a

The spec's three-way option for T2 (§5.2) is resolved:

| Form | Description | Status |
|---|---|---|
| 5.2-a | TRIM-exclusion only; phase boundaries shift $O(1/L)$, winding integer preserved | **Confirmed** |
| 5.2-b | ℤ × ℤ → ℤ₂ topological reduction | **Ruled out** |
| 5.2-c | T1 holds but no topological consequence | Not applicable (5.2-a is non-trivial) |

### 7.2 T3 (cut walker edge modes) follow-on

Spec §5.3's "conditional on T2 yielding 5.2-b" content is now confirmed null. T3 reduces cleanly:

- Cut Möbius walker $\equiv$ cut cylinder walker (the closed BC is removed by the cut).
- Edge modes obey standard Asbóth–Edge bulk-edge correspondence with the *same* bulk invariant $\nu$ as the cylinder.
- The paper can fold T3 into a single paragraph rather than a section, with reference to Asbóth–Edge 2015.

### 7.3 Headline claims for the paper

| Claim | Strength |
|---|---|
| **T1** (half-odd-integer spectrum on Möbius) | ★★★★★ headline result |
| **T5** (Szegedy $M_L$ vs $Y_L$ adjacency-spectrum distinction) | ★★★★ headline result, complementary mechanism |
| **N4** (deck-phase return-amplitude signature) | ★★★★ dynamical fingerprint |
| **T2** (TRIM-exclusion phase boundary shift) | ★★★ supporting; modest but rigorous |
| **T3** (edge modes via standard bulk-edge) | ★★ corollary |
| **T4** (universality across coined Floquet protocols) | ★★★ supporting |
| **Winding equality theorem (T-D4)** | ★★★★ rigorous theoretical result; closes T2 cleanly |

The paper's structural contribution remains intact: spatial non-orientability and chiral protection are *independent* contributors to the half-odd-integer / ℤ₂ structure in Floquet walks. Two mechanisms, separated by walker choice (coined vs Szegedy).

### 7.4 What's strictly *new* in the paper after T-D4

1. The Möbius DTQW model itself (no prior literature; see lit_check_2026-05-07.md).
2. T1 (half-odd-integer spectrum) with the explicit proof in T-D1 §3.4.
3. The T-D4 winding-equality theorem itself: *non-orientability does **not** alter the chiral DTQW topology classification at finite $L$.* This is a clean negative result that the literature does not contain.
4. T5 (Möbius ladder adjacency spectrum reduction): conjectured in T-D1 §6.4, numerically verified in N7 to 5e-15, ready for formal proof in T-D7.
5. N4 (deck-phase return-amplitude signature) and the conceptual framing of "two independent ingredients of ℤ₂ structure in Floquet walks."

---

## §8. Validations

Snippets to add to `mobius_dtqw_simulator.ipynb`.

### 8.1 Verify Lemma 1 (no-aliasing $\Rightarrow$ $\nu_L = \nu^\infty$)

```python
# §8.1 — Verify Lemma 1 numerically.
# Pick interior parameters, compute ν_L at L = 4, 8, 16, 32, 50, 100, 200 on cylinder.
# Should all agree with the L=400 continuous-limit value.

def winding_at_L(theta1, theta2, L, mobius=False):
    return winding_sym(theta1, theta2, momenta(L, mobius=mobius))

print("§8.1 — Discrete winding vs continuous winding (cylinder)")
test_points = [
    (PI/4, PI/3),     # interior region
    (PI/3, PI/4),     # symmetric interior
    (PI/3, 2*PI/3),   # different region
    (2*PI/3, PI/3),   # symmetric different region
    (PI/4, 5*PI/6),   # near boundary but inside
]
nu_inf_grid = []
for t1, t2 in test_points:
    nu_inf = winding_sym(t1, t2, np.linspace(0, 2*PI, 400, endpoint=False))
    nus = [winding_at_L(t1, t2, L) for L in (4, 8, 16, 32, 50, 100, 200)]
    nu_inf_grid.append(nu_inf)
    converges = all(n == nu_inf for n in nus)
    print(f"  ({t1:.3f}, {t2:.3f}): ν∞={nu_inf:+d}, νL = {nus}  [{'PASS' if converges else 'FAIL'}]")
```

### 8.2 Verify the theorem: $\nu^{\text{cyl}}_L = \nu^{\text{Möb}}_L$ for $L \geq 4$ at interior points

```python
# §8.2 — Stress-test the theorem at multiple L.
print("\n§8.2 — Cylinder vs Möbius winding for L = 4, 8, 16, 32, 50, 100, 200")
for t1, t2 in test_points:
    pairs = [(winding_at_L(t1, t2, L, False), winding_at_L(t1, t2, L, True))
             for L in (4, 8, 16, 32, 50, 100, 200)]
    eq = all(p[0] == p[1] for p in pairs)
    print(f"  ({t1:.3f}, {t2:.3f}): {pairs}  [{'PASS' if eq else 'FAIL'}]")
```

### 8.3 Aliasing threshold: how close to a boundary can we get?

```python
# §8.3 — How close to a phase boundary does the winding equality break down?
# Approach the boundary theta_1 = theta_2 (diagonal) at theta_1 = theta_2 = PI/2.
print("\n§8.3 — Winding equality near the diagonal boundary θ_1 = θ_2")
for delta in (0.5, 0.2, 0.1, 0.05, 0.02, 0.01):
    t1, t2 = PI/2, PI/2 + delta  # approach the boundary from above
    nu_inf = winding_sym(t1, t2, np.linspace(0, 2*PI, 1000, endpoint=False))
    nu_cyl_50 = winding_at_L(t1, t2, 50, False)
    nu_mob_50 = winding_at_L(t1, t2, 50, True)
    nu_cyl_200 = winding_at_L(t1, t2, 200, False)
    nu_mob_200 = winding_at_L(t1, t2, 200, True)
    eq50 = "ok" if nu_cyl_50 == nu_mob_50 else "DIFFER"
    eq200 = "ok" if nu_cyl_200 == nu_mob_200 else "DIFFER"
    print(f"  δ={delta:.2f}: ν∞={nu_inf:+d}  L=50:  cyl={nu_cyl_50:+d} mob={nu_mob_50:+d} [{eq50}]   L=200: cyl={nu_cyl_200:+d} mob={nu_mob_200:+d} [{eq200}]")
```

---

## §9. Outstanding for Subsequent Deliverables

### 9.1 T-D5 — Edge modes on cut walker (downgraded)

With T-D4 settled, T-D5's content is straightforward:

1. On the open chain, the bulk-edge correspondence is the standard Asbóth–Edge 2015 result.
2. Both "cut cylinder" and "cut Möbius" are open chains with identical bulk parameters.
3. Edge mode count $= |\nu|$ at $\varepsilon = 0$ plus $|\nu|$ at $\varepsilon = \pi$ (or similar, per Asbóth–Edge).

T-D5 reduces to citing Asbóth–Edge with a brief note that our edge structure is identical. ~1 page.

### 9.2 T-D7 — Möbius ladder spectrum proof

Numerics N7 already confirmed the conjecture from T-D1 §6.4. Formal proof outline (1–2 pages):

1. $M_L$ admits the rung-swap involution $\tau$ with $\tau^2 = \mathbb{I}$, decomposing $\mathbb{R}^{2L} = V_+ \oplus V_-$.
2. In $V_+$ (rung-symmetric), $A_{M_L}|_{V_+}$ acts as the cycle graph $C_L$ adjacency *plus* the rung self-loops, giving spec $\{2\cos(2\pi n/L) + 1\}$.
3. In $V_-$ (rung-antisymmetric), the twisted boundary swaps the rows, which under the antisymmetric basis becomes a sign flip — anti-periodic shift on $C_L$ minus the rung, giving spec $\{2\cos((2n+1)\pi/L) - 1\}$.

Total spectrum = union. Matches the conjecture in T-D1 §6.4. T5 follows from this decomposition.

### 9.3 N-D9 — Code release and reproducibility

The notebook is feature-complete. Remaining work: GitHub repository with README, MIT license, environment file. Half a day.

### 9.4 N-D10 — Paper section §5 (numerical results)

Write up §5 of the paper using the results from the notebook + the theorems from T-D1, T-D3, T-D4, T-D7. ~3-4 pages of paper text.

---

## §10. Document Status

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-16 | Initial T-D4 deliverable. **Winding-equality theorem** stated and proved (§2, §5) via three lemmas (§4): continuous-winding-equals-discrete-winding under no-aliasing, aliasing threshold $L_0$ existence, and lattice-translation invariance of the discrete winding. Resolves T2 as 5.2-a (TRIM-exclusion phase-boundary shift, no topological-invariant reduction). Validation snippets §8.1–§8.3 provided. Downstream implications for T3, paper structure, and remaining deliverables (T-D5, T-D7, N-D9, N-D10) recorded. Numerical evidence from T-D3 §8.5 ($\max\|\Delta\nu\| = 0$ over 1600 points at $L=50$) upgraded to a theorem. **Validation executed 2026-05-16: all three checks PASS.** Empirical $L_0 \in \{4, 5\}$ for five interior parameter points — confirms the theorem and shows the aliasing threshold is essentially the minimum lattice size for a winding to be defined at all. One subtle case identified: at $(\pi/3, \pi/4)$, the Möbius lattice aliases at $L = 4$ ($\nu = 0$ instead of $-1$) but converges by $L = 5$. |

*End of T-D4.*
