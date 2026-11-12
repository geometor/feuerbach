==================
geometor-feuerbach
==================

**Multi-Treatise Bilingual Book Codex & Exact Symbolic Triangle-Center Architecture: Euler (1765/1767) & Feuerbach (1822)**

``geometor-feuerbach`` unites in a single Digital Scriptorium Book Codex and exact symbolic `SymPy <https://www.sympy.org/>`_ package the two foundational treatises of modern triangle-center geometry:

1. **Leonhard Euler** — *Solutio facilis problematum quorumdam geometricorum difficillimorum* (*Novi Commentarii Academiae Scientiarum Imperialis Petropolitanae*, Tom. XI pro Anno 1765, publ. 1767, pp. 103–123, Eneström **E325**): synchronized 4-track edition (*English · Latina 1767 · Summary · Notes*) deriving the six mutual quadrances among the orthocenter :math:`E = X(4)`, centroid :math:`F = X(2)`, incenter :math:`G = X(1)`, and circumcenter :math:`H = X(3)`, discovering the **Euler Line** (:math:`FH = \tfrac{1}{2}EF`), and solving the inverse triangle-reconstruction problem via :math:`z^3 - pz^2 + qz - r = 0`.
2. **Karl Wilhelm Feuerbach** — *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks, und mehrerer durch sie bestimmten Linien und Figuren* (mit einer *Vorrede* von Karl Buzengeiger, Nürnberg: Riegel und Wießner, 1822, pp. I–XVI, 1–62): synchronized 4-track edition (*English · Deutsch 1822 · Summary · Notes*) introducing the orthic inradius :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma`, constructing the **Nine-Point Circle** centered at :math:`L = X(5)`, proving in **§ 57** its internal tangency to the incircle at the **Feuerbach Point** :math:`X(11)` and external tangency to all three excircles, and concluding with pure Euclidean Book I/III/VI synthetic demonstrations (*Synthetischer Anhang*, ``1.–9. Satz``).

Key Features
------------

* **100% Exact Symbolic Geometry** (``geometor.model`` + ``sympy``): Zero floating-point approximations. Every center, circle, radical axis, and tangency locus is constructed over exact rationals :math:`\mathbb{Q}` on the canonical ``(15, 13, 14)`` triangle ``A = (0, 0), B = (14, 0), C = (5, 12)``:

  - ``X(1) = (6, 4)``, ``X(2) = (19/3, 4)``, ``X(3) = (7, 33/8)``, ``X(4) = (5, 15/4)``
  - Nine-point center ``X(5) = (6, 63/16)`` (nine-point radius :math:`R/2 = 65/16`)
  - Feuerbach internal tangency point ``X(11) = (6, 8)`` (:math:`|X(5)X(1)| = 65/16 - 4 = 1/16`)
  - Excircle tangency points ``Fe_a = (2709/289, 1792/289)``, ``Fe_b = (553/233, 1344/233)``, ``Fe_c = (1672/257, -24/257)``

* **Interactive ``.euclid-graphic`` SVGs**: Four theme-adaptive geometric constructions wired directly to ``:g:`` and ``:just:`` roles across the bilingual codex.
* **Cross-Corpus Concordance**: Links Euler (1765) and Feuerbach (1822) notations to Kimberling's ETC (``geometor/etc``), Ceva (``geometor/ceva``), Menelaus (``geometor/menelaus``), Altshiller-Court (``geometor/altshiller-court``), and Euclid's *Elements* (``geometor/euclid``, ``geometor/elements``).

Usage & Verification
--------------------

.. code-block:: bash

   # Run exact symbolic test suite
   pytest

   # Run symbolic demonstrations & CLI summary
   python demos/euler_1765_identities.py
   python demos/feuerbach_tangency.py
   python -m geometor.feuerbach

   # Compile the multi-treatise Book Codex into docs/
   publish build

License
-------

Code and original translations/commentary are released under the **MIT License**; the 1767 Latin text of Euler and 1822 German text of Feuerbach & Buzengeiger are in the **Public Domain**.
