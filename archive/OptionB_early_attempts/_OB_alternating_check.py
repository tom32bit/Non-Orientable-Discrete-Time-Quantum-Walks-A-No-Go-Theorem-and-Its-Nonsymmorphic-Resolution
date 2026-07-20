# -*- coding: utf-8 -*-
"""Option B second sanity check: does the ALTERNATING-PARAMETERS walker
on a 2L-cylinder, with theta -> -theta at the seam, give NEW physics?

The walker is NOT translation-invariant: rotations at positions {0..L-1}
use angle theta, while at positions {L..2L-1} they use -theta. By
construction, D = T^L (x) sigma_x maps theta to -theta (via sigma_x sigma_y
sigma_x = -sigma_y), so the walker IS D-invariant.
"""

import numpy as np

PI = np.pi
sx = np.array([[0, 1], [1, 0]], dtype=complex)


def shift_T(L):
    """Standard cylinder shift on length-L lattice."""
    T = np.zeros((L, L), dtype=complex)
    for x in range(L - 1):
        T[x + 1, x] = 1.0
    T[0, L - 1] = 1.0
    return T


def coin_rotation(theta):
    c, s = np.cos(theta / 2.0), np.sin(theta / 2.0)
    return np.array([[c, -s], [s, c]], dtype=complex)


def U_sym_alternating(L2, t1, t2):
    """U_sym on a 2L-cylinder with theta -> -theta at positions {L..2L-1}.

    Specifically: at position x in {0..L-1}, use rotation R(theta).
    At position x in {L..2L-1}, use rotation R(-theta) = sigma_x R(theta) sigma_x.

    The shift operators are standard cylinder shifts of length 2L.
    """
    L = L2 // 2
    T = shift_T(L2)
    Ti = T.conj().T
    I = np.eye(L2, dtype=complex)
    PR = np.array([[1, 0], [0, 0]], dtype=complex)
    PL = np.array([[0, 0], [0, 1]], dtype=complex)
    Sp = np.kron(T, PR) + np.kron(I, PL)
    Sm = np.kron(I, PR) + np.kron(Ti, PL)

    # Position-dependent coin rotation: theta at first half, -theta at second
    # Construct R_pos(theta) as a 2L*2 x 2L*2 block-diagonal where each
    # position-block is the 2x2 rotation with appropriate angle.
    def R_pos(theta):
        out = np.zeros((2 * L2, 2 * L2), dtype=complex)
        for x in range(L2):
            angle = theta if x < L else -theta
            R_block = coin_rotation(angle)
            out[2*x:2*x+2, 2*x:2*x+2] = R_block
        return out

    # But wait, the standard tensor-product ordering uses kron(pos, coin). Let me
    # re-do with that ordering: a 2L_2 x 2 state |x>|c> indexes as x*2 + c.
    # That matches the Sp, Sm definitions above. So R_pos(theta) is a block-diagonal
    # matrix in this same ordering.

    R1 = R_pos(t1 / 2)
    R2 = R_pos(t2)
    return R1 @ Sm @ R2 @ Sp @ R1


def deck_D(L2):
    L = L2 // 2
    T = shift_T(L2)
    TL = np.linalg.matrix_power(T, L)
    return np.kron(TL, sx)


print("=" * 70)
print("  Option B ALTERNATING walker check")
print("=" * 70)

# ---- Check 1: D-invariance of the alternating walker
print("\n[1] Does the alternating walker commute with D = T^L (x) sigma_x?")
for L2 in (10, 20, 50, 100):
    np.random.seed(0)
    t1 = np.random.uniform(0.2, PI - 0.2)
    t2 = np.random.uniform(0.2, PI - 0.2)
    U = U_sym_alternating(L2, t1, t2)
    D = deck_D(L2)
    err_DU = np.max(np.abs(D @ U - U @ D))     # commute = symmetry
    err_DUD = np.max(np.abs(D @ U @ D - U.conj().T))  # chiral = U^-1
    err_uni = np.max(np.abs(U.conj().T @ U - np.eye(2 * L2)))
    print(f"  2L={L2:>3}: ||[D, U]|| = {err_DU:.2e}   ||DUD - U^-1|| = {err_DUD:.2e}   ||U^dag U - I|| = {err_uni:.2e}")

# ---- Check 2: Is the alternating walker translation-invariant under T (single step)?
# Expected: NO, because parameters depend on position.
print("\n[2] Is the alternating walker translation-invariant under T (single-step shift)?")
for L2 in (10, 20):
    np.random.seed(0)
    t1 = np.random.uniform(0.2, PI - 0.2)
    t2 = np.random.uniform(0.2, PI - 0.2)
    U = U_sym_alternating(L2, t1, t2)
    T = shift_T(L2)
    Tfull = np.kron(T, np.eye(2, dtype=complex))
    err = np.max(np.abs(Tfull @ U - U @ Tfull))
    print(f"  2L={L2}: ||[T, U]|| = {err:.2e}   {'(NOT translation-invariant — as expected)' if err > 1e-10 else '(translation-invariant — unexpected)'}")

# ---- Check 3: Is the alternating walker invariant under T^L (half-shift)?
# Expected: YES, because parameters have period L.
print("\n[3] Is the alternating walker invariant under T^L (half-shift, period of the angles)?")
for L2 in (10, 20, 50):
    L = L2 // 2
    np.random.seed(0)
    t1 = np.random.uniform(0.2, PI - 0.2)
    t2 = np.random.uniform(0.2, PI - 0.2)
    U = U_sym_alternating(L2, t1, t2)
    T = shift_T(L2)
    TL = np.linalg.matrix_power(T, L)
    TLfull = np.kron(TL, np.eye(2, dtype=complex))
    err = np.max(np.abs(TLfull @ U - U @ TLfull))
    print(f"  2L={L2}: ||[T^L, U]|| = {err:.2e}")

# ---- Check 4: Compare spectrum of alternating walker vs Option A walkers
print("\n[4] Spectrum comparison:")
print("    Option A on L-cylinder vs alternating walker on 2L-cylinder")
L = 10
t1, t2 = PI/3, PI/4

# Option A walker on L-cylinder (canonical Mobius = cylinder restricted to T^L = -1)
def U_sym_optA(L, t1, t2, mobius=False):
    T = shift_T(L)
    if mobius:
        T[0, L-1] = -1.0
    Ti = T.conj().T
    I = np.eye(L, dtype=complex)
    PR = np.array([[1, 0], [0, 0]], dtype=complex)
    PL = np.array([[0, 0], [0, 1]], dtype=complex)
    Sp = np.kron(T, PR) + np.kron(I, PL)
    Sm = np.kron(I, PR) + np.kron(Ti, PL)
    R_half = np.kron(I, coin_rotation(t1 / 2))
    R2 = np.kron(I, coin_rotation(t2))
    return R_half @ Sm @ R2 @ Sp @ R_half

U_cyl_A = U_sym_optA(L, t1, t2, mobius=False)
U_mob_A = U_sym_optA(L, t1, t2, mobius=True)
U_alt_B = U_sym_alternating(2 * L, t1, t2)

eps_cyl = np.sort(np.angle(np.linalg.eigvals(U_cyl_A)))
eps_mob = np.sort(np.angle(np.linalg.eigvals(U_mob_A)))
eps_alt = np.sort(np.angle(np.linalg.eigvals(U_alt_B)))
eps_AB_combined = np.sort(np.concatenate([eps_cyl, eps_mob]))

print(f"  Option A cylinder (L={L}, 2L states): first 5 quasi-energies = {[f'{x:+.3f}' for x in eps_cyl[:5]]}")
print(f"  Option A Mobius   (L={L}, 2L states): first 5 quasi-energies = {[f'{x:+.3f}' for x in eps_mob[:5]]}")
print(f"  Option B alternating (2L={2*L}, 4L states): first 10 quasi-energies = {[f'{x:+.3f}' for x in eps_alt[:10]]}")
print(f"  Option A cyl + mob (combined, 4L states): first 10 = {[f'{x:+.3f}' for x in eps_AB_combined[:10]]}")

# Is Option B spectrum equal to direct sum of Option A cyl + Option A mob?
err = np.max(np.abs(eps_alt - eps_AB_combined))
print(f"\n  ||spec(B_alt) - spec(A_cyl) U spec(A_mob)|| = {err:.4f}")
if err > 1e-6:
    print(f"  -> Option B alternating walker has DIFFERENT spectrum from naive direct sum.")
    print(f"     This means it is genuinely new physics, not equivalent to two copies of Option A.")
else:
    print(f"  -> Option B alternating walker is just two copies of Option A. NOT NEW.")

print("\n" + "=" * 70)
