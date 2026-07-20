"""
E8 -- Revision experiments for the bulk section (review items 5, 10).

E8a  Reality-broken family scan: insert sublattice coin phases (phi_A, phi_B)
     that break the antiunitary K symmetry, and scan random parameter points:
     (i) does zeta stay quantized (glide-only protection -- expected yes)?
     (ii) does the empirical identity zeta_0 = zeta_pi survive, or do the two
     gap invariants decouple once K is broken?

E8b  Second beta-slice audit: repeat the E3 phase-diagram boundary-alignment
     audit on an independent slice (beta_A, beta_B) = (0.4, 1.3), 41x41 grid,
     to address the genericity concern.
"""

import numpy as np
from spaceglide_walker import PI, point_data

# ------------------------------------------------------------------- E8a

print("E8a -- reality-broken family: quantization and zeta_0 vs zeta_pi")
rng = np.random.default_rng(2026)
classes = {}
qmax_gapped = 0.0
split_found = []
NPTS = 60
for _ in range(NPTS):
    p = tuple(rng.uniform(-PI, PI, 4))
    ph = tuple(rng.uniform(-PI, PI, 2))
    g0, gp, (z0, n0, dmin0, q0), (zp, npi, dminp, qp) = point_data(
        p, nk=257, phases=ph)
    gapped = g0 > 0.05 and gp > 0.05
    if gapped:
        qmax_gapped = max(qmax_gapped, q0, qp)
        classes[(z0, zp)] = classes.get((z0, zp), 0) + 1
        if z0 != zp:
            split_found.append((p, ph, (g0, gp)))
print(f"  gapped points: {sum(classes.values())}/{NPTS}")
print(f"  max quantization error on gapped points: {qmax_gapped:.2e}")
print(f"  (zeta_0, zeta_pi) class counts: {classes}")
if split_found:
    print("  *** zeta_0 != zeta_pi FOUND (K-breaking decouples the gaps): ***")
    for p, ph, g in split_found[:5]:
        print(f"    params={np.round(p,3)}, phases={np.round(ph,3)}, gaps={np.round(g,3)}")
else:
    print("  zeta_0 == zeta_pi at every gapped point even with K broken.")

# ------------------------------------------------------------------- E8b

print("\nE8b -- second beta-slice audit: (bA, bB) = (0.4, 1.3), 41x41")
BFIX = (0.4, 1.3)
NG = 41
grid = np.linspace(-PI, PI, NG)
Z0 = np.zeros((NG, NG), dtype=int)
ZP = np.zeros((NG, NG), dtype=int)
G0 = np.zeros((NG, NG))
GP = np.zeros((NG, NG))
QE = np.zeros((NG, NG))
for i, aA in enumerate(grid):
    for j, aB in enumerate(grid):
        g0, gp, (z0, n0, _, q0), (zp, npi, _, qp) = \
            point_data((aA, aB) + BFIX, nk=161)
        Z0[i, j], ZP[i, j] = z0, zp
        G0[i, j], GP[i, j] = g0, gp
        QE[i, j] = max(q0, qp)

gap_floor = np.minimum(G0, GP)
print(f"  quantization error on gapped points: "
      f"{QE[gap_floor > 0.05].max():.2e}")
print(f"  zeta_0 classes: {np.unique(Z0).tolist()}; both present? "
      f"{set(np.unique(Z0).tolist()) == {0, 1}}")
print(f"  zeta_0 == zeta_pi everywhere? {np.array_equal(Z0, ZP)}")
bad = 0
worst = 0.0
for Z, G, other in ((Z0, G0, GP), (ZP, GP, G0)):
    for ax in (0, 1):
        dz = np.diff(Z, axis=ax) != 0
        gmin = np.minimum(np.take(G, range(0, NG - 1), axis=ax),
                          np.take(G, range(1, NG), axis=ax))
        omin = np.minimum(np.take(other, range(0, NG - 1), axis=ax),
                          np.take(other, range(1, NG), axis=ax))
        floor = np.minimum(gmin, omin)
        bad += (dz & (floor > 0.25)).sum()
        if dz.any():
            worst = max(worst, floor[dz].max())
print(f"  zeta jumps across well-gapped steps (floor > 0.25): {bad}")
print(f"  largest gap floor on any zeta-jump step: {worst:.3f}")
np.savez("../figures/E8_second_slice.npz", grid=grid, Z0=Z0, ZP=ZP,
         G0=G0, GP=GP, QE=QE, BFIX=np.array(BFIX))
print("  saved ../figures/E8_second_slice.npz")
