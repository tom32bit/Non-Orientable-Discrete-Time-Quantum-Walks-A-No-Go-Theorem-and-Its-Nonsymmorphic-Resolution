# T-D7 — Adjacency Spectrum of the Möbius Ladder $M_L$ and Prism Graph $Y_L$

**Project:** Möbius Quantum Walk
**Deliverable:** T-D7 (Theory track; depends on T-D1)
**Status:** Draft v1.0
**Authority:** Defers to `mobius_dtqw_research_spec.md` v1.4 and `T-D1_walk_operators.md` v1.0 on conventions, notation, and graph definitions.

---

## §0. Purpose

T-D7 proves the conjecture from T-D1 §6.4 about the adjacency spectra of the Möbius ladder $M_L$ and prism graph $Y_L$. The proof identifies the **structural mechanism** by which non-orientability of the underlying graph manifests in the spectrum: the rung-swap-antisymmetric sector $V_-$ of $M_L$ inherits an anti-periodic boundary condition from the Möbius twist, giving half-odd-integer crystal momentum quantization — while the rung-symmetric sector $V_+$ is identical to $Y_L$.

This is the spectral foundation of **T5**: Szegedy walks (which are coinless and depend only on graph adjacency) on $M_L$ vs $Y_L$ exhibit different spectra, with the difference traceable purely to spatial non-orientability — no chiral symmetry or coin structure required.

The N7 validation in `mobius_dtqw_simulator.ipynb` already confirmed both spectrum formulas to relative error $\sim 5\times 10^{-15}$ at $L = 30$. T-D7 promotes this numerical observation to a theorem with explicit eigenvector construction.

---

## §1. Setup

### 1.1 The graphs

**Möbius ladder $M_L$.** Vertex set $V = \{(x, r) : x \in \mathbb{Z}/L\mathbb{Z},\ r \in \{0, 1\}\}$; $|V| = 2L$.

Edges:
- **Rung**: $(x, 0) \sim (x, 1)$ for all $x \in \{0, \dots, L-1\}$.
- **In-row non-boundary**: $(x, r) \sim (x+1, r)$ for $x \in \{0, \dots, L-2\}$, $r \in \{0, 1\}$.
- **Twisted boundary** (the Möbius identification): $(L-1, r) \sim (0, 1-r)$ for $r \in \{0, 1\}$.

**Prism graph $Y_L$** (cylinder counterpart). Same vertices, same rung and non-boundary edges, but untwisted boundary: $(L-1, r) \sim (0, r)$ for $r \in \{0, 1\}$. Equivalently $Y_L = C_L \square K_2$ (Cartesian product).

Both graphs are 3-regular.

### 1.2 Hilbert space and notation

Functions on the vertex set form $\mathcal{H} := \mathbb{C}^V \cong \mathbb{C}^{2L}$, with basis $\{|x, r\rangle\}_{x, r}$.

We will identify the basis with the ordering $|x, r\rangle \leftrightarrow$ index $2x + r$, but this is only for implementation; the proofs are basis-independent.

Adjacency operator: $A: \mathcal{H} \to \mathcal{H}$ with $(A\psi)(v) = \sum_{w \sim v} \psi(w)$.

---

## §2. The Theorem

### 2.1 Spectrum of the prism graph

**Theorem (Prism spectrum).** The adjacency spectrum of $Y_L$ is
$$\boxed{\;\mathrm{spec}(A_{Y_L}) = \{2\cos(2\pi n / L) + 1,\ 2\cos(2\pi n / L) - 1 : n = 0, 1, \dots, L-1\}.\;}$$

### 2.2 Spectrum of the Möbius ladder

**Theorem (Möbius ladder spectrum).** The adjacency spectrum of $M_L$ is
$$\boxed{\;\mathrm{spec}(A_{M_L}) = \{2\cos(2\pi n / L) + 1,\ 2\cos((2n+1)\pi/L) - 1 : n = 0, 1, \dots, L-1\}.\;}$$

### 2.3 Where the graphs differ

The eigenvalue sets agree in the **"$+1$" sector** (rung-symmetric eigenmodes have integer momentum, identically on both graphs):
$$\mathrm{spec}_+(A_{M_L}) = \mathrm{spec}_+(A_{Y_L}) = \{2\cos(2\pi n / L) + 1\}.$$

They differ in the **"$-1$" sector** (rung-antisymmetric eigenmodes):
$$\mathrm{spec}_-(A_{Y_L}) = \{2\cos(2\pi n / L) - 1\}\quad\text{vs.}\quad \mathrm{spec}_-(A_{M_L}) = \{2\cos((2n+1)\pi/L) - 1\}.$$

**Möbius non-orientability shifts the momentum quantization in the rung-antisymmetric sector from integer to half-odd-integer — and only in that sector.**

---

## §3. The Rung-Swap Symmetry

### 3.1 The involution $\tau$

Define $\tau: \mathcal{H} \to \mathcal{H}$ by $(\tau\psi)(x, r) := \psi(x, 1-r)$. This is a unitary involution: $\tau^2 = \mathbb{I}$, $\tau = \tau^\dagger$. It swaps the two rows of the ladder.

### 3.2 $\tau$ commutes with both adjacency operators

**Claim.** $[\tau, A_{M_L}] = [\tau, A_{Y_L}] = 0$.

**Proof.** $\tau$ permutes the vertex set; it commutes with the adjacency operator iff $\tau$ induces a graph automorphism. On $Y_L$, row-swap is obviously an automorphism (it preserves all rung, in-row, and untwisted boundary edges). On $M_L$, row-swap preserves rungs and in-row edges; the twisted boundary edge $(L-1, r) \sim (0, 1-r)$ maps under $\tau$ to $(L-1, 1-r) \sim (0, r)$, which is the same edge (re-labeled). Hence $\tau$ is a graph automorphism of both graphs. ∎

### 3.3 Eigenspace decomposition

$\tau$ has eigenvalues $\pm 1$. Decompose $\mathcal{H} = V_+ \oplus V_-$:
- $V_+ := \mathrm{ker}(\tau - \mathbb{I}) = \{\psi : \psi(x, 0) = \psi(x, 1)\}$, $\dim = L$.
- $V_- := \mathrm{ker}(\tau + \mathbb{I}) = \{\psi : \psi(x, 0) = -\psi(x, 1)\}$, $\dim = L$.

Both adjacency operators preserve this decomposition (since they commute with $\tau$). Diagonalize each sector separately.

**Notation.** For $\psi \in V_+$, let $v_+(x) := \psi(x, 0) = \psi(x, 1)$. For $\psi \in V_-$, let $v_-(x) := \psi(x, 0) = -\psi(x, 1)$. Both $v_\pm: \mathbb{Z}/L\mathbb{Z} \to \mathbb{C}$ are functions on the position circle.

---

## §4. Action on the Rung-Symmetric Sector $V_+$

### 4.1 Both graphs

For $\psi \in V_+$ and any $x$, the neighbors of $(x, r)$ contribute:
- Rung partner $(x, 1-r)$: $\psi(x, 1-r) = v_+(x)$.
- In-row left $(x-1, r)$ (or twisted variant): $\psi = v_+(x-1)$ — twist does not matter because $\psi$ is $r$-symmetric.
- In-row right $(x+1, r)$: $\psi = v_+(x+1)$.

Therefore $(A\psi)(x, r) = v_+(x-1) + v_+(x) + v_+(x+1)$, with **periodic** position indices mod $L$ (the twist swaps rows, but in $V_+$ both rows are equal, so the twist has no effect).

In terms of the position-circle operator on $v_+$:
$$A_{M_L}\big|_{V_+} = A_{Y_L}\big|_{V_+} = A_{C_L} + \mathbb{I}_L,$$
where $A_{C_L}$ is the adjacency of the cycle graph $C_L$ on $L$ vertices.

### 4.2 Cycle spectrum

The cycle $C_L$ has known spectrum
$$\mathrm{spec}(A_{C_L}) = \{2\cos(2\pi n / L) : n = 0, 1, \dots, L-1\},$$
with eigenvectors $v_+^{(n)}(x) = \frac{1}{\sqrt L} e^{2\pi i n x / L}$.

Therefore
$$\mathrm{spec}_+(A_{M_L}) = \mathrm{spec}_+(A_{Y_L}) = \{2\cos(2\pi n / L) + 1 : n = 0, \dots, L-1\}. \quad\square$$

---

## §5. Action on the Rung-Antisymmetric Sector $V_-$

This is where the graphs diverge.

### 5.1 Prism graph $Y_L$ (cylinder counterpart)

For $\psi \in V_-$, $\psi(x, 0) = v_-(x)$ and $\psi(x, 1) = -v_-(x)$.

For non-boundary $x$ and $r = 0$:
$$(A\psi)(x, 0) = \psi(x, 1) + \psi(x-1, 0) + \psi(x+1, 0) = -v_-(x) + v_-(x-1) + v_-(x+1).$$

For boundary $x = L-1$, $r = 0$, on $Y_L$ (untwisted): the right neighbor is $(0, 0)$, so $\psi = v_-(0)$.
$$(A\psi)(L-1, 0) = -v_-(L-1) + v_-(L-2) + v_-(0).$$

This is the same formula $(A\psi)(x, 0) = -v_-(x) + v_-(x-1) + v_-(x+1)$ with **periodic** index $x+1 \equiv 0 \pmod L$ when $x = L-1$.

In position-circle form:
$$A_{Y_L}\big|_{V_-} = A_{C_L} - \mathbb{I}_L,$$
with the cycle's periodic BC.

Spectrum: $\{2\cos(2\pi n / L) - 1 : n = 0, \dots, L-1\}$.

Combining with §4 gives Theorem 2.1: $\mathrm{spec}(A_{Y_L}) = \{2\cos(2\pi n / L) \pm 1\}$. $\square$

### 5.2 Möbius ladder $M_L$ — the twist enters

For $\psi \in V_-$ and the boundary $x = L-1$, $r = 0$ on $M_L$ (twisted): the right neighbor is $(0, 1-0) = (0, 1)$, so $\psi(0, 1) = -v_-(0)$.

$$(A\psi)(L-1, 0) = -v_-(L-1) + v_-(L-2) + \psi(0, 1) = -v_-(L-1) + v_-(L-2) - v_-(0).$$

Define the **anti-periodic extension** $\tilde{v}_-(x)$ on $\mathbb{Z}$ by $\tilde{v}_-(x+L) := -\tilde{v}_-(x)$, agreeing with $v_-$ on $\{0, \dots, L-1\}$. Then the boundary formula becomes
$$(A\psi)(L-1, 0) = -\tilde{v}_-(L-1) + \tilde{v}_-(L-2) + \tilde{v}_-(L) = -v_-(L-1) + v_-(L-2) - v_-(0),$$
matching above ✓. The Möbius twist exactly implements **anti-periodic BC on $v_-$**.

In position-circle form:
$$A_{M_L}\big|_{V_-} = \tilde{A}_{C_L} - \mathbb{I}_L,$$
where $\tilde{A}_{C_L}$ is the cycle adjacency with anti-periodic BC.

### 5.3 Anti-periodic cycle spectrum

Diagonalize $\tilde{A}_{C_L}$ by plane waves $\tilde{v}^{(n)}(x) = \frac{1}{\sqrt L} e^{ik x}$ satisfying $\tilde{v}^{(n)}(x+L) = -\tilde{v}^{(n)}(x)$.

Anti-periodicity: $e^{ikL} = -1$, so $k \in \{(2n+1)\pi / L : n = 0, 1, \dots, L-1\}$.

At these momenta: $\tilde{A}_{C_L}\tilde{v}^{(n)} = (e^{ik} + e^{-ik})\tilde{v}^{(n)} = 2\cos(k_n)\tilde{v}^{(n)}$ with $k_n = (2n+1)\pi/L$.

Therefore
$$\mathrm{spec}(\tilde{A}_{C_L}) = \{2\cos((2n+1)\pi/L) : n = 0, \dots, L-1\}.$$

So $\mathrm{spec}_-(A_{M_L}) = \{2\cos((2n+1)\pi/L) - 1 : n = 0, \dots, L-1\}.$

Combining with §4 gives Theorem 2.2:
$$\mathrm{spec}(A_{M_L}) = \{2\cos(2\pi n / L) + 1\} \cup \{2\cos((2n+1)\pi/L) - 1\}. \quad\square$$

---

## §6. Eigenvector Catalog

For both graphs and each $n \in \{0, \dots, L-1\}$:

**Rung-symmetric eigenvectors** ($V_+$, eigenvalue $\lambda_+^{(n)} = 2\cos(2\pi n/L) + 1$):
$$\psi^{(n,+)}(x, r) = \frac{1}{\sqrt{2L}} e^{2\pi i n x / L}, \quad r \in \{0, 1\}.$$

**Rung-antisymmetric eigenvectors on $Y_L$** ($V_-$, eigenvalue $\lambda_-^{(n), Y} = 2\cos(2\pi n/L) - 1$):
$$\psi^{(n,-), Y}(x, r) = \frac{(-1)^r}{\sqrt{2L}} e^{2\pi i n x / L}, \quad r \in \{0, 1\}.$$

**Rung-antisymmetric eigenvectors on $M_L$** ($V_-$, eigenvalue $\lambda_-^{(n), M} = 2\cos((2n+1)\pi/L) - 1$):
$$\psi^{(n,-), M}(x, r) = \frac{(-1)^r}{\sqrt{2L}} e^{i(2n+1)\pi x / L}, \quad r \in \{0, 1\}.$$

These are explicit closed-form eigenvectors that the numerics track can use for cross-validation.

---

## §7. Implications for T5 (Szegedy Walker Contrast)

### 7.1 Szegedy spectrum from adjacency spectrum

For a $d$-regular graph $G$ with adjacency $A$, the (coined-free) Szegedy walker on $G$ has spectrum
$$\mathrm{spec}(U^{\text{Sze}}_G) = \{e^{\pm i\arccos(\lambda/d)} : \lambda \in \mathrm{spec}(A)\}\ \cup\ \{\pm 1\text{-eigenvalues from edge-subspace kernel}\},$$
per Szegedy 2004 / Magniez–Nayak–Roland–Santha 2007. For our case $d = 3$ on both $Y_L$ and $M_L$.

### 7.2 Where the contrast lives

The eigenvalues $\lambda \in \mathrm{spec}_+(A) = \{2\cos(2\pi n/L) + 1\}$ are **identical** between $Y_L$ and $M_L$. Hence the rung-symmetric Szegedy modes are identical between cylinder and Möbius graphs.

The eigenvalues $\lambda \in \mathrm{spec}_-(A)$ differ:
- $Y_L$: $\{2\cos(2\pi n/L) - 1\}$ — integer crystal momentum.
- $M_L$: $\{2\cos((2n+1)\pi/L) - 1\}$ — half-odd-integer crystal momentum.

After mapping $\lambda \to e^{\pm i\arccos(\lambda/3)}$, these distinct $\lambda$ sets give distinct Szegedy eigenvalues on the unit circle. **The half-odd-integer signature of Möbius non-orientability shows up in the Szegedy walker's rung-antisymmetric sector — entirely independent of any coin or chiral structure.**

### 7.3 T5 in one paragraph (paper-ready)

Both the rung-symmetric and rung-antisymmetric sectors of the Möbius ladder $M_L$ are invariant subspaces of the adjacency operator. In the rung-symmetric sector, $M_L$ and the prism graph $Y_L$ have identical spectra (integer crystal momentum on a length-$L$ cycle, eigenvalues $2\cos(2\pi n/L) + 1$). In the rung-antisymmetric sector, the Möbius twist transforms periodic BC into anti-periodic BC on the underlying cycle, giving the half-odd-integer-momentum eigenvalues $2\cos((2n+1)\pi/L) - 1$ on $M_L$, distinct from the $2\cos(2\pi n/L) - 1$ eigenvalues on $Y_L$. The resulting half-odd-integer momentum signature in the Szegedy walker on $M_L$ depends only on the spatial non-orientability of the graph, with no contribution from coin structure or chiral symmetry. Together with T4 (winding equality), this establishes that spatial non-orientability and chiral protection are **independent ingredients** of the ℤ₂ structure observed in Floquet walks on Möbius-type geometries.

---

## §8. Validations

Snippets to add to `mobius_dtqw_simulator.ipynb` for the T-D7 proof. The N7 cell already validates the spectrum formula. These additional snippets validate the explicit $V_\pm$ decomposition and eigenvectors.

### 8.1 Verify $\tau$ commutes with $A_{M_L}$ and $A_{Y_L}$

```python
def rung_swap_matrix(L):
    """Tau: (x, r) -> (x, 1-r) in flat (2x + r) ordering."""
    n = 2 * L
    P = np.zeros((n, n), dtype=float)
    for x in range(L):
        P[2*x + 0, 2*x + 1] = 1
        P[2*x + 1, 2*x + 0] = 1
    return P

print("§8.1 — Rung-swap symmetry [tau, A] = 0")
for L in (8, 16, 30):
    P = rung_swap_matrix(L)
    for mob in (False, True):
        A = adjacency_ladder(L, mobius=mob)
        comm = P @ A - A @ P
        err = np.max(np.abs(comm))
        label = "Mobius" if mob else "prism"
        print(f"  [{'PASS' if err < 1e-12 else 'FAIL'}] L={L:>3} {label:>6}    ||[tau, A]|| = {err:.2e}")
```

### 8.2 Verify $V_+$ and $V_-$ spectra match the explicit formulas

Approach: change basis from $\{|x, r\rangle\}$ to $\{|x, +\rangle, |x, -\rangle\}$ where $|x, \pm\rangle = (|x, 0\rangle \pm |x, 1\rangle)/\sqrt 2$. Then $W^T A W$ is block-diagonal, with top-left block = $A|_{V_+}$ and bottom-right = $A|_{V_-}$.

```python
def basis_V_plus_minus(L):
    """Columns 0..L-1 span V_+; columns L..2L-1 span V_-."""
    W = np.zeros((2*L, 2*L), dtype=float)
    for x in range(L):
        W[2*x + 0, x]     =  1/np.sqrt(2)
        W[2*x + 1, x]     =  1/np.sqrt(2)
        W[2*x + 0, L + x] =  1/np.sqrt(2)
        W[2*x + 1, L + x] = -1/np.sqrt(2)
    return W

print("\n§8.2 — V_+ / V_- spectrum match formula (via block-diagonalization)")
for L in (8, 16, 30):
    W = basis_V_plus_minus(L)
    n_arr = np.arange(L)
    for mob in (False, True):
        A = adjacency_ladder(L, mobius=mob)
        A_blocks = W.T @ A @ W
        # Verify block-diagonal structure
        off_block_norm = np.linalg.norm(A_blocks[:L, L:]) + np.linalg.norm(A_blocks[L:, :L])
        # Extract V_+ block and V_- block
        eigs_plus = np.sort(np.linalg.eigvalsh(A_blocks[:L, :L]))
        eigs_minus = np.sort(np.linalg.eigvalsh(A_blocks[L:, L:]))
        expected_plus = np.sort(2 * np.cos(2 * PI * n_arr / L) + 1)
        if mob:
            expected_minus = np.sort(2 * np.cos((2 * n_arr + 1) * PI / L) - 1)
        else:
            expected_minus = np.sort(2 * np.cos(2 * PI * n_arr / L) - 1)
        err_plus = np.max(np.abs(eigs_plus - expected_plus))
        err_minus = np.max(np.abs(eigs_minus - expected_minus))
        status = "PASS" if max(err_plus, err_minus, off_block_norm) < 1e-10 else "FAIL"
        label = "Mobius" if mob else "prism"
        print(f"  [{status}] L={L:>3} {label:>6}   off-block={off_block_norm:.2e}  V+ err={err_plus:.2e}  V- err={err_minus:.2e}")
```

### 8.3 Verify the explicit eigenvectors from §6

```python
print("\n§8.3 — Explicit eigenvectors (§6) diagonalize A")
for L in (10, 20):
    n_arr = np.arange(L)
    for mob in (False, True):
        A = adjacency_ladder(L, mobius=mob)
        errs = []
        for n in n_arr:
            # V_+ eigenvector
            psi_plus = np.zeros(2 * L, dtype=complex)
            for x in range(L):
                psi_plus[2*x + 0] = np.exp(2j * PI * n * x / L) / np.sqrt(2 * L)
                psi_plus[2*x + 1] = psi_plus[2*x + 0]
            lam_plus = 2 * np.cos(2 * PI * n / L) + 1
            errs.append(np.max(np.abs(A @ psi_plus - lam_plus * psi_plus)))

            # V_- eigenvector
            psi_minus = np.zeros(2 * L, dtype=complex)
            k = (2 * n + 1) * PI / L if mob else 2 * PI * n / L
            for x in range(L):
                psi_minus[2*x + 0] = np.exp(1j * k * x) / np.sqrt(2 * L)
                psi_minus[2*x + 1] = -psi_minus[2*x + 0]
            lam_minus = 2 * np.cos(k) - 1
            errs.append(np.max(np.abs(A @ psi_minus - lam_minus * psi_minus)))
        label = "Mobius" if mob else "prism"
        max_err = max(errs)
        status = "PASS" if max_err < 1e-10 else "FAIL"
        print(f"  [{status}] L={L:>3} {label:>6}   max eigvec residual = {max_err:.2e}")
```

---

## §9. Document Status

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-16 | Initial T-D7 deliverable. Proves both adjacency spectrum formulas (Theorems 2.1, 2.2) via rung-swap symmetry decomposition $\mathcal{H} = V_+ \oplus V_-$ (§3), explicit action on each sector (§4, §5), and direct eigenvector construction (§6). Identifies the structural mechanism by which Möbius non-orientability manifests: anti-periodic boundary condition in the rung-antisymmetric sector only. Explicit eigenvector catalog provided. T5 paper paragraph (§7.3) written. Three validation snippets (§8.1–§8.3) provided. **All three executed 2026-05-16: PASS at machine precision.** §8.1 [$\tau$, A] = 0 (exact zero). §8.2 V_+ / V_- block-diagonalization confirms spectra to ~2e-15. §8.3 explicit eigenvectors from §6 diagonalize A to ~3e-15. The N7 cell in the simulator already validates the bulk spectrum formula to 5e-15 at $L = 30$. |

*End of T-D7.*
