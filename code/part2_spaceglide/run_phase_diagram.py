"""
E3 -- Phase diagram of the space-glide walker.

Scans the coin-angle slice (aA, aB) in [-pi, pi]^2 at fixed (bA, bB),
computing for every point:
  - both bulk quasienergy gaps (at eps = 0 and eps = pi),
  - both nonsymmorphic Z2 invariants (zeta_0, zeta_pi),
  - the quantization error of the half-zone winding integer n.

Outputs:
  ../figures/E3_phase_diagram.png
  ../figures/E3_phase_diagram.npz          (raw data)
and prints a boundary-alignment audit: every zeta jump between neighbouring
grid points must be accompanied by a small bulk gap along the step.

A consistency assert cross-checks the batched pipeline against the reference
scalar implementation in spaceglide_walker.glide_z2 at random points.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spaceglide_walker import PI, glide_z2

# Batched pipeline lives in the library (shared with the revision scripts).
from spaceglide_walker import point_data

# ------------------------------------------------------------- consistency

rng = np.random.default_rng(3)
for _ in range(4):
    p = tuple(rng.uniform(-PI, PI, 4))
    z0_ref, n0_ref, _, _ = glide_z2(p, gap="pi")
    zp_ref, np_ref, _, _ = glide_z2(p, gap="0")
    g0, gp, (z0, n0, _, _), (zp, npi, _, _) = point_data(p)
    assert (z0, zp) == (z0_ref, zp_ref), f"batched != reference at {p}"
print("consistency: batched pipeline matches reference glide_z2  [OK]")

# ------------------------------------------------------------------- scan

BFIX = (-1.24, -1.39)
NG = 61
grid = np.linspace(-PI, PI, NG)
Z0 = np.zeros((NG, NG), dtype=int)
ZP = np.zeros((NG, NG), dtype=int)
G0 = np.zeros((NG, NG))
GP = np.zeros((NG, NG))
QE = np.zeros((NG, NG))

for i, aA in enumerate(grid):
    for j, aB in enumerate(grid):
        g0, gp, (z0, n0, dmin0, q0), (zp, npi, dminp, qp) = \
            point_data((aA, aB) + BFIX, nk=161)
        Z0[i, j], ZP[i, j] = z0, zp
        G0[i, j], GP[i, j] = g0, gp
        QE[i, j] = max(q0, qp)
    if i % 10 == 0:
        print(f"  row {i+1}/{NG}")

np.savez("../figures/E3_phase_diagram.npz", grid=grid, Z0=Z0, ZP=ZP,
         G0=G0, GP=GP, QE=QE, BFIX=np.array(BFIX))

# --------------------------------------------------------------- audits

gap_floor = np.minimum(G0, GP)
print(f"\nquantization error: max {QE.max():.2e} "
      f"(on gapped points: {QE[gap_floor > 0.05].max():.2e})")
print(f"zeta_0 classes: {np.unique(Z0).tolist()}, "
      f"zeta_pi classes: {np.unique(ZP).tolist()}")
print(f"zeta_0 == zeta_pi everywhere? {np.array_equal(Z0, ZP)}")

# boundary alignment: every neighbouring zeta jump should sit at a small gap
bad = 0
worst = 0.0
for Z, G, other in ((Z0, G0, GP), (ZP, GP, G0)):
    for ax in (0, 1):
        dz = np.diff(Z, axis=ax) != 0
        gmin = np.minimum(np.take(G, range(0, NG - 1), axis=ax),
                          np.take(G, range(1, NG), axis=ax))
        # a zeta jump can also be caused by the OTHER gap closing (branch cut
        # smoothness), so use the min over both gaps:
        omin = np.minimum(np.take(other, range(0, NG - 1), axis=ax),
                          np.take(other, range(1, NG), axis=ax))
        floor = np.minimum(gmin, omin)
        viol = dz & (floor > 0.25)
        bad += viol.sum()
        if dz.any():
            worst = max(worst, floor[dz].max())
print(f"zeta jumps across a well-gapped step (gap floor > 0.25): {bad}")
print(f"largest gap floor found on any zeta-jump step: {worst:.3f}")

# --------------------------------------------------------------- figure

fig, axes = plt.subplots(2, 2, figsize=(9.2, 8.0), constrained_layout=True)
ext = [-PI, PI, -PI, PI]

# Z2 maps: two colorblind-safe fills (light neutral / medium blue)
from matplotlib.colors import ListedColormap
z2cmap = ListedColormap(["#e8e4da", "#3d6bb3"])
for ax, Z, name in ((axes[0, 0], Z0, r"$\zeta_0$"),
                    (axes[0, 1], ZP, r"$\zeta_\pi$")):
    ax.imshow(Z.T, origin="lower", extent=ext, cmap=z2cmap, vmin=0, vmax=1,
              interpolation="nearest", aspect="auto")
    ax.set_title(f"nonsymmorphic invariant {name}")
    ax.set_xlabel(r"$\alpha_A$")
    ax.set_ylabel(r"$\alpha_B$")
    ax.text(0.03, 0.95, r"$\zeta=1$ (blue), $\zeta=0$ (grey)",
            transform=ax.transAxes, fontsize=8, va="top")

for ax, G, name in ((axes[1, 0], G0, r"gap at $\varepsilon=0$"),
                    (axes[1, 1], GP, r"gap at $\varepsilon=\pi$")):
    im = ax.imshow(G.T, origin="lower", extent=ext, cmap="viridis",
                   interpolation="bilinear", aspect="auto")
    fig.colorbar(im, ax=ax, shrink=0.85)
    ax.contour(grid, grid, G.T, levels=[0.03], colors="w", linewidths=0.7)
    ax.set_title(name)
    ax.set_xlabel(r"$\alpha_A$")
    ax.set_ylabel(r"$\alpha_B$")

fig.suptitle(
    r"Space-glide DTQW phase diagram, $(\beta_A,\beta_B)=(-1.24,-1.39)$",
    fontsize=11)
fig.savefig("../figures/E3_phase_diagram.png", dpi=180)
print("saved ../figures/E3_phase_diagram.png")
