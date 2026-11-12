:title: Feuerbach (1822) §§ 49–60 — The Nine-Point Circle & Feuerbach's Tangency Theorem
:layout: book

.. _fb-03-en:

===========================================================================================
Unit III: The Nine-Point Circle, Feuerbach's Theorem & The Euler Line (§§ 49–60, Complete)
===========================================================================================

.. rubric:: Karl Wilhelm Feuerbach — *Properties of Several Remarkable Points of the Rectilinear Triangle* (1822, pp. 33–41, Tab. II Fig. 7)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. picture:: /_static/constructions/nine_point_circle.svg
   :alt: Feuerbach's Nine-Point Circle centered at L = X(5) bisecting OK, passing through the three altitude feet, three side midpoints, and three Euler midpoints

.. _fb-en-s49:

.. folio:: § 49
   :page: 33–34

§ 49. Distances from the Circumcenter K to S, S', S'', S''' — Euler (1765) & Fuß (1797)
---------------------------------------------------------------------------------------

Denoting by :math:`K` [:g:`X_3 <0038.g1:X3>`] the center of the circumscribed circle of :math:`\triangle ABC`, the squared distance from :math:`K` to the incenter :math:`S` [:g:`X_1 <0038.g2:X1>`] is :math:`\overline{KS}^2 = R^2 - 2rR`, and substituting :math:`-a, -b, -c` successively for :math:`+a, +b, +c` yields on page 34:

.. math::

   \overline{KS'}^2 &= R^2 + 2r'R, \\
   \overline{KS''}^2 &= R^2 + 2r''R, \\
   \overline{KS'''}^2 &= R^2 + 2r'''R;

that is: *In every triangle, the square of the distance from the center of the circumscribed circle to the center of any one of its externally touching circles equals the square on the radius of the former circle, increased by twice the rectangle contained by that radius and the radius of the externally touching circle.*

The first proposition :math:`\overline{KS}^2 = R^2 - 2rR` is proved by :person:`L'Huilier <lhuilier>` in No. V of the :cite:`*Annales* cited above <lhuilier_1810>` in a very laborious and circuitous manner. **It originates with** :person:`Euler <euler>` **and is found in a memoir:** :cite:`*Solutio facilis problematum quorumdam geometricorum difficillimorum*, *Nov. Commentar. Petrop.* T. XI, p. A. 1765, § 18, VI <euler_1765>`. :person:`Fuß <fuss>` proves it purely geometrically and very simply (:cite:`*De quadrilateris, quibus circulum tam inscribere quam circumscribere licet*, *Nov. Act. Petrop.* T. X, Petrop. 1797, p. 103, § 32 <fuss_1797>`). **Euler determines in the aforementioned memoir for the rectilinear triangle the mutual position of the intersection point of its altitudes, its centroid, and the centers of the inscribed and circumscribed circles, out of the sides of the triangle. Because, however, he did not introduce the radius** :math:`\rho` **into the calculation, he could not arrive at similarly simple results and geometric theorems for the determination of the remaining distances, such as we shall develop here.**

.. _fb-en-s50:

§ 50. Sum of Squared Distances from K to the Four Tritangent Centers
--------------------------------------------------------------------

Adding the values found for the squares of :math:`KS, KS', KS'', KS'''`, since (§ 5) :math:`r' + r'' + r''' = r + 4R`, one obtains:

.. math::

   \overline{KS}^2 + \overline{KS'}^2 + \overline{KS''}^2 + \overline{KS'''}^2 = 12R^2;

that is: *In every triangle the center of the circumscribed circle is so situated that the sum of the squares of its distances from the centers of the four touching circles equals three times the square on the diameter of the circumscribed circle.*

.. _fb-en-s51:

.. folio:: § 51
   :page: 35

§ 51. Squared Distance from the Orthocenter O to S (and the Excenter Sign Slip)
-------------------------------------------------------------------------------

If :math:`O` [:g:`X_4 <0038.g1:X4>`] is as hitherto the intersection point of the altitudes :math:`AM, BN, CP` of triangle :math:`ABC`, and one draws :math:`OS`, then :math:`\overline{OS}^2 = (AF - AP)^2 + (OP - SF)^2`, where :math:`F` is the contact point of the incircle on :math:`AB`. Now since :math:`AF = \tfrac{1}{2}(-a+b+c)` and :math:`AP = \frac{-a^2+b^2+c^2}{2c}`, while (§ 35) :math:`OP = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2)}{8c\Delta}` and (§ 2) :math:`SF = \frac{2\Delta}{a+b+c}`, we have:

.. math::

   AF - AP &= \frac{(a - b + c)(a + b - c) - c(a + b - c)}{2c}, \\
   OP - SF &= \frac{(-a^2 + b^2 + c^2)(a^2 - b^2 + c^2) - c(-a + b + c)(a - b + c)(a + b - c)}{8c\Delta}.

Substituting into the expression for :math:`\overline{OS}^2`, one brings it at length into the symmetric form:

.. math::

   \overline{OS}^2 = \frac{(-a+b+c)^2(a-b+c)^2(a+b-c)^2 - (-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{32\Delta^2},

whence, introducing the circle radii :math:`r, \rho, R`, there results:

.. math::

   \overline{OS}^2 = 2r^2 - 2\rho R;

that is: *In every acute-angled triangle, the square of the distance from the intersection point of its altitudes to the center of the inscribed circle equals twice the square on the radius of this circle, diminished by the rectangle contained by the diameter of the circumscribed circle and the radius of the circle inscribed in the orthic triangle.*

Setting :math:`a, b, c` negative successively in this expression, Feuerbach writes for the distances from :math:`O` to :math:`S', S'', S'''`:

.. math::

   \overline{OS'}^2 = 2r'^2 + 2\rho R, \qquad
   \overline{OS''}^2 = 2r''^2 + 2\rho R, \qquad
   \overline{OS'''}^2 = 2r'''^2 + 2\rho R

*[Editor's Critical Note: Because both :math:`R` and :math:`\rho` negate simultaneously under :math:`a \mapsto -a`, their product :math:`\rho R` is invariant; the true exact identities over :math:`\mathbb{Q}(a,b,c)` are :math:`\overline{OS^{(k)}}^2 = 2r^{(k)2} - 2\rho R`. Crucially, this slip does not affect §§ 53–59 at all; see :ref:`Unit III Critical Notes <fb-03-notes>` for the complete SymPy proof.]*

.. _fb-en-s52:

.. folio:: §§ 52–53
   :page: 36

§§ 52–53. Sum of Orthocenter Quadrances & The Distance KO
---------------------------------------------------------

* **§ 52**: Adding the four expressions of § 51 via (§ 28) :math:`r^2 + r'^2 + r''^2 + r'''^2 = 4R(2R - \rho)`, Feuerbach states :math:`\overline{OS}^2 + \overline{OS'}^2 + \overline{OS''}^2 + \overline{OS'''}^2 = 4R(4R - \rho)` *[true exact sum with :math:`-2\rho R` on all four terms: :math:`16R(R - \rho)`]*.
* **§ 53 (Exact Quadrance KO²)**: Joining the points :math:`K` [:g:`X_3 <0038.g1:X3>`] and :math:`O` [:g:`X_4 <0038.g1:X4>`] by a straight line [:g:`OK <0038.g1:[ X3 X4 ]>`], its square is :math:`\overline{KO}^2 = (Ac - AP)^2 + (OP - Kc)^2`, where :math:`c` is the midpoint of :math:`AB`. Now :math:`Ac - AP = \frac{a^2 - b^2}{2c}` and (§§ 35, 45) :math:`OP - Kc = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2) - c^2(a^2+b^2-c^2)}{8c\Delta}`; substituting and reducing yields:

  .. math::

     \overline{KO}^2 = \frac{a^2b^2c^2 - (-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{16\Delta^2} = R^2 - 4\rho R;

  that is: *In every acute-angled triangle, the square of the distance of the intersection point of its altitudes from the center of the circumscribed circle equals the square on the radius of the latter circle, diminished by twice the rectangle contained by this same radius and the diameter of the circle inscribed in the orthic triangle.*

.. _fb-en-s54:

.. folio:: §§ 54–55
   :page: 37

§§ 54–56. The Nine-Point Center L = X(5), Collinearity O–L–K, and Side Midpoints
--------------------------------------------------------------------------------

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

.. _fb-en-s58:

.. folio:: §§ 58–60
   :page: 39

§§ 58–60. Linear & Quadratic Center Sums and the Centroid G on KO
-----------------------------------------------------------------

* **§ 58 (Sum of Center Distances from L)**: Summing :math:`LS, LS', LS'', LS'''` via (§ 5) :math:`r' + r'' + r''' - r = 4R`:

  .. math::

     LS + LS' + LS'' + LS''' = \left(\frac{1}{2}R - r\right) + \frac{3}{2}R + (r + 4R) = 6R,

  *three times the diameter of the circumscribed circle* (note: for an equilateral triangle :math:`R = 2r`, :math:`LS = 0`; whenever :math:`R \ge 2r` by Euler's inequality, :math:`|R/2 - r| = \frac{1}{2}R - r`).

* **§ 59 (Sum of Squared Center Distances from L — 100% Exact!)**: Squaring :math:`LS, LS', LS'', LS'''` and summing via (§§ 5, 28) :math:`r' + r'' + r''' - r = 4R` and :math:`r^2 + r'^2 + r''^2 + r'''^2 = 4R(2R - \rho)`:

  .. math::

     \overline{LS}^2 + \overline{LS'}^2 + \overline{LS''}^2 + \overline{LS'''}^2 = 13R^2 - 4\rho R = R(13R - 4\rho),

  whence by §§ 50, 53 (:math:`\overline{KO}^2 = 4\overline{KL}^2 = R^2 - 4\rho R` and :math:`\sum \overline{KS_i}^2 = 12R^2`):

  .. math::

     \overline{KO}^2 + \overline{KS}^2 + \overline{KS'}^2 + \overline{KS''}^2 + \overline{KS'''}^2
     = \overline{LS}^2 + \overline{LS'}^2 + \overline{LS''}^2 + \overline{LS'''}^2.

.. folio:: § 60
   :page: 40–41

* **§ 60 (The Centroid G on the Euler Line & Harmonic Division)**: Drawing the median :math:`Cc` cutting :math:`KO` at :math:`G` [:g:`X_2 <0038.g1:X2>`], since :math:`CO \parallel Kc` and (§ 45) :math:`OC = 2\,Kc`, similar triangles :just:`[VI. 4] <VI.4>` give :math:`GC = 2\,Gc` and :math:`GO = 2\,GK`, so :math:`G` is the centroid (*Schwerpunkt*) of :math:`\triangle ABC` (citing Carnot), dividing :math:`KO` at the first trisection point from :math:`K` [forming with :math:`L` the :term:`harmonic range <harmonic-range>` :math:`(O, G; L, K) = -1`]:

  .. math::

     GK = \frac{1}{3}KO, \quad GO = \frac{2}{3}KO, \quad GL = \frac{1}{6}KO, \\
     \overline{GK}^2 = \frac{1}{9}(R^2 - 4\rho R), \quad
     \overline{GO}^2 = \frac{4}{9}(R^2 - 4\rho R), \quad
     \overline{GL}^2 = \frac{1}{36}(R^2 - 4\rho R).

  Applying the cosine law in :math:`\triangle GKS` yields :math:`\overline{GS}^2 = \frac{1}{9}\left(6\overline{KS}^2 + 3\overline{OS}^2 - 2\overline{KO}^2\right)`, and substituting the exact values from §§ 49, 51, 53 gives the exact incenter-centroid quadrance:

  .. math::

     \overline{GS}^2 = \frac{2}{9}R(2R + \rho) - \frac{2}{3}r(2R - r).

  *[For the excenters, Feuerbach again flips the sign of :math:`R` without flipping :math:`\rho`, printing :math:`\overline{GS^{(k)}}^2 = \frac{2}{9}R(2R - \rho) + \frac{2}{3}r^{(k)}(2R + r^{(k)})`, :math:`\sum \overline{GS_i}^2 = \frac{28}{9}R(4R - \rho)`, and :math:`9\sum \overline{GS_i}^2 = 7\sum \overline{OS_i}^2`; the true exact identities proved in :mod:`geometor.feuerbach.euler` are :math:`\overline{GS^{(k)}}^2 = \frac{2}{9}R(2R + \rho) + \frac{2}{3}r^{(k)}(2R + r^{(k)})` and :math:`9\sum \overline{GS_i}^2 = 16R(7R - \rho)`.]*
