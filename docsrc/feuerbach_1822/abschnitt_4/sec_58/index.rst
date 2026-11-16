:layout: book
:canonical_id: §§ 58–60
:breadcrumb_title: §§ 58–60
:order: 2
:folio: p. 39
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _fb-en-s58:

.. folio:: §§ 58–60
   :page: 39

§§ 58–60: Linear & Quadratic Center Sums and the Centroid G on KO
=================================================================

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

.. toctree::
   :hidden:

   de
   summary
   notes
