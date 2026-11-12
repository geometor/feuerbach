:title: Euler (1765) §§ 19–24 — Inverse Reconstruction Problem & Side-Length Cubic
:layout: book

.. _euler-03-en:

===============================================================================
Unit III: The Inverse Reconstruction Problem & Side-Length Cubic (§§ 19–24)
===============================================================================

.. rubric:: Leonhard Euler — *An Easy Solution of Certain Very Difficult Geometric Problems* (1765/1767, pp. 114–118)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _euler-en-s19:

.. folio:: § 19
   :page: 114

§ 19. Dimension-2 Auxiliary Invariants P, Q, R
----------------------------------------------

So that we may now recall these formulas to greater simplicity, let us set :math:`4pq - p^3 - 8r = 4s`, so that :math:`4\mathcal{A}^2 = ps` and :math:`4q = p^2 + \frac{8r}{p} + \frac{4s}{p}`; next let us make:

.. math::

   \frac{r^2}{ps} = R, \qquad \frac{r}{p} = Q, \qquad \text{and} \qquad p^2 = P,

so that :math:`P, Q, R` are quantities involving two dimensions [of length]. Since therefore from this we have :math:`\frac{s}{p} = \frac{Q^2}{R}` [printed :math:`\frac{-s}{p}` in the folio], we shall obtain:

.. math::

   p = \sqrt{P}, \qquad q = \frac{1}{4}P + 2Q + \frac{Q^2}{R}, \qquad \text{and} \qquad r = Q\sqrt{P},

.. folio:: § 19 (cont.)
   :page: 115

and :math:`4\mathcal{A}^2 = \frac{PQ^2}{R}`, and our six intervals will be so expressed:

.. math::

   \text{I.} \quad EF^2 &= R - \frac{2}{9}P + \frac{16}{9}Q + \frac{8Q^2}{9R} \\
   \text{II.} \quad EG^2 &= R - \frac{1}{4}P + 2Q + \frac{3Q^2}{R} \\
   \text{III.} \quad EH^2 &= \frac{9}{4}R - \frac{1}{2}P + 4Q + \frac{2Q^2}{R} \\
   \text{IV.} \quad FG^2 &= +\frac{1}{36}P - \frac{8}{9}Q + \frac{5Q^2}{9R} \\
   \text{V.} \quad FH^2 &= \frac{1}{4}R - \frac{1}{18}P + \frac{4}{9}Q + \frac{2Q^2}{9R} \\
   \text{VI.} \quad GH^2 &= \frac{1}{4}R - Q.

.. _euler-en-s20:

§ 20. Statement of the Unified Inverse Problem
----------------------------------------------

Since therefore any three of these four points—provided one does not take the collinear triad :math:`E, F`, and :math:`H`—already contain the determination of the fourth, a single problem results, which runs as follows.

**Problem** (`Tab. II, Fig. 5`). *Given in position these four points assignable in any triangle—1° the intersection of the perpendiculars drawn from the several angles upon the opposite sides* :math:`E`, *2° the center of gravity* :math:`F`, *3° the center of the inscribed circle* :math:`G`, *and 4° the center of the circumscribed circle* :math:`H`—*to construct the triangle.*

Which problem we shall be able to resolve concisely enough from the properties of these points elicited thus far.

.. _euler-en-s21:

§ 21. Rational Resolution for R, Q, and P
-----------------------------------------

**Solution.** Since the position of these four points is given through their mutual distances, let us call:

.. folio:: § 21 (cont.)
   :page: 116

.. math::

   GH = f, \qquad FH = g, \qquad \text{and} \qquad FG = h,

and we know that :math:`EF = 2g` and :math:`EH = 3g`, and likewise :math:`EG = \sqrt{6g^2 + 3h^2 - 2f^2}`. Now therefore we immediately have these three equations:

.. math::

   \text{I.} \quad f^2 &= \frac{1}{4}R - Q \\
   \text{II.} \quad g^2 &= \frac{1}{4}R - \frac{1}{18}P + \frac{4}{9}Q + \frac{2Q^2}{9R} \\
   \text{III.} \quad h^2 &= \frac{1}{36}P - \frac{8}{9}Q + \frac{5Q^2}{9R} \quad [\text{printed } \frac{6Q^2}{9R} \text{ in folio}],

from whose resolution we collect:

.. math::

   R &= \frac{4f^4}{3g^2 + 6h^2 - 2f^2}, \qquad
   Q = \frac{3f^2(f^2 - g^2 - 2h^2)}{3g^2 + 6h^2 - 2f^2}, \\
   P &= \frac{27f^4}{3g^2 + 6h^2 - 2f^2} - 12f^2 - 15g^2 + 6h^2,

whence we obtain:

.. math::

   \frac{Q^2}{R} = \frac{9(f^2 - g^2 - 2h^2)^2}{4(3g^2 + 6h^2 - 2f^2)}.

.. _euler-en-s22:

§ 22. Formation of the Side-Length Cubic Equation
-------------------------------------------------

Having found these values, let the three following expressions be computed:

.. math::

   p = \sqrt{P}, \qquad q = \frac{1}{4}P + 2Q + \frac{Q^2}{R}, \qquad \text{and} \qquad r = Q\sqrt{P},

and therefrom let this cubic equation be formed:

.. math::

   z^3 - pz^2 + qz - r = 0,

whose three roots will give the three sides of the sought triangle, whereby its construction is most easily obtained.

.. _euler-en-s23:

§ 23. Worked Numerical Example: The (5, 6, 7) Triangle
------------------------------------------------------

**Example.** Taking the sides of the triangle :math:`a = 5`, :math:`b = 6`, and :math:`c = 7`, so that the area is :math:`\mathcal{A} = 6\sqrt{6}`, therefrom are collected the squared distances of the four points:

.. folio:: § 23 (cont.)
   :page: 117

.. math::

   EF^2 = \frac{155}{72}; \quad EG^2 = \frac{11}{8}; \quad EH^2 = \frac{155}{32}; \quad FG^2 = \frac{1}{9}; \quad FH^2 = \frac{155}{288}; \quad GH^2 = \frac{35}{32},

whence the position of these points comes forth such as is represented in `Tab. II, Fig. 6`. Since therefore we have:

.. math::

   f^2 = \frac{35}{32}, \qquad g^2 = \frac{155}{288}, \qquad \text{and} \qquad h^2 = \frac{1}{9},

let us see whether the solution found leads back to the assumed triangle.

.. _euler-en-s24:

§ 24. Verification of the Reconstructed Cubic
---------------------------------------------

Now from these we obtain :math:`3g^2 + 6h^2 - 2f^2 = \frac{3}{32}`, and further :math:`f^2 - g^2 - 2h^2 = \frac{1}{3}` and :math:`4f^2 + 5g^2 - 2h^2 = \frac{219}{32}`; hence there is collected:

.. math::

   R = \frac{1225}{24}, \qquad Q = \frac{35}{3}, \qquad P = 324, \qquad \text{and} \qquad \frac{Q^2}{R} = \frac{24}{9} = \frac{8}{3},

whence we obtain:

.. math::

   p = \sqrt{P} = 18, \qquad q = 107, \qquad \text{and} \qquad r = \frac{35}{3} \cdot 18 = 5 \cdot 6 \cdot 7 = 210,

and hence this cubic equation arises:

.. math::

   z^3 - 18z^2 + 107z - 210 = 0,

whose three roots are manifestly :math:`5, 6, 7`, which are the very three sides of the satisfying triangle.
