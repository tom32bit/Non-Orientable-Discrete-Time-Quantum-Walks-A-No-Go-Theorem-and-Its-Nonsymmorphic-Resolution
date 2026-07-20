"""
E4 -- Domain walls: bulk-defect correspondence for the glide Z2.
E5 -- Bridge to Part I: the canonical (scalar) Moebius twist on the glide
      walker is still just a momentum shift -- the no-go persists -- while the
      nonsymmorphic Z2 lives entirely in the glide structure.
E6 -- Dynamical signature: a walker launched at a topological wall stays.

E4 protocol: ring of Nc cells, coin-angle profile with two domains
  domain 1: alpha angles of the zeta = 1 representative,
  domain 0: alpha angles of the zeta = 0 representative,
(beta angles common), smooth walls of width w cells. Diagonalise U, find
in-gap states, measure their localisation at the two walls. Control: both
domains zeta = 0 (two distinct trivial parameter sets).

E5 protocol: even ring, canonical twist (-1 on seam-crossing hops). The
spectrum must equal the analytic Bloch spectrum at half-odd-integer cell
momenta k_m = (2m+1) pi / Nc -- Part I's T1 carried verbatim to the 4-band
walker -- and the glide-chiral identity must still hold (scalar deck commutes
with everything).

E6 protocol: launch |cell at wall, A up> in the E4 ring; track the staying
probability P_stay(t) = sum of |psi|^2 within +/-4 cells of the wall, for the
topological wall vs the control wall.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from spaceglide_walker import (PI, U_real, U_bloch, gamma_real, coin_real,
                               shift_up_real, shift_dn_real, glide_z2)

BLUE, RUST, GREY = "#3d6bb3", "#b3573d", "#8a8578"

P1 = (2.094395102393195, 2.7227136331111534, -1.24, -1.39)   # zeta = 1
P0 = (2.094395102393195, 1.1519173063162569, -1.24, -1.39)   # zeta = 0
P0b = (0.9, 2.1, -1.24, -1.39)                               # zeta = 0 (generic alt)

for tag, p in (("P1", P1), ("P0", P0), ("P0b", P0b)):
    z, n, dmin, q = glide_z2(p)
    print(f"{tag}: zeta={z} (n={n}, min|d|={dmin:.2f})")

# --------------------------------------------------------------- E4

def wall_profile(Nc, pL, pR, w=3):
    """Per-site alpha-angle profile: left half domain pL, right half pR,
    tanh walls of width w cells centred at cell Nc/4 and 3 Nc/4."""
    Ns = 2 * Nc
    prof = np.zeros(Ns)
    c1, c2 = Nc // 4, 3 * Nc // 4
    for x in range(Ns):
        cell = x // 2
        # smooth interpolation parameter: 1 inside [c1, c2), 0 outside
        s = 0.5 * (np.tanh((cell - c1) / w) - np.tanh((cell - c2) / w))
        aL = pL[0] if x % 2 == 0 else pL[1]
        aR = pR[0] if x % 2 == 0 else pR[1]
        prof[x] = aR + (aL - aR) * s      # s=1 -> pL (inner), s=0 -> pR (outer)
    return prof


def wall_spectrum(Nc, pInner, pOuter, w=3):
    Ns = 2 * Nc
    prof = wall_profile(Nc, pInner, pOuter, w)
    params = (0.0, 0.0, pInner[2], pInner[3])       # alpha via profile
    U = U_real(Ns, params, profiles=(prof, None))
    evals, evecs = np.linalg.eig(U)
    eps = -np.angle(evals)
    # localisation diagnostics
    prob = np.abs(evecs) ** 2
    cellprob = prob.reshape(Ns, 2, -1).sum(axis=1)      # (site, state)
    x = np.arange(Ns)
    ipr = (cellprob ** 2).sum(axis=0)
    c1, c2 = 2 * (Nc // 4), 2 * (3 * Nc // 4)
    def wallweight(centre):
        d = np.minimum(np.abs(x - centre), Ns - np.abs(x - centre))
        return cellprob[d <= 8].sum(axis=0)
    return eps, ipr, wallweight(c1) + wallweight(c2), U, prof


Nc = 60
print("\nE4 -- domain-wall spectra")
eps_t, ipr_t, ww_t, U_t, prof_t = wall_spectrum(Nc, P1, P0)
eps_c, ipr_c, ww_c, U_c, prof_c = wall_spectrum(Nc, P0b, P0)

# bulk gaps of the two domains (the in-gap window is their intersection)
from spaceglide_walker import bulk_gaps
g0_1, gp_1 = bulk_gaps(P1)
g0_0, gp_0 = bulk_gaps(P0)
g0_0b, gp_0b = bulk_gaps(P0b)
g0_min_t, gp_min_t = min(g0_1, g0_0), min(gp_1, gp_0)
g0_min_c, gp_min_c = min(g0_0b, g0_0), min(gp_0b, gp_0)

def ingap_states(eps, ww, g0, gp, margin=0.55):
    """States deep inside a bulk gap AND localised at the walls (weight > 0.5)."""
    sel0 = (np.abs(eps) < margin * g0) & (ww > 0.5)
    selp = (PI - np.abs(eps) < margin * gp) & (ww > 0.5)
    return np.where(sel0)[0], np.where(selp)[0]

t0, tp = ingap_states(eps_t, ww_t, g0_min_t, gp_min_t)
c0, cp = ingap_states(eps_c, ww_c, g0_min_c, gp_min_c)
print(f"topological walls (dzeta=1): {len(t0)} wall-localised states in gap 0 "
      f"(eps = {np.sort(eps_t[t0]).round(3)}), {len(tp)} in gap pi "
      f"(pi-|eps| = {np.sort(PI-np.abs(eps_t[tp])).round(3)})")
print(f"control walls   (dzeta=0): {len(c0)} in gap 0, {len(cp)} in gap pi")

# --------------------------------------------------------------- E5

print("\nE5 -- canonical cell twist on the glide walker (Part I bridge)")
NcB = 24
Ns = 2 * NcB
for twist in (False, True):
    U = U_real(Ns, P1, twist=twist)
    G = gamma_real(Ns, twist=twist)
    uerr = np.max(np.abs(U.conj().T @ U - np.eye(2 * Ns)))
    cerr = np.max(np.abs(G @ U @ G.conj().T - U.conj().T))
    ev = np.sort(np.angle(np.linalg.eigvals(U)))
    ms = np.arange(NcB)
    kms = (2 * ms + 1) * PI / NcB if twist else 2 * PI * ms / NcB
    bl = np.sort(np.angle(np.concatenate(
        [np.linalg.eigvals(U_bloch(k, P1)) for k in kms])))
    serr = np.max(np.abs(ev - bl))
    lat = "half-odd-integer" if twist else "integer"
    print(f"  twist={twist}: unitarity {uerr:.1e}, glide-chiral {cerr:.1e}, "
          f"spectrum == Bloch at {lat} momenta to {serr:.1e}")

# --------------------------------------------------------------- E6

print("\nE6 -- dynamics: staggered return amplitude (pi-mode detector)")
def staggered_return(U, Nc, centre_cell, T=20000):
    """S_pi(T) = |(1/T) sum_t (-1)^t <psi0|psi(t)>| -> total weight of psi0 on
    quasienergy-EXACTLY-pi modes; decays ~1/(T*delta) for modes split by delta."""
    Ns = 2 * Nc
    psi0 = np.zeros(2 * Ns, dtype=complex)
    psi0[2 * (2 * centre_cell)] = 1.0               # |A up> at the wall cell
    psi = psi0.copy()
    acc = 0.0 + 0.0j
    trace = []
    sign = 1.0
    for t in range(1, T + 1):
        psi = U @ psi
        sign = -sign
        acc += sign * np.vdot(psi0, psi)
        if t % 100 == 0:
            trace.append((t, abs(acc) / t))
    return np.array(trace)

tr_t = staggered_return(U_t, Nc, Nc // 4)
tr_c = staggered_return(U_c, Nc, Nc // 4)
print(f"S_pi(T=20000): topological wall {tr_t[-1,1]:.4f}, "
      f"control wall {tr_c[-1,1]:.4f}")

# --------------------------------------------------------------- figure

fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.6), constrained_layout=True)

for ax, eps, ww, g0m, gpm, name in (
        (axes[0, 0], eps_t, ww_t, g0_min_t, gp_min_t,
         r"$\Delta\zeta = 1$ walls"),
        (axes[0, 1], eps_c, ww_c, g0_min_c, gp_min_c,
         r"$\Delta\zeta = 0$ walls (control)")):
    order = np.argsort(eps)
    sc = ax.scatter(np.arange(len(eps)), eps[order], c=ww[order], s=7,
                    cmap="viridis", vmin=0, vmax=1)
    for g, sgn in ((g0m, 1), (g0m, -1)):
        ax.axhline(sgn * g, color=GREY, lw=0.6, ls=":")
    ax.axhline(PI - gpm, color=GREY, lw=0.6, ls="--")
    ax.axhline(-(PI - gpm), color=GREY, lw=0.6, ls="--")
    ax.set_xlabel("state index (sorted)")
    ax.set_ylabel(r"$\varepsilon$")
    ax.set_title(name)
fig.colorbar(sc, ax=axes[0, :], shrink=0.8, label="weight within 4 cells of walls")

ax = axes[1, 0]
Ns = 2 * Nc
evals_t, evecs_t = np.linalg.eig(U_t)
eps_full = -np.angle(evals_t)
sel = np.argsort(PI - np.abs(eps_full))[:2]        # the two pi-pinned modes
x = np.arange(Ns) / 2.0
for idx, s in enumerate(sel):
    cellprob = (np.abs(evecs_t[:, s]) ** 2).reshape(Ns, 2).sum(axis=1)
    ax.plot(x, cellprob + idx * 0.30, lw=1.4,
            color=BLUE if idx == 0 else RUST,
            label=rf"$\pi - |\varepsilon| = {PI - abs(eps_full[s]):.1e}$")
ax.axvline(Nc // 4, color=GREY, lw=0.8, ls="--")
ax.axvline(3 * Nc // 4, color=GREY, lw=0.8, ls="--")
ax.set_xlabel("cell")
ax.set_ylabel(r"$|\psi|^2$ (offset)")
ax.legend(frameon=False, fontsize=8)
ax.set_title(r"the two $\pi$-pinned wall modes, $\Delta\zeta = 1$ ring")

ax = axes[1, 1]
ax.loglog(tr_t[:, 0], tr_t[:, 1], lw=1.6, color=BLUE,
          label=r"$\Delta\zeta = 1$ wall")
ax.loglog(tr_c[:, 0], tr_c[:, 1], lw=1.6, color=RUST,
          label=r"$\Delta\zeta = 0$ wall")
ax.set_xlabel("step $T$")
ax.set_ylabel(r"$S_\pi(T)$")
ax.legend(frameon=False, fontsize=9)
ax.set_title(r"staggered return amplitude ($\pi$-mode weight)")

fig.suptitle("Domain walls of the glide Z2: spectra, states, dynamics", fontsize=12)
fig.savefig("../figures/E4_E6_walls.png", dpi=180)
print("saved ../figures/E4_E6_walls.png")
