# Option B Research Project Specification

**Project:** Intrinsic M\"obius Quantum Walker — A Research Roadmap
**Authors:** S. M. Yousuf Iqbal Tomal, Abdullah Al Shafin
**Status:** **Open research problem.** No walker construction yet committed. Multiple candidates have failed sanity checks; spec below records the failures honestly and lists the remaining candidates that warrant investigation.
**Date:** 2026-05-16
**Predecessor:** `Option_A_chiral_DTQW_mobius/` — submitted as a characterization paper with clean negative-result theorem.

---

## 0. Premise and Goal

### 0.1 What we're trying to find

A discrete-time quantum walker on a 1-D position lattice, with a non-canonical deck operator $\Sigma$ acting on the coin Hilbert space, such that:

1. The deck $D$ acts non-trivially on coin (e.g., $\sigma_x$ rather than $\pm \mathbb{I}$).
2. The walker is $D$-invariant in some useful sense (a unitary symmetry, a chiral symmetry, or a symmetry-protecting operator).
3. The resulting walker is **NOT equivalent** to Option A's canonical Möbius walker via restriction or quotient.
4. The walker admits a richer topological classification than Option A's single chiral integer winding.

The hope is to find genuine non-orientable Floquet topology that Option A ruled out for $\Sigma = -\mathbb{I}$.

### 0.2 Why this is hard

Option A established a sharp structural fact: for the standard split-step DTQW, the only deck operator commuting with all walker factors is $\Sigma \propto \mathbb{I}_d$. Any non-canonical deck must therefore EITHER (i) commute with the walker only partially (giving non-symmetry behavior) OR (ii) require a redesigned walker.

Both routes have failure modes. The next several sections record specific failures observed during Option B kickoff (2026-05-16), to ensure we don't repeat them.

---

## 1. Failed Candidates (documented honestly)

### 1.1 Candidate Failure 1: Cylinder walker on $2L$-lattice with $D = T^L \otimes \sigma_x$ as a "new" symmetry

**Construction.** Use the standard symmetric-frame Kitagawa walker $U_{\rm sym}$ on a $2L$-cylinder (Option A's walker, on a doubled lattice). Claim that $D = T^L \otimes \sigma_x$ acts as an additional chiral symmetry (alongside $\Gamma = \sigma_x$), giving a $\mathbb{Z}_2 \times \mathbb{Z}_2$ symmetry group and potentially a richer classification.

**Verification, sanity check `_OB_sanity_check.py`:**

- $D U_{\rm sym} D = U_{\rm sym}^{-1}$ holds to exact zero. ✓ (Both $\Gamma$ and $D$ are chiral symmetries.)
- $[\Gamma, D] = 0$ exactly. ✓
- $T^L$-eigenspace decomposition: $T^L = +1$ sector = Option A cylinder walker; $T^L = -1$ sector = Option A canonical Möbius walker.
- In each sector, $D$ acts as $\pm\Gamma$. Same chiral structure as Option A locally.
- Winding scan at $L = 50, 100, 200$ on $100 \times 100$ grid: $\nu_+ = \nu_-$ at **every single point**, $0/10000$ disagreements.

**Conclusion:** The construction is mathematically valid (both chiral symmetries hold), but it does NOT give new physics. The walker decomposes as Option A cylinder $\oplus$ Option A Möbius, and by Option A's T-D4 winding-equality theorem, the two have identical topology. The "$\mathbb{Z}_2 \times \mathbb{Z}_2$ refinement" is null in the thermodynamic limit.

**Implication:** Translation-invariant walkers on a doubled lattice cannot give richer M\"obius topology than the canonical Option A walker.

### 1.2 Candidate Failure 2: Alternating-parameter walker with anti-periodic angle profile

**Construction.** On a $2L$-cylinder, use position-dependent coin rotations: $R(\theta)$ at positions $\{0, \dots, L-1\}$ and $R(-\theta)$ at positions $\{L, \dots, 2L-1\}$. The naïve expectation: since $\sigma_x R(\theta) \sigma_x = R(-\theta)$, the deck $D = T^L \otimes \sigma_x$ should map the walker to itself ($D$-invariant).

**Verification, sanity check `_OB_alternating_check.py`:**

- $[D, U_{\rm alt}] \neq 0$: numerical norm $\approx 1.76$, i.e., $D$ does NOT commute with $U_{\rm alt}$ (not a unitary symmetry).
- $D U_{\rm alt} D \neq U_{\rm alt}^{-1}$: numerical norm $\approx 1.76$ (not a chiral symmetry).
- $[T, U_{\rm alt}] \neq 0$ (NOT translation-invariant under single-step shift — as expected).
- $[T^L, U_{\rm alt}] \neq 0$ — also NOT invariant under the half-shift, contrary to naïve expectation.
- Spectrum: NOT equal to direct sum of Option A cylinder + Option A Möbius spectra (max difference $\approx 0.96$, large).

**Conclusion:** The alternating walker has genuinely different spectrum from any direct-sum of Option A walkers, but **$D$ is neither a unitary nor a chiral symmetry of it**. So this walker is not an "intrinsic Möbius walker" in any natural sense — it's just a position-dependent walker that happens to have angle-flipping at the boundary.

**Implication:** Position-dependent angle profiles don't directly give $D$-invariant walkers, because the shifts $S_+, S_-$ don't transform appropriately under $D$. Designing a $D$-invariant walker requires more care than just flipping angles.

### 1.3 Lessons learned

1. **Translation-invariance + canonical chiral symmetry $\Rightarrow$ no new physics** beyond Option A. Translation-invariant walkers on the doubled lattice always decompose into two sectors that are equivalent to Option A.

2. **Position-dependent walkers** can break translation invariance but require careful design to maintain a meaningful $D$ symmetry. Naïve angle-flipping does NOT preserve $D$ as a symmetry of the full walker.

3. **The "non-symmorphic chiral DTQW" framing is correct in spirit but the explicit construction is non-trivial.** Standard shift operators do not transform compatibly with deck operators acting on coin space.

---

## 2. Remaining Candidates (not yet investigated)

### 2.1 Candidate A: Glide-symmetric walker with redesigned shift

**Idea.** Replace the standard split-step shifts $S_\pm$ with new shifts $\tilde S_\pm$ that commute with $D = T^L \otimes \sigma_x$. The walker on a $2L$-cylinder, built from $\tilde S_\pm$ and standard coin rotations, would then have $D$ as a genuine unitary symmetry.

**Requirement for $D$ commutation:** $D \tilde S D^{-1} = \tilde S$. With $D$ shifting position by $L$ and flipping coin by $\sigma_x$, this constraints $\tilde S$ to be invariant under "translate by $L$ and flip coin by $\sigma_x$."

**Concrete proposal:** $\tilde S_+ = T \otimes |+_x\rangle\langle +_x| + T \otimes |-_x\rangle\langle -_x|$? No, that's just $T \otimes I$, the boring uniform shift.

What about $\tilde S = T \otimes |+_x\rangle\langle +_x| + T^{-1} \otimes |-_x\rangle\langle -_x|$? This shifts $|+_x\rangle$-coin states right and $|-_x\rangle$-coin states left. In the $\sigma_z$-basis: $|+_x\rangle = (|R\rangle + |L\rangle)/\sqrt{2}$, $|-_x\rangle = (|R\rangle - |L\rangle)/\sqrt{2}$. So $|+_x\rangle\langle +_x| = (I + \sigma_x)/2$, $|-_x\rangle\langle -_x| = (I - \sigma_x)/2$. Thus $\tilde S$ has coin part $(I + \sigma_x)/2 \cdot T + (I - \sigma_x)/2 \cdot T^{-1} = (T + T^{-1})/2 \otimes I + (T - T^{-1})/2 \otimes \sigma_x$. This DOES commute with $\sigma_x$ on coin, since the $\sigma_x$ term commutes with itself. So $D \tilde S D = T^L \otimes \sigma_x \cdot \tilde S \cdot T^L \otimes \sigma_x = \tilde S$ (using $T^L$ commutes with $T$, and the coin part of $\tilde S$ commutes with $\sigma_x$). ✓

**Now: does this walker still have an integer winding under chiral symmetry?** With $\tilde S$ diagonal in $\sigma_x$-eigenbasis, the walker on $2L$-cylinder built from $\tilde S$ and $R(\theta) = e^{-i\theta\sigma_y/2}$ is... let me think. Actually $R(\theta)$ doesn't commute with $\sigma_x$ (since $\sigma_y$ doesn't commute with $\sigma_x$). So the walker mixes $|+_x\rangle$ and $|-_x\rangle$ sectors. Combined with the $\tilde S$ that's diagonal in $\sigma_x$-basis, this gives a genuine 2-band system.

This walker is essentially the **chiral DTQW with a sublattice $\sigma_x$-grading** instead of the usual $\sigma_z$-grading. It's NOT the same as Option A — the shift operates on different coin eigenstates.

**Status:** Worth pursuing. Need to:
1. Verify the walker is unitary.
2. Identify what chiral symmetry it has (likely $\Gamma = \sigma_z$ instead of $\sigma_x$, by analogy).
3. Compute the bulk dispersion and topological invariants.
4. Decompose under $D = T^L \otimes \sigma_x$ to find the joint $(\Gamma, D)$ classification.

### 2.2 Candidate B: Doubled-coin walker with "side" and "spin" labels

**Idea.** Hilbert space $\mathbb{C}^L \otimes \mathbb{C}^2_{\rm side} \otimes \mathbb{C}^2_{\rm spin}$ (dimension $4L$). The "side" coordinate tracks which sheet of the M\"obius double cover. The shift moves the walker around the cycle and flips the side at the seam:

$S_+^{\rm doubled} |x, r, c\rangle = \begin{cases} |x+1, r, c\rangle & x < L-1 \\ |0, 1-r, c\rangle & x = L-1 \end{cases}$

(R-coin shifts right, with the side flipping at the seam; L-coin similar but moving left.)

**Status:** Worth pursuing. Need to:
1. Verify unitarity (4 distinct sources to 4 distinct targets — should work since the side-flip resolves the collisions that plagued Option A's intrinsic attempts).
2. Define the deck operator: probably $D = I \otimes \sigma_x^{\rm side} \otimes I^{\rm spin}$ (side-flip without position translation, since the side already encodes the M\"obius identification).
3. Topological classification: this is a $4$-dim coin walker, the framework of Cedzich et al. and Roy-Harper extends but the details are non-trivial.

### 2.3 Candidate C: Two-step walker with anti-periodic Floquet drive

**Idea.** $U = U_2 U_1$ where $U_1$ uses parameters $(\theta_1, \theta_2)$ at all positions, $U_2$ uses parameters $(-\theta_1, -\theta_2) = \sigma_x (\theta_1, \theta_2) \sigma_x$ at all positions. The half-period sign flip is the Floquet analogue of the M\"obius anti-periodic structure.

This isn't a "spatial" Möbius walker — it's a TEMPORAL Möbius/Floquet structure. The classification falls under "anomalous Floquet" topology (Rudner-Lindner-Berg-Levin 2013).

**Status:** Worth pursuing as a different framing. May be EQUIVALENT to existing anomalous Floquet phase results — would need careful comparison.

### 2.4 Candidate D: Brillouin-zone-twisted walker

**Idea.** Identify the M\"obius twist not at the position-space level but at the Brillouin-zone level: replace the standard $k$-integration domain $[0, 2\pi)$ with a "twisted" domain where the band structure is identified anti-periodically at $k = 0$ and $k = 2\pi$.

**Status:** Unclear whether this gives anything beyond a basis change. Low priority.

---

## 3. Recommended Research Plan

### Phase A: Literature pre-emption (mandatory first step)

Search the literature for any of the following, in roughly the priority listed:

1. **"Glide-symmetric DTQW"** or "non-symmorphic Floquet topological phase" — covers Candidates A and similar.
2. **"Multi-coin DTQW"** or "walker on a doubled lattice with sub-coin symmetry" — covers Candidate B.
3. **"Anti-periodic Floquet drive"** with explicit M\"obius interpretation — covers Candidate C.
4. **"Möbius-symmetric quantum walk"** — covers anything we might have missed.

Search engines: Google Scholar, arXiv, ADS, Semantic Scholar. Forward-cite Kitagawa 2010, Cedzich et al., Roy-Harper 2017, Asbóth-Edge.

**Hard-stop conditions:**
- A paper covering Candidate A construction in essentially the form described: project pivots to Candidate B or C.
- A paper covering Candidate B in detail: project pivots to a different setting (e.g., higher-dimensional spatial topology).
- All four candidates pre-empted: project does not have a clear Option B target; consider closing out the M\"obius DTQW research line.

### Phase B: Construction commitment (after literature check)

Pick ONE candidate (A, B, C, or D) based on:
- Literature originality (lowest pre-emption risk).
- Tractability (Candidate A and C are likely simplest).
- Likely yield of new physics (Candidate A has the most concrete framing; Candidate B is more ambitious).

Default recommendation if literature check is clean: **Candidate A** (glide-symmetric walker with $\sigma_x$-grading shifts). The construction is concrete, the symmetry analysis is tractable, and the analogy with non-symmorphic crystalline topology gives a clear theoretical reference framework.

### Phase C: Walker definition and validation

For the committed candidate:
1. Write explicit operator forms (analogue of Option A's T-D1).
2. Verify unitarity and the desired symmetries numerically.
3. Compute Bloch decomposition.
4. Identify topological invariants under the joint symmetry group.

### Phase D: Topological characterization

Compute the topological classification carefully. The key question is whether the candidate yields a classification richer than $\mathbb{Z}$ (Option A's result).

### Phase E: Numerical experiments

Reproduce the experiment suite analogous to Option A's N0-N7 for the new walker. Compare topological invariants, spectral signatures, edge modes, and dynamics with Option A's results.

### Phase F: Writeup

If Phases A-E yield a clean result (positive or negative), write up as Option B's paper.

---

## 4. Risk Register

### R1: All candidates may pre-empt or fail

The chiral DTQW topology landscape has been thoroughly studied since 2010. There is a real chance that all four candidates have been considered and either ruled out or found to reduce to known cases. The literature pre-emption check is mandatory and may close out Option B entirely.

### R2: The right walker may exist but be hard to construct

Designing a walker that simultaneously (a) has rich coin dynamics, (b) is invariant under $D = T^L \otimes \sigma_x$, and (c) is not equivalent to a known model is the central technical challenge. The first two attempts failed; further attempts may also fail.

### R3: The classification result may be the same as Option A

Even with a properly-constructed Option B walker, the topological invariants may reduce to Option A's $\mathbb{Z}$ classification (with no $\mathbb{Z}_2$ refinement). The result would be a more nuanced negative finding rather than a discovery.

### R4: Project may exceed scope

Option B requires walker design, symmetry analysis, topological classification, AND numerics — all of which are open. The project could reasonably take 6-12 months. Plan accordingly.

### R5: Tony Stark fandom alone is not a research direction

The M\"obius framing was inspired by *Avengers: Endgame*. Option B is at risk of being pursued because the framing is "cool," not because the underlying physics is rich. Honest assessment at each phase is essential.

---

## 5. Decision Points

### DP1: After literature check (Phase A)

Question: Are all four candidates pre-empted, or is at least one open?

Branch:
- All pre-empted → Close Option B; the research line is exhausted.
- One+ open → Proceed to Phase B.

### DP2: After construction commitment (Phase B)

Question: Is the chosen candidate's construction self-consistent (unitary walker with the desired symmetry, distinct from Option A and from any known model)?

Branch:
- Self-consistent and novel → Proceed.
- Self-consistent but equivalent to known model → Try next candidate.
- Not self-consistent → Try next candidate or pivot.

### DP3: After classification analysis (Phase D)

Question: Does the topological classification differ from Option A's $\mathbb{Z}$?

Branch:
- Genuinely richer (e.g., $\mathbb{Z} \times \mathbb{Z}$ or $\mathbb{Z} \to \mathbb{Z}_2$ refinement) → Write a positive-result paper.
- Same as Option A → Write a "two negative results" paper covering Option A + Option B (potentially combinable with Option A's paper as an extended version).
- Pathological (e.g., walker is not gapped, classification is ill-defined) → Pivot or close.

---

## 6. Sanity Check Artifacts

The two failed sanity checks are preserved as `_OB_sanity_check.py` (Candidate Failure 1) and `_OB_alternating_check.py` (Candidate Failure 2) in this folder. They document the specific failures and provide concrete numerical evidence. Future work should re-run them as a sanity floor before any new construction.

---

## 7. Document Status

| Version | Date | Changes |
|---|---|---|
| 1.0 (draft) | 2026-05-16 | Initial OB spec proposing $\mathbb{Z}_2 \times \mathbb{Z}_2$ structure via $D = T^L \otimes \sigma_x$ chiral symmetry. |
| 1.1 (revised) | 2026-05-16 | **Major honest revision after two sanity-check failures.** Candidate Failure 1 (constant-parameter cylinder walker on $2L$-cylinder) collapses to Option A. Candidate Failure 2 (alternating angles) does not have $D$ as a symmetry. Spec now records failures honestly, lists four remaining candidates (glide-symmetric with redesigned shift; doubled-coin; anti-periodic Floquet drive; BZ-twisted), and proposes a phased research plan with explicit decision points and risk register. **Option B is now framed as an open research problem, not a confident plan.** |

---

*End of Option B research project specification (open).*
