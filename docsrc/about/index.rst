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

*GEOMETOR feuerbach* unites in a single computational and philological Book Codex the two foundational treatises that transformed classical Euclidean triangle geometry into a unified science of collinear centers, symmetric polynomial invariants, and circle tangencies: :person:`Leonhard Euler <euler>`'s *Solutio facilis problematum quorumdam geometricorum difficillimorum* (presented to the St. Petersburg Academy in 1765, published 1767, Eneström **E325**) and :person:`Karl Wilhelm Feuerbach <feuerbach>`'s landmark monograph *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks* (Nürnberg: Riegel und Wießner, 1822). Together, these works establish the foundational coordinate and synthetic relationships governing the orthocenter :math:`X(4)`, centroid :math:`X(2)`, incenter :math:`X(1)`, circumcenter :math:`X(3)`, and the nine-point circle center :math:`X(5)`.

Every proposition, enunciation, derivation step, and diagram from both treatises has been extracted into addressable semantic elements. Rather than relying on lossy optical character recognition or static facsimile scans, each Latin and German passage has been transcribed and verified directly against high-resolution archival scans—recovering historical errata such as Euler's St. Petersburg typesetting slips in § 7 (``bc`` pro ``6c``) and § 12 (``=`` pro ``-``), as well as Feuerbach's sign slip in § 51. The original engraved copper plates (*Tabulae*) have been reconstructed as calibrated, resolution-independent vector graphics, and every algebraic relation across both treatises is verified to exact symbolic zero.

This edition operates as an integral node within the broader GEOMETOR ecosystem. It anchors the triangle centers of :cite:`Kimberling's ETC <kimberling_etc>` to their historical and algebraic origins, directly linking with the axiomatic foundations of :cite:`Euclid's Elements <euclid_elements>`, the cevian concurrency theorems of :cite:`Ceva (1678) <ceva_1678>`, and the projective collinearity principles of :cite:`Menelaus <menelaus_sphaerica>`. Through the computational engine of :mod:`geometor.feuerbach`, these historical proofs become executable algebraic objects.

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
    * **Leonhard Euler (1767)**: *Solutio facilis problematum quorumdam geometricorum difficillimorum*, *Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae*, Tom. XI pro Anno 1765 (Petropoli: Typis Academiae Scientiarum, 1767), pp. 103–123, with Tabula II. Eneström index **E325**.
    * **Karl Wilhelm Feuerbach (1822)**: *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks und mehrerer durch sie bestimmten Linien und Figuren. Eine analytisch-trigonometrische Abhandlung*, with a *Vorrede* by :person:`Karl Buzengeiger <buzengeiger>` (Nürnberg: Bei Riegel und Wießner, 1822), pp. I–XVI, 1–62, with Tabulae I–II.

Digital Scriptorium Methodology
    * **Parallel Bilingual Presentation**: Verbatim historical transcriptions (Latin for Euler, German for Feuerbach) are paired section-by-section with original GEOMETOR English translations, detailed scholarly notes, and summary synopses.
    * **Zero-Float Verification**: All triangle centers, distances, and tangency points are computed symbolically over rational coordinates on the canonical Heronian triangle :math:`A = (0, 0)`, :math:`B = (14, 0)`, :math:`C = (5, 12)`, verifying Feuerbach's Theorem (:math:`X(5)` circle tangent internally to :math:`X(1)` incircle at :math:`X(11)` and externally to the three excircles) without floating-point approximations.
    * **Cross-Treatise Concordance**: See :doc:`/concordance` for side-by-side mapping of Euler's 1765 and Feuerbach's 1822 notations and centers, :doc:`/persons` for biographical profiles, and :doc:`/bibliography` for full archival citations.
