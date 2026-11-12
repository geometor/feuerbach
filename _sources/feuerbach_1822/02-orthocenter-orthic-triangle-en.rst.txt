:title: Feuerbach (1822) §§ 19–48 — Second Section: Orthocenter, Orthic Triangle & Inradius ρ
:layout: book

.. _fb-02-en:

=====================================================================================
Unit II: Second Section — The Orthocenter, Orthic Triangle & Inradius ρ (§§ 19–48)
=====================================================================================

.. rubric:: Karl Wilhelm Feuerbach — *Properties of Several Remarkable Points of the Rectilinear Triangle* (1822, pp. 15–32, Fig. 2–5)

.. contents:: Sections in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _fb-en-s19:

.. folio:: § 19
   :page: 15

§ 19. Fagnano's Minimal-Perimeter Orthic Triangle MNP
-----------------------------------------------------

When from the three vertices of any triangle :math:`ABC` one drops upon its opposite sides the perpendiculars :math:`AM, BN, CP`—which, as is well known, intersect in one and the same point :math:`O` [:g:`X_4 <0038.g1:X4>`]—the feet of these perpendiculars [:g:`M <0038.g1:H1>`, :g:`N <0038.g1:H2>`, :g:`P <0038.g1:H3>`] determine a triangle :math:`MNP` [:term:`orthic triangle <orthic-triangle>`], which is remarkable because among all triangles inscribed in triangle :math:`ABC` it possesses the *least perimeter* [*Footnote:* :person:`Fagnano <fagnano>` perhaps first taught this in the memoir :cite:`*Problemata quaedam ad methodum max. et min. spectantia*, *Acta Erud.*, June 1775 <fagnano_1775>`]. It will therefore not be without interest to consider this triangle more closely, and above all to determine its perimeter and area, together with their ratios to the perimeter and area of the given triangle :math:`ABC`.

Retaining the notation of the preceding section, we have :math:`AP = b\cos\alpha` and :math:`AN = c\cos\alpha`, whence :math:`\overline{NP}^2 = (b^2 + c^2 - 2bc\cos\alpha)\cos^2\alpha = a^2\cos^2\alpha`, and therefore:

.. math::

   NP = a\cos\alpha = \frac{a(-a^2 + b^2 + c^2)}{2bc}, \quad
   MP = b\cos\beta = \frac{b(a^2 - b^2 + c^2)}{2ac}, \quad
   MN = c\cos\gamma = \frac{c(a^2 + b^2 - c^2)}{2ab}.

Adding these three values together, since :math:`a^2(-a^2+b^2+c^2) + b^2(a^2-b^2+c^2) + c^2(a^2+b^2-c^2) = 16\Delta^2` and :math:`\frac{abc}{4\Delta} = R`, one obtains the sought perimeter:

.. math::

   MN + MP + NP = \frac{8\Delta^2}{abc} = \frac{2\Delta}{R}.

.. _fb-en-s23:

.. folio:: §§ 23–28
   :page: 18

§§ 23–28. Area of ΔMNP, the Orthic Inradius ρ, and Circumradius ½R
------------------------------------------------------------------

* **§ 23 (Area of ΔMNP)**: Since :math:`\triangle ANP = \Delta\cos^2\alpha`, :math:`\triangle BMP = \Delta\cos^2\beta`, :math:`\triangle CMN = \Delta\cos^2\gamma` and :math:`1 - (\cos^2\alpha + \cos^2\beta + \cos^2\gamma) = 2\cos\alpha\cos\beta\cos\gamma`, the area of the orthic triangle in an acute triangle :math:`ABC` is

  .. math::

     \triangle MNP = 2\Delta\cos\alpha\cos\beta\cos\gamma.

* **§ 24 (Orthic Inradius ρ and Tritangent Duality, p. 18)**: Denoting by :math:`\rho` the inradius of :math:`\triangle MNP` and by :math:`\rho^{(1)}, \rho^{(2)}, \rho^{(3)}` its three exradii, § 19 (:math:`a\cos\alpha + b\cos\beta + c\cos\gamma = \frac{2\Delta}{R}`) gives for an acute triangle :math:`ABC`:

  .. math::

     \rho = \frac{2\,\triangle MNP}{MN + MP + NP}
          = 2R\cos\alpha\cos\beta\cos\gamma
          = \frac{(-a^2 + b^2 + c^2)(a^2 - b^2 + c^2)(a^2 + b^2 - c^2)}{16abc\Delta},

  whence :math:`\triangle MNP : \Delta = \rho : R`. Moreover, because quadrilaterals :math:`ANOP` and :math:`BMOP` are cyclic :just:`[III. 22] <III.22>`, :math:`\angle APN = \angle BPM`, so the altitudes :math:`AM, BN, CP` bisect the interior angles of :math:`\triangle MNP` while the sides :math:`BC, AC, AB` bisect its exterior angles. Thus **the vertices** :math:`A, B, C` **together with the orthocenter** :math:`O` **are themselves the four tritangent centers of the orthic triangle** :math:`\triangle MNP`! (When :math:`\angle A > 90^\circ`, :math:`A` becomes the incenter of :math:`\triangle MNP`, and :math:`\rho` passes into :math:`-\rho^{(1)}`.)

* **§§ 26–28 (Orthic Circumradius ½R and Sum of Side Squares, pp. 19–20)**: Applying :math:`R_{MNP} = \frac{MN \cdot MP \cdot NP}{4\,\triangle MNP}` yields

  .. math::

     R_{MNP} = \frac{abc\cos\alpha\cos\beta\cos\gamma}{8\Delta\cos\alpha\cos\beta\cos\gamma} = \frac{1}{2}R,

  *the first appearance in the monograph of the nine-point radius* :math:`\tfrac{1}{2}R`! Furthermore, since :math:`\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1 - \frac{\rho}{R}`:

  .. math::

     a^2 + b^2 + c^2 = 4R(2R + \rho) = 8R^2 + 4\rho R,
     \qquad
     r^2 + r'^2 + r''^2 + r'''^2 = 4R(2R - \rho).

.. _fb-en-s30:

.. folio:: §§ 30–36
   :page: 21

§§ 30–36. Exradii of ΔMNP and Altitude-Segment Products Through O
-----------------------------------------------------------------

* **§§ 30–31 (p. 21)**: The perpendiculars :math:`Am, Bn, Cp` dropped from :math:`A, B, C` onto the opposite sides of :math:`\triangle MNP` are the three exradii :math:`\rho^{(1)}, \rho^{(2)}, \rho^{(3)}` of :math:`\triangle MNP`:

  .. math::

     Am = \frac{2\Delta\cos\alpha}{a}, \quad
     Bn = \frac{2\Delta\cos\beta}{b}, \quad
     Cp = \frac{2\Delta\cos\gamma}{c}, \qquad
     Am + Bn + Cp = \rho + 2R,

  and the projection segments on the sides satisfy

  .. math::

     AP \cdot BM \cdot CN = AN \cdot BP \cdot CM = MN \cdot MP \cdot NP = 2R \cdot \triangle MNP = 2\rho\Delta.

.. folio:: §§ 35–36
   :page: 24

* **§§ 32–36 (pp. 22–24)**: The circumradii of :math:`\triangle BCO, \triangle ACO, \triangle ABO` are each equal to :math:`R` (§ 33). From :math:`AO = 2R\cos\alpha` and :math:`OM = 2R\cos\beta\cos\gamma`, the orthocenter :math:`O` divides each altitude so that:

  .. math::

     AO \cdot OM = BO \cdot ON = CO \cdot OP = 2\rho R, \qquad
     OM \cdot ON \cdot OP = 2\rho^2 R, \qquad
     AO \cdot BO \cdot CO = 4\rho R^2.

.. _fb-en-s41:

.. folio:: §§ 41–48
   :page: 28

§§ 41–48. Corner Orthocenters M', N', P' and Circumcenter Sub-Circles
---------------------------------------------------------------------

* **§§ 41–42 (p. 28)**: Let :math:`M', N', P'` be the orthocenters of the corner triangles :math:`\triangle ANP, \triangle BMP, \triangle CMN`. Since :math:`AO` is the diameter of circle :math:`(ANP)`, :math:`AM' = AO\cos\alpha = 2R\cos^2\alpha`, whence:

  .. math::

     AM' + BN' + CP' &= 2(R - \rho), \\
     AM' \cdot BN' = \overline{OP}^2, \quad AM' \cdot CP' &= \overline{ON}^2, \quad BN' \cdot CP' = \overline{OM}^2, \\
     OM \cdot ON \cdot OP &= AM' \cdot BN' \cdot CP'.

.. folio:: §§ 47–48
   :page: 32

* **§§ 47–48 (p. 32)**: Denoting by :math:`Ka, Kb, Kc` the distances from the circumcenter :math:`K` [:g:`X_3 <0038.g1:X3>`] to the three sides (:math:`Ka = \tfrac{1}{2}AO`, :math:`Kb = \tfrac{1}{2}BO`, :math:`Kc = \tfrac{1}{2}CO`), and by :math:`R', R'', R'''` the circumradii of :math:`\triangle BCK, \triangle ACK, \triangle ABK`:

  .. math::

     R' \cdot AO = R'' \cdot BO = R''' \cdot CO = R^2, \qquad
     R' + R'' + R''' : OM + ON + OP = R : 2\rho.
