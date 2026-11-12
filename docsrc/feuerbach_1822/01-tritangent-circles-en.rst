:title: Feuerbach (1822) §§ 1–18 — First Section: The Four Tritangent Circle Centers
:layout: book

.. _fb-01-en:

===============================================================================
Unit I: First Section — On the Centers of the Four Tritangent Circles (§§ 1–18)
===============================================================================

.. rubric:: Karl Wilhelm Feuerbach — *Properties of Several Remarkable Points of the Rectilinear Triangle* (1822, pp. 1–14, Fig. 1)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _fb-en-s01:

.. folio:: § 1
   :page: 1

§ 1. The Four Tritangent Circles and the Excentral Orthocentric System
----------------------------------------------------------------------

As is well known, for any triangle :math:`ABC` whatever, four distinct circles touching its three sides [:term:`tritangent circles <tritangent-circles>`] are possible, of which only one lies within, whereas the remaining three lie outside the triangle (*Fig. 1*). The first internally touching or inscribed circle touches all three sides of the triangle itself and lies simultaneously in the planes [interior sectors] of all three of its angles. Each of the three latter externally touching circles, on the contrary, touches only *one* of the three sides itself together with the prolongations of the other two, and lies in the sector of that angle which stands opposite the side touched by itself.

Furthermore, if :math:`S` [:g:`X_1 <0038.g2:X1>`] represents the center of the inscribed circle, then by the familiar construction :just:`[IV. 4] <IV.4>` :math:`S` is at the same time the intersection point of the straight lines :math:`AS, BS, CS` bisecting the angles :math:`CAB, ABC, BCA` of triangle :math:`ABC`. And if :math:`S', S'', S'''` [:g:`J_1 <0038.g2:J1>`, :g:`J_2 <0038.g2:J2>`, :g:`J_3 <0038.g2:J3>`] represent in order the centers of the externally touching circles situated in the sectors of the angles :math:`CAB, ABC, BCA`, then :math:`S'` is simultaneously the intersection of the straight lines :math:`AS', BS', CS'`, the first of which bisects the angle :math:`CAB` while the other two bisect the exterior supplementary angles (*Nebenwinkel*) of :math:`ABC, BCA`; likewise :math:`S''` is the intersection of :math:`AS'', BS'', CS''`, the second of which bisects :math:`ABC` while the other two bisect the supplementary angles of :math:`CAB, BCA`; and finally :math:`S'''` is the intersection of :math:`AS''', BS''', CS'''`, the third of which bisects :math:`BCA` while the other two bisect the supplementary angles of :math:`CAB, ABC`.

.. folio:: § 1 (cont.)
   :page: 2

Since therefore each of the straight lines :math:`AS, AS'` bisects the angle :math:`CAB`, the three points :math:`A, S, S'` lie on a single straight line, which holds likewise of the points :math:`B, S, S''` and :math:`C, S, S'''`; so that the straight lines :math:`AS', BS'', CS'''` intersect one another in the center :math:`S` of the inscribed circle. And because the straight lines :math:`AS'', AS'''` bisect the two supplementary angles of :math:`CAB`, the points :math:`A, S'', S'''` also lie on a straight line, which holds likewise of :math:`B, S', S'''` and :math:`C, S', S''`; so that triangle :math:`S'S''S'''` is circumscribed about triangle :math:`ABC`. Since moreover :math:`\angle BAS''' = \angle CAS''` and :math:`\angle BAS = \angle CAS`, the straight line :math:`AS'` stands perpendicular to :math:`S''S'''` :just:`[I. 13] <I.13>`, and likewise :math:`BS'' \perp S'S'''` and :math:`CS''' \perp S'S''`; **so that the vertices** :math:`A, B, C` **of triangle** :math:`ABC` **are simultaneously the feet of the altitudes dropped in triangle** :math:`S'S''S'''` **from the vertices** :math:`S', S'', S'''` **upon the opposite sides** [with :math:`S` as orthocenter of :math:`\triangle S'S''S'''`].

.. _fb-en-s02:

§ 2. Expressions of the Four Radii and L'Huilier's Theorem
----------------------------------------------------------

Let the radii of the circles around the centers :math:`S, S', S'', S'''` be denoted in order by the letters :math:`r, r', r'', r'''`; then as is well known their values are:

.. math::

   r = \frac{2\Delta}{a + b + c}, \qquad
   r' = \frac{2\Delta}{-a + b + c}, \qquad
   r'' = \frac{2\Delta}{a - b + c}, \qquad
   r''' = \frac{2\Delta}{a + b - c},

where according to customary notation :math:`a, b, c` denote in order the sides :math:`BC, AC, BA` and :math:`\Delta` the area of triangle :math:`ABC`.

Multiplying these expressions of the four radii together, and using Heron's identity :math:`(a+b+c)(-a+b+c)(a-b+c)(a+b-c) = 16\Delta^2`, one obtains:

.. math::

   r\,r'\,r''\,r''' = \frac{16\Delta^4}{16\Delta^2} = \Delta^2,

that is: *In every triangle the radii of the four circles touching its three sides are so constituted that between the rectangle contained by any two of them and the rectangle contained by the remaining two, the given triangle itself is the mean geometric proportional.* This proposition is due to :person:`L'Huilier <lhuilier>`; he proves it in :cite:`*Annales de mathématiques* <lhuilier_1810>`, Nov. 1810, No. V.

.. _fb-en-s03:

.. folio:: §§ 3–5
   :page: 3

§§ 3–7. Symmetric Polynomial Laws Among the Four Tritangent Radii
-----------------------------------------------------------------

* **§ 3 (Pairwise Exradius Sum)**: Multiplying the values of :math:`r', r'', r'''` two by two and summing the products yields

  .. math::

     r'r'' + r'r''' + r''r''' = \frac{4\Delta^2(a + b + c)}{(-a + b + c)(a - b + c)(a + b - c)} = \frac{1}{4}(a + b + c)^2,

  that is, the sum of the three rectangles formed by the three exradii taken in pairs equals the square on the semiperimeter :math:`s = \tfrac{1}{2}(a+b+c)`.

* **§ 4 (Reciprocal & Volume Relation)**: Substituting :math:`a+b+c = \frac{2\Delta}{r}` and :math:`\Delta^2 = rr'r''r'''` gives

  .. math::

     r'\,r''\,r''' = r\left(r'r'' + r'r''' + r''r'''\right) = \frac{1}{2}(a + b + c)\Delta
     \qquad \Longleftrightarrow \qquad
     \frac{1}{r'} + \frac{1}{r''} + \frac{1}{r'''} = \frac{1}{r}.

* **§ 5 (Linear Sum of Exradii, pp. 3–4)**: Adding :math:`r', r'', r'''` via the algebraic identity :math:`(a+b+c)\big[(-a+b+c)(a-b+c) + (-a+b+c)(a+b-c) + (a-b+c)(a+b-c)\big] = (-a+b+c)(a-b+c)(a+b-c) + 8abc` and introducing the circumradius :math:`R = \frac{abc}{4\Delta}` yields

  .. math::

     r' + r'' + r''' = \frac{(-a+b+c)(a-b+c)(a+b-c) + 8abc}{8\Delta} = r + 4R.

  *The sum of the three exradii equals the inradius increased by twice the diameter of the circumcircle.*

.. folio:: §§ 6–7
   :page: 4

* **§ 6 (All Six Pairwise Products & Side-Squares)**: Combining :math:`r(r'+r''+r''') = ab + ac + bc - \frac{1}{4}(a+b+c)^2` with § 3 by addition and subtraction produces the twin symmetric laws:

  .. math::

     rr' + rr'' + rr''' + r'r'' + r'r''' + r''r''' &= ab + ac + bc, \tag{1} \\
     r'r'' + r'r''' + r''r''' - r(r' + r'' + r''') &= \frac{1}{2}(a^2 + b^2 + c^2). \tag{2}

* **§ 7 (Sum of Exradius Squares)**: From :math:`r'^2 + r''^2 + r'''^2 = (r'+r''+r''')^2 - 2(r'r''+r'r'''+r''r''')` and §§ 3, 5:

  .. math::

     r'^2 + r''^2 + r'''^2 = (r + 4R)^2 - \frac{1}{2}(a + b + c)^2.

.. _fb-en-s08:

.. folio:: §§ 8–11
   :page: 6

§§ 8–11. Contact Triangles δ, δ', δ'', δ''' and Vertex-to-Center Products
-------------------------------------------------------------------------

* **§§ 8–9 (Areas of the Four Contact Triangles, pp. 5–6)**: Let :math:`\delta = \triangle DEF` denote the area of the contact triangle formed by the points where the incircle touches the three sides of :math:`\triangle ABC`, and let :math:`\delta', \delta'', \delta'''` denote the areas of the corresponding contact triangles of the three excircles (obtained algebraically by substituting :math:`-a`, :math:`-b`, :math:`-c` for :math:`+a, +b, +c`, under which :math:`r \mapsto r'`, :math:`+R \mapsto -R`, while :math:`\Delta` remains unaltered in magnitude). Then:

  .. math::

     \frac{\delta}{r} = \frac{\delta'}{r'} = \frac{\delta''}{r''} = \frac{\delta'''}{r'''} = \frac{\Delta}{2R},
     \qquad \text{whence by § 5:} \qquad
     \delta' + \delta'' + \delta''' = \delta + 2\Delta.

* **§§ 10–11 (Half-Angle Identities & Vertex-to-Center Products, pp. 6–8)**: Using :math:`\sin\tfrac{1}{2}\alpha \sin\tfrac{1}{2}\beta \sin\tfrac{1}{2}\gamma = \frac{r}{4R}` and :math:`\cos^2\tfrac{1}{2}\alpha + \cos^2\tfrac{1}{2}\beta + \cos^2\tfrac{1}{2}\gamma = 2 + \frac{r}{2R}`, the distances from the vertices :math:`A, B, C` to the four tritangent centers satisfy:

  .. math::

     AS \cdot BS \cdot CS = 4r^2R, \qquad
     AS' \cdot BS' \cdot CS' = 4r'^2R, \qquad
     AS'' \cdot BS'' \cdot CS'' = 4r''^2R, \qquad
     AS''' \cdot BS''' \cdot CS''' = 4r'''^2R.

.. _fb-en-s12:

.. folio:: §§ 12–18
   :page: 10

§§ 12–18. Sub-Circumradii and the Six Mutual Distances Among S, S', S'', S'''
-----------------------------------------------------------------------------

* **§§ 12–14 (Circumradii of the Sub-Triangles, p. 10)**: Denoting by :math:`\mathfrak{A}, \mathfrak{B}, \mathfrak{C}` the circumradii of :math:`\triangle BCS, \triangle ACS, \triangle ABS` (and by :math:`\mathfrak{A}^{(k)}, \mathfrak{B}^{(k)}, \mathfrak{C}^{(k)}` those for :math:`S^{(k)}`), Feuerbach proves:

  .. math::

     \mathfrak{A}^2 + \mathfrak{B}^2 + \mathfrak{C}^2 = 2R(2R - r), \qquad
     \mathfrak{A}^{(k)2} + \mathfrak{B}^{(k)2} + \mathfrak{C}^{(k)2} = 2R\left(2R + r^{(k)}\right), \qquad
     AS \cdot \mathfrak{A} = BS \cdot \mathfrak{B} = CS \cdot \mathfrak{C} = 2rR.

.. folio:: §§ 15–17
   :page: 12

* **§§ 15–18 (Mutual Quadrances Among the Four Tritangent Centers, pp. 11–14)**: Because :math:`\angle SBS' = \angle SCS' = 90^\circ`, the segment :math:`SS'` is the diameter :math:`2\mathfrak{A}` of circle :math:`(BCSS')`. Setting

  .. math::

     A = SS', \quad B = SS'', \quad C = SS''', \qquad
     A' = S''S''', \quad B' = S'S''', \quad C' = S'S'',

  Feuerbach establishes the remarkable metric laws governing the orthocentric quadrangle :math:`(S, S', S'', S''')`:

  .. math::

     ABC &= 16rR^2, \qquad A'B'C' = A'BC + AB'C + ABC' = 8(a + b + c)R^2, \\
     A^2 + B^2 + C^2 &= 8R(2R - r), \qquad A'^2 + B'^2 + C'^2 = 8R(6R + r) = 8R(r' + r'' + r''' + 2R), \\
     A^2 + B^2 + C^2 &+ A'^2 + B'^2 + C'^2 = 48R^2, \\
     A^2 + A'^2 &= B^2 + B'^2 = C^2 + C'^2 = 16R^2.

  That is (**§ 17**, p. 13): *The centers of the four circles touching the three sides of any triangle are so situated that the square of the distance between any two of them, added to the square of the distance between the remaining two, always equals the square on twice the diameter of the circumcircle* (:math:`(4R)^2 = 16R^2`).
