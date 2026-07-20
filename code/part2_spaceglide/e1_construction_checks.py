"""
E1 -- Construction verification for the space-glide walker.

  E1a  Unitarity (Bloch and real space), locality (banded real-space U).
  E1b  Real-space vs Bloch cross-validation (momentum-sector projection).
  E1c  Glide-chiral identity Gamma(k) U(k) Gamma(k)^{-1} = U(k)^dag, all k.
  E1d  2 pi periodicity of U(k); projectivity Gamma(k)^2 = e^{-ik} I.
  E1e  H_eff block-off-diagonal in the twisted basis (diagonal leak ~ 0).
  E1f  NO-COLLAPSE 1: no k-independent chiral operator Gamma_0 exists with
       Gamma_0 U(k) Gamma_0^{-1} = U(k)^dag  (else ordinary AIII in disguise).
  E1g  NO-COLLAPSE 2: the commutant of {U(k)} over sampled k is trivial
       (no k-independent block decomposition; the failure mode of the old
       Option B candidate constructions).
  E1h  Gamma-eigenbasis Moebius transition: V(k+2pi) = V(k) X with X the
       sector swap, and d(k+2pi) related to conj(d(k)) as derived.
"""

import sys
import numpy as np
from spaceglide_walker import (PI, U_bloch, U_real, F_real, gamma_real,
                               gamma_bloch, twisted_basis, heff_bloch,
                               offdiag_det, translate_real)

results = []


def report(name, ok, detail=""):
    results.append(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")


params = (0.9, 2.1, 0.4, 1.3)      # generic point (aA, aB, bA, bB)
Nc = 12                            # cells -> 24 sites, dim 48
Ns = 2 * Nc

print("E1a -- unitarity and locality")
U = U_real(Ns, params)
err = np.max(np.abs(U.conj().T @ U - np.eye(2 * Ns)))
report("real-space unitarity", err < 1e-12, f"err={err:.2e}")
ks = np.linspace(0, 2 * PI, 13)
err = max(np.max(np.abs(U_bloch(k, params).conj().T @ U_bloch(k, params) - np.eye(4)))
          for k in ks)
report("Bloch unitarity", err < 1e-12, f"err={err:.2e}")
# locality: U should not connect sites farther than 4 sites apart (F range 2,
# conjugated F range 2, glide 1)
maxrange = 0
for i in range(2 * Ns):
    for j in range(2 * Ns):
        if abs(U[i, j]) > 1e-12:
            dx = abs(i // 2 - j // 2)
            dx = min(dx, Ns - dx)
            maxrange = max(maxrange, dx)
report("locality (hop range <= 4 sites)", maxrange <= 4, f"range={maxrange}")

print("E1b -- real space vs Bloch")
worst = 0.0
for m in range(Nc):
    k = 2 * PI * m / Nc
    # momentum-sector basis vectors |k, s, c>
    B = np.zeros((2 * Ns, 4), dtype=complex)
    for n in range(Nc):
        ph = np.exp(1j * k * n) / np.sqrt(Nc)
        B[2 * (2 * n) + 0, 0] = ph      # A up
        B[2 * (2 * n) + 1, 1] = ph      # A down
        B[2 * (2 * n + 1) + 0, 2] = ph  # B up
        B[2 * (2 * n + 1) + 1, 3] = ph  # B down
    Uk_num = B.conj().T @ U @ B
    leak = np.linalg.norm(U @ B - B @ Uk_num)
    worst = max(worst, leak, np.max(np.abs(Uk_num - U_bloch(k, params))))
report("sector-projected U == analytic U(k)", worst < 1e-12, f"err={worst:.2e}")

print("E1c -- glide-chiral identity")
err = max(np.max(np.abs(gamma_bloch(k) @ U_bloch(k, params)
                        @ gamma_bloch(k).conj().T
                        - U_bloch(k, params).conj().T)) for k in ks)
report("Gamma U Gamma^-1 = U^dag (Bloch, all k)", err < 1e-12, f"err={err:.2e}")
G = gamma_real(Ns)
err = np.max(np.abs(G @ U @ G.conj().T - U.conj().T))
report("Gamma U Gamma^-1 = U^dag (real space)", err < 1e-12, f"err={err:.2e}")

print("E1d -- periodicity and projectivity")
err = max(np.max(np.abs(U_bloch(k + 2 * PI, params) - U_bloch(k, params)))
          for k in ks)
report("U(k+2pi) = U(k)", err < 1e-12, f"err={err:.2e}")
err = max(np.max(np.abs(gamma_bloch(k) @ gamma_bloch(k)
                        - np.exp(-1j * k) * np.eye(4))) for k in ks)
report("Gamma(k)^2 = e^{-ik} I", err < 1e-12, f"err={err:.2e}")

print("E1e -- twisted-basis block structure of H_eff")
worstleak = max(offdiag_det(k, params)[1] for k in np.linspace(0.1, 2 * PI, 23))
report("diagonal blocks of H_eff vanish", worstleak < 1e-9,
       f"leak={worstleak:.2e}")

print("E1f -- no k-independent chiral operator (no-collapse 1)")
# Solve X U(k) - U(k)^dag X = 0 for constant 4x4 X across sampled k.
rows = []
for k in np.linspace(0.05, 2 * PI, 9):
    Uk = U_bloch(k, params)
    rows.append(np.kron(np.eye(4), Uk.T) - np.kron(Uk.conj().T, np.eye(4)))
    # vec convention: vec(X U) = (U^T (x) I) vec(X); vec(U^dag X) = (I (x) U^dag) vec(X)
M = np.vstack([np.kron(U_bloch(k, params).T, np.eye(4))
               - np.kron(np.eye(4), U_bloch(k, params).conj().T)
               for k in np.linspace(0.05, 2 * PI, 9)])
nullity = 16 - np.linalg.matrix_rank(M, tol=1e-8)
report("constant-chiral solution space is empty", nullity == 0, f"dim={nullity}")

print("E1g -- trivial commutant of {U(k)} (no-collapse 2)")
M = np.vstack([np.kron(U_bloch(k, params).T, np.eye(4))
               - np.kron(np.eye(4), U_bloch(k, params))
               for k in np.linspace(0.05, 2 * PI, 9)])
nullity = 16 - np.linalg.matrix_rank(M, tol=1e-8)
report("commutant = scalars only", nullity == 1, f"dim={nullity}")

print("E1h -- Moebius transition of the twisted basis")
X = np.zeros((4, 4))
X[0, 3] = X[1, 2] = X[2, 1] = X[3, 0] = 1.0
k0 = 0.7
V1, V2 = twisted_basis(k0), twisted_basis(k0 + 2 * PI)
# find permutation/phase matrix P = V1^dag V2 and check it is the sector swap
P = V1.conj().T @ V2
offblock = np.linalg.norm(P[:2, :2]) + np.linalg.norm(P[2:, 2:])
report("V(k+2pi) = V(k) x (sector swap)", offblock < 1e-12,
       f"intra-sector residue={offblock:.2e}")
d1, _ = offdiag_det(k0, params)
d2, _ = offdiag_det(k0 + 2 * PI, params)
rel = abs(d2 - np.conj(d1)) / max(abs(d1), 1e-15)
report("d(k+2pi) == conj(d(k))", rel < 1e-9,
       f"d(k)={d1:.4f}, d(k+2pi)={d2:.4f}, rel={rel:.1e}")

print("\n" + ("E1 ALL PASS" if all(results) else ">>> E1 FAILURES <<<"))
sys.exit(0 if all(results) else 1)
