# T-D1 — Explicit Walk Operators in Position+Coin Form

**Project:** Möbius Quantum Walk
**Deliverable:** T-D1 (Theory track, first artifact)
**Status:** Draft v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.2 on scope, conventions, and notation.

---

## Purpose

This document fixes the explicit operator-level definitions of all four walk protocols used in the project, in two forms each: position+coin (real-space) and momentum (Bloch-decomposed). It is the canonical reference for the numerics track to implement and for the theory track to derive results from. Subsequent theorem proofs and code modules cite operator equations from this document by section number.

This is **not** a paper section. The eventual paper §3 (model) will be a condensed and polished version of selected material here. T-D1 contains derivations and conventions that are working-document-level.

---

## §1. Notation Recap (matches spec §4.1)

| Symbol | Meaning |
|---|---|
| $L$ | Number of position sites; $L \in \mathbb{Z}_{\ge 4}$. |
| $\mathcal{H}_L = \ell^2(\mathbb{Z}/L\mathbb{Z}) \otimes \mathbb{C}^d$ | Coined-walker Hilbert space. |
| $\|x\rangle$, $x \in \{0, \dots, L-1\}$ | Position basis. |
| $\|R\rangle = (1, 0)^T$, $\|L\rangle = (0, 1)^T$ | Coin basis ($d=2$). |
| $\sigma_x, \sigma_y, \sigma_z$ | Pauli matrices in coin basis. |
| $T$ | Position translation: $T\|x\rangle = \|(x+1) \bmod L\rangle$. |
| $T^{-1}$ | Inverse translation: $T^{-1}\|x\rangle = \|(x-1) \bmod L\rangle$. |
| $R(\theta) = e^{-i\theta\sigma_y/2}$ | Coin rotation (real-valued, see §1.1). |
| $\Sigma$ | Deck operator on coin. **Canonical project choice: $\Sigma = -\mathbb{I}_2$.** |
| $H = \frac{1}{\sqrt 2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$ | Hadamard coin. |

### 1.1 Explicit form of $R(\theta)$

$$R(\theta) = \cos(\theta/2)\,\mathbb{I} - i\sin(\theta/2)\,\sigma_y = \begin{pmatrix}\cos(\theta/2) & -\sin(\theta/2)\\ \sin(\theta/2) & \cos(\theta/2)\end{pmatrix}.$$

Note: $R(\theta)$ is real-valued (no $i$'s after expansion), since $\sigma_y$ is purely imaginary.

### 1.2 Convention choice (important; commits the project)

We use **Kitagawa et al. 2010 split-step convention**: two half-shifts $S_+, S_-$ interleaved with two coin rotations. This is the original split-step walk definition. Asbóth & Edge 2015 use a related but distinct "two full shifts" convention; we do not use theirs. All comparisons to Asbóth & Edge will note the convention difference.

---

## §2. Cylinder Split-Step DTQW

### 2.1 Operators in position-coin basis

**Half-shift right (R-component only):**
$$S_+ = T \otimes |R\rangle\langle R|\;+\;\mathbb{I} \otimes |L\rangle\langle L| = \sum_{x=0}^{L-1}\Big(\big|(x+1) \bmod L,\,R\big\rangle\big\langle x,\,R\big| + \big|x,\,L\big\rangle\big\langle x,\,L\big|\Big).$$

**Half-shift left (L-component only):**
$$S_- = \mathbb{I} \otimes |R\rangle\langle R|\;+\;T^{-1} \otimes |L\rangle\langle L| = \sum_{x=0}^{L-1}\Big(\big|x,\,R\big\rangle\big\langle x,\,R\big| + \big|(x-1) \bmod L,\,L\big\rangle\big\langle x,\,L\big|\Big).$$

Both are unitary on $\mathcal{H}_L$. Position arithmetic is mod $L$ (cylinder boundary).

### 2.2 Walk operator (one full step)

$$\boxed{\;U^{\text{cyl}}_{\text{ss}}(\theta_1, \theta_2) := S_- \,(\,\mathbb{I} \otimes R(\theta_2)\,)\, S_+ \,(\,\mathbb{I} \otimes R(\theta_1)\,)\;}$$

For brevity we write $R(\theta_i)$ to mean $\mathbb{I} \otimes R(\theta_i)$ throughout when the context is unambiguous.

**Matrix dimension:** $2L \times 2L$ over $\mathbb{C}$, in basis ordering $(|0,R\rangle, |0,L\rangle, |1,R\rangle, |1,L\rangle, \dots)$ or alternative. Implementation choice — not physically meaningful, but tests must verify chosen ordering is consistent.

### 2.3 Bloch decomposition

Cylinder is translation-invariant; diagonalize with Fourier transform on position:
$$|k, c\rangle = \frac{1}{\sqrt L}\sum_{x=0}^{L-1} e^{ikx}\,|x, c\rangle, \qquad k \in K^{\text{cyl}}_L := \left\{\frac{2\pi n}{L} \;\middle|\; n = 0, 1, \dots, L-1\right\}.$$

In the $|k\rangle$ basis, $T \to e^{ik}$ and $T^{-1} \to e^{-ik}$. Thus:
$$S_+(k) = \begin{pmatrix}e^{ik} & 0\\ 0 & 1\end{pmatrix}, \qquad S_-(k) = \begin{pmatrix}1 & 0\\ 0 & e^{-ik}\end{pmatrix}.$$

The walk operator becomes a $2 \times 2$ unitary at each $k$:
$$U^{\text{cyl}}_{\text{ss}}(\theta_1, \theta_2; k) = S_-(k)\,R(\theta_2)\,S_+(k)\,R(\theta_1).$$

### 2.4 Bulk dispersion (explicit)

Let $c_i := \cos(\theta_i/2)$, $s_i := \sin(\theta_i/2)$. Direct computation (verified in this document; see §2.4.1 for the calculation):

$$U^{\text{cyl}}_{\text{ss}}(\theta_1, \theta_2; k) = \begin{pmatrix}c_1 c_2 e^{ik} - s_1 s_2 & -c_2 s_1 e^{ik} - s_2 c_1 \\ s_2 c_1 + c_2 s_1 e^{-ik} & c_1 c_2 e^{-ik} - s_1 s_2\end{pmatrix}.$$

This is in $\mathrm{SU}(2)$ (verify: $\det = c_1^2 c_2^2 - 2c_1 c_2 s_1 s_2 \cos k + s_1^2 s_2^2 + s_1^2 c_2^2 + c_1^2 s_2^2 - $ wait, let me just compute directly: $\det U = U_{11} U_{22} - U_{12} U_{21}$).

Eigenvalues are $e^{\pm i\varepsilon(k; \theta_1, \theta_2)}$ with quasi-energy

$$\boxed{\;\cos\varepsilon(k; \theta_1, \theta_2) = \cos(\theta_1/2)\cos(\theta_2/2)\cos k - \sin(\theta_1/2)\sin(\theta_2/2)\;}$$

Two bands per $k$: $\varepsilon^+(k) = +\arccos(\cdot)$, $\varepsilon^-(k) = -\arccos(\cdot)$, both in $(-\pi, \pi]$.

#### 2.4.1 Computation detail (for the numerics test suite to verify)

Step-by-step:

$S_+(k)\,R(\theta_1) = \begin{pmatrix}e^{ik} & 0\\ 0 & 1\end{pmatrix}\begin{pmatrix}c_1 & -s_1\\ s_1 & c_1\end{pmatrix} = \begin{pmatrix}c_1 e^{ik} & -s_1 e^{ik}\\ s_1 & c_1\end{pmatrix}.$

$R(\theta_2) [S_+(k) R(\theta_1)] = \begin{pmatrix}c_2 & -s_2\\ s_2 & c_2\end{pmatrix}\begin{pmatrix}c_1 e^{ik} & -s_1 e^{ik}\\ s_1 & c_1\end{pmatrix} = \begin{pmatrix}c_1 c_2 e^{ik} - s_1 s_2 & -c_2 s_1 e^{ik} - s_2 c_1\\ c_1 s_2 e^{ik} + c_2 s_1 & -s_1 s_2 e^{ik} + c_1 c_2\end{pmatrix}.$

Hmm, the $(2,2)$ entry I get is $-s_2 s_1 e^{ik} + c_2 c_1$, not $c_1 c_2 e^{-ik} - s_1 s_2$. Let me redo.

Wait, that's because $S_-$ hasn't been applied yet. Continuing:

$S_-(k) [R(\theta_2) S_+(k) R(\theta_1)] = \begin{pmatrix}1 & 0\\ 0 & e^{-ik}\end{pmatrix}\begin{pmatrix}c_1 c_2 e^{ik} - s_1 s_2 & -c_2 s_1 e^{ik} - s_2 c_1\\ c_1 s_2 e^{ik} + c_2 s_1 & -s_1 s_2 e^{ik} + c_1 c_2\end{pmatrix}$

$= \begin{pmatrix}c_1 c_2 e^{ik} - s_1 s_2 & -c_2 s_1 e^{ik} - s_2 c_1\\ c_1 s_2 + c_2 s_1 e^{-ik} & -s_1 s_2 + c_1 c_2 e^{-ik}\end{pmatrix}.$

So the final entries:
- $U_{11} = c_1 c_2 e^{ik} - s_1 s_2$
- $U_{12} = -c_2 s_1 e^{ik} - s_2 c_1$
- $U_{21} = c_1 s_2 + c_2 s_1 e^{-ik}$
- $U_{22} = -s_1 s_2 + c_1 c_2 e^{-ik}$

Trace: $U_{11} + U_{22} = c_1 c_2 (e^{ik} + e^{-ik}) - 2 s_1 s_2 = 2 c_1 c_2 \cos k - 2 s_1 s_2$. ✓

So $\cos\varepsilon(k) = \frac{1}{2}\text{tr}\,U(k) = c_1 c_2 \cos k - s_1 s_2$. ✓ (matches boxed equation above)

This derivation should be reproduced numerically by the simulator at $L = 50$, all $k \in K^{\text{cyl}}_L$, all $(\theta_1, \theta_2) \in [0, \pi]^2$ on a grid, with relative agreement $< 10^{-12}$.

### 2.5 Chiral symmetry — note for theory track

The split-step DTQW has a chiral symmetry $\Gamma$ such that $\Gamma U \Gamma = U^{-1}$, but the explicit form of $\Gamma$ depends on the time frame chosen. In the canonical Kitagawa convention used here, $\Gamma$ is non-trivial in the as-written walk operator; symmetric time-frame redefinition (per Asbóth & Obuse, *Phys. Rev. B* **88**, 121406(R), 2013) brings $\Gamma$ into a clean form.

**Theory track action item (T-D3 in spec §7.1):** Identify the explicit chiral operator $\Gamma$ for our convention by:
1. Computing $H_{\text{eff}}(k) = i\log U(k)$ via the parametrization $U(k) = a_0(k)\mathbb{I} - i \mathbf{a}(k)\cdot\boldsymbol{\sigma}$.
2. Extracting $a_0, a_x, a_y, a_z$ as explicit functions of $(k, \theta_1, \theta_2)$ — done in §2.4.1 algebraically.
3. Identifying the time frame in which $a_z(k) = 0$ identically; in that frame, $\Gamma = \sigma_z$ anti-commutes with $H_{\text{eff}}$.
4. The original frame's chiral operator is $\Gamma' = U_{\text{frame}}^{-1} \sigma_z U_{\text{frame}}$ where $U_{\text{frame}}$ is the time-frame change.

**Computed coefficients from §2.4.1:**
- $a_0(k) = c_1 c_2 \cos k - s_1 s_2$
- $a_z(k) = -c_1 c_2 \sin k$ (from $\text{Im}(U_{11}) = -a_z$)
- $a_x(k) = c_2 s_1 \sin k$ (from imaginary parts of off-diagonal)
- $a_y(k) = c_1 s_2 + c_2 s_1 \cos k$

Note $a_z \neq 0$ in general — the chiral time frame requires modification. The eventual paper §3 will give the explicit time-frame-shift; this document just records the coefficients.

---

## §3. Möbius Split-Step DTQW (Canonical $\Sigma = -\mathbb{I}$)

### 3.1 Anti-periodic boundary condition

The canonical Möbius walker has the same operator form as the cylinder walker, **but acts on a different Hilbert space** — the anti-periodic subspace defined by:
$$\psi(x+L, c) = -\psi(x, c) \quad \text{for all } c \in \{R, L\}.$$

Equivalently, the Hilbert space is

$$\mathcal{H}_L^{\text{Möb}} = \left\{\psi: \mathbb{Z} \to \mathbb{C}^2 \;\middle|\; \psi(x+L) = -\psi(x),\; \sum_{x=0}^{L-1}\|\psi(x)\|^2 < \infty\right\}.$$

This is isomorphic to $\mathbb{C}^L \otimes \mathbb{C}^2$ via the restriction map $\psi \mapsto \psi|_{\{0, \dots, L-1\}}$, and we use this isomorphism implicitly when implementing the walker as a $2L \times 2L$ matrix.

### 3.2 Quotient construction (equivalent formulation)

Define the cylinder walker on a $2L$-position lattice (period $2L$), call it $U^{\text{cyl}}_{ss, 2L}(\theta_1, \theta_2)$. Define the deck operator
$$D := T^L \otimes \Sigma \quad \text{on } \mathcal{H}_{2L}, \qquad \Sigma = -\mathbb{I}_2.$$

Then $D^2 = T^{2L} \otimes \mathbb{I} = \mathbb{I}$ (since $T^{2L} = \mathbb{I}$ on the $2L$-cylinder). $D$ has eigenvalues $\pm 1$.

The Möbius walker is the restriction of $U^{\text{cyl}}_{ss, 2L}$ to the $D = -1$ eigenspace:
$$U^{\text{Möb}}_{ss}(\theta_1, \theta_2) := U^{\text{cyl}}_{ss, 2L}(\theta_1, \theta_2)\big|_{D = -1}.$$

The $D = -1$ eigenspace has dimension $L \cdot 2 = 2L$, matching $\dim \mathcal{H}_L^{\text{Möb}}$.

**Why this works:** $\Sigma = -\mathbb{I}$ commutes with all coin operations and with translation, hence with $U^{\text{cyl}}_{ss, 2L}$. Restriction of a unitary to an invariant subspace is itself unitary.

**Why $\Sigma = -\mathbb{I}$ is the project's canonical choice (recap from spec §3.2):** $R(\theta) = e^{-i\theta\sigma_y/2}$ requires $[\Sigma, \sigma_y] = 0$; the spin-dependent shift $S$ requires $[\Sigma, \sigma_z] = 0$ (since the coin part of $S$ involves $\sigma_z$-projections). Both constraints together force $\Sigma \propto \mathbb{I}$. The choice $\Sigma = +\mathbb{I}$ is the cylinder; $\Sigma = -\mathbb{I}$ is the Möbius.

### 3.3 Twisted Bloch decomposition

The momentum eigenstates compatible with the anti-periodic BC are
$$|k, c\rangle^{\text{Möb}} = \frac{1}{\sqrt L}\sum_{x=0}^{L-1} e^{ikx}\,|x, c\rangle, \qquad k \in K^{\text{Möb}}_L := \left\{\frac{(2n+1)\pi}{L} \;\middle|\; n = 0, 1, \dots, L-1\right\}.$$

These satisfy $\psi(x+L) = e^{ikL}\psi(x) = e^{i(2n+1)\pi}\psi(x) = -\psi(x)$ ✓.

In this basis, the walk operator at each $k$ is **identical to the cylinder walk operator** evaluated at the same $k$:
$$U^{\text{Möb}}_{ss}(\theta_1, \theta_2; k) = S_-(k)\,R(\theta_2)\,S_+(k)\,R(\theta_1) = U^{\text{cyl}}_{ss}(\theta_1, \theta_2; k).$$

The only difference between cylinder and Möbius is **which $k$ values are populated**:
- Cylinder: $k \in \{0, 2\pi/L, 4\pi/L, \dots, 2(L-1)\pi/L\}$.
- Möbius: $k \in \{\pi/L, 3\pi/L, 5\pi/L, \dots, (2L-1)\pi/L\}$.

### 3.4 T1 — half-odd-integer momentum quantization (proved here)

**Theorem.** The quasi-energy spectrum of $U^{\text{Möb}}_{ss}(\theta_1, \theta_2)$ is
$$\text{spec}\,U^{\text{Möb}}_{ss} = \left\{e^{\pm i\varepsilon(k; \theta_1, \theta_2)} \;:\; k \in K^{\text{Möb}}_L\right\}, \qquad \cos\varepsilon(k) = c_1 c_2 \cos k - s_1 s_2,$$
where $K^{\text{Möb}}_L = \{(2n+1)\pi/L : n = 0, \dots, L-1\}$.

**Proof.** §3.2 establishes that $U^{\text{Möb}}_{ss}$ is the restriction of $U^{\text{cyl}}_{ss, 2L}$ to the $D = -1$ eigenspace. The $D = -1$ eigenspace is spanned by $\{|k, c\rangle^{\text{Möb}} : k \in K^{\text{Möb}}_L, c \in \{R, L\}\}$. The walk operator's action on this subspace is fiber-wise identical to the cylinder's action at the same momenta (§3.3). The cylinder dispersion (§2.4) gives the quasi-energies. ∎

**Consequence (TRIM exclusion).** The momenta $k = 0$ and $k = \pi$ — the time-reversal-invariant momenta of 1D systems — are absent from $K^{\text{Möb}}_L$:
- $k = 0$: never in $K^{\text{Möb}}_L$ for any $L$.
- $k = \pi$: in $K^{\text{Möb}}_L$ iff $\pi = (2n+1)\pi/L$ for some integer $n$, i.e., iff $L = 2n+1$ is odd. (Wait, $(2n+1)/L = 1$ means $L = 2n+1$, so $k = \pi$ is in $K^{\text{Möb}}_L$ for **odd** $L$, not even. Re-check: for $L$ even, $\pi$ is in $K^{\text{cyl}}_L$ but not $K^{\text{Möb}}_L$. For $L$ odd, $\pi$ is in $K^{\text{Möb}}_L$ and not $K^{\text{cyl}}_L$.)

This parity-of-$L$ subtlety is why the spec §8.M3 mandates separate analysis of even and odd $L$.

### 3.5 Chiral symmetry persistence on Möbius

Since $\Sigma = -\mathbb{I}$ commutes with every operator on coin space (including any chiral operator $\Gamma$), the chiral symmetry of the cylinder walker lifts to the Möbius walker without modification:
$$\Gamma U^{\text{Möb}}_{ss} \Gamma = (U^{\text{Möb}}_{ss})^{-1}$$
holds whenever the analogous cylinder relation holds. The chiral classification (winding numbers) is therefore well-defined on Möbius. The *values* of the winding integrals — which involve $\oint dk$ over the BZ — may differ between cylinder and Möbius due to the different discrete momentum lattices, and this is the technical heart of T2 (spec §5.2).

---

## §4. Hadamard DTQW (Cylinder + Möbius)

### 4.1 Operators

**Full shift** (R goes right, L goes left in one step):
$$F := T \otimes |R\rangle\langle R| + T^{-1} \otimes |L\rangle\langle L|.$$

**Hadamard coin:** $H = \frac{1}{\sqrt 2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$.

### 4.2 Walk operators

$$U^{\text{cyl}}_H := F \,(\,\mathbb{I} \otimes H\,), \qquad U^{\text{Möb}}_H := F^{\text{Möb}} \,(\,\mathbb{I} \otimes H\,).$$

Where $F^{\text{Möb}}$ is the full shift on $\mathcal{H}_L^{\text{Möb}}$ (anti-periodic BC).

### 4.3 Bloch decomposition

In momentum space:
$$F(k) = \begin{pmatrix}e^{ik} & 0\\ 0 & e^{-ik}\end{pmatrix}, \qquad U_H(k) = F(k)\,H = \frac{1}{\sqrt 2}\begin{pmatrix}e^{ik} & e^{ik}\\ e^{-ik} & -e^{-ik}\end{pmatrix}.$$

Trace: $\text{tr}\,U_H(k) = \frac{1}{\sqrt 2}(e^{ik} - e^{-ik}) = i\sqrt 2 \sin k$. So $\cos\varepsilon_H(k) = \frac{1}{\sqrt 2}\sin k - i \cdot 0$. Wait, this is imaginary; the trace must be real for $U \in \mathrm{SU}(2)$.

Let me re-check. $\det U_H(k) = \frac{1}{2}(e^{ik} \cdot (-e^{-ik}) - e^{ik} \cdot e^{-ik}) = \frac{1}{2}(-1 - 1) = -1$. So $U_H(k) \in \mathrm{U}(2) \setminus \mathrm{SU}(2)$; det is $-1$, not $1$.

This means $U_H(k) = e^{i\pi/2 \cdot \text{something}} \cdot \mathrm{SU}(2)$ matrix. Eigenvalues $\lambda$ satisfy $\lambda_1 \lambda_2 = -1$, so $\lambda_1 = e^{i\varepsilon}, \lambda_2 = -e^{-i\varepsilon}$ for some $\varepsilon$.

Trace: $\lambda_1 + \lambda_2 = e^{i\varepsilon} - e^{-i\varepsilon} = 2i\sin\varepsilon$. We had trace $= i\sqrt 2 \sin k$. So $\sin\varepsilon = \frac{1}{\sqrt 2}\sin k$, giving $\varepsilon_H(k) = \arcsin(\sin k / \sqrt 2)$.

Bulk dispersion: $\sin\varepsilon_H(k) = \frac{1}{\sqrt 2}\sin k$, so $\varepsilon_H(k) \in [-\pi/4, \pi/4]$ (and the second band is at $\pi - \varepsilon_H(k)$ by the eigenvalue structure).

This is fine; the Hadamard walker is well-known. The Möbius version replaces $k \in K^{\text{cyl}}_L$ with $k \in K^{\text{Möb}}_L$, identically to the split-step case.

### 4.4 Role in the paper

Hadamard walker confirms T1 (half-odd-integer momenta) without parameters $(\theta_1, \theta_2)$ — universality across the protocol class. No phase diagram (no parameters), just spectrum comparison.

---

## §5. Three-State Grover DTQW

### 5.1 Operators

Coin space: $\mathbb{C}^3$ with basis $\{|0\rangle, |+\rangle, |-\rangle\}$ (stay, right, left).

**Grover coin (3-state):**
$$G_3 = \frac{2}{3}J_3 - \mathbb{I}_3 = \frac{1}{3}\begin{pmatrix}-1 & 2 & 2\\ 2 & -1 & 2\\ 2 & 2 & -1\end{pmatrix}, \qquad J_3 = \begin{pmatrix}1 & 1 & 1\\ 1 & 1 & 1\\ 1 & 1 & 1\end{pmatrix}.$$

**Three-state shift:**
$$S_3 = \mathbb{I} \otimes |0\rangle\langle 0| + T \otimes |+\rangle\langle +| + T^{-1} \otimes |-\rangle\langle -|.$$

### 5.2 Walk operators

$$U^{\text{cyl}}_3 := S_3 \,(\,\mathbb{I} \otimes G_3\,), \qquad U^{\text{Möb}}_3 := S_3^{\text{Möb}} \,(\,\mathbb{I} \otimes G_3\,).$$

### 5.3 Bloch decomposition (sketch)

$S_3(k) = \text{diag}(1, e^{ik}, e^{-ik})$ on $\mathbb{C}^3$. $U_3(k) = S_3(k) G_3$, a $3 \times 3$ unitary at each $k$. Three bands per $k$.

Möbius: $k \in K^{\text{Möb}}_L$, three bands per allowed $k$, total $3L$ states matching $\dim \mathcal{H}_L^{\text{Möb}}$ for $d = 3$.

### 5.4 Role in the paper

Three-state walker confirms T1 with a larger coin space ($d = 3$). No parameters; spectrum-only comparison.

---

## §6. Szegedy Walks on Prism and Möbius Ladder Graphs

### 6.1 The two graphs

Both graphs have $2L$ vertices, indexed $(x, r)$ with $x \in \{0, \dots, L-1\}$, $r \in \{0, 1\}$. They differ only at the boundary edges.

**Prism graph $Y_L$ (cylinder counterpart):**
- In-row edges: $(x, r) \sim (x+1, r)$ for $x \in \{0, \dots, L-2\}$, $r \in \{0, 1\}$.
- Closing in-row edges: $(L-1, r) \sim (0, r)$ for $r \in \{0, 1\}$.
- Rung edges: $(x, 0) \sim (x, 1)$ for $x \in \{0, \dots, L-1\}$.

**Möbius ladder $M_L$:**
- In-row edges: $(x, r) \sim (x+1, r)$ for $x \in \{0, \dots, L-2\}$, $r \in \{0, 1\}$.
- Closing twisted edges: $(L-1, 0) \sim (0, 1)$ and $(L-1, 1) \sim (0, 0)$. (This is the Möbius twist.)
- Rung edges: $(x, 0) \sim (x, 1)$ for $x \in \{0, \dots, L-1\}$.

Both are 3-regular ($|E| = 3L$, $|\vec E| = 6L$ directed edges).

### 6.2 Adjacency matrices

In the basis ordering $\{(0,0), (0,1), (1,0), (1,1), \dots, (L-1, 0), (L-1, 1)\}$:

$A^{Y_L}$ and $A^{M_L}$ are $2L \times 2L$ block-circulant matrices over $\mathbb{Z}/L\mathbb{Z}$, with $2 \times 2$ blocks:
- Diagonal block: $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ (the rung edge between row 0 and row 1 at the same $x$).
- Adjacent blocks (off-diagonal): $\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}$ for in-row edges $(x, r) \sim (x+1, r)$.
- Boundary block from $(L-1, \cdot)$ to $(0, \cdot)$:
  - $Y_L$: $\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}$ (untwisted).
  - $M_L$: $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ (twisted — swap rows).

### 6.3 Szegedy walk operators

**Classical chain transition matrix:** $P^G_{vw} = \frac{1}{3}A^G_{vw}$ for $G \in \{Y_L, M_L\}$ (uniform random walk on a 3-regular graph).

**Edge-state vectors:** for each vertex $v$,
$$|\pi_v\rangle = \sum_w \sqrt{P^G_{vw}}\,|v\rangle|w\rangle = \frac{1}{\sqrt 3}\sum_{w \sim v} |v\rangle|w\rangle.$$

**Projection operator:** $\Pi_G = \sum_v |\pi_v\rangle\langle\pi_v|$.

**Reflection:** $R_G = 2\Pi_G - \mathbb{I}_{|V|^2}$.

**Swap:** $\mathcal{S} : |v\rangle|w\rangle \to |w\rangle|v\rangle$.

**Szegedy walker:**
$$U^{\text{Sze}}_G := \mathcal{S}\,R_G = \mathcal{S}\,(2\Pi_G - \mathbb{I}).$$

This is $4L^2 \times 4L^2$ in principle, but the dynamics preserve the edge subspace of dimension $|\vec E| = 6L$. Implementations should restrict to the edge subspace for efficiency.

### 6.4 Spectral structure (for theory track)

Szegedy walker spectrum is determined by the spectrum of $P^G$ via Szegedy's spectral theorem:

If $P^G$ has eigenvalues $\{\lambda_j\}$ (real, in $[-1, 1]$ for a doubly-stochastic transition matrix), then $U^{\text{Sze}}_G$ has eigenvalues $\{e^{\pm i\arccos\lambda_j}\}$ plus possibly some $\pm 1$ eigenvalues from the edge subspace structure.

**Comparison strategy for T5:** the prism graph $Y_L$ and Möbius ladder $M_L$ have *different* adjacency spectra — this is a known result in algebraic graph theory. Quantizing each gives different Szegedy spectra. The half-odd-integer signature of T1 has an analog here in the eigenvalue structure of $A^{M_L}$ vs. $A^{Y_L}$.

**Theory track action item:** derive the eigenvalues of $A^{Y_L}$ and $A^{M_L}$ in closed form using the rung-swap × position-rotation symmetry of each graph. Both graphs commute with rung-swap (the $\mathbb{Z}_2$ symmetry $(x, r) \to (x, 1-r)$); they differ in how this symmetry combines with position rotation. The analytical eigenvalues are
- $Y_L$: $\lambda^\pm_n = \pm 1 + 2\cos(2\pi n/L)$ for $n = 0, 1, \dots, L-1$ (sign from rung-swap eigenvalue).
- $M_L$: should be similar but with momentum quantization shift due to the twist; expected form $\lambda_n^\pm = \pm 1 + 2\cos(\pi(2n+1)/L)$ (to be verified).

If the conjectured $M_L$ spectrum is correct, T5 follows directly: half-odd-integer-quantized eigenvalues of $A^{M_L}$ map to a Szegedy walker spectrum distinct from $Y_L$'s integer-quantized one.

---

## §7. Implementation Hints for the Numerics Track

These notes are practical and non-binding; the numerics track owner has discretion.

### 7.1 Hilbert space ordering

Use the convention `psi[x*d + c]` where `x` is position index and `c` is coin index (column-major-like). Or use a 2D array `psi[x, c]` if the implementation supports it. Either is fine; document the choice in code.

### 7.2 Operator construction for cylinder + Möbius

The shifts $T, T^{-1}$ are circulant matrices on the position space:
- Cylinder: standard $L \times L$ circulant with 1 on the off-diagonal.
- Möbius: $L \times L$ circulant with 1 on the off-diagonal **and a $-1$ on the boundary entry** (the wraparound $|L-1\rangle \to |0\rangle$ entry becomes $-1$ instead of $+1$).

Implementation tip: implement once as `shift(L, sign=+1)` for cylinder and `shift(L, sign=-1)` for Möbius. Both are sparse $L \times L$ matrices.

### 7.3 Test suite (mandatory before any new figure)

- `test_unitarity`: $\|U^\dagger U - \mathbb{I}\| < 10^{-12}$ for both cylinder and Möbius walkers.
- `test_shift_BC`: `shift(L, -1) @ shift(L, -1) @ ... @ shift(L, -1)` ($L$ times) equals $-\mathbb{I}_L$ (since $L$ Möbius shifts wrap around with the $-1$ phase).
- `test_dispersion`: numerical spectrum at $L = 50$ matches analytical $\cos\varepsilon = c_1 c_2 \cos k - s_1 s_2$ to relative error $< 10^{-12}$ for 100 random $(\theta_1, \theta_2)$.
- `test_cylinder_baseline`: Asbóth–Edge phase diagram reproduced (per spec §6.8 N0).
- `test_TRIM_exclusion`: $k = 0$ is in cylinder spectrum, not Möbius spectrum (any $L$); $k = \pi$ logic per parity of $L$.

### 7.4 Performance

At $L = 200$, $\dim \mathcal{H} = 400$, full eigendecomposition is $\sim 10$ms. The phase-diagram experiment N2 ($51 \times 51$ grid) requires ~2600 diagonalizations, total $\sim 30$s. Acceptable on a laptop.

---

## §8. Cross-References to Spec

| T-D1 Section | Spec Section | Topic |
|---|---|---|
| §1 | §4.1 | Notation |
| §2 | §4.2 | Cylinder split-step DTQW |
| §3 | §4.2 + §3.1 + §3.2 | Möbius split-step DTQW + deck operator |
| §3.4 | §5.1 (T1) | Half-odd-integer momentum theorem |
| §3.5 | §5.2 (T2) | Chiral symmetry, gateway to T2 |
| §4 | §4.3 | Hadamard DTQW |
| §5 | §4.4 | Three-state Grover DTQW |
| §6 | §3.1 + §4.5 | Möbius ladder graph + Szegedy walks |
| §7 | §6.9, §11 | Numerics implementation |

---

## §9. Outstanding Items for Theory Track

Things this document defers to subsequent theory-track work:

1. **Explicit chiral operator $\Gamma$** in our convention (T-D3). Coefficients $a_{0,x,y,z}(k)$ are computed in §2.4.1; time-frame change to put $a_z = 0$ remains.
2. **Winding-number formula** evaluated at $K^{\text{Möb}}_L$ vs. $K^{\text{cyl}}_L$ (T-D4). The integral form is standard; the discrete-vs.-continuous BZ comparison is the substance of T2.
3. **Edge-mode construction** on cut walker (T-D5) — standard transfer-matrix exercise, conditional T3 interpretation per spec §5.3 v1.2.
4. **$M_L$ adjacency spectrum** in closed form (T-D7) — conjecture in §6.4 to be verified.

---

## §10. Document Status

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial T-D1 deliverable. Operator definitions for split-step (cylinder + Möbius), Hadamard, three-state Grover, and Szegedy walks (prism + Möbius ladder). Bulk dispersion derived for split-step. Coefficients $a_0, a_x, a_y, a_z$ for chiral analysis recorded. T1 proved at the Bloch level. Implementation hints for numerics track. Awaits theory-track and numerics-track follow-on (T-D2 onward, N-D1 onward). |

*End of T-D1.*
