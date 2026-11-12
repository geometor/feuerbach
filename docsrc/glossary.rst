:title: Technical Glossary of Geometric & Algebraic Terms
:layout: book

.. _glossary:

Technical Glossary
==================

.. rubric:: Bilingual Latin, German, and Modern Triangle-Geometry Terminology

Every inline ``:term:`` role links directly to its entry below.

----

.. _term-euler-line:

Euler Line (*Linea Euleri* / *Eulersche Gerade*)
------------------------------------------------

* **Tradition:** Euler E325 (§§ 16–18, 1765/1767); Feuerbach (§§ 54–55, § 60, 1822)
* **Formulation:** Collinear axis through ``X(4)``, ``X(5)``, ``X(2)``, ``X(3)``

The straight line passing through the orthocenter :math:`E = X(4)`, nine-point center :math:`L = X(5)`, centroid :math:`F = X(2)`, and circumcenter :math:`H = X(3)` of any non-equilateral triangle, with :math:`EF : FH = 2 : 1` and :math:`EL = LH = \frac{3}{4}EF`.

.. _term-nine-point-circle:

Nine-Point Circle (*Kreis durch die Fußpunkte der Perpendikel*)
---------------------------------------------------------------

* **Tradition:** Brianchon & Poncelet (1821); Feuerbach (§§ 26, 54–56, 9. Satz, 1822); Terquem (1842)
* **Formulation:** Circle of center ``X(5)`` and radius :math:`R_9 = \frac{1}{2}R`

The circle passing simultaneously through the three altitude feet (:math:`H_a, H_b, H_c`), the three side midpoints (:math:`M_a, M_b, M_c`), and the three Euler midpoints bisecting the segments from each vertex to the orthocenter (:math:`E_a, E_b, E_c`).

.. _term-feuerbach-point:

Feuerbach Point ``X(11)`` (*Innerer Berührungspunkt*)
-----------------------------------------------------

* **Tradition:** Feuerbach (§ 57, 1822); Kimberling ETC ``X(11)``
* **Formulation:** Unique internal tangency point of the nine-point circle and the incircle

Because the distance between the nine-point center :math:`L = X(5)` and the incenter :math:`S = X(1)` satisfies :math:`\overline{LS}^2 = (\frac{1}{2}R - r)^2`, the nine-point circle and incircle touch internally at ``X(11)`` (or coincide when :math:`\triangle ABC` is equilateral).

.. _term-tritangent-circles:

Tritangent Circles (*Vier berührende Kreise*)
---------------------------------------------

* **Tradition:** L'Huilier (1810); Feuerbach (*Erster Abschnitt*, §§ 1–18, 1822)
* **Formulation:** Incircle :math:`(S, r)` and three excircles :math:`(S', r'), (S'', r''), (S''', r''')`

The four circles tangent to all three extended sidelines of :math:`\triangle ABC`, whose centers lie at the intersections of the internal and external angle bisectors and satisfy :math:`rr'r''r''' = \Delta^2` and :math:`r' + r'' + r''' - r = 4R`.

.. _term-orthic-triangle:

Orthic Triangle (*Fußpunktdreieck* :math:`\triangle MNP`)
---------------------------------------------------------

* **Tradition:** Fagnano (1775); Feuerbach (*Zweiter Abschnitt*, §§ 19–26, 1822)
* **Formulation:** Pedal triangle of the orthocenter ``X(4)``

The triangle formed by the feet of the three altitudes of :math:`\triangle ABC`. In an acute triangle, its perimeter is :math:`\frac{2\Delta}{R}`, its circumradius is :math:`\frac{1}{2}R`, its incenter is the orthocenter :math:`O = X(4)`, and its inradius is :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma`.

.. _term-feuerbach-triangle:

Feuerbach Triangle (:math:`\triangle Fe_a Fe_b Fe_c`)
-----------------------------------------------------

* **Tradition:** Feuerbach (§ 57, 1822); Modern Triangle Geometry
* **Formulation:** Triangle of external nine-point / excircle tangency points

The triangle inscribed in the nine-point circle whose vertices are the three points where the nine-point circle touches the excircles externally (:math:`LS^{(k)} = \frac{1}{2}R + r^{(k)}`).

.. _term-quadrance:

Quadrance
---------

* **Tradition:** Euler (§ 18, 1765); Feuerbach (§§ 49–60, 1822); Wildberger (2005)
* **Formulation:** Exact squared distance :math:`Q(P, Q) = (x_Q - x_P)^2 + (y_Q - y_P)^2`

Polynomial metric invariant over :math:`\mathbb{Q}(a, b, c)` free of square-root branch ambiguities.

.. _term-harmonic-range:

Harmonic Range (:math:`(X_4, X_2; X_5, X_3) = -1`)
--------------------------------------------------

* **Tradition:** Pappus (Book VII); Projective Geometry
* **Formulation:** Collinear quadruple with cross-ratio :math:`-1`

Along the Euler line, the nine-point center ``X(5)`` and circumcenter ``X(3)`` divide the segment from the orthocenter ``X(4)`` to the centroid ``X(2)`` internally and externally in ratio :math:`3 : 1`.

.. _term-casus-irreducibilis:

Casus Irreducibilis
-------------------

* **Tradition:** Cardano (1545); Euler (E325 § 34, p. 123)
* **Formulation:** Three-real-root cubic regime requiring trigonometric trisection

In Euler's inverse triangle reconstruction :math:`z^3 - pz^2 + qz - r = 0`, whenever three distinct positive side lengths :math:`(a, b, c)` exist, the cubic discriminant is strictly positive, placing radical extraction in the *casus irreducibilis*.

.. _term-symmetric-polynomials:

Elementary Symmetric Polynomials :math:`(p, q, r)`
--------------------------------------------------

* **Tradition:** Euler (E325 § 10, p. 107)
* **Formulation:** :math:`p = a + b + c`, :math:`q = ab + ac + bc`, :math:`r = abc`

The three algebraic generators of symmetric functions of the triangle sides, in terms of which Heron's formula reads :math:`16A^2 = -p^4 + 4p^2q - 8pr`.
