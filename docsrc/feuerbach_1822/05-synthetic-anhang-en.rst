:title: Feuerbach (1822) Anhang (1.–9. Satz) — Synthetic Euclidean Demonstrations
:layout: book

.. _fb-05-en:

===========================================================================================
Unit V: Synthetic Appendix (*Anhang*) — Pure Euclidean Proofs of Nine Theorems (pp. 56–62)
===========================================================================================

.. rubric:: Karl Wilhelm Feuerbach — *Properties of Several Remarkable Points of the Rectilinear Triangle* (1822, pp. 56–62, Fig. 13–17)

.. contents:: Propositions in This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _fb-en-anhang-1-4:

.. folio:: Anhang, 1.–4. Satz
   :page: 56–59

Synopsis of Propositions 1–4 (pp. 56–59)
----------------------------------------

In the closing *Anhang*, :person:`Feuerbach <feuerbach>` demonstrates the foundational metric lemmas of Sections II and III purely synthetically from Books I–IV and VI of :person:`Euclid <euclid>`'s :cite:`*Elements* <euclid_elements>`, without trigonometric functions or coordinate algebra:

* **1st Proposition (*1. Satz*)**: In any triangle :math:`ABC` with circumcenter :math:`K`, orthocenter :math:`O`, and midpoint :math:`D` of side :math:`AB`, the altitude segment from the opposite vertex equals twice the distance of the circumcenter from that side: :math:`CO = 2\,KD`.
* **2nd Proposition (*2. Satz*)**: The square on any side :math:`AB` added to the square on the opposite vertex-to-orthocenter segment :math:`CO` equals the square on the diameter of the circumscribed circle: :math:`\overline{AB}^2 + \overline{CO}^2 = 4R^2`.
* **3rd & 4th Propositions (*3.–4. Satz*)**: From cyclic orthic quadrilaterals and :just:`[VI. 16] <VI.16>`, the rectangle contained by the inradius :math:`r` and the perimeter of :math:`\triangle ABC` equals the rectangle contained by the circumradius :math:`R` and the perimeter of the orthic triangle :math:`\triangle MNP`:

  .. math::

     r(AB + AC + BC) = R(MN + MP + NP) \qquad \Longleftrightarrow \qquad MN + MP + NP = \frac{2\Delta}{R}.

----

.. _fb-en-anhang-5:

.. folio:: 5. Satz
   :page: 60

5th Proposition (*5. Satz*) — Ratio of the Orthic Area to ΔABC (Complete Translation)
-------------------------------------------------------------------------------------

**Enunciation.** *The area of triangle* :math:`MNP`, *which the feet of the altitudes form in an acute-angled triangle* :math:`ABC`, *bears to the area of triangle* :math:`ABC` *the same ratio as the radius of the circle inscribed in the former bears to the radius of the circle circumscribed about the latter.*

**Proof.** For if the radius of the circle inscribed in triangle :math:`MNP` is :math:`\rho`, and :math:`r, R` are as before the radii of the circles inscribed in and circumscribed about triangle :math:`ABC`, then as is well known :math:`2\,\triangle MNP = \rho(MN + MP + NP)` and :math:`2\,\triangle ABC = r(AB + AC + BC)`, whence

.. math::

   \triangle MNP : \triangle ABC = \rho(MN + MP + NP) : r(AB + AC + BC).

Now however there follows from the preceding [4th] Proposition :just:`[VI. 16] <VI.16>` :math:`r(AB + AC + BC) = R(MN + MP + NP)`, and therefore:

.. math::

   \triangle MNP : \triangle ABC = \rho : R. \qquad \text{Q.E.D.}

.. _fb-en-anhang-6:

6th Proposition (*6. Satz*) — Altitude-Segment Rectangle CO · OP = 2Rρ
----------------------------------------------------------------------

**Enunciation.** *The intersection point* :math:`O` *of the altitudes in an acute-angled triangle* :math:`ABC` *divides each of them* :math:`CP` *into two such segments* :math:`CO, OP` *that the rectangle contained by them equals the rectangle contained by the diameter of the circle circumscribed about triangle* :math:`ABC` *and the radius of the circle inscribed in the triangle* :math:`MNP` *formed by the feet of those altitudes.*

**Proof.** Erect from :math:`O` upon side :math:`MP` the perpendicular :math:`OJ`. Because :just:`[III. 22] <III.22>` a circle can be circumscribed about the quadrilateral :math:`ANOP`, we have :just:`[III. 21] <III.21>` :math:`\angle NPO = \angle NAO`, and for the very same reason :math:`\angle MPO = \angle MBO`. Because however :just:`[I. 15] <I.15>` :math:`\angle AON = \angle BOM` and :math:`\angle ANB = \text{right} = \angle AMB`, we have :math:`\angle NAO = \angle MBO`, consequently also :math:`\angle NPO = \angle MPO`. In just the same way it is proved that :math:`\angle NMO = \angle PMO`; therefore :just:`[IV. 4] <IV.4>` :math:`O` is the center of the circle inscribed in triangle :math:`MNP` and the perpendicular :math:`OJ` is a radius [:math:`\rho`] of this circle.

Now pass through the vertex :math:`A` and the center :math:`K` of the circle circumscribed about triangle :math:`ABC` a diameter :math:`AG = 2R` of the same, and draw :math:`BG`; then :just:`[III. 31] <III.31>` :math:`\angle ABG = \text{right}` and :just:`[III. 21] <III.21>` :math:`\angle AGB = \angle ACB`, consequently :math:`\angle GAB = \angle CBN`. Since now :math:`\angle MBO = \angle MPO`, we also have :math:`\angle GAB = \angle MPO`, and hence the right triangles :math:`ABG, OPJ` are equiangular, so that :just:`[VI. 4] <VI.4>` :math:`AG : BG = OP : OJ`.

Erect furthermore from :math:`K` upon :math:`AB` the perpendicular :math:`KD`; then triangles :math:`ADK, ABG` are equiangular, whence :just:`[VI. 4] <VI.4>` :math:`AD : DK = AB : BG`, and because :just:`[III. 3] <III.3>` :math:`AB = 2\,AD`, we also have :math:`BG = 2\,KD`. By the 1st Proposition, however, :math:`CO = 2\,KD`, consequently :math:`BG = CO`; and therefore :math:`AG : CO = OP : OJ` and :just:`[VI. 16] <VI.16>`:

.. math::

   \operatorname{Rect}(AG, OJ) = \operatorname{Rect}(CO, OP) \qquad \Longleftrightarrow \qquad CO \cdot OP = 2R\rho. \qquad \text{Q.E.D.}

.. _fb-en-anhang-7:

.. folio:: 7. Satz
   :page: 61

7th Proposition (*7. Satz*) — Sum of Squared Sides AB² + AC² + BC² = 8R² + 4ρR
------------------------------------------------------------------------------

**Enunciation.** *The sum of the squares on the sides of an acute-angled triangle* :math:`ABC` *equals twice the square on the diameter of the circumscribed circle, increased by the rectangle contained by this diameter and the diameter of the circle inscribed in triangle* :math:`MNP` *formed by the feet of the altitudes in triangle* :math:`ABC`.

**Proof.** Let :math:`O` be the intersection point of the altitudes. Draw from any vertex :math:`C` of triangle :math:`ABC` to the midpoint :math:`D` of the opposite side :math:`AB` the median :math:`CD`. Since :math:`AB` is bisected at :math:`D`, we have :just:`[II. 5] <II.5>` :math:`AP \cdot BP + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2`. Because however :math:`\angle ABN = \angle ACP`, the right triangles :math:`APC, BPO` are equiangular, whence :just:`[VI. 4] <VI.4>` :math:`AP : CP = OP : BP` and :just:`[VI. 16] <VI.16>` :math:`AP \cdot BP = CP \cdot OP`. Since now :math:`CP = CO + OP`, we have also :just:`[II. 3] <II.3>` :math:`AP \cdot BP = CO \cdot OP + \overline{OP}^2`, and therefore :math:`CO \cdot OP + \overline{OP}^2 + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2`.

Now by :just:`[I. 47] <I.47>` and :just:`[II. 4] <II.4>`, :math:`\overline{CD}^2 = \overline{CO}^2 + 2\,CO \cdot OP + \overline{OP}^2 + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2 + \overline{CO}^2 + CO \cdot OP`. Furthermore, by a well-known corollary to :just:`[II. 12] <II.12>` [Apollonius's median theorem]:

.. math::

   \overline{AC}^2 + \overline{BC}^2 = \frac{1}{2}\overline{AB}^2 + 2\overline{CD}^2 = \overline{AB}^2 + 2\overline{CO}^2 + 2\,CO \cdot OP;

and adding :math:`\overline{AB}^2` to both sides gives :math:`\overline{AB}^2 + \overline{AC}^2 + \overline{BC}^2 = 2\overline{AB}^2 + 2\overline{CO}^2 + 2\,CO \cdot OP`. Denoting the radii of the circles circumscribed about :math:`\triangle ABC` and inscribed in :math:`\triangle MNP` by :math:`R, \rho`, we have by the 2nd Proposition :math:`\overline{AB}^2 + \overline{CO}^2 = 4R^2` and by the 6th Proposition :math:`CO \cdot OP = 2\rho R`. Therefore:

.. math::

   \overline{AB}^2 + \overline{AC}^2 + \overline{BC}^2 = 8R^2 + 4\rho R. \qquad \text{Q.E.D.}

.. _fb-en-anhang-8:

.. folio:: 8. Satz
   :page: 61–62

8th Proposition (*8. Satz*) — Pedal Segment GH Equals Semiperimeter of ΔMNP
---------------------------------------------------------------------------

**Enunciation.** *When from any altitude foot* :math:`P` *in side* :math:`AB` *of an acute-angled triangle* :math:`ABC` *one drops upon the other two sides* :math:`AC, BC` *the perpendiculars* :math:`PG, PH` (*Fig. 16*), *the straight line* :math:`GH` *joining the feet of these perpendiculars equals the semiperimeter of the orthic triangle* :math:`MNP`.

**Proof.** Produce :math:`PG, PH` until they meet the prolongation of :math:`MN` at :math:`J` and :math:`K`. Because :just:`[III. 22] <III.22>` a circle can be circumscribed about quadrilateral :math:`CNOM`, we have :just:`[III. 21] <III.21>` :math:`\angle CMN = \angle CON`; likewise :math:`\angle BMP = \angle BOP`; consequently :just:`[I. 15] <I.15>` :math:`\angle CMN = \angle BMP` and hence also :math:`\angle BMK = \angle BMP`. Now :math:`PH \perp BC`, whence :just:`[I. 26] <I.26>` :math:`MP = MK` and :math:`PH = HK`. In just the same way it is proved that :math:`NP = NJ` and :math:`PG = GJ`.

Since therefore :math:`G, H` are the midpoints of :math:`PJ, PK`, :just:`[VI. 2] <VI.2>` :math:`GH \parallel JK`, whence :just:`[VI. 4] <VI.4>` :math:`PG : GH = PJ : JK`. Now :math:`PJ = 2\,PG`, so also :math:`JK = 2\,GH`; and because :math:`JK = MN + MK + NJ = MN + MP + NP`, we have:

.. math::

   GH = \frac{1}{2}(MN + MP + NP). \qquad \text{Q.E.D.}

.. _fb-en-anhang-9:

.. folio:: 9. Satz
   :page: 62

9th Proposition (*9. Satz*) — Pure Euclidean Proof of the Nine-Point Circle
---------------------------------------------------------------------------

.. picture:: /_static/constructions/nine_point_circle.svg
   :alt: Synthetic Euclidean construction of the nine-point center L = mid(OK) with LM = LN = LP = LD = R/2 (9. Satz)

**Enunciation.** *The radius of the circle circumscribed about triangle* :math:`MNP`, *which the feet of the altitudes form in triangle* :math:`ABC`, *is half as great as the radius of the circle circumscribed about triangle* :math:`ABC`; *and the locus* :math:`L` *of the center of the former circle bisects the distance of the center* :math:`K` *of the latter circle from the intersection point* :math:`O` *of those altitudes* (*Fig. 17*).

**Proof.** Draw from :math:`K` [:g:`X_3 <0038.g1:X3>`] to :math:`O` [:g:`X_4 <0038.g1:X4>`] and :math:`C` the straight lines :math:`OK, CK`, and upon :math:`AB` drop the perpendicular :math:`KD` [to the side midpoint :g:`D <0038.g1:M3>`]. Furthermore pass through :math:`D` and the midpoint :math:`L` [:g:`X_5 <0038.g1:X5>`] of the straight line :math:`OK` the line :math:`DL`, which prolonged meets the altitude :math:`CP` at :math:`J` [the Euler midpoint :g:`J <0038.g1:E3>`].

Because :math:`LO = LK`, and furthermore :just:`[I. 15] <I.15>` :math:`\angle OLJ = \angle KLD` and—since :math:`OJ \parallel KD`—:just:`[I. 29] <I.29>` :math:`\angle LOJ = \angle LKD`, it follows :just:`[I. 26] <I.26>` that :math:`OJ = KD` and :math:`JL = DL`. Now since by the 1st Proposition :math:`KD = \frac{1}{2}CO`, we also have :math:`OJ = \frac{1}{2}CO` [so :math:`J` is the Euler midpoint of :math:`CO`!] and therefore :math:`CJ = KD`; and because :math:`CJ \parallel KD`, we have :just:`[I. 33] <I.33>` :math:`JD = CK`, consequently:

.. math::

   DL = \frac{1}{2}CK.

Drop furthermore from :math:`L` upon :math:`AB` the perpendicular :math:`LE` and draw :math:`LP` [to the altitude foot :g:`P <0038.g1:H3>`]; because the straight lines :math:`OP, LE, KD` all run parallel to one another, :just:`[VI. 2] <VI.2>` :math:`OL : KL = PE : DE`, and since :math:`OL = KL`, we also have :math:`PE = DE`; hence :just:`[I. 4] <I.4>` :math:`LD = LP`. Since now :math:`LD = \frac{1}{2}CK`, we also have :math:`LP = \frac{1}{2}CK`.

In the very same manner it is proved that :math:`LN = \frac{1}{2}BK` and :math:`LM = \frac{1}{2}AK`; consequently, because :math:`AK = BK = CK` [:math:`= R`], we have also:

.. math::

   LM = LN = LP \left[= LD = LJ = \frac{1}{2}R\right],

and :math:`L`, that is, the midpoint of :math:`OK`, is the center of the circle circumscribed about triangle :math:`MNP`. **Q.E.D.**
