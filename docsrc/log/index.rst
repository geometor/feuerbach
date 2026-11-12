:navigation: footer
:order: 20
:layout: book

Research & Editorial Log
========================

2026-11-12 — Initial Euler (1765) & Feuerbach (1822) Bilingual Book Codex (``v0.1.0``)
--------------------------------------------------------------------------------------

* Transcribed and translated :person:`Leonhard Euler <euler>`'s *Solutio facilis problematum quorumdam geometricorum difficillimorum* (**E325**, 1765/1767, §§ 1–34, pp. 103–123) and :person:`Karl Wilhelm Feuerbach <feuerbach>`'s *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks* (1822, *Vorrede* pp. I–XVI, §§ 1–87, and synthetic Euclidean *Anhang* `1.–9. Satz`, pp. 56–62) directly from archival scans.
* Proved 30 symbolic polynomial identities in :mod:`sympy` (:func:`~geometor.feuerbach.euler.prove_euler_1765_identities`), identifying and correcting Feuerbach's § 51 sign slip (:math:`\overline{OS^{(k)}}^2 = 2r^{(k)2} - 2\rho R`) and showing why the cancellation of :math:`\rho R` in Apollonius's median theorem preserved the exact truth of **§ 57 (Feuerbach's Theorem)**.
* Implemented exact ``geometor.model`` compass-and-straightedge constructions on Heronian ``(15, 13, 14)`` yielding ``X(5) = (6, 63/16)``, ``X(11) = (6, 8)``, and ``Fea, Feb, Fec``, with four theme-adaptive ``.euclid-graphic`` SVGs.
