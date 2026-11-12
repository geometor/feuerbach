:title: Euler (1765) §§ 10–18 — Symmetric Polynomials, Six Quadrances & The Euler Line
:layout: book

.. _euler-02-en:

=====================================================================================
Unit II: Symmetric Polynomials, Six Mutual Quadrances & The Euler Line (§§ 10–18)
=====================================================================================

.. rubric:: Leonhard Euler — *An Easy Solution of Certain Very Difficult Geometric Problems* (1765/1767, pp. 107–114)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. picture:: /_static/constructions/euler_1765_centers.svg
   :alt: Euler's four centers E=X(4), F=X(2), G=X(1), H=X(3), circumcircle, incircle, and Euler line on the (15, 13, 14) triangle

.. _euler-en-s10:

.. folio:: § 10
   :page: 107

§ 10. Expression of the Six Squared Inter-Center Distances
----------------------------------------------------------

Hence we shall now be able to define the distances among these four points, if indeed they are represented in the same figure; for by the Pythagorean theorem :just:`[I. 47] <I.47>` we shall have:

.. math::

   EF^2 &= (AP - AQ)^2 + (PE - QF)^2 \\
   EG^2 &= (AP - AR)^2 + (PE - RG)^2 \\
   EH^2 &= (AP - AS)^2 + (PE - SH)^2

.. folio:: § 10 (cont.)
   :page: 108

.. math::

   FG^2 &= (AQ - AR)^2 + (QF - RG)^2 \\
   FH^2 &= (AQ - AS)^2 + (QF - SH)^2 \\
   GH^2 &= (AR - AS)^2 + (RG - SH)^2.

Now these intervals ought to be gathered for this reason: that if any three of these four points are proposed as given, nothing else besides their mutual distances is assumed as known, whence thereafter the sides of the triangle are to be investigated.

.. _euler-en-s11:

§ 11. Symmetric Polynomials of the Three Sides and Heron's Identity
-------------------------------------------------------------------

Here, however, it must above all be observed that those distances among our four points must necessarily be so expressed that the three sides of the triangle enter equally into the expressions, since no prerogative whatever can be granted to any one side over the rest with respect to these distances. On account of which, intending to contemplate the sides of the triangle without any distinction, I set:

.. math::

   a + b + c = p; \qquad ab + ac + bc = q \qquad \text{and} \qquad abc = r,

so that in place of the sides I am now going to introduce into the calculation those three quantities :math:`p, q`, and :math:`r` equally related to each side [:term:`elementary symmetric polynomials <symmetric-polynomials>`]. Hence, since we have:

.. math::

   a^2 + b^2 + c^2 &= p^2 - 2q, \\
   a^2b^2 + a^2c^2 + b^2c^2 &= q^2 - 2pr, \\
   a^4 + b^4 + c^4 &= p^4 - 4p^2q + 2q^2 + 4pr,

the area :math:`\mathcal{A}` is so expressed that:

.. math::

   \mathcal{A}^2 = \frac{1}{16}p\left(-p^3 + 4pq - 8r\right) = \frac{-p^4 + 4p^2q - 8pr}{16}.

Having noted this, I am going to reduce each of the six distances above separately to these new quantities.

.. _euler-en-s12:

.. folio:: § 12
   :page: 109

§ 12. I. Investigation of the Distance of Points E and F
--------------------------------------------------------

Here first we have [between :g:`E <0114.g1:X4>` and :g:`F <0114.g1:X2>`]:

.. math::

   AP - AQ &= \frac{c^2 + b^2 - a^2}{2c} - \frac{3c^2 + b^2 - a^2}{6c} = \frac{b^2 - a^2}{3c}, \\
   PE - QF &= \frac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}} - \frac{2\mathcal{A}}{3c} \\
           &= \frac{3(c^2 + b^2 - a^2)(a^2 + c^2 - b^2) - 16\mathcal{A}^2}{24c\mathcal{A}},

which expressions, reduced to a common denominator, become:

.. math::

   AP - AQ &= \frac{(b^2 - a^2)\sqrt{2a^2b^2 + 2a^2c^2 + 2b^2c^2 - a^4 - b^4 - c^4}}{12c\mathcal{A}}, \\
   PE - QF &= \frac{2c^4 - a^4 - b^4 + 2a^2b^2 - b^2c^2 - a^2c^2}{12c\mathcal{A}},

whose squares added together furnish [correcting the folio's interim ``16`` to ``36``]:

.. math::

   EF^2 = \frac{1}{36\mathcal{A}^2}\left(a^6 + b^6 + c^6 - a^4b^2 - a^2b^4 - a^4c^2 - a^2c^4 - b^4c^2 - b^2c^4 + 3a^2b^2c^2\right),

wherein indeed the letters :math:`a, b, c` enter symmetrically. Now we have:

.. math::

   \sum_{\text{sym}} a^4b^2 &= p^2q^2 - 2q^3 - 2p^3r + 4pqr - 3r^2, \\
   a^6 + b^6 + c^6 &= p^6 - 6p^4q + 9p^2q^2 - 2q^3 + 6p^3r - 12pqr + 3r^2,

from which we obtain:

.. math::

   EF^2 = \frac{1}{36\mathcal{A}^2}\left(p^6 - 6p^4q + 8p^2q^2 + 8p^3r - 16pqr + 9r^2\right),

which expression may be reduced [using :math:`16\mathcal{A}^2 = -p^4 + 4p^2q - 8pr`, correcting the folio's ``=`` to ``-``] to this form:

.. math::

   EF^2 = \frac{r^2}{4\mathcal{A}^2} - \frac{4}{9}(p^2 - 2q).

.. _euler-en-s13:

.. folio:: § 13
   :page: 110

§ 13. II. Investigation of the Distance of Points E and G
---------------------------------------------------------

Here we have [ along segment :g:`EG <0114.g1:/ X4 X1 />` ]:

.. math::

   AP - AR &= \frac{c^2 + b^2 - a^2}{2c} - \frac{c - b + a}{2} = \frac{b^2 - bc - a^2 + ac}{2c}, \\
   PE - RG &= \frac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}} - \frac{2\mathcal{A}}{a + b + c} \\
           &= \frac{c^4 - a^4 - b^4 + 2a^2b^2}{8c\mathcal{A}} + \frac{p^3 - 4pq + 8r}{8\mathcal{A}},

and upon reducing to a common denominator:

.. math::

   AP - AR &= \frac{(b^2 - bc - a^2 + ac)\sqrt{2a^2b^2 + 2a^2c^2 + 2b^2c^2 - a^4 - b^4 - c^4}}{8c\mathcal{A}}, \\
   PE - RG &= \frac{2c^4 - (a + b)c^3 - (a - b)^2 c^2 + (a + b)(a - b)^2 c - (a^2 - b^2)^2}{8c\mathcal{A}},

the sum of whose squares, divided by :math:`4c^2`, returns to the symmetric degree-6 form:

.. math::

   EG^2 = \frac{1}{16\mathcal{A}^2}\left(\sum a^6 - \sum_{\text{sym}} a^5b - \sum_{\text{sym}} a^4b^2 + 3\sum_{\text{cyc}} a^4bc - 2\sum_{\text{sym}} a^3b^2c + 2\sum_{\text{cyc}} a^3b^3 + 6a^2b^2c^2\right).

Before reducing this expression to the letters :math:`p, q`, and :math:`r`, I observe that adding :math:`a^2 + b^2 + c^2 - ab - ac - bc` simplifies the numerator dramatically:

.. math::

   EG^2 + a^2 + b^2 + c^2 - ab - ac - bc
   &= \frac{abc}{4\mathcal{A}^2}\left(a^3 + b^3 + c^3 - a^2b - ab^2 - a^2c - ac^2 - b^2c - bc^2 + 3abc\right) \\
   &= \frac{abc(a^2 + b^2 + c^2 - 2ab - 2ac - 2bc)(a + b + c)}{4\mathcal{A}^2} + \frac{9a^2b^2c^2}{4\mathcal{A}^2}.

.. folio:: § 13 (cont.)
   :page: 111

Now since :math:`a^2 + b^2 + c^2 = p^2 - 2q`, the reduction is easy, inasmuch as there comes forth:

.. math::

   EG^2 + p^2 - 3q = \frac{pr(p^2 - 4q) + 9r^2}{4\mathcal{A}^2},

and thus this distance is so defined that:

.. math::

   EG^2 = \frac{r(p^3 - 4pq + 9r)}{4\mathcal{A}^2} - p^2 + 3q = \frac{r^2}{4\mathcal{A}^2} - \frac{4r}{p} - p^2 + 3q.

.. _euler-en-s14:

§ 14. III. Investigation of the Distance of Points E and H
----------------------------------------------------------

Since here [between :g:`E <0114.g1:X4>` and :g:`H <0114.g1:X3>`] we have:

.. math::

   AP - AS &= \frac{c^2 + b^2 - a^2}{2c} - \frac{1}{2}c = \frac{b^2 - a^2}{2c}, \\
   PE - SH &= \frac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}} - \frac{c(a^2 + b^2 - c^2)}{8\mathcal{A}}
           = \frac{2c^4 - (a^2 + b^2)c^2 - (a^2 - b^2)^2}{8c\mathcal{A}},

adding the squares and dividing through by :math:`4c^2`, there is obtained:

.. math::

   EH^2 = \frac{1}{16\mathcal{A}^2}\left(a^6 + b^6 + c^6 - a^4b^2 - a^2b^4 - a^4c^2 - a^2c^4 - b^4c^2 - b^2c^4 + 3a^2b^2c^2\right),

which on account of :math:`16\mathcal{A}^2 = -a^4 - b^4 - c^4 + 2a^2b^2 + 2a^2c^2 + 2b^2c^2` reduces to this form:

.. math::

   EH^2 = \frac{9a^2b^2c^2}{16\mathcal{A}^2} - a^2 - b^2 - c^2,

wherein substitution is easily accomplished, for there results:

.. math::

   EH^2 = \frac{9r^2}{16\mathcal{A}^2} - p^2 + 2q.

.. _euler-en-s15:

.. folio:: § 15
   :page: 112

§ 15. IV. Investigation of the Distance of Points F and G
---------------------------------------------------------

From the formulas found above we have here [along segment :g:`FG <0114.g1:/ X2 X1 />`]:

.. math::

   AQ - AR &= \frac{3c^2 + b^2 - a^2}{6c} - \frac{c - b + a}{2} = \frac{3(a - b)c - a^2 + b^2}{6c}, \\
   QF - RG &= \frac{2\mathcal{A}}{3c} - \frac{2\mathcal{A}}{a + b + c} = \frac{2\mathcal{A}(a + b - 2c)}{3c(a + b + c)},

the sum of whose squares reduces to this purely rational symmetric form (entirely free of :math:`\mathcal{A}^2`!):

.. math::

   FG^2 = \frac{1}{9(a + b + c)^2}\left(-(a^4 + b^4 + c^4) + \sum_{\text{sym}} a^3b + 4(a^2b^2 + a^2c^2 + b^2c^2) - 5abc(a + b + c)\right).

Since now we have :math:`\sum_{\text{sym}} a^3b = p^2q - 2q^2 - pr` and :math:`abc(a + b + c) = pr`, the expression found puts on this form:

.. math::

   FG^2 = \frac{1}{9p^2}\left(-p^4 + 5p^2q - 18pr\right) = \frac{-p^3 + 5pq - 18r}{9p}.

.. _euler-en-s16:

§ 16. V. Investigation of the Distance of Points F and H (Vectorial Euler Line Proof)
-------------------------------------------------------------------------------------

For this case [between :g:`F <0114.g1:X2>` and :g:`H <0114.g1:X3>`] we have:

.. math::

   AQ - AS &= \frac{3c^2 + b^2 - a^2}{6c} - \frac{1}{2}c = \frac{b^2 - a^2}{6c}, \\
   QF - SH &= \frac{2\mathcal{A}}{3c} - \frac{c(a^2 + b^2 - c^2)}{8\mathcal{A}} = \frac{2c^4 - (a^2 + b^2)c^2 - (a^2 - b^2)^2}{24c\mathcal{A}}.

.. folio:: § 16 (cont.)
   :page: 113

Now if we compare these formulas with the first case (§ 12), we discover that:

.. math::

   AQ - AS = \frac{1}{2}(AP - AQ) \qquad \text{and} \qquad QF - SH = \frac{1}{2}(PE - QF),

whence it is manifest that :math:`FH = \tfrac{1}{2}EF`, and therefore:

.. math::

   FH^2 = \frac{r^2}{16\mathcal{A}^2} - \frac{1}{9}(p^2 - 2q).

.. _euler-en-s17:

§ 17. VI. Investigation of the Distance of Points G and H (Euler's Incenter–Circumcenter Theorem)
-------------------------------------------------------------------------------------------------

For this last case [along segment :g:`GH <0114.g1:/ X3 X1 />`] we have:

.. math::

   AR - AS &= \frac{c + b - a}{2} - \frac{1}{2}c = \frac{b - a}{2}, \\
   RG - SH &= \frac{2\mathcal{A}}{a + b + c} - \frac{c(a^2 + b^2 - c^2)}{8\mathcal{A}}
           = \frac{(a + b)c^3 + (a^2 + b^2)c^2 - (a + b)(a^2 + b^2)c - (a^2 - b^2)^2}{8(a + b + c)\mathcal{A}},

and if the squares of these two formulas are added together, and reduced by :math:`a + b + c`, there results:

.. math::

   GH^2 = \frac{abc}{16(a + b + c)\mathcal{A}^2}\left(a^4 + b^4 + c^4 + abc(a + b + c) - 2a^2b^2 - 2a^2c^2 - 2b^2c^2\right),

whence upon performing the substitution we collect:

.. math::

   GH^2 = \frac{r}{16p\mathcal{A}^2}\left(p^4 - 4p^2q + 9pr\right) = \frac{r(p^3 - 4pq + 9r)}{16\mathcal{A}^2}, \qquad \text{or} \qquad GH^2 = \frac{r^2}{16\mathcal{A}^2} - \frac{r}{p}.

.. _euler-en-s18:

.. folio:: § 18
   :page: 114

§ 18. Synopsis of the Six Quadrances, Discovery of the Euler Line & Stewart's Law
---------------------------------------------------------------------------------

Behold therefore under a single view the squares of these six intervals:

.. math::

   \text{I.} \quad EF^2 &= \frac{r^2}{4\mathcal{A}^2} - \frac{4}{9}(p^2 - 2q) \\
   \text{II.} \quad EG^2 &= \frac{r^2}{4\mathcal{A}^2} - p^2 + 3q - \frac{4r}{p} \\
   \text{III.} \quad EH^2 &= \frac{9r^2}{16\mathcal{A}^2} - p^2 + 2q \\
   \text{IV.} \quad FG^2 &= -\frac{1}{9}p^2 + \frac{5}{9}q - \frac{2r}{p} \\
   \text{V.} \quad FH^2 &= \frac{r^2}{16\mathcal{A}^2} - \frac{1}{9}(p^2 - 2q) \\
   \text{VI.} \quad GH^2 &= \frac{r^2}{16\mathcal{A}^2} - \frac{r}{p},

wherein (`Tab. II, Fig. 5`) it is evident that :math:`EH = \tfrac{3}{2}EF` and :math:`FH = \tfrac{1}{2}EF`, and thus the point :g:`H <0114.g1:X3>` is determined of its own accord by the points :g:`E <0114.g1:X4>` and :g:`F <0114.g1:X2>`: namely, if the three points :math:`E, F, G` form a triangle :math:`EFG`, then the fourth point :math:`H` will be so situated on the straight line :g:`EF <0114.g1:[ X3 X4 ]>` produced that :math:`FH = \tfrac{1}{2}EF`, and therefore :math:`EH = \tfrac{3}{2}EF` [:term:`Euler Line <euler-line>`]. Moreover, from this there is deduced:

.. math::

   4GH^2 + 2EG^2 = 3EF^2 + 6FG^2,

which agrees most admirably with the values found above.
