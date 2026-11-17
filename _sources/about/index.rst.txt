:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-feuerbach:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

*Karl Wilhelm Feuerbach* presents in a complete, synchronized 4-track Digital Scriptorium edition the foundational 1822 Nuremberg monograph: :person:`Karl Wilhelm Feuerbach <feuerbach>`'s *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks* (Nürnberg: Riegel und Wießner, 1822, with :person:`Karl Buzengeiger <buzengeiger>`'s *Vorrede*). Feuerbach's treatise discovered the :term:`Nine-Point Circle <nine-point-circle>` centered at :math:`X(5)`, introduced the orthic inradius :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma`, proved the celebrated fourfold tangency theorem (§ 57) at the :term:`Feuerbach Point <feuerbach-point>` :math:`X(11)` and the three excircles, and established nine pure synthetic Euclidean propositions.

For :person:`Leonhard Euler <euler>`'s foundational 1765 memoir discovering the Euler line and the six mutual center quadrances, see sister codex :cite:`Euler (1765) <euler_1765>` in ``geometor/euler`` and the cross-treatise :doc:`/concordance`.

The GEOMETOR Mission
--------------------

Founded and directed by **phi ARCHITECT**, the GEOMETOR initiative is dedicated to the systematic digitization, symbolic formalization, and multi-medium re-articulation of classical geometric and axiomatic literature across 2,300+ years of mathematical history. GEOMETOR bridges historical philology and modern computational geometry through three structural pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and lossy optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of classical, Renaissance, and modern mathematical treatises. Enunciations, geometric constructions, proof steps, axiomatic justifications, marginal citations, primary-source folios (rendered dynamically through ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams are converted into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Eliminating floating-point approximation errors entirely, GEOMETOR anchors geometric constructions and center proofs in 100% exact symbolic algebra via :mod:`sympy` and Rational Trigonometry invariants (quadrance, spread, cross-ratio) evaluated over exact algebraic number fields. Every center, line concurrence, circle intersection, and tangency condition is verified to exact symbolic zero.

Repurposing Knowledge Across Mediums
    Extracted semantic and algebraic models are mobilized across synchronized multi-track Book Codices and EPUB 3 editions via ``photon-platform/publish``, computable deductive canons (:mod:`geometor.elements`, :mod:`geometor.etc`, :mod:`geometor.pappus`, :mod:`geometor.divine`), interactive SVG laboratories (:mod:`geometor.explorer`), high-definition visual broadcasts, and neuro-symbolic program synthesis engines (:mod:`geometor.seer`) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition synthesizes primary archival sources and rigorous symbolic computation:

Archival Sources
    * **Karl Wilhelm Feuerbach (1822)**: *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks und mehrerer durch sie bestimmten Linien und Figuren. Eine analytisch-trigonometrische Abhandlung*, with a *Vorrede* by :person:`Karl Buzengeiger <buzengeiger>` (Nürnberg: Bei Riegel und Wießner, 1822), pp. I–XVI, 1–62, with Tabulae I–II.
    * **Leonhard Euler (1767)**: *Solutio facilis problematum quorumdam geometricorum difficillimorum*, E325 (Petropoli, 1767; see standalone codex ``geometor/euler``).

Digital Scriptorium Methodology
    * **Parallel Bilingual Presentation**: Verbatim historical German transcription is paired section-by-section with original GEOMETOR English translation, detailed scholarly notes, and summary synopses.
    * **Zero-Float Verification**: All triangle centers, distances, and tangency points are computed symbolically over rational coordinates on the canonical Heronian triangle :math:`A = (0, 0)`, :math:`B = (14, 0)`, :math:`C = (5, 12)`, verifying Feuerbach's Theorem (:math:`X(5)` circle tangent internally to :math:`X(1)` incircle at :math:`X(11)` and externally to the three excircles) without floating-point approximations.
    * **Cross-Treatise Concordance**: See :doc:`/concordance` for side-by-side mapping of Euler's 1765 and Feuerbach's 1822 notations and centers, :doc:`/people/index` for biographical profiles, and :doc:`/bibliography` for full archival citations.
