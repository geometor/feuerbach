:layout: book
:canonical_id: § 19
:breadcrumb_title: § 19
:order: 1
:folio: p. 15
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _fb-02-en:
.. _fb-en-s19:

.. folio:: § 19
   :page: 15

§ 19: Fagnano's Minimal-Perimeter Orthic Triangle MNP
=====================================================

When from the three vertices of any triangle :math:`ABC` one drops upon its opposite sides the perpendiculars :math:`AM, BN, CP`—which, as is well known, intersect in one and the same point :math:`O` [:g:`X_4 <0038.g1:X4>`]—the feet of these perpendiculars [:g:`M <0038.g1:H1>`, :g:`N <0038.g1:H2>`, :g:`P <0038.g1:H3>`] determine a triangle :math:`MNP` [:term:`orthic triangle <orthic-triangle>`], which is remarkable because among all triangles inscribed in triangle :math:`ABC` it possesses the *least perimeter* [*Footnote:* :person:`Fagnano <fagnano>` perhaps first taught this in the memoir :cite:`*Problemata quaedam ad methodum max. et min. spectantia*, *Acta Erud.*, June 1775 <fagnano_1775>`]. It will therefore not be without interest to consider this triangle more closely, and above all to determine its perimeter and area, together with their ratios to the perimeter and area of the given triangle :math:`ABC`.

Retaining the notation of the preceding section, we have :math:`AP = b\cos\alpha` and :math:`AN = c\cos\alpha`, whence :math:`\overline{NP}^2 = (b^2 + c^2 - 2bc\cos\alpha)\cos^2\alpha = a^2\cos^2\alpha`, and therefore:

.. math::

   NP = a\cos\alpha = \frac{a(-a^2 + b^2 + c^2)}{2bc}, \quad
   MP = b\cos\beta = \frac{b(a^2 - b^2 + c^2)}{2ac}, \quad
   MN = c\cos\gamma = \frac{c(a^2 + b^2 - c^2)}{2ab}.

Adding these three values together, since :math:`a^2(-a^2+b^2+c^2) + b^2(a^2-b^2+c^2) + c^2(a^2+b^2-c^2) = 16\Delta^2` and :math:`\frac{abc}{4\Delta} = R`, one obtains the sought perimeter:

.. math::

   MN + MP + NP = \frac{8\Delta^2}{abc} = \frac{2\Delta}{R}.

.. toctree::
   :hidden:

   de
   summary
   notes
