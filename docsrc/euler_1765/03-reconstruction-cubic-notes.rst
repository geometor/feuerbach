:title: Euler (1765) §§ 19–24 — Critical & Symbolic Notes
:layout: book

.. _euler-03-notes:

===============================================================================
Critical & Symbolic Notes — Unit III: Inverse Reconstruction Cubic (§§ 19–24)
===============================================================================

.. rubric:: Algebraic Mechanism of Q² Cancellation & 1767 Folio Notes

1. Two Typographical Details in §§ 19–21 (pp. 114–116)
------------------------------------------------------

* **p. 114, § 19, penult. line**: The folio prints ``Quoniam igitur hinc est -s/p = QQ/R``; since :math:`R = \frac{r^2}{ps}` and :math:`Q = \frac{r}{p}`, we have :math:`\frac{Q^2}{R} = \frac{r^2/p^2}{r^2/(ps)} = +\frac{s}{p}` (as Euler immediately uses in :math:`q = \frac{1}{4}P + 2Q + \frac{Q^2}{R}`).
* **p. 116, § 21, Eq. III**: The folio prints ``hh = 1/36 P - 8/9 Q + 6 QQ / (9 R)`` (`6` pro `5`), whereas on the facing page 115 (§ 19 IV) Euler correctly printed ``+ 5 QQ / (9 R)``. Euler's solved rational expressions for :math:`R, Q, P` immediately below Eq. III use the true coefficient ``5``: only ``5 · II - 2 · III`` eliminates :math:`\frac{Q^2}{R}` to produce the denominator :math:`3g^2 + 6h^2 - 2f^2`.

2. Perfect-Square Factorization of 3g² + 6h² − 2f² Under Collinearity
---------------------------------------------------------------------

Consider the denominator governing all three invariants :math:`R, Q, P` in **§ 21**:

.. math::

   \mathcal{D} = 3g^2 + 6h^2 - 2f^2 = 3FH^2 + 6FG^2 - 2GH^2.

Whenever the incenter :math:`G` lies on the Euler line so that :math:`g = f - h` (Euler's § 25), substituting :math:`g = f - h` into :math:`\mathcal{D}` yields an **exact square**:

.. math::

   3(f - h)^2 + 6h^2 - 2f^2 = f^2 - 6fh + 9h^2 = (f - 3h)^2 \ge 0.

Thus :math:`\mathcal{D}` vanishes only at the equilateral coalescence :math:`f = 3h` (where :math:`E, F, G, H` coincide), and for every non-equilateral collinear configuration :math:`P` factors up to the single quadratic radical :math:`\sqrt{3h(4f - 3h)}`, forcing a double root :math:`a = b` in Unit IV (§§ 25–26).

3. Constructibility Barrier: Why Compass and Straightedge Cannot Construct (A, B, C)
------------------------------------------------------------------------------------

In **§ 22**, Euler remarks that once :math:`z^3 - pz^2 + qz - r = 0` is formed, its three roots give the sides :math:`(a, b, c)`. Over a general rational configuration of centers :math:`(E, F, G, H)`, this cubic is **irreducible over** :math:`\mathbb{Q}(f, g, h)` with three distinct positive real roots (:term:`casus irreducibilis <casus-irreducibilis>`). By Wantzel's theorem (1837), reconstructing :math:`\triangle ABC` from :math:`(E, F, G, H)` in general requires **angle trisection** (or conic intersections) and is impossible by Euclidean ruler and compass alone—a fact already recognized empirically by :person:`Euler <euler>` in **§ 34** (p. 123)!
