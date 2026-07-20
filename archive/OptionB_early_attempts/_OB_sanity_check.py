# -*- coding: utf-8 -*-
"""Option B sanity check: does D = T^L (x) sigma_x act as a chiral symmetry of
U_sym on a 2L-cylinder, and does it give a topological classification distinct
from Option A?
"""

import numpy as np

PI = np.pi
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)


def shift_T(L, mobius=False):
    sign = -1.0 if mobius else +1.0
    T = np.zeros((L, L), dtype=complex)
    for x in range(L - 1):
        T[x + 1, x] = 1.0
    T[0, L - 1] = sign
    return T


def coin_rotation(theta):
    c, s = np.cos(theta / 2.0), np.sin(theta / 2.0)
    return np.array([[c, -s], [s, c]], dtype=complex)


def U_sym(L, t1, t2, mobius=False):
    T = shift_T(L, mobius=mobius)
    Ti = T.conj().T
    I = np.eye(L, dtype=complex)
    PR = np.array([[1, 0], [0, 0]], dtype=complex)
    PL = np.array([[0, 0], [0, 1]], dtype=complex)
    Sp = np.kron(T, PR) + np.kron(I, PL)
    Sm = np.kron(I, PR) + np.kron(Ti, PL)
    R_half = np.kron(I, coin_rotation(t1 / 2))
    R2 = np.kron(I, coin_rotation(t2))
    return R_half @ Sm @ R2 @ Sp @ R_half


def deck_D(L2):
    """D = T^L (x) sigma_x on a 2L-cylinder, where L = L2/2."""
    L = L2 // 2
    T = shift_T(L2, mobius=False)
    TL = np.linalg.matrix_power(T, L)
    return np.kron(TL, sx)


def Gamma_local(L2):
    return np.kron(np.eye(L2, dtype=complex), sx)


print("=" * 70)
print("  Option B sanity check")
print("=" * 70)

# ---- Check 1: D U_sym D = U_sym^(-1) on the 2L-cylinder
print("\n[1] Does D = T^L (x) sigma_x act as a chiral symmetry of U_sym?")
for L2 in (20, 50, 100):
    L = L2 // 2
    np.random.seed(0)
    t1 = np.random.uniform(0.2, PI - 0.2)
    t2 = np.random.uniform(0.2, PI - 0.2)
    U = U_sym(L2, t1, t2)  # walker on 2L-cylinder (no mobius BC)
    D = deck_D(L2)
    G = Gamma_local(L2)
    DUD = D @ U @ D
    U_inv = U.conj().T
    GUG = G @ U @ G
    err_D = np.max(np.abs(DUD - U_inv))
    err_G = np.max(np.abs(GUG - U_inv))
    err_comm = np.max(np.abs(G @ D - D @ G))
    print(f"  2L={L2}: ||D U D - U^-1|| = {err_D:.2e}   "
          f"||Gamma U Gamma - U^-1|| = {err_G:.2e}   "
          f"||[Gamma, D]|| = {err_comm:.2e}")

# ---- Check 2: T^L eigenspace decomposition; winding in each
print("\n[2] Decompose into T^L eigenspaces; check the windings in each sector.")

def winding_at_lattice(t1, t2, ks):
    c1, s1 = np.cos(t1/2), np.sin(t1/2)
    c2, s2 = np.cos(t2/2), np.sin(t2/2)
    a_y = c1 * s2 + c2 * s1 * np.cos(ks)
    a_z = -c2 * np.sin(ks)
    phi = np.arctan2(a_z, a_y)
    p = np.concatenate([phi, [phi[0]]])
    d = np.diff(p)
    d = (d + PI) % (2 * PI) - PI
    return int(round(d.sum() / (2 * PI)))


# On 2L-cylinder, T^L = +1 sector has momenta k = 2*pi*n/L (integer), and
# T^L = -1 has k = (2n+1)*pi/L (half-odd-integer). These ARE the cylinder vs
# Mobius lattices from Option A. So winding in each sector = Option A's
# cylinder winding and Mobius winding respectively.
print("\n  Verify: winding in T^L = +1 sector (cylinder modes) == winding in T^L = -1 sector (Mobius modes)?")
print("  This is exactly Option A's T-D4 theorem applied to the 2L-cylinder walker.")
print("")
print("  At sample (theta_1, theta_2) points:")
L_test = 50
for t1, t2 in [(PI/3, PI/4), (PI/4, PI/3), (PI/3, 2*PI/3), (PI/4, 5*PI/6)]:
    ks_cyl = 2 * PI * np.arange(L_test) / L_test
    ks_mob = (2 * np.arange(L_test) + 1) * PI / L_test
    nu_plus = winding_at_lattice(t1, t2, ks_cyl)
    nu_minus = winding_at_lattice(t1, t2, ks_mob)
    diff = nu_plus - nu_minus
    refinement = "TRIVIAL (no Z_2 refinement)" if diff == 0 else f"NONTRIVIAL refinement: nu_+ - nu_- = {diff}"
    print(f"    (theta_1, theta_2) = ({t1:.3f}, {t2:.3f}):  nu_+ = {nu_plus:+d}, nu_- = {nu_minus:+d}  -> {refinement}")

# ---- Check 3: Where might the windings disagree?
print("\n[3] Scan to find if ANY (theta_1, theta_2) point has nu_+ != nu_-")
print("    (would indicate a non-trivial Z_2 refinement)")
for L_test in (50, 100, 200):
    ks_cyl = 2 * PI * np.arange(L_test) / L_test
    ks_mob = (2 * np.arange(L_test) + 1) * PI / L_test
    n_diff = 0
    n_total = 0
    for t1 in np.linspace(0.05, PI - 0.05, 100):
        for t2 in np.linspace(0.05, PI - 0.05, 100):
            nu_p = winding_at_lattice(t1, t2, ks_cyl)
            nu_m = winding_at_lattice(t1, t2, ks_mob)
            if nu_p != nu_m:
                n_diff += 1
            n_total += 1
    print(f"  L={L_test:>4}: grid points where nu_+ != nu_-: {n_diff}/{n_total}  ({100*n_diff/n_total:.2f}%)")

print("\n" + "=" * 70)
print("  Conclusion:")
print("=" * 70)
print("""
  - D = T^L (x) sigma_x IS a chiral symmetry of U_sym on 2L-cylinder (Check 1).
  - But the T^L eigenspace decomposition (Check 2) maps to exactly Option A's
    cylinder vs Mobius sectors.
  - In each sector, the chiral symmetry restricts to (a sign-flipped version of)
    the local chirality Gamma. Same winding integer.
  - By Option A's T-D4 theorem, the windings in the two sectors agree everywhere
    off phase boundaries -> no Z_2 refinement.
  - The 'two-chirality' framing is REAL but the additional information content
    is null for translation-invariant walkers.

  -> The first proposed Option B construction (just put U_sym on a 2L-cylinder
    and label D as a 'new' chiral symmetry) does NOT give new physics.

  Implication: Option B needs a walker that BREAKS translation symmetry between
  the two halves of the 2L-cylinder (position-dependent parameters, alternating
  protocols, or similar). The non-symmorphic chiral DTQW where coin rotations
  at positions x and x+L differ by sigma_x conjugation (theta -> -theta) is the
  natural candidate.
""")
