:layout: book
:canonical_id: §§ 23–28
:breadcrumb_title: §§ 23–28
:order: 2
:folio: p. 18
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-en-s23:

.. folio:: §§ 23–28
   :page: 18

§§ 23–28: Area of ΔMNP, the Orthic Inradius ρ, and Circumradius ½R
==================================================================

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

.. toctree::
   :hidden:

   de
   summary
   notes
