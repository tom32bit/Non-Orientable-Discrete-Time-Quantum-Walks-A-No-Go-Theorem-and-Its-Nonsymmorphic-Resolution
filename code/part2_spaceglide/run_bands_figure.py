"""
E2 -- Bulk spectra and the momentum-space Moebius structure.

Produces the paper figure showing, for one trivial (zeta = 0) and one
nontrivial (zeta = 1) parameter point:
  (a,b) quasienergy bands over the doubled zone k in [0, 4 pi]
        (2 pi periodic, gaps at 0 and pi marked);
  (c,d) the phase theta(k) = arg d(k) over the doubled zone, exhibiting the
        glide constraint theta(k + 2 pi) = -theta(k) mod 2 pi and the
        half-zone winding integer n (even = trivial, odd = nontrivial);
  (e,f) the trajectory of d(k) in the complex plane over [0, 2 pi].

Representative points are picked automatically from the E3 scan data:
the best-gapped zeta = 0 and zeta = 1 points of the scanned slice.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spaceglide_walker import PI, U_bloch, offdiag_det, glide_z2

dat = np.load("../figures/E3_phase_diagram.npz")
grid, Z0, G0, GP, BFIX = dat["grid"], dat["Z0"], dat["G0"], dat["GP"], dat["BFIX"]
floor = np.minimum(G0, GP)

points = {}
for z in (0, 1):
    m = np.where(Z0 == z, floor, -1.0)
    order = np.argsort(m.ravel())[::-1]
    for flat in order:                    # best-gapped first, skip degenerate d
        i, j = np.unravel_index(flat, m.shape)
        if m[i, j] < 0:
            break
        p = (grid[i], grid[j]) + tuple(BFIX)
        dpath = np.array([offdiag_det(k, p)[0]
                          for k in np.linspace(0.2, 2 * PI, 40)])
        if np.abs(dpath.imag).max() > 0.05:
            points[z] = p
            print(f"zeta={z} representative: (aA,aB)=({grid[i]:+.3f},"
                  f"{grid[j]:+.3f}), gaps=({G0[i,j]:.3f},{GP[i,j]:.3f})")
            break

fig, axes = plt.subplots(3, 2, figsize=(9.6, 10.2), constrained_layout=True)
BLUE, RUST = "#3d6bb3", "#b3573d"

for col, z in enumerate((0, 1)):
    p = points[z]
    zeta, n, dmin, qerr = glide_z2(p, gap="pi")
    assert zeta == z

    ks = np.linspace(0, 4 * PI, 601)
    eps = np.array([np.sort(-np.angle(np.linalg.eigvals(U_bloch(k, p))))
                    for k in ks])
    ax = axes[0, col]
    for b in range(4):
        ax.plot(ks / PI, eps[:, b] / PI, lw=1.4, color=BLUE)
    ax.axhline(0, color="0.6", lw=0.6, ls=":")
    ax.axhline(1, color="0.6", lw=0.6, ls=":")
    ax.axhline(-1, color="0.6", lw=0.6, ls=":")
    ax.axvline(2, color="0.75", lw=0.8, ls="--")
    ax.set_xlabel(r"$k/\pi$")
    ax.set_ylabel(r"$\varepsilon/\pi$")
    ax.set_title(rf"$\zeta = {z}$:  bands over the doubled zone")

    ks2 = np.linspace(0, 4 * PI, 801)
    ds = np.array([offdiag_det(k, p)[0] for k in ks2])
    th = np.unwrap(np.angle(ds))
    ax = axes[1, col]
    ax.plot(ks2 / PI, th / PI, lw=1.6, color=RUST)
    ax.axvline(2, color="0.75", lw=0.8, ls="--")
    ax.set_xlabel(r"$k/\pi$")
    ax.set_ylabel(r"$\theta(k)/\pi$")
    ax.set_title(rf"$\theta = \arg d(k)$;  half-zone integer $n = {n}$")
    ax.text(0.03, 0.9, r"$\theta(k{+}2\pi) \equiv -\theta(k)\ (\mathrm{mod}\ 2\pi)$",
            transform=ax.transAxes, fontsize=8)

    half = ks2 <= 2 * PI + 1e-9
    ax = axes[2, col]
    ax.plot(ds[half].real, ds[half].imag, lw=1.6, color=BLUE)
    ax.plot(ds[0].real, ds[0].imag, "o", ms=6, color=RUST, zorder=5)
    ax.annotate(r"$d(0)$", (ds[0].real, ds[0].imag), textcoords="offset points",
                xytext=(6, 4), fontsize=9)
    kmid = np.argmin(np.abs(ks2 - 2 * PI))
    ax.plot(ds[kmid].real, ds[kmid].imag, "s", ms=6, color=RUST, zorder=5)
    ax.annotate(r"$d(2\pi)$", (ds[kmid].real, ds[kmid].imag),
                textcoords="offset points", xytext=(6, -10), fontsize=9)
    ax.axhline(0, color="0.8", lw=0.6)
    ax.axvline(0, color="0.8", lw=0.6)
    ax.plot(0, 0, "x", ms=7, color="0.4")
    ax.set_xlabel(r"$\mathrm{Re}\, d(k)$")
    ax.set_ylabel(r"$\mathrm{Im}\, d(k)$")
    ax.set_title(rf"$d(k)$, $k \in [0, 2\pi]$   ($\min |d| = {dmin:.2f}$)")
    ax.set_aspect("equal", adjustable="datalim")

fig.suptitle("Space-glide DTQW: bulk bands and the nonsymmorphic winding data",
             fontsize=12)
fig.savefig("../figures/E2_bands_and_winding.png", dpi=180)
print("saved ../figures/E2_bands_and_winding.png")
print("points used:", points)
