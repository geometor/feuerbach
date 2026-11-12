:title: Euler (1765) §§ 1–9 — The Four Classical Centers & Orthogonal Coordinates
:layout: book

.. _euler-01-en:

===============================================================================
Unit I: The Four Classical Triangle Centers & Orthogonal Coordinates (§§ 1–9)
===============================================================================

.. rubric:: Leonhard Euler — *An Easy Solution of Certain Very Difficult Geometric Problems* (1765/1767, pp. 103–107)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _euler-en-s1:

.. folio:: § 1
   :page: 103

§ 1. Enumeration of the Four Notable Points of Any Triangle
-----------------------------------------------------------

In every triangle there are chiefly four points that are accustomed to be considered in Geometry:

1. The intersection of the three perpendiculars dropped from the several vertices upon the opposite sides [:term:`orthocenter <euler-line>` :math:`E = X(4)`].
2. The intersection of the three straight lines drawn from the several vertices bisecting the opposite sides; which point is at the same time the center of gravity of the triangle [centroid :math:`F = X(2)`].
3. The intersection of the three straight lines bisecting the several angles, upon which point falls the center of the circle inscribed in the triangle :just:`[IV. 4] <IV.4>` [incenter :math:`G = X(1)`].
4. The intersection of the three straight lines normal to the several sides and bisecting them, at which point is found the center of the circle circumscribed about the triangle :just:`[IV. 5] <IV.5>` [circumcenter :math:`H = X(3)`].

.. _euler-en-s2:

§ 2. The Four Inverse Triangle-Determination Problems
-----------------------------------------------------

From these four points, if any three whatever are given in position, it is evident that the triangle is determined therefrom, unless perchance those points coalesce into one—which happens in the equilateral triangle, in which case all equilateral triangles equally satisfy the problem.

.. folio:: § 2 (cont.)
   :page: 104

Hence therefore four problems arise, according as each one of those four points is omitted for the determination of the triangle; and how these may be most conveniently resolved, I have undertaken to show here.

.. _euler-en-s3:

§ 3. Strategic Choice of Unknowns and Promise of Mutual Properties
------------------------------------------------------------------

That these problems, however, are most difficult to solve, anyone who attacks them will soon experience, since it can scarcely be perceived what sort of unknown quantities ought to be introduced into the calculation so as even to arrive at equations containing the solution. The whole business therefore reduces to a suitable choice of unknown quantities, wherein above all care must be taken lest we fall into most tedious and altogether inextricable calculations. Moreover, once all difficulties have been happily overcome, certain remarkable properties among those four points reveal themselves, the knowledge of which must be judged of no small importance in Geometry.

.. _euler-en-s4:

§ 4. Separation of the Four Diagrams (Tab. II, Fig. 1–4)
--------------------------------------------------------

Lest the figures be burdened by an excessive multitude of lines to be drawn in them, I exhibit the same triangle :math:`ABC` four times (`Tab. II, Fig. 1, 2, 3, 4`):

* In the first (`Fig. 1`), the straight lines :math:`AM`, :math:`BN`, and :math:`CP` [printed :math:`CN` in the 1767 folio] are normal to the opposite sides, and I denote their intersection by the letter :g:`E <0114.g1:X4>`, where the first point of those four which I have mentioned is situated.
* In the second figure (`Fig. 2`), the straight lines :math:`Aa`, :math:`Bb`, and :math:`Cc` bisect the opposite sides, whose intersection indicates the second point :g:`F <0114.g1:X2>` of those four mentioned points, and the center of gravity of the triangle.

.. folio:: § 4 (cont.)
   :page: 105

* In the third figure (`Fig. 3`), the straight lines :math:`A\alpha`, :math:`B\beta`, :math:`C\gamma` bisect the angles :math:`A, B, C`, and their intersection :g:`G <0114.g1:X1>` furnishes the third point mentioned above, namely the center of the inscribed circle.
* Finally, in the fourth figure (`Fig. 4`), from the midpoints :math:`S, T, V` of the several sides there are erected perpendiculars :math:`SH, TH`, and :math:`VH`, exhibiting by their intersection :g:`H <0114.g1:X3>` the center of the circumscribed circle.

.. _euler-en-s5:

§ 5. Base Coordinates and Heron's Area Formula
----------------------------------------------

So that I may define the position of these four points more easily and subsequently compare them with one another, from each of them upon the side :math:`AB` assumed as base I drop the perpendiculars :math:`EP`, :math:`FQ`, :math:`GR`, and :math:`HS`—of which indeed the first and the fourth already occur in the construction itself. Next I call the three sides of the triangle:

.. math::

   AB = c, \qquad AC = b, \qquad \text{and} \qquad BC = a.

Furthermore, it is also fitting to bring the area of the triangle into the reckoning; let it be :math:`= \mathcal{A}`, and as is well known we shall have:

.. math::

   \mathcal{A}^2 = \frac{1}{16}(a + b + c)(a + b - c)(b + c - a)(c + a - b)

or

.. math::

   \mathcal{A}^2 = \frac{1}{16}\left(2a^2b^2 + 2a^2c^2 + 2b^2c^2 - a^4 - b^4 - c^4\right).

Hence therefore I investigate separately the position of each of these four points with respect to the base :math:`AB` in the following manner (`Tab. II, Fig. 1`).

.. _euler-en-s6:

§ 6. I. For the Intersection of the Perpendiculars E
----------------------------------------------------

First, from the *Elements* :just:`[II. 12, 13] <II.12, II.13>` it is established that:

.. math::

   AP = \frac{c^2 + b^2 - a^2}{2c}, \qquad \text{and in like manner} \qquad BM = \frac{a^2 + c^2 - b^2}{2a}.

Next, since :math:`\tfrac{1}{2} AM \cdot BC = \mathcal{A}`, we shall have :math:`AM = \frac{2\mathcal{A}}{a}`,

.. folio:: § 6 (cont.)
   :page: 106

whence the similarity of triangles :math:`ABM` and :math:`AEP` :just:`[VI. 4] <VI.4>` furnishes

.. math::

   AM : BM = AP : EP

and hence we obtain

.. math::

   EP = \frac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}}.

Wherefore the position of point :math:`E` with respect to the base :math:`AB` is so defined that:

.. math::

   AP = \frac{c^2 + b^2 - a^2}{2c} \qquad \text{and} \qquad PE = \frac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}}.

.. _euler-en-s7:

§ 7. II. For the Center of Gravity F
------------------------------------

Having dropped from angle :math:`C` upon the base :math:`AB` the perpendicular :math:`CP` (`Tab. II, Fig. 2`), we have as before :math:`AP = \frac{c^2 + b^2 - a^2}{2c}` and :math:`CP = \frac{2\mathcal{A}}{c}`. Now from the elements of statics and geometry it is established that :math:`FQ = \tfrac{1}{3}CP = \frac{2\mathcal{A}}{3c}` and :math:`cQ = \tfrac{1}{3}cP` [where :math:`c` denotes the midpoint of base :math:`AB`]. Since however :math:`Ac = \tfrac{1}{2}c`, we shall have :math:`cP = \frac{b^2 - a^2}{2c}`, and therefore :math:`cQ = \frac{b^2 - a^2}{6c}` [printed :math:`bc` in the 1767 folio], and consequently :math:`AQ = \frac{3c^2 + b^2 - a^2}{6c}`. On account of which the position of point :math:`F` with respect to the base :math:`AB` is so defined that:

.. math::

   AQ = \frac{3c^2 + b^2 - a^2}{6c} \qquad \text{and} \qquad QF = \frac{2\mathcal{A}}{3c}.

.. _euler-en-s8:

§ 8. III. For the Center of the Inscribed Circle G
--------------------------------------------------

Since :math:`GR` (`Fig. 3`) is the radius of the inscribed circle, :math:`\tfrac{1}{2}GR(a + b + c)` will be the area of the triangle :math:`= \mathcal{A}`, whence :math:`GR = \frac{2\mathcal{A}}{a + b + c}`. Next, setting the segment :math:`AR = x`, if an equal portion is cut off from :math:`AC` starting from :math:`A`, one will obtain there the point of tangency :just:`[III. 17] <III.17>`, from which accordingly the point :math:`C` stands at the interval :math:`= b - x`. Furthermore, since :math:`BR = c - x`, if from side :math:`BC` starting from :math:`B` [printed :math:`A` in the 1767 folio] an equal interval :math:`c - x` is cut off,

.. folio:: § 8 (cont.)
   :page: 107

that side will there be touched by the circle, whence point :math:`C` will stand from that point at the interval :math:`= a - c + x`; since by the nature of the circle this is equal to the former :math:`b - x`, we shall have :math:`x = \frac{c + b - a}{2}`. Wherefore this point :math:`G` with respect to the base :math:`AB` is so defined that:

.. math::

   AR = \frac{c + b - a}{2} \qquad \text{and} \qquad RG = \frac{2\mathcal{A}}{a + b + c}.

.. _euler-en-s9:

§ 9. IV. For the Center of the Circumscribed Circle H
-----------------------------------------------------

Here indeed (`Tab. II, Fig. 4`) we have immediately from the construction :math:`AS = \tfrac{1}{2}c`. Next, having drawn from :math:`A` upon :math:`BC` the perpendicular :math:`AM`, we shall have :math:`AM = \frac{2\mathcal{A}}{a}` and :math:`CM = \frac{a^2 + b^2 - c^2}{2a}`. Having joined the straight line :math:`AH`, however, from the nature of the circle :just:`[III. 20] <III.20>` it is clear that angle :math:`AHS` will be equal to angle :math:`ACB`, and therefore triangle :math:`AHS` will be similar to triangle :math:`ACM` :just:`[VI. 4] <VI.4>`, whence we obtain:

.. math::

   AM : CM = AS : HS

and thus we collect :math:`HS = \frac{c(a^2 + b^2 - c^2)}{8\mathcal{A}}`. Wherefore the position of point :math:`H` with respect to the base :math:`AB` is so defined that:

.. math::

   AS = \frac{1}{2}c \qquad \text{and} \qquad SH = \frac{c(a^2 + b^2 - c^2)}{8\mathcal{A}}.
