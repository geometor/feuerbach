"""Exact symbolic constructions, polynomial proofs, and codex concordance for Euler (1765) and Feuerbach (1822).

Provides:

- :mod:`geometor.feuerbach.euler`: Symbolic SymPy polynomial proofs of Leonhard Euler's 1765/1767
  memoir *Solutio facilis problematum quorumdam geometricorum difficillimorum* (E325, §§ 1–34),
  Karl Wilhelm Feuerbach's 1822 treatise *Eigenschaften einiger merkwürdigen Punkte des
  geradlinigen Dreiecks* (§§ 1–60), and the exact compass-and-straightedge construction of
  Euler's four classical centers and the Euler line.
- :mod:`geometor.feuerbach.tangency`: Exact :class:`~geometor.model.Model` construction and
  deductive verification of the nine-point circle, the Feuerbach point ``X(11)``, and the three
  excircle tangency points ``Fea``, ``Feb``, ``Fec`` on the canonical Heronian ``(15, 13, 14)``
  triangle.
- :mod:`geometor.feuerbach.render`: Theme-adaptive ``.euclid-graphic`` SVG exporter for the
  bilingual Book Codices.
- :mod:`geometor.feuerbach.concordance`: Structured access to the cross-treatise concordance and
  archival source manifest.
"""

from __future__ import annotations

__version__ = "0.1.1"

from geometor.feuerbach.concordance import (
    ConcordanceEntry,
    load_concordance,
    load_sources_manifest,
)
from geometor.feuerbach.euler import (
    EulerCentersResult,
    EulerCubicExample,
    EulerIdentitiesReport,
    HeronianNumericCheck,
    construct_euler_1765_centers,
    prove_euler_1765_identities,
    solve_euler_reconstruction_cubic,
)
from geometor.feuerbach.primitives import (
    construct_altitude_foot,
    construct_altitude_line,
    construct_angle_bisectors,
    construct_midpoint,
    construct_perp_bisector,
)
from geometor.feuerbach.render import export_all_codex_svgs, render_model_svg
from geometor.feuerbach.tangency import (
    FeuerbachTangencyResult,
    construct_feuerbach_tangency,
)

__all__ = [
    "ConcordanceEntry",
    "EulerCentersResult",
    "EulerCubicExample",
    "EulerIdentitiesReport",
    "FeuerbachTangencyResult",
    "HeronianNumericCheck",
    "__version__",
    "construct_altitude_foot",
    "construct_altitude_line",
    "construct_angle_bisectors",
    "construct_euler_1765_centers",
    "construct_feuerbach_tangency",
    "construct_midpoint",
    "construct_perp_bisector",
    "export_all_codex_svgs",
    "load_concordance",
    "load_sources_manifest",
    "prove_euler_1765_identities",
    "render_model_svg",
    "solve_euler_reconstruction_cubic",
]
