# T-D3 — Chiral Symmetry of the Split-Step DTQW

**Project:** Möbius Quantum Walk
**Deliverable:** T-D3 (Theory track; depends on T-D1)
**Status:** Draft v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.2 and `T-D1_walk_operators.md` v1.0 on scope, conventions, and notation.

---

## Purpose

T-D3 identifies the explicit chiral symmetry operator $\Gamma$ for the canonical project walker (Kitagawa split-step DTQW with $\Sigma = -\mathbb{I}$), in a parameter-independent form that can be used as the basis for **T-D4** (winding-number integrals over $K^{\text{Möb}}_L$).

The key obstacle: in the asymmetric time frame fixed by spec §4.2 / T-D1 §2.2, the natural chiral operator depends on $\theta_1$, which is unworkable for topological classification. We resolve this by a unitary time-frame change to the symmetric form, in which the chiral operator becomes $\Gamma = \sigma_x$ — constant and parameter-free.

T-D3 also delivers a numerical validation routine that the numerics track can drop into the existing notebook as one extra cell.

---

## §1. Setup Recap (from T-D1)

**Walk operator (asymmetric Kitagawa convention).** For $(\theta_1, \theta_2) \in [0, \pi]^2$ on the cylinder:
$$U^{\text{cyl}}(\theta_1, \theta_2) = S_- \, R(\theta_2) \, S_+ \, R(\theta_1).$$

**Coin rotation.** $R(\theta) = e^{-i\theta\sigma_y/2} = \cos(\theta/2)\,\mathbb{I} - i\sin(\theta/2)\,\sigma_y$.

**Bloch decomposition.** With $c_i := \cos(\theta_i/2)$, $s_i := \sin(\theta_i/2)$, the Bloch walker is
$$U^{\text{cyl}}(k; \theta_1, \theta_2) = a_0(k)\,\mathbb{I} - i\,\mathbf{a}(k)\cdot\boldsymbol{\sigma},$$
with
- $a_0(k) = c_1 c_2 \cos k - s_1 s_2$ ,
- $a_x(k) = c_2 s_1 \sin k$ ,
- $a_y(k) = c_1 s_2 + c_2 s_1 \cos k$ ,
- $a_z(k) = -c_1 c_2 \sin k$ ,

(derived in T-D1 §2.4.1). All coefficients are real, and $a_0^2 + a_x^2 + a_y^2 + a_z^2 = 1$ since $U \in \mathrm{SU}(2)$.

**Möbius walker.** Same operator form, anti-periodic BC on coin ($\Sigma = -\mathbb{I}$); the Bloch decomposition is identical at each $k$, only the discrete set of allowed $k$ differs (half-odd-integer on Möbius, integer on cylinder).

---

## §2. Pre-cautions and Conventions

These commitments fix the project's notation throughout T-D3 and T-D4. Deviations are bugs.

### 2.1 Rotation sign convention

$R(\alpha) = e^{-i\alpha\sigma_y/2}$ represents a rotation of physical 3-vectors by angle $+\alpha$ around the $y$-axis (right-hand rule). Concretely:
$$R(\alpha)\,\sigma_x\,R(-\alpha) = \cos\alpha\,\sigma_x - \sin\alpha\,\sigma_z,$$
$$R(\alpha)\,\sigma_z\,R(-\alpha) = \sin\alpha\,\sigma_x + \cos\alpha\,\sigma_z,$$
$$R(\alpha)\,\sigma_y\,R(-\alpha) = \sigma_y.$$
Verified directly at $\alpha = \pi/2$ in §8.1.

### 2.2 Chiral-symmetry definition

For a Floquet unitary $U$, a chiral symmetry is a unitary involution $\Gamma$ ($\Gamma^2 = \mathbb{I}$) satisfying
$$\boxed{\;\Gamma\, U\, \Gamma = U^{-1} = U^\dagger.\;}$$
This is equivalent to demanding that the effective Hamiltonian $H_{\text{eff}}(k) = \mathbf{a}(k)\cdot\boldsymbol{\sigma}/|\mathbf{a}(k)|$ anti-commutes with $\Gamma$, i.e., $\Gamma H_{\text{eff}}(k)\Gamma = -H_{\text{eff}}(k)$ pointwise in $k$ (and in $(\theta_1, \theta_2)$ if we want a global classification).

**Important:** some references use "$\Gamma U \Gamma = U^\dagger$" with $\Gamma$ acting on the *coin* and a possible time-reversal; for a unitary $U$ on a finite-dim space the two definitions coincide (since $U^{-1} = U^\dagger$). The project commits to the unitary form throughout.

### 2.3 Asymmetric vs. symmetric time frame

A "time frame" refers to the cyclic position of factors in $U$. Cyclic shifts of $U$'s factor decomposition give walks that are conjugate to $U$ and hence have the same quasi-energy spectrum and the same topological invariants. However, the *chiral operator's explicit form* depends on the frame. We exploit this freedom to find the cleanest frame.

### 2.4 Comparison with Asbóth & Obuse 2013 (PRB 88, 121406)

Asbóth & Obuse define chiral symmetry for the Kitagawa split-step using a different decomposition; their final result is $\Gamma = \sigma_x$ in a specific symmetric frame. Our derivation in §4 reproduces their conclusion in our notation. Where their conventions diverge from ours, we make the difference explicit (footnote in §8.3).

### 2.5 Things that will go wrong if you ignore this section

- Using $R(\theta) = e^{+i\theta\sigma_y/2}$ (opposite sign): flips $\Gamma_{\text{asym}}$ to $\cos(\theta_1/2)\sigma_x - \sin(\theta_1/2)\sigma_z$. All downstream formulas pick up sign flips. The *winding number* is sign-sensitive — getting this wrong inverts topology.
- Using `np.arctan(a_z/a_y)` instead of `np.arctan2(a_z, a_y)` for winding-angle calculation: misses sign of denominator, undercounts windings by factor 2.
- Treating $\Gamma$ in the asymmetric frame as $\theta_1$-independent: produces nonsensical "winding" that has discontinuities at $\theta_1 \in \{0, \pi\}$ which are artifacts of the chiral-operator parameter dependence, not physical phase transitions.

---

## §3. Asymmetric-Frame Chiral Operator (Parameter-Dependent)

**Goal of this section.** Show that in the asymmetric time frame of T-D1, the natural chiral operator is $\theta_1$-dependent, hence unworkable.

**Geometric construction.** The Bloch vector $\mathbf{a}(k) = (a_x, a_y, a_z)(k)$ traces a curve in $\mathbb{R}^3$ as $k$ varies over $[0, 2\pi)$. Chiral symmetry exists iff this curve lies in a **2-plane through the origin** for all $k$ and all $(\theta_1, \theta_2)$. The chiral operator is then $\Gamma = \hat{\mathbf{n}}_\perp \cdot \boldsymbol{\sigma}$ where $\hat{\mathbf{n}}_\perp$ is the unit normal to the plane.

**Decomposition.** From T-D1 §2.4.1:
$$\mathbf{a}(k) = \sin k \cdot \mathbf{v}_1 + \cos k \cdot \mathbf{v}_2 + \mathbf{v}_3,$$
with
$$\mathbf{v}_1 = (c_2 s_1,\ 0,\ -c_1 c_2), \quad \mathbf{v}_2 = (0,\ c_2 s_1,\ 0), \quad \mathbf{v}_3 = (0,\ c_1 s_2,\ 0).$$

Observation: $\mathbf{v}_2$ and $\mathbf{v}_3$ are both along $\hat{\mathbf{y}}$, so their sum collapses to a single $\hat{\mathbf{y}}$-aligned vector. Hence $\mathbf{a}(k)$ lies in $\mathrm{span}(\mathbf{v}_1,\ \hat{\mathbf{y}})$ for all $k$. ✓ — chiral symmetry exists.

**Normal to the plane.** $\hat{\mathbf{n}}_\perp \propto \mathbf{v}_1 \times \hat{\mathbf{y}}$:
$$\mathbf{v}_1 \times \hat{\mathbf{y}} = (c_2 s_1,\ 0,\ -c_1 c_2) \times (0,\ 1,\ 0) = (c_1 c_2,\ 0,\ c_2 s_1).$$
Normalizing (norm $= |c_2|$):
$$\hat{\mathbf{n}}_\perp = (c_1,\ 0,\ s_1) = (\cos(\theta_1/2),\ 0,\ \sin(\theta_1/2)).$$

**Chiral operator (asymmetric frame).**
$$\Gamma_{\text{asym}}(\theta_1) = \cos(\theta_1/2)\,\sigma_x + \sin(\theta_1/2)\,\sigma_z.$$

**Problem.** $\Gamma_{\text{asym}}$ depends on $\theta_1$. For topological classification over the full parameter space $[0, \pi]^2$, we need a chiral operator that is **simultaneously valid for all $(\theta_1, \theta_2)$**. Parameter dependence makes the operator change discontinuously across the parameter space and breaks the standard winding-number machinery. We need a better frame.

---

## §4. Symmetric-Frame Analysis

**Strategy.** Apply a $\theta$-dependent unitary similarity transformation $W$ such that the new walker $U' = W^{-1} U W$ has a chiral operator that is $(\theta_1, \theta_2)$-independent in the *new* frame.

**Choice of $W$.** Take $W = R(-\theta_1/2)$. Then:
$$U_{\text{sym}} := R(\theta_1/2)\, U\, R(-\theta_1/2) = R(\theta_1/2)\, S_-\, R(\theta_2)\, S_+\, R(\theta_1)\, R(-\theta_1/2).$$

Using $R(\theta_1)\,R(-\theta_1/2) = R(\theta_1/2)$ (both are rotations around $\sigma_y$, so they commute and angles add):
$$\boxed{\;U_{\text{sym}}(\theta_1, \theta_2) = R(\theta_1/2)\, S_-\, R(\theta_2)\, S_+\, R(\theta_1/2).\;}$$

This is a **symmetric** form: the walk is sandwiched between two equal half-rotations of $\theta_1$.

**Bloch decomposition of $U_{\text{sym}}$.** Under the conjugation $R(\theta_1/2)\,\cdot\,R(-\theta_1/2)$, the $\mathbf{a}$-vector rotates in the $xz$-plane by angle $-\theta_1/2$:
$$a_x'(k) = \cos(\theta_1/2)\,a_x(k) + \sin(\theta_1/2)\,a_z(k),$$
$$a_z'(k) = -\sin(\theta_1/2)\,a_x(k) + \cos(\theta_1/2)\,a_z(k),$$
$$a_y'(k) = a_y(k), \qquad a_0'(k) = a_0(k).$$

Plugging in the explicit forms:
$$a_x'(k) = c_2 \sin k \cdot [s_1 \cos(\theta_1/2) - c_1 \sin(\theta_1/2)] = c_2 \sin k \cdot [\sin(\theta_1/2)\cos(\theta_1/2) - \cos(\theta_1/2)\sin(\theta_1/2)] = 0.$$

So $a_x'(k) \equiv 0$ for all $(k, \theta_1, \theta_2)$. ✓

And:
$$a_z'(k) = -c_2 \sin k \cdot [s_1 \sin(\theta_1/2) + c_1 \cos(\theta_1/2)] = -c_2 \sin k \cdot [\sin^2(\theta_1/2) + \cos^2(\theta_1/2)] = -c_2 \sin k.$$

Therefore in the symmetric frame:
$$\boxed{\;a_0'(k) = c_1 c_2 \cos k - s_1 s_2,\quad a_x'(k) = 0,\quad a_y'(k) = c_1 s_2 + c_2 s_1 \cos k,\quad a_z'(k) = -c_2 \sin k.\;}$$

The vector $\mathbf{a}'(k) = (0,\ a_y'(k),\ a_z'(k))$ lies in the **$yz$-plane** for all $k$ and all $(\theta_1, \theta_2)$. The unit normal to this plane is $\hat{\mathbf{x}}$. Hence:
$$\boxed{\;\Gamma_{\text{sym}} = \sigma_x.\;}$$

The chiral operator in the symmetric frame is $\sigma_x$ — **constant in $(\theta_1, \theta_2)$ and $k$**.

---

## §5. Direct Verification

We verify $\sigma_x\, U_{\text{sym}}(k)\, \sigma_x = U_{\text{sym}}(k)^{-1}$ algebraically.

Write $U_{\text{sym}}(k) = a_0\,\mathbb{I} - i\,(0\cdot\sigma_x + a_y'\sigma_y + a_z'\sigma_z)$ (suppressing the prime on $a_0$ since $a_0' = a_0$).

Apply $\sigma_x$ from both sides. Using $\sigma_x \sigma_x \sigma_x = \sigma_x$, $\sigma_x \sigma_y \sigma_x = -\sigma_y$, $\sigma_x \sigma_z \sigma_x = -\sigma_z$:
$$\sigma_x\, U_{\text{sym}}(k)\, \sigma_x = a_0\,\mathbb{I} - i\,(0 - a_y'\sigma_y - a_z'\sigma_z) = a_0\,\mathbb{I} + i\,(a_y'\sigma_y + a_z'\sigma_z).$$

Compute $U_{\text{sym}}(k)^{-1} = U_{\text{sym}}(k)^\dagger$:
$$U_{\text{sym}}(k)^\dagger = \overline{a_0}\,\mathbb{I} + i\,(\overline{a_y'}\sigma_y + \overline{a_z'}\sigma_z) = a_0\,\mathbb{I} + i\,(a_y'\sigma_y + a_z'\sigma_z)$$
(using that all coefficients are real).

Both expressions match. ✓

---

## §6. Möbius Transfer

The Möbius walker (canonical $\Sigma = -\mathbb{I}$) shares the operator form with the cylinder walker; only the BC on the walker Hilbert space differs. The symmetric time-frame change $W = R(-\theta_1/2)$ is an operator on **coin only**, acting as $\mathbb{I}_L \otimes R(-\theta_1/2)$ on the full Hilbert space. It commutes with $\Sigma = -\mathbb{I}_2$:
$$[\mathbb{I}_L \otimes R(-\theta_1/2),\ \mathbb{I}_L \otimes (-\mathbb{I}_2)] = 0.$$

Therefore the symmetric time-frame walker on Möbius is:
$$U_{\text{sym}}^{\text{Möb}}(\theta_1, \theta_2) = R(\theta_1/2)\, S_-^{\text{Möb}}\, R(\theta_2)\, S_+^{\text{Möb}}\, R(\theta_1/2),$$
acting on $\mathcal{H}_L^{\text{Möb}}$ (anti-periodic BC). The Bloch decomposition is identical to the cylinder case, sampled at $k \in K^{\text{Möb}}_L$.

**The chiral operator $\Gamma = \sigma_x$ is the same on Möbius and cylinder.** Both walkers admit the same chiral classification machinery, with the only difference being the discrete momentum set used in the winding integral.

---

## §7. Setup for T-D4: Winding Number Formula

With chiral symmetry $\Gamma = \sigma_x$ secured, the winding number for $\mathrm{SU}(2)$ chiral DTQW is computed as follows.

**Definition.** The vector $\mathbf{a}'(k) = (0,\ a_y'(k),\ a_z'(k))$ defines an angle in the $yz$-plane:
$$\phi(k;\, \theta_1, \theta_2) := \mathrm{atan2}\!\big(a_z'(k),\ a_y'(k)\big) \in (-\pi, \pi].$$

The **winding number** is:
$$\boxed{\;\nu(\theta_1, \theta_2) := \frac{1}{2\pi}\oint_{\text{BZ}} dk\,\partial_k \phi(k;\, \theta_1, \theta_2) \in \mathbb{Z}.\;}$$

**Discrete-momentum versions** (the substance of T-D4):
- **Cylinder:** $\nu^{\text{cyl}}_L = \frac{1}{2\pi}\sum_{n=0}^{L-1} \Delta\phi_n$ with $k_n = 2\pi n/L$, $\Delta\phi_n = \phi(k_{n+1}) - \phi(k_n)$ unwrapped.
- **Möbius:** $\nu^{\text{Möb}}_L = \frac{1}{2\pi}\sum_{n=0}^{L-1} \Delta\phi_n$ with $k_n = (2n+1)\pi/L$.

The question for T-D4: under what conditions on $(\theta_1, \theta_2)$ and $L$ do $\nu^{\text{cyl}}_L$ and $\nu^{\text{Möb}}_L$ differ?

**Pre-emptive observation.** In the thermodynamic limit $L \to \infty$, both Riemann sums converge to the same continuous integral, hence the same integer. *Differences at finite $L$ are quantization artifacts that vanish asymptotically — unless the integrand has a non-trivial sub-leading sensitivity to the momentum lattice (e.g., a contribution from a "TRIM-mediated" winding component).*

This pre-emptive observation suggests that T2 most likely lands as **5.2-a (modest TRIM-exclusion)** rather than 5.2-b (strict ℤ × ℤ → ℤ₂ reduction). Confirming this requires T-D4's explicit calculation.

**Decomposition into chiral subspaces** (for chiral-symmetric Hamiltonians, gives two windings):

In the $\sigma_x$-eigenbasis $|\pm\rangle_x = (|R\rangle \pm |L\rangle)/\sqrt{2}$, the effective Hamiltonian $H_{\text{eff}}'(k) = a_y'(k)\sigma_y + a_z'(k)\sigma_z$ has off-diagonal blocks; the winding in each chiral subspace gives $\nu_\pm$. For $\mathrm{SU}(2)$ DTQW the two are related: $\nu_+ = -\nu_-$, hence one integer $\nu$ characterizes the topology. This matches Asbóth & Edge 2015's framework.

For the *non-canonical* split-step variant (Asbóth–Edge convention with two full shifts and two coin rotations), $\nu_+$ and $\nu_-$ can differ, giving the $\mathbb{Z}\times\mathbb{Z}$ classification mentioned in spec §5.2. Our Kitagawa convention gives the $\mathbb{Z}$ classification (one winding number); whether non-orientability further reduces this to $\mathbb{Z}_2$ at finite $L$ is the T-D4 question.

---

## §8. Validations

Concrete checks the numerics track should add to `mobius_dtqw_simulator.ipynb` as one additional cell. Code provided is paste-ready.

### 8.1 Sanity: rotation conventions

```python
# §8.1 — Verify R(α) rotation conventions used in T-D3 §2.1
alpha = PI / 2
R_a = coin_rotation(alpha)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)

err_x = np.max(np.abs(R_a @ sx @ R_a.conj().T - (np.cos(alpha)*sx - np.sin(alpha)*sz)))
err_z = np.max(np.abs(R_a @ sz @ R_a.conj().T - (np.sin(alpha)*sx + np.cos(alpha)*sz)))
err_y = np.max(np.abs(R_a @ sy @ R_a.conj().T - sy))
print(f"  [{'PASS' if max(err_x, err_y, err_z) < 1e-12 else 'FAIL'}] rotation convention   err = {max(err_x, err_y, err_z):.2e}")
```

Expected: PASS at machine precision.

### 8.2 Direct: $\Gamma_{\text{asym}}$ is parameter-dependent chiral op

```python
# §8.2 — Verify Γ_asym(θ_1) = cos(θ_1/2) σ_x + sin(θ_1/2) σ_z anti-commutes with H_eff (asym frame)
def H_eff_asym_bloch(theta1, theta2, k):
    """Effective Hamiltonian Bloch components (a_x, a_y, a_z) for asymmetric walker.
    Returns the 2x2 traceless Hermitian matrix H = a_x σ_x + a_y σ_y + a_z σ_z."""
    c1, s1 = np.cos(theta1/2), np.sin(theta1/2)
    c2, s2 = np.cos(theta2/2), np.sin(theta2/2)
    a_x = c2 * s1 * np.sin(k)
    a_y = c1 * s2 + c2 * s1 * np.cos(k)
    a_z = -c1 * c2 * np.sin(k)
    return a_x * sx + a_y * sy + a_z * sz

errs = []
for _ in range(20):
    theta1 = np.random.uniform(0, PI)
    theta2 = np.random.uniform(0, PI)
    k = np.random.uniform(0, 2*PI)
    Gamma_asym = np.cos(theta1/2) * sx + np.sin(theta1/2) * sz
    H = H_eff_asym_bloch(theta1, theta2, k)
    anticomm = Gamma_asym @ H + H @ Gamma_asym
    errs.append(np.max(np.abs(anticomm)))
print(f"  [{'PASS' if max(errs) < 1e-12 else 'FAIL'}] Γ_asym anti-commutes with H_eff (20 random pts)   max err = {max(errs):.2e}")
```

Expected: PASS. Confirms the $\theta_1$-dependent chiral operator $\Gamma_{\text{asym}}$.

### 8.3 Direct: $\Gamma_{\text{sym}} = \sigma_x$ in symmetric frame

```python
# §8.3 — Verify σ_x is the chiral op in the symmetric frame.
def U_sym_bloch(theta1, theta2, k):
    """Bloch walker in symmetric frame: U_sym = R(θ_1/2) S_- R(θ_2) S_+ R(θ_1/2)."""
    R_half = coin_rotation(theta1 / 2)
    R2 = coin_rotation(theta2)
    Sp_k = np.diag([np.exp(1j*k), 1]).astype(complex)
    Sm_k = np.diag([1, np.exp(-1j*k)]).astype(complex)
    return R_half @ Sm_k @ R2 @ Sp_k @ R_half

errs_chi, errs_anti = [], []
for _ in range(40):
    theta1 = np.random.uniform(0.05, PI - 0.05)
    theta2 = np.random.uniform(0.05, PI - 0.05)
    k = np.random.uniform(0, 2*PI)
    U_s = U_sym_bloch(theta1, theta2, k)
    # Chiral relation: σ_x U_s σ_x = U_s^(-1)
    lhs = sx @ U_s @ sx
    rhs = U_s.conj().T
    errs_chi.append(np.max(np.abs(lhs - rhs)))
    # And: a_x' = 0 directly
    # Extract a_x' from U_s
    a_x_prime = -np.real((1j/2) * np.trace(sx @ U_s))
    errs_anti.append(abs(a_x_prime))

print(f"  [{'PASS' if max(errs_chi) < 1e-12 else 'FAIL'}] σ_x U_sym σ_x = U_sym^(-1)         max err = {max(errs_chi):.2e}")
print(f"  [{'PASS' if max(errs_anti) < 1e-12 else 'FAIL'}] a_x'(k) = 0 in symmetric frame    max err = {max(errs_anti):.2e}")
```

Expected: both PASS at machine precision. This is the key validation that $\Gamma = \sigma_x$ in the symmetric frame.

### 8.4 Cross-check: cylinder phase boundaries via winding

```python
# §8.4 — Winding-number scan reproduces Asbóth-Edge cylinder phase diagram
def winding_sym(theta1, theta2, ks):
    """Discrete winding number from a'(k) = (0, a_y', a_z') around the BZ.
    Sum of unwrapped Δφ over consecutive momentum samples."""
    c1, s1 = np.cos(theta1/2), np.sin(theta1/2)
    c2, s2 = np.cos(theta2/2), np.sin(theta2/2)
    a_y = c1 * s2 + c2 * s1 * np.cos(ks)
    a_z = -c2 * np.sin(ks)
    phi = np.arctan2(a_z, a_y)
    # Close the loop
    phi_closed = np.concatenate([phi, [phi[0]]])
    dphi = np.diff(phi_closed)
    # Unwrap (treat ±π jumps as ∓2π wraps)
    dphi = (dphi + PI) % (2 * PI) - PI
    return int(round(dphi.sum() / (2 * PI)))

# Sample at fine k-grid (continuous-k limit)
ks_fine = np.linspace(0, 2*PI, 400, endpoint=False)
thetas_scan = np.linspace(0.05, PI - 0.05, 40)
wind_grid = np.array([[winding_sym(t1, t2, ks_fine) for t2 in thetas_scan] for t1 in thetas_scan])

# Visualization
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(wind_grid.T, origin="lower", extent=[0.05, PI-0.05, 0.05, PI-0.05],
               cmap="RdYlBu_r", aspect="equal", vmin=-1, vmax=1)
ax.set_xlabel(r"$\theta_1$"); ax.set_ylabel(r"$\theta_2$")
ax.set_title("§8.4 — Winding ν in symmetric frame (continuous k)")
ax.set_xticks([0, PI/2, PI]); ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
ax.set_yticks([0, PI/2, PI]); ax.set_yticklabels(["0", r"$\pi/2$", r"$\pi$"])
plt.colorbar(im, ax=ax, label=r"$\nu$", ticks=[-1, 0, 1])
plt.tight_layout()
plt.show()

unique_phases = sorted(set(wind_grid.flatten()))
print(f"§8.4: winding values observed in [0.05, π-0.05]² = {unique_phases}")
```

Expected outcome: at least two distinct winding integers (likely $\{-1, 0\}$ or $\{0, 1\}$) showing across the parameter space, with transitions on the lines $\theta_1 \pm \theta_2 \in \{0, \pi\}$ matching N0/N2.

### 8.5 The T-D4 setup: same winding scan with Möbius momentum lattice

```python
# §8.5 — Compute the SAME winding integral but on the Möbius momentum lattice.
# This is the empirical input to T-D4: do cylinder and Möbius winding diagrams differ?

L_wind = 50

def winding_sym_at_momenta(theta1, theta2, L, mobius):
    return winding_sym(theta1, theta2, momenta(L, mobius=mobius))

wind_cyl = np.array([[winding_sym_at_momenta(t1, t2, L_wind, mobius=False) for t2 in thetas_scan] for t1 in thetas_scan])
wind_mob = np.array([[winding_sym_at_momenta(t1, t2, L_wind, mobius=True) for t2 in thetas_scan] for t1 in thetas_scan])
diff = wind_mob - wind_cyl

fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6))
extent = [0.05, PI-0.05, 0.05, PI-0.05]
vmin, vmax = min(wind_cyl.min(), wind_mob.min()) - 0.5, max(wind_cyl.max(), wind_mob.max()) + 0.5
im0 = axes[0].imshow(wind_cyl.T, origin="lower", extent=extent, cmap="RdYlBu_r", aspect="equal", vmin=vmin, vmax=vmax)
axes[0].set_title(f"Cylinder winding (L={L_wind})")
im1 = axes[1].imshow(wind_mob.T, origin="lower", extent=extent, cmap="RdYlBu_r", aspect="equal", vmin=vmin, vmax=vmax)
axes[1].set_title(f"Möbius winding (L={L_wind})")
im2 = axes[2].imshow(diff.T, origin="lower", extent=extent, cmap="RdBu_r", aspect="equal", vmin=-2, vmax=2)
axes[2].set_title("Möbius − Cylinder")
for ax in axes:
    ax.set_xlabel(r"$\theta_1$"); ax.set_ylabel(r"$\theta_2$")
for ax, im in zip(axes, [im0, im1, im2]):
    plt.colorbar(im, ax=ax, shrink=0.85)
plt.tight_layout()
plt.show()

print(f"§8.5: max |Δν| over the scan = {np.abs(diff).max()}")
print(f"      Cylinder unique values = {sorted(set(wind_cyl.flatten()))}")
print(f"      Möbius unique values   = {sorted(set(wind_mob.flatten()))}")
```

**This is the critical empirical test of T2.** Possible outcomes:
- $|\Delta\nu|$ is zero or vanishingly small ($O(1/L)$): supports 5.2-a (TRIM-exclusion only).
- $|\Delta\nu|$ takes integer values in $\{0, 1\}$ in a structured pattern: 5.2-b candidate; investigate further.
- $|\Delta\nu|$ takes integer values $> 1$: unexpected; investigate before claiming any T2 form.

### 8.6 Result of running §8.5 (executed 2026-05-16)

| Quantity | Value |
|---|---|
| Lattice size | $L = 50$ |
| Grid scanned | $40 \times 40 = 1600$ points in $(\theta_1, \theta_2) \in [0.05, \pi-0.05]^2$ |
| Cylinder winding values | $\{-1, 0\}$ |
| Möbius winding values | $\{-1, 0\}$ |
| **$\max_{(\theta_1,\theta_2)} \|\Delta\nu\|$** | **$0$** |
| Grid points with $\Delta\nu \neq 0$ | $0 / 1600$ |

**Outcome: T2 lands as 5.2-a.** The discrete winding numbers on cylinder and Möbius are *identical* across the entire scanned parameter grid. The TRIM-exclusion mechanism (which T1 and N2 establish) shifts the *location* of phase boundaries by $O(1/L)$, but does **not** alter the integer-valued topological invariant of the chiral DTQW. The dramatic ℤ → ℤ₂ reduction does not occur for the canonical $\Sigma = -\mathbb{I}$ walker.

**Project implications.**
- T2's contribution to the paper is now well-defined: TRIM-exclusion-driven phase-boundary shifts, with the *value* of the winding invariant robust under cylinder→Möbius. Modest result, still publishable, no longer open.
- T-D4's analytical task narrows considerably: prove that $\nu^{\text{Möb}}_L = \nu^{\text{cyl}}_L$ for all $L$ and all $(\theta_1, \theta_2)$ off the boundary lines. The proof should follow from the fact that $\phi(k) = \mathrm{atan2}(a_z'(k), a_y'(k))$ is a continuous function on the BZ and the shift from integer to half-odd-integer momentum lattice is a uniform $\pi/L$ translation — it cannot change the winding integer for a continuous function.
- T3's "5.2-b conditional content" (spec §5.3) is now confirmed null. T3 reduces cleanly to standard chiral-DTQW edge-mode counting on the cut walker — the same edge modes appear on cylinder and Möbius.
- The paper's strongest claims are now: **T1** (half-odd-integer spectrum), **N4** (deck-phase dynamical signature), and **T5** (Szegedy on Möbius ladder), with T2 + T3 + T4 supporting roles.

---

## §9. Outstanding for T-D4

T-D4's formal task: given the explicit chiral operator $\Gamma = \sigma_x$ (this document) and the explicit symmetric-frame Bloch coefficients $a_0', a_y', a_z'$, derive the winding-number formula on the discrete Möbius lattice $K^{\text{Möb}}_L$ and compare to cylinder $K^{\text{cyl}}_L$.

Concretely:

1. Define $\phi(k) = \mathrm{atan2}(a_z'(k), a_y'(k))$ as the angle of the symmetric-frame Bloch vector in the $yz$-plane.
2. Show that on cylinder, $\nu^{\text{cyl}}_L = \nu_\infty + O(1/L^p)$ for some $p$, with $\nu_\infty$ the continuous integral.
3. Show the analogous Möbius statement: $\nu^{\text{Möb}}_L = \nu_\infty + O(1/L^p)$ with the *same* $\nu_\infty$ — or, if they differ, characterize the difference exactly.
4. Identify any sub-leading contribution from the TRIM momenta $k = 0, \pi$ (which are absent from the Möbius lattice) that could change the integer winding.
5. If §8.5 numerically shows a difference: hypothesize the form, prove it analytically, and characterize when it occurs.

This document (T-D3) is the foundation. Pre-cautions in §2 are mandatory carry-overs into T-D4. Validation §8.4 is the cylinder baseline that T-D4 must match.

---

## §10. Document Status

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-16 | Initial T-D3 deliverable. Derives parameter-dependent $\Gamma_{\text{asym}}(\theta_1)$ in §3; uses time-frame change $W = R(-\theta_1/2)$ to obtain the symmetric-frame walker $U_{\text{sym}}$ in §4 with parameter-independent chiral operator $\Gamma_{\text{sym}} = \sigma_x$. Verifies $\sigma_x U_{\text{sym}}(k) \sigma_x = U_{\text{sym}}(k)^{-1}$ algebraically (§5) and provides numerical validation snippets (§8) that drop into the existing notebook. Sets up T-D4's winding-number computation (§7). Pre-cautions on sign conventions, atan2 usage, and frame consistency in §2. |

*End of T-D3.*
