:layout: book
:canonical_id: §§ 54–57 (Notes)
:breadcrumb_title: Notes
:order: 1
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-03-notes:
.. _fb-notes-s54:

§§ 54–57: §§ 54–57: Feuerbach's Nine-Point Circle Tangency Theorem — Notes
==========================================================================

.. rubric:: Historical, Philological & Symbolic Commentary

GEOMETOR Commentary & Symbolic Notes
------------------------------------

1. Why § 57 (Feuerbach's Tangency Theorem) and § 59 Are 100% Unscathed!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crucially, Feuerbach's algebraic slip on the excenters in § 51 has **zero impact** on the validity of the Nine-Point Tangency Theorem in **§ 57**:

* In **§ 57**, Feuerbach applies Apollonius's median theorem in :math:`\triangle KOS`:

  .. math::

     2\overline{LS}^2 + 2\overline{OL}^2 = \overline{KS}^2 + \overline{OS}^2.

  Substituting :math:`\overline{OL}^2 = \frac{1}{4}R^2 - \rho R`, :math:`\overline{KS}^2 = R^2 - 2rR`, and the **exact** incenter distance :math:`\overline{OS}^2 = 2r^2 - 2\rho R`:

  .. math::

     2\overline{LS}^2 + 2\left(\frac{1}{4}R^2 - \rho R\right) = (R^2 - 2rR) + (2r^2 - 2\rho R).

  Observe that the term :math:`-2\rho R` **cancels identically from both sides of the equation**!
* Thus :math:`\overline{LS}^2 = (\frac{1}{2}R - r)^2`, yielding :math:`LS = |\frac{1}{2}R - r|`.
* Applying the sign substitution :math:`a \mapsto -a` to this simplified equation (which no longer contains :math:`\rho`!) sends :math:`R \mapsto -R` and :math:`r \mapsto r^{(k)}`, yielding the exact excenter distances:

  .. math::

     LS^{(k)} = \frac{1}{2}R + r^{(k)}.

  **Feuerbach's Theorem is 100% algebraically and geometrically exact!**

2. Exact Coordinates & Benchmarks on the Canonical (15, 13, 14) Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :mod:`geometor.feuerbach.tangency`:

* Nine-point center :math:`X(5) = (6, \frac{63}{16})` with radius :math:`R_9 = \frac{65}{16}`.
* Incenter :math:`X(1) = (6, 4)` with radius :math:`r = 4`.
* Inner tangency point: :term:`Feuerbach point <feuerbach-point>` :math:`X(11) = (6, 8)`.
* Distance :math:`X(5)X(1) = |\frac{65}{16} - 4| = \frac{1}{16}`, so quadrance :math:`Q(X_5, X_1) = \frac{1}{256}`.
* Excircle tangency points:
  :math:`Fe_a = (\frac{2709}{289}, \frac{1792}{289})`,
  :math:`Fe_b = (\frac{553}{233}, \frac{1344}{233})`,
  :math:`Fe_c = (\frac{1672}{257}, \frac{-24}{257})`.
