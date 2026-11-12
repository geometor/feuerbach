# GEOMETOR • feuerbach

Multi-Treatise Bilingual Book Codex & Exact Symbolic Triangle-Center Architecture uniting **Leonhard Euler's *Solutio facilis problematum quorumdam geometricorum difficillimorum* (1765/1767, Eneström E325)** and **Karl Wilhelm Feuerbach's *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks* (Nürnberg, 1822)**.

---

## 1. Purpose & Scope

`geometor-feuerbach` bridges the Digital Scriptorium and Constructive Geometry pillars of the GEOMETOR ecosystem:

1. **Book I — `docsrc/euler_1765/` (4 Units × 4 Synchronized Tracks: English · Latina 1767 · Summary · Notes)**:
   - Folio-verified edition of Euler's St. Petersburg memoir (*Novi Commentarii*, Tom. XI, pp. 103–123, §§ 1–34, Tab. II Fig. 1–9).
   - Derives the six mutual quadrances among `E = X(4)`, `F = X(2)`, `G = X(1)`, and `H = X(3)` in elementary symmetric polynomials `(p, q, r)`, establishes the **Euler Line** (`FH = 1/2 EF`, `EH = 3/2 EF`) and Stewart compatibility law `4 GH^2 + 2 EG^2 = 3 EF^2 + 6 FG^2`, reconstructs `(a, b, c)` from `z^3 - p z^2 + q z - r = 0`, and analyzes collinear isosceles degeneracy and the *casus irreducibilis*.
2. **Book II — `docsrc/feuerbach_1822/` (6 Units × 4 Synchronized Tracks: English · Deutsch 1822 · Summary · Notes)**:
   - Folio-verified edition of Feuerbach's 1822 Nuremberg monograph (with Karl Buzengeiger's *Vorrede*, pp. I–XVI, §§ 1–87, and the pure Euclidean *Synthetischer Anhang* `1.–9. Satz`, pp. 56–62).
   - Introduces the orthic inradius `rho = 2 R cos(alpha) cos(beta) cos(gamma)`, constructs the **Nine-Point Circle** centered at `L = X(5) = mid(OK)` of radius `R/2`, proves **Feuerbach's Theorem (§ 57)** (`LS = |R/2 - r|` at `X(11)` and `LS_k = R/2 + r_k` at `Fe_a, Fe_b, Fe_c`), and documents via exact SymPy verification Feuerbach's historical sign-substitution slip (`+2 rho R` pro `-2 rho R` in §§ 51, 52, 60) alongside why § 57 and § 59 remain 100% exact.
3. **100% Exact Symbolic Python Package (`src/geometor/feuerbach/`)**:
   - Zero `float` or `sp.Float` approximations anywhere in `Model` construction or polynomial proof verification.
   - Canonical rational Heronian `(15, 13, 14)` benchmark `A = (0, 0), B = (14, 0), C = (5, 12)` (`Delta = 84`, `R = 65/8`, `r = 4`, `r_a = 14`, `r_b = 21/2`, `r_c = 12`, `rho = 99/52`), where every center and tangency point has exact rational coordinates over `Q`:
     - `X(1) = (6, 4)`, `X(2) = (19/3, 4)`, `X(3) = (7, 33/8)`, `X(4) = (5, 15/4)`, `X(5) = (6, 63/16)`, `X(11) = (6, 8)`
     - Excircle tangency vertices: `Fe_a = (2709/289, 1792/289)`, `Fe_b = (553/233, 1344/233)`, `Fe_c = (1672/257, -24/257)`.

---

## 2. Key Modules & Repository Layout

- `src/geometor/feuerbach/`:
  - `primitives.py` — `TriangleInvariants`, `compute_triangle_invariants`, `construct_fundamental_centers` (`X(1)`–`X(4)` with targeted DAG intersections).
  - `euler.py` — `prove_euler_1765_identities` (all Euler E325 & Feuerbach 1822 polynomial identities reduced to symbolic `0`), `construct_euler_line_harmonic` (`(X4, X2; X5, X3) = -1`), `solve_euler_reconstruction_cubic`.
  - `tangency.py` — `construct_nine_point_circle` (all 9 concyclic points at quadrance `R^2/4 = 4225/256`), `construct_feuerbach_tangency` (`X(11)` and `Fe_a, Fe_b, Fe_c` proved tangent via exact quadrance & collinearity).
  - `render.py` — Exports the 4 theme-adaptive interactive `.euclid-graphic` SVGs in `docsrc/_static/constructions/` (`0114.g1`, `0038.g1`, `0038.g2`, `0038.g3`).
  - `concordance.py` & `__main__.py` — Programmatic concordance loader and CLI entry point (`python -m geometor.feuerbach`).
- `resources/`:
  - `persons.json`, `citations.json`, `glossary.json`, `feuerbach/sources_manifest.json`, `feuerbach/concordance.json` (cross-referenced to `geometor/ceva`, `geometor/menelaus`, `geometor/etc`, `geometor/altshiller-court`, `geometor/euclid`, `geometor/elements`).
- `demos/` & `tests/`:
  - `demos/euler_1765_identities.py`, `demos/feuerbach_tangency.py`, `tests/test_feuerbach.py`.

---

## 3. Offline Sandbox Verification Commands

Always run single-purpose, prefix-matchable commands on Python 3.13 inside the offline sandbox:

```bash
/home/phi/PROJECTS/geometor/.venv/bin/pytest
/home/phi/.local/bin/ruff check src demos tests
/home/phi/.local/bin/publish build
```
