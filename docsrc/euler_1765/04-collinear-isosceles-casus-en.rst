:title: Euler (1765) §§ 25–34 — Collinear Centers, Isosceles Degeneracy & Casus Irreducibilis
:layout: book

.. _euler-04-en:

===========================================================================================
Unit IV: Collinear Centers, Isosceles Degeneracy & Casus Irreducibilis (§§ 25–34)
===========================================================================================

.. rubric:: Leonhard Euler — *An Easy Solution of Certain Very Difficult Geometric Problems* (1765/1767, pp. 117–123)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _euler-en-s25:

.. folio:: § 25
   :page: 117

§ 25. Case Where All Four Points Lie in a Straight Line
-------------------------------------------------------

*Case in which the four points are situated in a straight line* (`Tab. II, Fig. 7`). In this case therefore, since we have:

.. math::

   FH = g; \quad FG = h; \quad GH = f; \quad EF = 2g; \quad EH = 3g \quad \text{and} \quad EG = 2g - h,

.. folio:: § 25 (cont.)
   :page: 118

we shall have :math:`g = f - h`, whence upon making this substitution we collect:

.. math::

   R = \frac{4f^4}{(3h - f)^2}; \qquad Q = \frac{3f^2 h(2f - 3h)}{(f - 3h)^2}; \qquad P = \frac{3h(4f - 3h)^3}{(f - 3h)^2},

and therefore :math:`\frac{Q^2}{R} = \frac{9h^2(2f - 3h)^2}{4(f - 3h)^2}`. From these we further elicit:

.. math::

   p &= \frac{(4f - 3h)\sqrt{3h(4f - 3h)}}{f - 3h}, \\
   q &= \frac{3fh(4f - 3h)(5f - 6h)}{(f - 3h)^2}, \\
   r &= \frac{3f^2 h(2f - 3h)(4f - 3h)\sqrt{3h(4f - 3h)}}{(f - 3h)^3}.

.. _euler-en-s26:

§ 26. Double Root of the Cubic and Isosceles Necessity
------------------------------------------------------

Since now the roots of this cubic equation :math:`z^3 - pz^2 + qz - r = 0` furnish the three sides :math:`a, b, c` of the sought triangle, in order to render it neater let us set

.. math::

   z = \frac{y\sqrt{3h(4f - 3h)}}{f - 3h},

and this equation will come forth:

.. math::

   y^3 - (4f - 3h)y^2 + f(5f - 6h)y - f^2(2f - 3h) = 0,

whose roots are manifestly :math:`f, f`, and :math:`2f - 3h`. Wherefore the sides of the sought triangle, which becomes **isosceles**, will be:

.. math::

   a = b = \frac{f\sqrt{3h(4f - 3h)}}{f - 3h}; \qquad \text{and} \qquad c = \frac{(2f - 3h)\sqrt{3h(4f - 3h)}}{f - 3h}.

.. _euler-en-s27:

§ 27. Direct Verification on an Isosceles Triangle
--------------------------------------------------

Now this case is also easy to solve in itself, since that straight line on which the given points lie necessarily cuts the triangle

.. folio:: § 27 (cont.)
   :page: 119

into two similar halves, and therefore the triangle becomes isosceles. Indeed, setting :math:`b = a` right from the start, we obtain :math:`\mathcal{A} = \tfrac{1}{4}c\sqrt{4a^2 - c^2}` and :math:`AP = AQ = AR = AS = \tfrac{1}{2}c`, and further:

.. math::

   PE = \frac{c^3}{4\mathcal{A}}; \qquad QF = \frac{2\mathcal{A}}{3c}; \qquad RG = \frac{2\mathcal{A}}{2a + c}; \qquad SH = \frac{c(2a^2 - c^2)}{8\mathcal{A}},

whence, because the feet :math:`P, Q, R, S` coincide at the midpoint of the base—let it be :math:`O`—the intervals among these points will be:

.. math::

   OF - OE &= \frac{2(a^2 - c^2)}{3\sqrt{4a^2 - c^2}}; \qquad
   OG - OE = \frac{c(a - c)}{\sqrt{4a^2 - c^2}}; \qquad
   OH - OE = \frac{a^2 - c^2}{\sqrt{4a^2 - c^2}}; \\
   OF - OG &= \frac{(a - c)(2a - c)}{3\sqrt{4a^2 - c^2}}; \qquad
   OH - OF = \frac{a^2 - c^2}{3\sqrt{4a^2 - c^2}}; \qquad
   OH - OG = \frac{a(a - c)}{\sqrt{4a^2 - c^2}}.

.. _euler-en-s28:

§ 28. Ordering of the Collinear Points When a > c vs. a < c
-----------------------------------------------------------

Here it is fitting to contemplate two cases according as :math:`a > c` or :math:`a < c`, for if :math:`a = c`, i.e. an equilateral triangle, all four points coalesce into one:

* **I. If** :math:`a > c`: the points will be arranged as `Tab. II, Fig. 8` shows, where :math:`HF = \tfrac{1}{3}EH` or :math:`EF = \tfrac{2}{3}EH` and :math:`EG < \tfrac{1}{2}EH`; and in this case the midpoint :math:`O` of the base falls on the straight line :math:`HE` produced beyond :math:`E`, so that :math:`OE = \frac{c^2}{2\sqrt{4a^2 - c^2}}`.
* **II. If** :math:`a < c`: the points will be arranged as `Fig. 9` shows, where again :math:`HF = \tfrac{1}{3}EH` or :math:`EF = \tfrac{2}{3}EH`, whereas :math:`EG > \tfrac{1}{2}EH`. In this case, however, the midpoint :math:`O` of the base falls on the straight line :math:`EH` produced beyond :math:`H`, so that

.. folio:: § 28 (cont.)
   :page: 120

.. math::

   HO = \frac{2a^2 - c^2}{2\sqrt{4a^2 - c^2}},

whence if :math:`2a^2 < c^2` [an obtuse isosceles triangle], the point :math:`O` even falls between :math:`H` and :math:`E`.

.. _euler-en-s29:

§ 29. Explicit Isosceles Formulas Relative to the Midpoint of EH
----------------------------------------------------------------

Given therefore on a straight line the three points :math:`E, G`, and :math:`H` such that :math:`G` is situated between the extremes :math:`E` and :math:`H`, one must inspect whether :math:`EG < \tfrac{1}{2}EH` or :math:`EG > \tfrac{1}{2}EH`:

* **In the former case**, where :math:`EG < \tfrac{1}{2}EH` (`Tab. II, Fig. 8`), let :math:`EH = 2d` and :math:`EG = d - e`; hence there is found:

  .. math::

     a = b = \frac{d + e}{2e}\sqrt{(d + 3e)(3d + e)}, \qquad
     c = \frac{d - e}{2e}\sqrt{(d + 3e)(3d + e)}, \qquad
     OE = \frac{(d - e)^2}{4e}.

* **In the latter case**, where :math:`EG > \tfrac{1}{2}EH` (`Fig. 9`), let :math:`EH = 2d` and :math:`EG = d + e`; hence there is collected:

  .. math::

     a = b = \frac{d - e}{2e}\sqrt{(d - 3e)(3d - e)}, \qquad
     c = \frac{d + e}{2e}\sqrt{(d - 3e)(3d - e)}, \qquad
     OE = \frac{(d + e)^2}{4e} \quad [\text{printed } 2e \text{ in folio}],

  whence it is clear that this case cannot take place if :math:`d` lies between the limits :math:`3e` and :math:`\tfrac{1}{3}e`. Indeed, since we must have :math:`2a > c`, it is necessary that :math:`d > 3e` [so :math:`EG < \frac{2}{3}EH = EF`, meaning :math:`G` always lies strictly between :math:`E` and :math:`F`!].

.. _euler-en-s30:

§ 30. Concise General Formulation Omitting the Centroid F
---------------------------------------------------------

From this case we may gather that in general, too (`Fig. 5`), a neater solution will come forth if, omitting the point :math:`F`, the three points :math:`E, G`, and :math:`H` are considered. Let us therefore set:

.. math::

   EG = e, \qquad GH = f, \qquad \text{and} \qquad EH = k;

then we shall have :math:`FH = g = \tfrac{1}{3}k`, :math:`EF = \tfrac{2}{3}k`, and :math:`FG = h = \sqrt{\tfrac{1}{3}e^2 + \tfrac{2}{3}f^2 - \tfrac{2}{9}k^2}`, and hence we obtain:

.. math::

   R = \frac{4f^4}{2f^2 + 2e^2 - k^2}, \qquad Q = \frac{f^2(k^2 - f^2 - 2e^2)}{2e^2 + 2f^2 - k^2},

.. folio:: § 30 (cont.)
   :page: 121

.. math::

   P = \frac{27f^4}{2e^2 + 2f^2 - k^2} + 2e^2 - 8f^2 - 3k^2
     = \frac{4e^4 + 11f^4 + 3k^4 - 12e^2f^2 + 2f^2k^2 - 8e^2k^2}{2e^2 + 2f^2 - k^2},

and furthermore :math:`\frac{Q^2}{R} = \frac{(k^2 - f^2 - 2e^2)^2}{4(2e^2 + 2f^2 - k^2)}`, whence we obtain:

.. math::

   p = \sqrt{P}, \qquad
   q = \frac{2e^4 + f^4 + k^4 - 6e^2f^2 - 3e^2k^2 + 2f^2k^2}{2e^2 + 2f^2 - k^2}, \qquad
   r = Q\sqrt{P},

and the roots of the equation :math:`z^3 - pz^2 + qz - r = 0` give the sides of the sought triangle; which equation, upon setting :math:`z = y\sqrt{P}`, passes into this rational-coefficient form:

.. math::

   y^3 - y^2 + \frac{(2e^4 + f^4 + k^4 - 6e^2f^2 - 3e^2k^2 + 2f^2k^2)y - f^2(k^2 - 2e^2 - f^2)(2e^2 + 2f^2 - k^2)/( \dots )}{P} = 0

[written in the folio with common denominator :math:`4e^4 + 11f^4 + 3k^4 - 12e^2f^2 - 8e^2k^2 + 2f^2k^2`].

.. _euler-en-s31:

§ 31. Diorismos: Positivity Inequalities on (e, f, k)
-----------------------------------------------------

Here, however, I observe that these given quantities :math:`e, f, k` must not only be so assumed that they form a triangle, but since the sides :math:`a, b, c` of the sought triangle must be regarded as positive, :math:`P` as well as :math:`Q` and :math:`R` must also receive positive values. Not only, therefore, must :math:`k^2 < 2e^2 + 2f^2`, but also :math:`k^2 > 2e^2 + f^2`; and further, so that :math:`P` may become positive, it is necessary that

.. math::

   3k^2 > 4e^2 + f^2 + 2\sqrt{e^4 + 11e^2f^2 - 8f^4},

and when this condition is compared with the preceding ones [requiring :math:`3(2e^2 + 2f^2) > 4e^2 + f^2 + 2\sqrt{e^4 + 11e^2f^2 - 8f^4}` and reality of the radical], there follows that :math:`f^2` must exceed the lower bound of real configurations—otherwise the problem would admit no solution.

.. _euler-en-s32:

§ 32. Reducible Family e = f (60° Angle) and Worked Example
-----------------------------------------------------------

**Example.** Let :math:`e^2 = f^2` [i.e. :math:`EG = GH`]; we shall have:

.. math::

   R = \frac{4f^4}{4f^2 - k^2}; \qquad
   Q = \frac{f^2(k^2 - 3f^2)}{4f^2 - k^2}; \qquad
   P = \frac{3(k^2 - f^2)^2}{4f^2 - k^2}; \qquad
   \frac{Q^2}{R} = \frac{(k^2 - 3f^2)^2}{4(4f^2 - k^2)},

and therefore:

.. math::

   p = \frac{(k^2 - f^2)\sqrt{3}}{\sqrt{4f^2 - k^2}}; \qquad
   q = \frac{k^4 - f^2k^2 - 3f^4}{4f^2 - k^2}; \qquad
   r = \frac{f^2(k^2 - 3f^2)(k^2 - f^2)\sqrt{3}}{4(4f^2 - k^2)\sqrt{4f^2 - k^2}}.

.. folio:: § 32 (cont.)
   :page: 122

Now let :math:`e^2 = f^2 = 2` and :math:`k^2 = 7`; there will come forth :math:`p = 5\sqrt{3}`, :math:`q = 23`, and :math:`r = 10\sqrt{3}`, and the sides of the sought triangle will be the roots of this cubic equation:

.. math::

   z^3 - 5z^2\sqrt{3} + 23z - 10\sqrt{3} = 0,

which upon setting :math:`z = \frac{y}{\sqrt{3}}` passes into :math:`y^3 - 15y^2 + 69y - 90 = 0`, one root of which is :math:`y = 6`, whence the remaining two are :math:`y = \frac{9 \pm \sqrt{21}}{2}`, and thus the sides of the sought triangle are:

.. math::

   a = \frac{3\sqrt{3} + \sqrt{7}}{2}; \qquad b = \frac{3\sqrt{3} - \sqrt{7}}{2}; \qquad c = 2\sqrt{3}.

.. _euler-en-s33:

§ 33. Universal Factorization Whenever EG = GH
----------------------------------------------

Indeed, even more generally, while :math:`e^2 = f^2` remains, however :math:`k` be chosen, if we set :math:`z = \frac{y}{\sqrt{3(4f^2 - k^2)}}`, we have this equation to solve:

.. math::

   y^3 - 3(k^2 - f^2)y^2 + 3(k^4 - f^2k^2 - 3f^4)y - 9f^2(k^2 - 3f^2)(k^2 - f^2) = 0,

which is satisfied first by :math:`y = 3f^2`, and the remaining two roots come from the quadratic equation :math:`y^2 - 3(k^2 - 2f^2)y + 3(k^2 - 3f^2)(k^2 - f^2) = 0`, namely :math:`y = \frac{3(k^2 - 2f^2) \pm k\sqrt{3(4f^2 - k^2)}}{2}`; and thus the three sides of the sought triangle become:

.. math::

   a = \frac{(k^2 - 2f^2)\sqrt{3}}{2\sqrt{4f^2 - k^2}} + \frac{1}{2}k, \qquad
   b = \frac{(k^2 - 2f^2)\sqrt{3}}{2\sqrt{4f^2 - k^2}} - \frac{1}{2}k, \qquad
   c = \frac{f^2\sqrt{3}}{\sqrt{4f^2 - k^2}}.

.. _euler-en-s34:

.. folio:: § 34
   :page: 123

§ 34. The Irreducible General Case & Solution by Angle Trisection
-----------------------------------------------------------------

In the remaining cases the business is not dispatched so easily, because the cubic equation does not admit rational factors [:term:`casus irreducibilis <casus-irreducibilis>`]. To show this by an example, let :math:`e^2 = 3`, :math:`f^2 = 2`, and :math:`k^2 = 9`; whence the sides of the triangle are the roots of this cubic equation:

.. math::

   z^3 - z^2\sqrt{71} + 22z - 2\sqrt{71} = 0;

to resolve which, let an acute angle :math:`\alpha` be sought whose cosine is given by the trigonometric depressed-cubic formula [see Critical Notes on Euler's printed :math:`+\sqrt{\frac{71}{75}}` vs. :math:`-\sqrt{\frac{71}{125}}`], and once this is found, the sides of the triangle will be expressed in the form:

.. math::

   a = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cos\left(60^\circ - \frac{1}{3}\alpha\right), \quad
   b = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cos\left(60^\circ + \frac{1}{3}\alpha\right), \quad
   c = \frac{1}{3}\sqrt{71} - \frac{2}{3}\sqrt{5}\cos\frac{1}{3}\alpha;

and thus **by the trisection of an angle** the problem will always be resolved expeditiously enough.
