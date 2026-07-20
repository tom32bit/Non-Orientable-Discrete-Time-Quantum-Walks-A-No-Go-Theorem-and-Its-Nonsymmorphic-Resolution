"""
Space-glide (nonsymmorphic chiral) discrete-time quantum walk.

Construction
------------
Lattice: sites x in Z, two-site unit cell (A = even x, B = odd x), coin C^2.
Internal cell space: (A up, A down, B up, B down), dim 4.

Glide-chiral operator:
    Gamma = T_site . (I_pos (x) sigma_x)
i.e. translate every amplitude by ONE SITE (half a unit cell) and flip the
coin. In the Bloch (periodic-gauge) picture
    Gamma(k) = t(k) (x) sigma_x,   t(k) = [[0, e^{-ik}], [1, 0]]  (A,B basis),
    Gamma(k)^2 = e^{-ik} I_4        (projective / nonsymmorphic),
with eigenvalues +/- e^{-ik/2} that EXCHANGE under k -> k + 2 pi: the
Gamma-eigenbundle over the Brillouin zone is a Moebius bundle.

Walk unitary: for ANY local, cell-periodic half-protocol F,
    U = Gamma F^dag Gamma^{-1} F
satisfies the glide-chiral symmetry
    Gamma U Gamma^{-1} = U^dag
(proof: Gamma^2 = scalar in each k sector; see theory/part2_nonsymmorphic/).

Half-protocol used here (three sub-steps, all standard DTQW primitives):
    F = Rc(beta) S Rc(alpha)
    Rc(alpha): coin rotation R(alpha_A) on A sites, R(alpha_B) on B sites
    S: spin-dependent one-site shift (up: x -> x+1, down: x -> x-1)

Everything is implemented BOTH in real space (finite even ring of 2*Nc sites)
and in momentum space (4x4 Bloch matrices); the two are cross-validated
numerically in run_experiments.py E1.
"""

import numpy as np

PI = np.pi
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
Pup = np.diag([1.0, 0.0]).astype(complex)
Pdn = np.diag([0.0, 1.0]).astype(complex)


def rot(theta):
    """Coin rotation R(theta) = exp(-i theta sigma_y / 2)."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], dtype=complex)


# ---------------------------------------------------------------------------
# Bloch (momentum-space) operators. Basis order: (A up, A down, B up, B down).
# Periodic gauge: |k, s, c> = (1/sqrt(Nc)) sum_n e^{ikn} |x = 2n+s, c>.
# ---------------------------------------------------------------------------

def t_site(k):
    """One-site translation x -> x+1 in the (A,B) cell basis."""
    return np.array([[0, np.exp(-1j * k)], [1, 0]], dtype=complex)


def gamma_bloch(k):
    """Glide-chiral operator Gamma(k) = t(k) (x) sigma_x."""
    return np.kron(t_site(k), sx)


def shift_up_bloch(k):
    """Partial shift: spin-up moves x -> x+1, spin-down stays.

    Mixed displacement parity (odd for up paths, even for down paths). This is
    essential: if every factor of F has definite odd parity (e.g. the full
    spin-dependent shift), U = Gamma F^dag Gamma^{-1} F has all-even
    displacements and conserves the sublattice grading -- the walker collapses
    to two decoupled 2-band chains (verified failure mode, see E1 log).
    """
    return np.kron(t_site(k), Pup) + np.kron(I2, Pdn)


def shift_dn_bloch(k):
    """Partial shift: spin-down moves x -> x-1, spin-up stays."""
    return np.kron(I2, Pup) + np.kron(t_site(k).conj().T, Pdn)


def coin_bloch(theta_A, theta_B):
    """Sublattice-dependent coin layer, k-independent."""
    out = np.zeros((4, 4), dtype=complex)
    out[:2, :2] = rot(theta_A)
    out[2:, 2:] = rot(theta_B)
    return out


def F_bloch(k, params):
    """Half-protocol (split-step form):
        F(k) = S_dn(k) Rc(beta) S_up(k) Rc(alpha)
    params = (aA, aB, bA, bB): alpha = (aA, aB), beta = (bA, bB).
    """
    aA, aB, bA, bB = params
    return (shift_dn_bloch(k) @ coin_bloch(bA, bB)
            @ shift_up_bloch(k) @ coin_bloch(aA, aB))


def U_bloch(k, params):
    """Full step U(k) = Gamma F^dag Gamma^{-1} F  (2 pi periodic in k)."""
    G = gamma_bloch(k)
    F = F_bloch(k, params)
    return G @ F.conj().T @ G.conj().T @ F


# ---------------------------------------------------------------------------
# Twisted (Moebius) eigenbasis of Gamma(k), smooth over the DOUBLED zone.
#
# t(k) v_pm = pm e^{-ik/2} v_pm with v_pm = (pm e^{-ik/2}, 1)/sqrt(2).
# sigma_x |pm> = pm |pm>,      |pm> = (1, pm 1)/sqrt(2).
# Gamma eigenvalue +e^{-ik/2}: u1 = v_+ (x) |+>,  u2 = v_- (x) |->
# Gamma eigenvalue -e^{-ik/2}: u3 = v_+ (x) |->,  u4 = v_- (x) |+>
# V(k + 2 pi) = V(k) . (sector swap): the transition function of the
# Moebius bundle.
# ---------------------------------------------------------------------------

def twisted_basis(k):
    e = np.exp(-1j * k / 2)
    vp = np.array([e, 1], dtype=complex) / np.sqrt(2)
    vm = np.array([-e, 1], dtype=complex) / np.sqrt(2)
    cp = np.array([1, 1], dtype=complex) / np.sqrt(2)
    cm = np.array([1, -1], dtype=complex) / np.sqrt(2)
    u1 = np.kron(vp, cp)
    u2 = np.kron(vm, cm)
    u3 = np.kron(vp, cm)
    u4 = np.kron(vm, cp)
    return np.column_stack([u1, u2, u3, u4])


def heff_bloch(k, params, gap="pi"):
    """Effective Hamiltonian H = i log U with the branch cut in the chosen gap.

    gap="pi": quasienergies taken in (-pi, pi]   (cut at eps = pi)
    gap="0" : quasienergies taken in (0, 2 pi]   (cut at eps = 0)
    """
    U = U_bloch(k, params)
    evals, evecs = np.linalg.eig(U)
    eps = -np.angle(evals)                       # U = e^{-iH}, eps in (-pi, pi]
    if gap == "0":
        eps = np.where(eps <= 0.0, eps + 2 * PI, eps)   # eps in (0, 2 pi]
    # eig of a unitary: eigenvectors orthonormal up to degeneracies; use QR to
    # be safe against non-orthogonal returns in degenerate subspaces.
    Q, _ = np.linalg.qr(evecs)
    # re-diagonalise within QR basis only if needed; for generic k spectra are
    # non-degenerate, so evecs are fine. Fall back to evecs.
    H = evecs @ np.diag(eps) @ np.linalg.inv(evecs)
    return 0.5 * (H + H.conj().T)                # hermitise (numerical noise)


def offdiag_det(k, params, gap="pi"):
    """det of the (+,-) block of H_eff in the twisted Gamma(k) eigenbasis.

    Glide-chirality forces H to be block-off-diagonal in this basis; the
    determinant d(k) = det H_{+-}(k) is the object whose behaviour over the
    doubled zone encodes the nonsymmorphic invariant.
    """
    V = twisted_basis(k)
    H = heff_bloch(k, params, gap=gap)
    W = V.conj().T @ H @ V
    diag_leak = max(np.abs(W[:2, :2]).max(), np.abs(W[2:, 2:]).max())
    return np.linalg.det(W[:2, 2:]), diag_leak


def quasienergies(k, params):
    return np.sort(-np.angle(np.linalg.eigvals(U_bloch(k, params))))


def gamma_grading(k, params):
    """For each Bloch eigenstate, the Moebius-normalised Gamma expectation
    g = <psi| Gamma |psi> * e^{+ik/2}  (real, in [-1, 1]; +/-1 = pure sector).
    Returns (eps sorted, gradings aligned)."""
    U = U_bloch(k, params)
    evals, evecs = np.linalg.eig(U)
    eps = -np.angle(evals)
    G = gamma_bloch(k)
    g = np.real(np.exp(1j * k / 2) *
                np.einsum("ij,ji->i", evecs.conj().T @ G, evecs)
                / np.einsum("ij,ji->i", evecs.conj().T, evecs))
    order = np.argsort(eps)
    return eps[order], g[order]


# ---------------------------------------------------------------------------
# Real-space operators on an even ring of 2*Nc sites (Nc unit cells).
# Basis index: 2*x + c  (site x in 0..2Nc-1, coin c in {0: up, 1: down}).
# ---------------------------------------------------------------------------

def translate_real(Nsites, step=1, twist=False):
    """One-site translation; with twist=True, hops that wrap around the ring
    seam (between site Nsites-1 and site 0) pick up a factor -1: the CANONICAL
    (scalar) Moebius deck of Part I, applied at the cell level."""
    T = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x in range(Nsites):
        xp = (x + step) % Nsites
        ph = -1.0 if (twist and x + step >= Nsites) else 1.0
        T[2 * xp, 2 * x] = ph
        T[2 * xp + 1, 2 * x + 1] = ph
    return T


def gamma_real(Nsites, twist=False):
    """Glide: translate by one site, then flip the coin."""
    T = translate_real(Nsites, 1, twist)
    flip = np.kron(np.eye(Nsites), sx)
    return flip @ T


def shift_up_real(Nsites, twist=False):
    """Partial shift: up component x -> x+1, down stays."""
    S = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x in range(Nsites):
        ph = -1.0 if (twist and x == Nsites - 1) else 1.0
        S[2 * ((x + 1) % Nsites), 2 * x] = ph
        S[2 * x + 1, 2 * x + 1] = 1.0
    return S


def shift_dn_real(Nsites, twist=False):
    """Partial shift: down component x -> x-1, up stays."""
    S = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x in range(Nsites):
        ph = -1.0 if (twist and x == 0) else 1.0
        S[2 * ((x - 1) % Nsites) + 1, 2 * x + 1] = ph
        S[2 * x, 2 * x] = 1.0
    return S


def coin_real(Nsites, theta_A, theta_B, profile=None):
    """Sublattice-dependent coin layer. Optional per-site override `profile`:
    an array of length Nsites of angles (overrides A/B pattern where not nan)."""
    blocks = []
    for x in range(Nsites):
        th = theta_A if x % 2 == 0 else theta_B
        if profile is not None and not np.isnan(profile[x]):
            th = profile[x]
        blocks.append(rot(th))
    out = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x, b in enumerate(blocks):
        out[2 * x:2 * x + 2, 2 * x:2 * x + 2] = b
    return out


def F_real(Nsites, params, profiles=(None, None), twist=False):
    aA, aB, bA, bB = params
    return (shift_dn_real(Nsites, twist) @ coin_real(Nsites, bA, bB, profiles[1])
            @ shift_up_real(Nsites, twist) @ coin_real(Nsites, aA, aB, profiles[0]))


def U_real(Nsites, params, profiles=(None, None), twist=False):
    G = gamma_real(Nsites, twist)
    F = F_real(Nsites, params, profiles, twist)
    return G @ F.conj().T @ G.conj().T @ F


def U_open(Nsites, params, termination="hard"):
    """Open chain: build the ring operators, then remove all hops that cross
    the boundary bond (between site Nsites-1 and site 0) by replacing them
    with reflective identity on the orphaned amplitude. Implemented by zeroing
    the wrap matrix elements of each shift-type factor and re-unitarising that
    factor with reflection (spin flip at the wall).
    """
    # Split-step partial shifts with reflecting walls: an amplitude that would
    # cross an end stays in place with its coin flipped (standard DTQW wall).
    Su = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    Sd = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x in range(Nsites):
        Su[2 * x + 1, 2 * x + 1] = 1.0         # down always stays under S_up
        Sd[2 * x, 2 * x] = 1.0                 # up always stays under S_dn
        if x + 1 < Nsites:
            Su[2 * (x + 1), 2 * x] = 1.0       # up moves right
        else:
            Su[2 * x + 1, 2 * x] = 1.0         # reflect up -> down at right end
            Su[2 * x + 1, 2 * x + 1] = 0.0     # (unitarity: down slot occupied)
            Su[2 * x, 2 * x + 1] = 1.0         # ...so down flips to up in place
        if x - 1 >= 0:
            Sd[2 * (x - 1) + 1, 2 * x + 1] = 1.0   # down moves left
        else:
            Sd[2 * x, 2 * x + 1] = 1.0         # reflect down -> up at left end
            Sd[2 * x, 2 * x] = 0.0
            Sd[2 * x + 1, 2 * x] = 1.0         # ...and up flips to down in place
    # Glide with a reflecting end (translation truncated, coin still flips).
    G = np.zeros((2 * Nsites, 2 * Nsites), dtype=complex)
    for x in range(Nsites):
        if x + 1 < Nsites:
            G[2 * (x + 1):2 * (x + 1) + 2, 2 * x:2 * x + 2] = sx
        else:
            G[2 * x:2 * x + 2, 2 * x:2 * x + 2] = sx   # act in place at the end
    aA, aB, bA, bB = params
    F = Sd @ coin_real(Nsites, bA, bB) @ Su @ coin_real(Nsites, aA, aB)
    return G @ F.conj().T @ G.conj().T @ F, F, G


# ---------------------------------------------------------------------------
# Invariants
# ---------------------------------------------------------------------------

def winding_of_dets(params, gap="pi", nk=401, kmax=4 * PI):
    """Winding of d(k) = det H_{+-}(k) over [0, kmax). Returns (winding,
    min |d|, max diagonal leak). Winding in units of full 2 pi turns."""
    ks = np.linspace(0, kmax, nk, endpoint=False)
    ds, leaks = [], []
    for k in ks:
        d, leak = offdiag_det(k, params, gap=gap)
        ds.append(d)
        leaks.append(leak)
    ds = np.array(ds)
    ph = np.angle(ds)
    dph = np.diff(np.concatenate([ph, ph[:1] + (0 if kmax < 4 * PI else 0)]))
    dph = (dph + PI) % (2 * PI) - PI
    return dph[:-1].sum() / (2 * PI), np.abs(ds).min(), max(leaks), ds, ks


def glide_z2(params, gap="pi", nk=257):
    """Nonsymmorphic Z2 invariant of the space-glide walker.

    Structure: d(k) = det H_{+-}(k) in the twisted basis obeys
        d(k + 2 pi) = conj(d(k))          (glide-chirality, Moebius transition)
    which, with the 2 pi periodicity of H, pins theta(0) + theta(2 pi) into
    2 pi Z and makes the total winding over the doubled zone vanish. The
    topological content is the RELATIVE half-zone winding: lift
    theta(k) = arg d(k) continuously over [0, 2 pi]; then
        theta(2 pi) = -theta(0) + 2 pi n,   n in Z,
    and a change of branch of theta(0) shifts n by 2. Hence
        zeta = n mod 2  in  {0, 1}
    is well defined -- the DTQW analogue of the Moebius-insulator Z2 index.
    Quantization requires ONLY the glide-chirality (verified numerically to
    survive coin phases that break the coins' reality); with real coins the
    additional relation d(-k) = conj(d(k)) also pins d(0), d(2 pi) real.

    gap="pi": branch cut at eps = pi -> d = 0 detects the eps = 0 gap
              (this is the gap-0 invariant zeta_0).
    gap="0" : branch cut at eps = 0 -> the gap-pi invariant zeta_pi.
    Well-defined only when BOTH quasienergy gaps are open.
    Returns (zeta, n, min |d|).
    """
    ks = np.linspace(0.0, 2 * PI, nk)
    ds = np.array([offdiag_det(k, params, gap=gap)[0] for k in ks])
    th = np.unwrap(np.angle(ds))
    # snap the endpoint pinning: theta(0), theta(2pi) in {0, pi} mod 2pi
    n = (th[-1] + th[0]) / (2 * PI)
    n_int = int(np.rint(n))
    return n_int % 2, n_int, np.abs(ds).min(), abs(n - n_int)


def bulk_gaps(params, nk=401):
    """Minimal distance of the quasienergy spectrum to eps = 0 and eps = pi."""
    ks = np.linspace(0, 2 * PI, nk, endpoint=False)
    g0, gp = PI, PI
    for k in ks:
        eps = quasienergies(k, params)
        g0 = min(g0, np.abs(eps).min())
        gp = min(gp, (PI - np.abs(eps)).min())
    return g0, gp


# ---------------------------------------------------------------------------
# Batched Bloch pipeline (vectorised over k) for parameter scans.
# ---------------------------------------------------------------------------

def bkron(A, B):
    """Batched Kronecker product; A, B broadcastable stacks of 2x2."""
    A = np.asarray(A, dtype=complex)
    B = np.asarray(B, dtype=complex)
    if A.ndim == 2:
        A = A[None]
    if B.ndim == 2:
        B = B[None]
    n = max(A.shape[0], B.shape[0])
    A = np.broadcast_to(A, (n, 2, 2))
    B = np.broadcast_to(B, (n, 2, 2))
    return np.einsum("nij,nab->niajb", A, B).reshape(n, 4, 4)


def batched_U(ks, params, phases=(0.0, 0.0)):
    """U(k) for a stack of momenta. `phases` = (phi_A, phi_B) inserts a
    sublattice-resolved coin phase layer diag(1, e^{i phi}) after the alpha
    coins, breaking the walker's reality when nonzero (used to test which
    results require the antiunitary K symmetry)."""
    aA, aB, bA, bB = params
    phA, phB = phases
    nk = len(ks)
    e = np.exp(-1j * ks)
    t = np.zeros((nk, 2, 2), dtype=complex)
    t[:, 0, 1] = e
    t[:, 1, 0] = 1.0
    tH = np.conj(np.transpose(t, (0, 2, 1)))
    G = bkron(t, sx)
    Su = bkron(t, Pup) + bkron(I2, np.broadcast_to(Pdn, (nk, 2, 2)))
    Sd = bkron(I2, np.broadcast_to(Pup, (nk, 2, 2))) + bkron(tH, Pdn)
    Rca = np.zeros((4, 4), dtype=complex)
    Rca[:2, :2] = np.diag([1, np.exp(1j * phA)]) @ rot(aA)
    Rca[2:, 2:] = np.diag([1, np.exp(1j * phB)]) @ rot(aB)
    Rcb = np.zeros((4, 4), dtype=complex)
    Rcb[:2, :2], Rcb[2:, 2:] = rot(bA), rot(bB)
    F = Sd @ Rcb[None] @ Su @ Rca[None]
    FH = np.conj(np.transpose(F, (0, 2, 1)))
    GH = np.conj(np.transpose(G, (0, 2, 1)))
    return G @ FH @ GH @ F


def batched_V(ks):
    nk = len(ks)
    e = np.exp(-1j * ks / 2)
    V = np.zeros((nk, 4, 4), dtype=complex)
    s2 = np.sqrt(2)
    vp = np.stack([e / s2, np.full_like(e, 1 / s2)], axis=1)
    vm = np.stack([-e / s2, np.full_like(e, 1 / s2)], axis=1)
    cp = np.array([1, 1]) / s2
    cm = np.array([1, -1]) / s2
    V[:, :, 0] = np.einsum("na,b->nab", vp, cp).reshape(nk, 4)
    V[:, :, 1] = np.einsum("na,b->nab", vm, cm).reshape(nk, 4)
    V[:, :, 2] = np.einsum("na,b->nab", vp, cm).reshape(nk, 4)
    V[:, :, 3] = np.einsum("na,b->nab", vm, cp).reshape(nk, 4)
    return V


def point_data(params, nk=161, phases=(0.0, 0.0)):
    """Gaps and both Z2 invariants (canonical frame) for one parameter point.
    Returns (gap0, gappi, (z0, n0, dmin0, qerr0), (zpi, npi, dminpi, qerrpi))."""
    ks = np.linspace(0.0, 2 * PI, nk)                 # endpoint INCLUDED
    U = batched_U(ks, params, phases)
    evals, evecs = np.linalg.eig(U)
    eps = -np.angle(evals)
    gap0 = np.abs(eps).min()
    gappi = (PI - np.abs(eps)).min()
    Vinv = np.linalg.inv(evecs)
    V = batched_V(ks)
    VH = np.conj(np.transpose(V, (0, 2, 1)))
    out = {}
    for gap, tag in (("pi", "0"), ("0", "pi")):       # branch -> invariant tag
        e = eps if gap == "pi" else np.where(eps <= 0, eps + 2 * PI, eps)
        H = np.einsum("nij,nj,njk->nik", evecs, e, Vinv)
        W = VH @ H @ V
        d = np.linalg.det(W[:, :2, 2:])
        th = np.unwrap(np.angle(d))
        n = (th[-1] + th[0]) / (2 * PI)
        n_int = int(np.rint(n))
        out[tag] = (n_int % 2, n_int, np.abs(d).min(), abs(n - n_int))
    return gap0, gappi, out["0"], out["pi"]
