"""
E7 -- Revision experiments for the defect section (review items 2, 4, 8).

E7a  Protection mechanism of the pi-pinned wall modes:
     - real angle disorder (wall-localised AND global) preserves the walker's
       reality => antiunitary K (particle-hole) symmetry survives => pinning;
     - complex phase disorder breaks K => modes unpin linearly in strength.
     Produces the disorder panel for the paper (deviation vs strength).

E7b  Inter-wall hybridisation: deviation of the two pi-modes from pi vs wall
     separation s on a large ring; expected delta ~ exp(-s/xi) + exp(-(N-s)/xi).
     Extracts the localisation length xi.

E7c  S_pi signal optimisation: overlap of candidate local initial states with
     the exact pi-modes (the T -> infinity value of S_pi), for the paper's
     experimental-outlook estimate.

Outputs: ../figures/E7_defect_revision.png, printed data blocks.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spaceglide_walker import (PI, gamma_real, coin_real, shift_up_real,
                               shift_dn_real, bulk_gaps)

BLUE, RUST, GREY, GOLD = "#3d6bb3", "#b3573d", "#8a8578", "#8a6d1f"

P1 = (2.094395102393195, 2.7227136331111534, -1.24, -1.39)   # zeta = 1
P0 = (2.094395102393195, 1.1519173063162569, -1.24, -1.39)   # zeta = 0


def build_wall_U(Nc, pI, pO, w=3, c1=None, c2=None, angle_dis=None,
                 phase_dis=None, rng=None):
    """Ring with two walls; optional real angle disorder (array or (mask, W))
    and complex phase disorder. Returns U and the alpha profile."""
    Ns = 2 * Nc
    c1 = Nc // 4 if c1 is None else c1
    c2 = 3 * Nc // 4 if c2 is None else c2
    prof = np.zeros(Ns)
    for x in range(Ns):
        cell = x // 2
        # distance-based smooth wall on a ring
        s = 0.5 * (np.tanh((cell - c1) / w) - np.tanh((cell - c2) / w))
        aI = pI[0] if x % 2 == 0 else pI[1]
        aO = pO[0] if x % 2 == 0 else pO[1]
        prof[x] = aO + (aI - aO) * s
    if angle_dis is not None:
        mask, W = angle_dis
        prof = prof + np.where(mask, W * rng.uniform(-1, 1, Ns), 0.0)
    G = gamma_real(Ns)
    Su, Sd = shift_up_real(Ns), shift_dn_real(Ns)
    Rb = coin_real(Ns, pI[2], pI[3])
    Ra = coin_real(Ns, 0, 0, prof)
    Phi = np.eye(2 * Ns, dtype=complex)
    if phase_dis is not None:
        mask, W = phase_dis
        ph = np.where(mask, W * rng.uniform(-1, 1, Ns), 0.0)
        for x in range(Ns):
            Phi[2 * x + 1, 2 * x + 1] = np.exp(1j * ph[x])
    F = Sd @ Rb @ Su @ Phi @ Ra
    return G @ F.conj().T @ G.conj().T @ F, prof


def pi_deviation(U):
    eps = -np.angle(np.linalg.eigvals(U))
    return np.sort(PI - np.abs(eps))[:2]


# ------------------------------------------------------------------- E7a

print("E7a -- disorder study (K-symmetry mechanism)")
Nc = 60
Ns = 2 * Nc
rng = np.random.default_rng(42)
x = np.arange(Ns)
c1s, c2s = 2 * (Nc // 4), 2 * (3 * Nc // 4)
dwall = np.minimum.reduce([np.abs(x - c1s), np.abs(x - c2s),
                           Ns - np.abs(x - c1s), Ns - np.abs(x - c2s)])
wallmask = dwall <= 6
allmask = np.ones(Ns, bool)

Ws = np.array([0.02, 0.05, 0.1, 0.15, 0.2, 0.3])
NTRIAL = 6
curves = {}
for tag, kind in (("real, wall-localised", ("angle", wallmask)),
                  ("real, global", ("angle", allmask)),
                  ("complex phase, wall-localised", ("phase", wallmask))):
    devs = []
    for W in Ws:
        worst = 0.0
        for _ in range(NTRIAL):
            kw = {}
            if kind[0] == "angle":
                kw["angle_dis"] = (kind[1], W)
            else:
                kw["phase_dis"] = (kind[1], W)
            U, _ = build_wall_U(Nc, P1, P0, rng=rng, **kw)
            worst = max(worst, pi_deviation(U).max())
        devs.append(worst)
        print(f"  {tag:30s} W={W:.2f}: max dev {worst:.2e}")
    curves[tag] = np.array(devs)

# ------------------------------------------------------------------- E7b

print("\nE7b -- inter-wall hybridisation vs separation")
NcB = 90
seps = np.array([8, 12, 16, 20, 24, 28, 32, 36, 40, 44])
devs_sep = []
for s in seps:
    U, _ = build_wall_U(NcB, P1, P0, c1=10, c2=10 + s)
    devs_sep.append(pi_deviation(U).max())
    print(f"  s={s:2d} cells: max dev {devs_sep[-1]:.3e}")
devs_sep = np.array(devs_sep)
# delta ~ A exp(-s/xi) until the smooth tanh-profile tails set a floor: at
# tail depth d from each wall the alpha profile deviates from its bulk value
# by ~exp(-2d/w), which for these geometries saturates the deviation near
# 1e-8 -- this, not second-wall hybridisation (exp(-(N-s)/xi) ~ 1e-15 here),
# explains the upturn beyond s ~ 30. Fit the clean exponential regime.
sel = seps <= 28
coef = np.polyfit(seps[sel], np.log(devs_sep[sel]), 1)
xi = -1.0 / coef[0]
print(f"  localisation length xi = {xi:.2f} cells "
      f"(fit on s <= 28; r={np.corrcoef(seps[sel], np.log(devs_sep[sel]))[0,1]:.6f})")
print("  note: the s > 30 upturn is the tanh-profile tail floor (~1e-8), "
      "not hybridisation")

# ------------------------------------------------------------------- E7c

print("\nE7c -- S_pi initial-state optimisation")
U, prof = build_wall_U(Nc, P1, P0)
evals, evecs = np.linalg.eig(U)
eps = -np.angle(evals)
modes = evecs[:, np.argsort(PI - np.abs(eps))[:2]]
# orthonormalise the two pi-modes
Q, _ = np.linalg.qr(modes)
wall_site = c1s  # site index at wall 1

def spi_limit(psi0):
    return float(np.sum(np.abs(Q.conj().T @ psi0) ** 2))

cands = {}
v = np.zeros(2 * Ns, dtype=complex); v[2 * wall_site] = 1
cands["|A up> at wall site (paper's current choice)"] = v
v = np.zeros(2 * Ns, dtype=complex)
v[2 * wall_site] = v[2 * wall_site + 1] = 1 / np.sqrt(2)
cands["equal coin superposition, one site"] = v
# best state supported on the 4 internal components of the wall cell pair
supp = [2 * wall_site, 2 * wall_site + 1, 2 * (wall_site + 1), 2 * (wall_site + 1) + 1]
M = Q[supp, :] @ Q[supp, :].conj().T
w_, v_ = np.linalg.eigh(M)
v = np.zeros(2 * Ns, dtype=complex)
v[supp] = v_[:, -1]
cands["optimal state on the wall unit cell"] = v
# best state on +-2 cells around the wall
supp = [2 * s_ + c for s_ in range(wall_site - 4, wall_site + 5) for c in (0, 1)]
M = Q[supp, :] @ Q[supp, :].conj().T
w_, v_ = np.linalg.eigh(M)
v = np.zeros(2 * Ns, dtype=complex)
v[supp] = v_[:, -1]
cands["optimal state on +-2 cells"] = v

for name, psi in cands.items():
    print(f"  {name:45s}: S_pi(inf) = {spi_limit(psi):.3f}")

# ------------------------------------------------------------------- figure

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.9), constrained_layout=True)

ax = axes[0]
styles = {"real, wall-localised": (BLUE, "o-"),
          "real, global": (GOLD, "s-"),
          "complex phase, wall-localised": (RUST, "^-")}
for tag, dev in curves.items():
    c, st = styles[tag]
    ax.loglog(Ws, dev, st, lw=1.5, ms=4.5, color=c, label=tag)
ax.set_xlabel("disorder strength $W$")
ax.set_ylabel(r"max deviation of $\pi$-modes from $\varepsilon=\pi$")
ax.legend(frameon=False, fontsize=8)
ax.set_title(r"(a) $K$-symmetry pins; breaking $K$ unpins")

ax = axes[1]
ax.semilogy(seps, devs_sep, "o", ms=5, color=BLUE, label="numerics")
ss = np.linspace(seps.min(), 30, 200)
ax.semilogy(ss, np.exp(np.polyval(coef, ss)), "-", lw=1.2, color=GREY,
            label=rf"$\propto e^{{-s/\xi}}$, $\xi = {xi:.2f}$ cells")
ax.axhspan(1e-9, 4e-8, color=GREY, alpha=0.15, lw=0)
ax.text(34, 6e-8, "wall-profile\ntail floor", fontsize=8, color=GREY)
ax.set_xlabel("wall separation $s$ (cells)")
ax.set_ylabel(r"$\pi$-mode splitting")
ax.legend(frameon=False, fontsize=8)
ax.set_title("(b) inter-wall hybridisation")

fig.suptitle("Wall-mode protection: mechanism and finite-size scaling", fontsize=11)
fig.savefig("../figures/E7_defect_revision.png", dpi=180)
print("\nsaved ../figures/E7_defect_revision.png")
