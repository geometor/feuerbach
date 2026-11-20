:layout: book
:canonical_id: 9. Satz
:breadcrumb_title: 9. Satz
:order: 6
:folio: 9. Satz
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-en-anhang-9:

.. folio:: 9. Satz
   :page: 62

9th Proposition (9. Satz): Pure Euclidean Proof of the Nine-Point Circle
========================================================================

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

.. toctree::
   :hidden:

   de
   summary
   notes
