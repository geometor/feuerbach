:layout: book
:canonical_id: 7. Satz
:breadcrumb_title: 7. Satz
:order: 4
:folio: p. 61
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _fb-en-anhang-7:

.. folio:: 7. Satz
   :page: 61

7th Proposition (7. Satz): Sum of Squared Sides AB² + AC² + BC² = 8R² + 4ρR
===========================================================================

**Enunciation.** *The sum of the squares on the sides of an acute-angled triangle* :math:`ABC` *equals twice the square on the diameter of the circumscribed circle, increased by the rectangle contained by this diameter and the diameter of the circle inscribed in triangle* :math:`MNP` *formed by the feet of the altitudes in triangle* :math:`ABC`.

**Proof.** Let :math:`O` be the intersection point of the altitudes. Draw from any vertex :math:`C` of triangle :math:`ABC` to the midpoint :math:`D` of the opposite side :math:`AB` the median :math:`CD`. Since :math:`AB` is bisected at :math:`D`, we have :just:`[II. 5] <II.5>` :math:`AP \cdot BP + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2`. Because however :math:`\angle ABN = \angle ACP`, the right triangles :math:`APC, BPO` are equiangular, whence :just:`[VI. 4] <VI.4>` :math:`AP : CP = OP : BP` and :just:`[VI. 16] <VI.16>` :math:`AP \cdot BP = CP \cdot OP`. Since now :math:`CP = CO + OP`, we have also :just:`[II. 3] <II.3>` :math:`AP \cdot BP = CO \cdot OP + \overline{OP}^2`, and therefore :math:`CO \cdot OP + \overline{OP}^2 + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2`.

Now by :just:`[I. 47] <I.47>` and :just:`[II. 4] <II.4>`, :math:`\overline{CD}^2 = \overline{CO}^2 + 2\,CO \cdot OP + \overline{OP}^2 + \overline{PD}^2 = \frac{1}{4}\overline{AB}^2 + \overline{CO}^2 + CO \cdot OP`. Furthermore, by a well-known corollary to :just:`[II. 12] <II.12>` [Apollonius's median theorem]:

.. math::

   \overline{AC}^2 + \overline{BC}^2 = \frac{1}{2}\overline{AB}^2 + 2\overline{CD}^2 = \overline{AB}^2 + 2\overline{CO}^2 + 2\,CO \cdot OP;

and adding :math:`\overline{AB}^2` to both sides gives :math:`\overline{AB}^2 + \overline{AC}^2 + \overline{BC}^2 = 2\overline{AB}^2 + 2\overline{CO}^2 + 2\,CO \cdot OP`. Denoting the radii of the circles circumscribed about :math:`\triangle ABC` and inscribed in :math:`\triangle MNP` by :math:`R, \rho`, we have by the 2nd Proposition :math:`\overline{AB}^2 + \overline{CO}^2 = 4R^2` and by the 6th Proposition :math:`CO \cdot OP = 2\rho R`. Therefore:

.. math::

   \overline{AB}^2 + \overline{AC}^2 + \overline{BC}^2 = 8R^2 + 4\rho R. \qquad \text{Q.E.D.}

.. toctree::
   :hidden:

   de
   summary
   notes
