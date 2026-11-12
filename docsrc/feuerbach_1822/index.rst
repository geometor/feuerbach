:title: Karl Wilhelm Feuerbach — Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks (1822)
:book_title: Eigenschaften einiger merkwürdigen Punkte (1822)
:layout: book

.. _feuerbach-1822-index:

===============================================================================================
EIGENSCHAFTEN EINIGER MERKWÜRDIGEN PUNKTE DES GERADLINIGEN DREIECKS UND MEHRERER LINIEN (1822)
===============================================================================================

.. rubric:: *Properties of Several Remarkable Points of the Rectilinear Triangle, and of Several Lines and Figures Determined by Them* — :person:`Karl Wilhelm Feuerbach <feuerbach>`

| **Editio Princeps (Deutsch, 1822):** *Eigenschaften einiger merkwürdigen Punkte des geradlinigen Dreiecks, und mehrerer durch sie bestimmten Linien und Figuren. Eine analytisch-trigonometrische Abhandlung von Karl Wilhelm Feuerbach, der Philosophie Doktor. Mit einer Vorrede von Karl Buzengeiger, ordentlichem Professor der Mathematik an der großherz. badischen Universität zu Freiburg.* Nürnberg, 1822. Bei Riegel und Wießner (pp. I–XVI, 1–62, Tab. I–II, Fig. 1–17).
| **English Translation:** Original folio-verified translation curated for the GEOMETOR Digital Scriptorium.
| **Synchronized 4-Track Codex:** *English · Deutsch (1822) · Summary · Notes*, paired with exact symbolic verification in :mod:`geometor.feuerbach.euler` and :mod:`geometor.feuerbach.tangency`.

.. epigraph::

   „In jedem Dreieck trifft der Kreis, welcher durch die Fußpunkte seiner Perpendikel geht, zugleich die Seiten desselben in ihren Mitten. […] Der Kreis, welcher durch die Fußpunkte der Perpendikel eines Dreiecks geht, berührt alle vier die drei Seiten desselben berührenden Kreise, und zwar den innerhalb berührenden innerhalb, jeden der ausserhalb berührenden aber ausserhalb.“

   “In every triangle, the circle which passes through the feet of its altitudes simultaneously meets the sides of the same at their midpoints. […] The circle which passes through the feet of the altitudes of a triangle touches all four circles touching the three sides of the same: namely, it touches the internally touching circle internally, whereas it touches each of the externally touching circles externally.”

   — :person:`Karl Wilhelm Feuerbach <feuerbach>`, :cite:`*Eigenschaften* <feuerbach_1822>`, **§§ 56–57** (p. 38)

----

Conspectus Operis (6 Units × 4 Synchronized Tracks)
---------------------------------------------------

**Unit 0 — Karl Buzengeiger's Vorrede (pp. III–XVI, Freiburg, 16 March 1822)**
   :ref:`English <fb-00-en>` · :ref:`Deutsch (1822) <fb-00-de>` · :ref:`Summary <fb-00-summary>` · :ref:`Notes <fb-00-notes>`

   Mathematics contemplated as *Wissenschaft* (:person:`Euclid <euclid>`'s :cite:`*Elements* <euclid_elements>`) versus *Kunst* (Greek geometric *Analysis* in :cite:`Euclid's *Data* <euclid_data>`, :person:`Apollonius <apollonius>`, Robert Simson's restorations, and Diophantus), reflections on combinatorial analysis and factorials, and :person:`Buzengeiger <buzengeiger>`'s commendation of his Freiburg pupil :person:`Feuerbach <feuerbach>`.

**Unit I — Erster Abschnitt: The Four Tritangent Circle Centers (§§ 1–18, pp. 1–14)**
   :ref:`English <fb-01-en>` · :ref:`Deutsch (1822) <fb-01-de>` · :ref:`Summary <fb-01-summary>` · :ref:`Notes <fb-01-notes>`

   Incenter :math:`S = X(1)` and excenters :math:`S', S'', S'''` as orthocentric system, :person:`L'Huilier <lhuilier>`'s symmetric law :math:`rr'r''r''' = \Delta^2` (§ 2), :math:`r'r'' + r'r''' + r''r''' = s^2` (§ 3), :math:`r' + r'' + r''' = r + 4R` (§ 5), contact triangles :math:`\delta, \delta', \delta'', \delta'''` (§ 8), and the six mutual center-chord laws :math:`A^2 + A'^2 = B^2 + B'^2 = C^2 + C'^2 = 16R^2` (§§ 12–18).

**Unit II — Zweiter Abschnitt: Orthocenter, Orthic Triangle & Inradius ρ (§§ 19–48, pp. 15–32)**
   :ref:`English <fb-02-en>` · :ref:`Deutsch (1822) <fb-02-de>` · :ref:`Summary <fb-02-summary>` · :ref:`Notes <fb-02-notes>`

   Orthocenter :math:`O = X(4)` as incenter of :person:`Fagnano <fagnano>`'s minimal-perimeter :term:`orthic triangle <orthic-triangle>` :math:`\triangle MNP` (§ 19), introduction of the orthic inradius :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma` (§§ 23–25), orthic circumradius :math:`\tfrac{1}{2}R` (§ 26), :math:`r^2 + r'^2 + r''^2 + r'''^2 = 4R(2R - \rho)` (§ 28), and the equal circumradii :math:`R' = R'' = R''' = R` of :math:`\triangle BCO, \triangle ACO, \triangle ABO`.

**Unit III — Dritter & Vierter Abschnitt: The Nine-Point Circle & Feuerbach's Tangency Theorem (§§ 49–60, pp. 33–41)**
   :ref:`English <fb-03-en>` · :ref:`Deutsch (1822) <fb-03-de>` · :ref:`Summary <fb-03-summary>` · :ref:`Notes <fb-03-notes>`

   **Complete verbatim edition of §§ 49–60**: citation of :person:`Euler <euler>` (1765) and :person:`Fuß <fuss>` (1797) for :math:`\overline{KS}^2 = R^2 - 2rR` (§ 49), nine-point center :math:`L = X(5)` bisecting :math:`KO` (§§ 53–55), the nine concyclic points (§ 56), **§ 57 Feuerbach's Theorem** (:math:`LS = \tfrac{1}{2}R - r` at :math:`X(11)` and :math:`LS^{(k)} = \tfrac{1}{2}R + r^{(k)}`), :math:`LS + LS' + LS'' + LS''' = 6R` (§ 58), :math:`\sum LS_i^2 = R(13R - 4\rho)` (§ 59), and the :term:`harmonic range <harmonic-range>` :math:`(O, G; L, K) = -1` (§ 60), together with exact SymPy diagnosis of Feuerbach's § 51 sign-substitution slip.

**Unit IV — Fünfter Abschnitt: Proportional Contact Triangles & Excentral Orthocenter (§§ 61–87, pp. 41–55)**
   :ref:`English <fb-04-en>` · :ref:`Deutsch (1822) <fb-04-de>` · :ref:`Summary <fb-04-summary>` · :ref:`Notes <fb-04-notes>`

   Geometric-mean area proportionals :math:`\mu^{(k)} : \delta^{(k)} = \delta^{(k)} : \Delta` (§ 63), the five-triangle area law :math:`\mu + \mu' + \mu'' + \mu''' + \triangle MNP = 2\Delta` (§ 64), half-perimeter law (§ 65), corner-circle inradii (§§ 71–73), and § 87 establishing that :math:`S = X(1)` is the orthocenter of :math:`\triangle O'O''O'''`.

**Unit V — Synthetischer Anhang: Pure Euclidean Proofs of Nine Core Propositions (1.–9. Satz, pp. 56–62)**
   :ref:`English <fb-05-en>` · :ref:`Deutsch (1822) <fb-05-de>` · :ref:`Summary <fb-05-summary>` · :ref:`Notes <fb-05-notes>`

   Pure synthetic demonstrations grounded in :cite:`Euclid's *Elements* <euclid_elements>` Books I, III, and VI, culminating in `5. Satz` (:math:`\triangle MNP : \triangle ABC = \rho : R`), `6. Satz` (:math:`CO \cdot OP = 2R\rho`), `7. Satz` (:math:`a^2 + b^2 + c^2 = 8R^2 + 4\rho R`), and verbatim **9. Satz** proving :math:`LM = LN = LP = \tfrac{1}{2}R` for the midpoint :math:`L` of :math:`OK`.

.. picture:: /_static/constructions/nine_point_circle.svg
   :alt: Feuerbach's nine-point circle centered at L = X(5) passing through the three altitude feet, three side midpoints, and three Euler midpoints

.. toctree::
   :maxdepth: 1
   :caption: English Translation

   00-vorrede-buzengeiger-en
   01-tritangent-circles-en
   02-orthocenter-orthic-triangle-en
   03-nine-point-tangency-theorem-en
   04-proportional-triangles-en
   05-synthetic-anhang-en

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Editio Princeps Deutsch (1822)

   00-vorrede-buzengeiger-de
   01-tritangent-circles-de
   02-orthocenter-orthic-triangle-de
   03-nine-point-tangency-theorem-de
   04-proportional-triangles-de
   05-synthetic-anhang-de

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Summaries & Critical Notes

   00-vorrede-buzengeiger-summary
   00-vorrede-buzengeiger-notes
   01-tritangent-circles-summary
   01-tritangent-circles-notes
   02-orthocenter-orthic-triangle-summary
   02-orthocenter-orthic-triangle-notes
   03-nine-point-tangency-theorem-summary
   03-nine-point-tangency-theorem-notes
   04-proportional-triangles-summary
   04-proportional-triangles-notes
   05-synthetic-anhang-summary
   05-synthetic-anhang-notes
