:layout: book
:canonical_id: §§ 63–65 (Notes)
:breadcrumb_title: Notes
:order: 2
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-notes-s63:

§§ 63–65: §§ 63–65: Orthic Triangles μ, μ', μ'', μ''' Inside the Four Contact Triangles — Notes
===============================================================================================

.. rubric:: Historical, Philological & Symbolic Commentary

GEOMETOR Commentary & Symbolic Notes
------------------------------------

1. Angle-Doubling, Similarity, and Homothety
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In any acute triangle :math:`ABC` with angles :math:`(\alpha, \beta, \gamma)`:

* Passing to the **contact triangle** :math:`\triangle DEF` replaces angles by :math:`(90^\circ - \frac{1}{2}\alpha, 90^\circ - \frac{1}{2}\beta, 90^\circ - \frac{1}{2}\gamma)`.
* Passing from :math:`\triangle DEF` to its **orthic triangle** :math:`\triangle mnp` applies :math:`\theta \mapsto 180^\circ - 2\theta`, restoring the original angles:

  .. math::

     180^\circ - 2\left(90^\circ - \frac{1}{2}\alpha\right) = \alpha!

* Furthermore, by the tangent-chord theorem :just:`[III. 32] <III.32>`, every side of :math:`\triangle mnp` is parallel to the corresponding side of :math:`\triangle ABC`, yielding a pure homothety with ratio :math:`\frac{r}{2R}` and area ratio :math:`\frac{r^2}{4R^2}`.

2. Exact Verification of § 64 on the Canonical (15, 13, 14) Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With :math:`\Delta = 84`, :math:`R = \frac{65}{8}`, :math:`4R^2 = \frac{4225}{16}`, :math:`(r, r_a, r_b, r_c) = (4, 14, \frac{21}{2}, 12)`, and :math:`\rho = \frac{99}{52}`:

* Sum of derived contact-orthic areas: :math:`\sum \mu^{(k)} = \frac{125328}{845}`.
* Orthic area: :math:`\triangle MNP = \frac{\rho}{R}\Delta = \frac{16632}{845}`.
* Total: :math:`\sum \mu^{(k)} + \triangle MNP = \frac{141960}{845} = 168 = 2\Delta`.
