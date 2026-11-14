=========
Changelog
=========

0.1.1 (2026-11-13)
------------------

- Curated and mapped primary-source folio links across Euler (1765/1767) and Feuerbach (1822) treatises (115/115 directives resolved).

0.1.0 (2026-11-12)
------------------

* **Euler (1765/1767, E325) 4-Track Bilingual Book Codex** (``docsrc/euler_1765/``):
  Verbatim 1767 St. Petersburg Latin, original GEOMETOR English translation, mathematical summaries, and critical apparatus across §§ 1–34, documenting authentic 1767 printing *errata* on pp. 106 and 109.
* **Feuerbach (1822) 4-Track Bilingual Book Codex** (``docsrc/feuerbach_1822/``):
  Verbatim 1822 Nuremberg German, original GEOMETOR English translation, summaries, and critical apparatus covering Buzengeiger's *Vorrede* (pp. III–XVI), the analytical-trigonometric treatise (§§ 1–87, culminating in § 57 Feuerbach's Theorem), and the pure Euclidean synthetic *Anhang* (`1.–9. Satz`, pp. 56–62), including critical proof of the corrected § 51 / § 52 / § 60 orthocenter-excenter identities.
* **Exact Symbolic ``geometor.feuerbach`` Package**:
  30 exact rational-function polynomial proofs in SymPy, Euler's inverse cubic solver on ``(5, 6, 7)`` and ``(15, 13, 14)``, ``@proposition`` compass-and-straightedge ``Model(..., auto_intersect=False)`` constructions of ``X(1)..X(5)``, ``X(11) = (6, 8)``, and ``Fea, Feb, Fec``, plus four interactive ``.euclid-graphic`` SVGs and cross-corpus JSON concordance.
