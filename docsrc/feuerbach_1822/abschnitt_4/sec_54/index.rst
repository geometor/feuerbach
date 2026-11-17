:layout: book
:canonical_id: §§ 54–57
:breadcrumb_title: §§ 54–57
:order: 1
:folio: p. 37
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-03:
.. _fb-03-en:
.. _fb-en-s54:

.. folio:: §§ 54–55
   :page: 37

§§ 54–57: Feuerbach's Nine-Point Circle Tangency Theorem
========================================================

* **§ 54 (Relation KO = 2 OL)**: Let :math:`L` [:g:`X_5 <0038.g1:X5>`] be taken for the center of the circle [:g:`(MNP) <0038.g1:( X5 H1 )>`] circumscribed about the orthic triangle :math:`MNP`, whose radius was found (§ 26) equal to :math:`\tfrac{1}{2}R`, and draw :math:`OL`. Because :math:`O` is simultaneously the center of the circle *inscribed* in :math:`\triangle MNP` (inradius :math:`\rho`), Euler's formula (§ 49) applied to :math:`\triangle MNP` immediately gives

  .. math::

     \overline{OL}^2 = \left(\frac{1}{2}R\right)^2 - 2\rho\left(\frac{1}{2}R\right) = \frac{1}{4}R^2 - \rho R,

  and since we just found :math:`\overline{KO}^2 = R^2 - 4\rho R`, it follows that :math:`\overline{KO}^2 = 4\overline{OL}^2`, or:

  .. math::

     KO = 2\,OL

  (which holds likewise when :math:`\triangle ABC` is obtuse, e.g. at :math:`A`, from :math:`\overline{OL}^2 = \frac{1}{4}R^2 + \rho^{(1)}R` and :math:`\overline{KO}^2 = R^2 + 4\rho^{(1)}R`): *In every triangle, the intersection point of its altitudes is twice as far from the center of the circumscribed circle as from the center of the circle passing through the feet of those altitudes.*

* **§ 55 (Collinearity of O, L, K — Midpoint Property)**: Drop from the center :math:`L` upon the straight lines :math:`AB, CP` the perpendiculars :math:`LJ, LH`; then :math:`LJ = PH`, and in :math:`\triangle OPL` we have :math:`PH = \frac{-\overline{OL}^2 + \overline{OP}^2 + \overline{LP}^2}{2\,OP}`. Now :math:`LP = \frac{1}{2}R` and (§ 54) :math:`\overline{OL}^2 = \frac{1}{4}R^2 - \rho R` *[correcting the 1822 printing slip ``1/2 R^2``]*, while (§§ 35, 45) :math:`OP \cdot Kc = \rho R`, whence :math:`\overline{LP}^2 - \overline{OL}^2 = OP \cdot Kc`. Substituting into :math:`PH = LJ` yields:

  .. math::

     LJ = \frac{1}{2}(OP + Kc),

  from which property one concludes that **the points** :math:`O, L, K` **lie on one and the same straight line, whose midpoint is** :math:`L`!

.. folio:: §§ 56–57
   :page: 38

* **§ 56 (Bisection of the Three Sides — The Nine-Point Circle)**: Because :math:`L` lies at the midpoint of segment :math:`KO`, its projection :math:`J` is likewise the midpoint of :math:`Pc` (between the altitude foot :g:`P <0038.g1:H3>` and side midpoint :g:`c <0038.g1:M3>`), whence :math:`Lc = LP = \frac{1}{2}R`; and since the very same holds for the sides :math:`AC` [:g:`b <0038.g1:M2>`] and :math:`BC` [:g:`a <0038.g1:M1>`]:

  *In every triangle, the circle passing through the feet of its altitudes simultaneously meets the sides of the same at their midpoints.*

.. _fb-en-s57:

§ 57. FEUERBACH'S THEOREM — Fourfold Tangency of the Nine-Point Circle
----------------------------------------------------------------------

.. picture:: /_static/constructions/feuerbach_tangency.svg
   :alt: Feuerbach's Theorem (§ 57): Nine-point circle tangent internally to the incircle at X(11) and externally to the three excircles at F1, F2, F3

If one draws the straight line :math:`LS` [joining :g:`L = X_5 <0038.g2:X5>` and :g:`S = X_1 <0038.g2:X1>`], then by a known property of the median in triangle :math:`KOS` :just:`[II. 12–13] <II.12>`, because :math:`L` is the midpoint of :math:`KO`:

.. math::

   2\overline{LS}^2 + 2\overline{OL}^2 = \overline{KS}^2 + \overline{OS}^2.

Substituting herein the values of the squares of :math:`OL, KS, OS` known from §§ 54, 49, 51:

.. math::

   2\overline{LS}^2 + 2\left(\frac{1}{4}R^2 - \rho R\right) = \left(R^2 - 2rR\right) + \left(2r^2 - 2\rho R\right),

*[observe how :math:`-2\rho R` cancels identically on both sides!]* there results

.. math::

   \overline{LS}^2 = \frac{1}{4}R^2 - rR + r^2 = \left(\frac{1}{2}R - r\right)^2,
   \qquad \text{or:} \qquad
   LS = \frac{1}{2}R - r;

and when one sets :math:`a, b, c` negative successively herein [sending :math:`R \mapsto -R` and :math:`r \mapsto r^{(k)}` in an expression already completely free of :math:`\rho`!]:

.. math::

   LS' &= \frac{1}{2}R + r', \\
   LS'' &= \frac{1}{2}R + r'', \\
   LS''' &= \frac{1}{2}R + r'''.

Since now (§ 26) :math:`\tfrac{1}{2}R` is the radius of the circle circumscribed about :math:`\triangle MNP` itself, there follows by the well-known property of circles that touch one another :just:`[III. 11–12] <III.11>` the following theorem:

   **THEOREM (Feuerbach, 1822, § 57, p. 38):** *The circle which passes through the feet of the altitudes of a triangle touches all four circles touching the three sides of the same: namely, it touches the internally touching circle internally* [at the :term:`Feuerbach point <feuerbach-point>` :g:`X_{11} <0038.g2:X11>`], *whereas it touches each of the externally touching circles externally* [at :g:`F_a <0038.g2:F1>`, :g:`F_b <0038.g2:F2>`, :g:`F_c <0038.g2:F3>`].

.. picture:: /_static/constructions/feuerbach_incircle_zoom.svg
   :alt: Magnified view of the internal tangency between the incircle (center X1, radius r=4) and nine-point circle (center X5, radius R/2=65/16) at X(11)=(6,8)

.. toctree::
   :hidden:

   de
   summary
   notes
