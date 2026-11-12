:title: GEOMETOR • feuerbach — Euler (1765) & Feuerbach (1822) Bilingual Book Codex
:layout: book

==================
GEOMETOR feuerbach
==================

.. rubric:: Multi-Treatise Bilingual Book Codex & Exact Symbolic Triangle-Center Architecture

This Digital Scriptorium edition unites in a single computational and philological codex the two foundational treatises that transformed classical Euclidean triangle geometry into a unified science of collinear centers, symmetric polynomial invariants, and circle tangencies:

1. :person:`Leonhard Euler <euler>` — :cite:`*Solutio facilis problematum quorumdam geometricorum difficillimorum* <euler_1765>` (*Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae*, Tom. XI pro Anno 1765, publ. 1767, pp. 103–123, Eneström **E325**): verbatim 1767 St. Petersburg Latin alongside an original GEOMETOR English translation, deriving the six mutual quadrances among the orthocenter :math:`E = X(4)`, centroid :math:`F = X(2)`, incenter :math:`G = X(1)`, and circumcenter :math:`H = X(3)`, discovering the :term:`Euler Line <euler-line>`, and reconstructing the triangle via the side-length cubic :math:`z^3 - pz^2 + qz - r = 0`.
2. :person:`Karl Wilhelm Feuerbach <feuerbach>` — :cite:`*Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks* <feuerbach_1822>` (Nürnberg: Riegel und Wießner, 1822, pp. I–XVI, 1–62, with :person:`Karl Buzengeiger <buzengeiger>`'s *Vorrede*): verbatim 1822 German alongside an original GEOMETOR English translation, introducing the orthic inradius :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma`, establishing the :term:`Nine-Point Circle <nine-point-circle>` centered at :math:`L = X(5)`, proving in **§ 57** its internal tangency to the incircle at the :term:`Feuerbach Point <feuerbach-point>` :math:`X(11)` and external tangency to all three excircles, and concluding with a pure Euclidean Book I/III/VI synthetic *Anhang* (`1.–9. Satz`).

.. picture:: /_static/constructions/feuerbach_tangency.svg
   :alt: Feuerbach's Theorem (1822, § 57): Nine-point circle tangent internally to the incircle at X(11) and externally to all three excircles

Every algebraic identity across both treatises is verified to exact symbolic zero in :mod:`sympy` (:func:`~geometor.feuerbach.euler.prove_euler_1765_identities`), and every geometric center and tangency locus is constructed without floating-point numbers on the canonical Heronian ``(15, 13, 14)`` triangle ``A = (0, 0), B = (14, 0), C = (5, 12)`` (:func:`~geometor.feuerbach.tangency.construct_feuerbach_tangency`), where :g:`X_5 <0038.g2:X5>` ``= (6, 63/16)`` and :g:`X_{11} <0038.g2:X11>` ``= (6, 8)``. For cevian concurrency and projective transversal duality, see the companion codices :cite:`Ceva (1678) <ceva_1678>` and :cite:`Menelaus (*Sphaerica*) <menelaus_sphaerica>`.

.. toctree::
   :maxdepth: 2
   :caption: Primary Treatises (4-Track Bilingual Codices)

   euler_1765/index
   feuerbach_1822/index

.. toctree::
   :maxdepth: 2
   :caption: Scholarly Apparatus

   concordance
   bibliography
   persons
   glossary
