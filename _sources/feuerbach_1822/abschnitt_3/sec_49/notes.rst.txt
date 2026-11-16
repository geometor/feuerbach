:layout: book
:canonical_id: § 49 (Notes)
:breadcrumb_title: Notes
:order: 1
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _fb-notes-s49:

§ 49: § 49: Distances from Circumcenter K to S, S', S'', S''' — Euler (1765) & Fuß (1797) — Notes
=================================================================================================

.. rubric:: Historical, Philological & Symbolic Commentary

GEOMETOR Commentary & Symbolic Notes
------------------------------------

1. Discovery & Diagnosis of Feuerbach's § 51 / § 52 / § 60 Sign-Substitution Slip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When encoding every equation of :cite:`Feuerbach (1822) <feuerbach_1822>` §§ 49–60 in :func:`geometor.feuerbach.euler.prove_euler_1765_identities` over :math:`\mathbb{Q}(a, b, c)` in :mod:`sympy`, a striking philological fact emerged on pages 35, 36, and 40–41:

* In **§ 51** (p. 35), :person:`Feuerbach <feuerbach>` proves directly from coordinates the 100% exact incenter quadrance

  .. math::

     \overline{OS}^2 = 2r^2 - 2\rho R.

* Immediately below on p. 35, he applies his customary substitution :math:`(a, b, c) \mapsto (-a, b, c)` to write:

  .. math::

     \overline{OS^{(k)}}^2 \stackrel{\text{1822 text}}{=} 2r^{(k)2} + 2\rho R \qquad \text{(printed slip!)}.

* **Why this fails algebraically**: By **§ 24** (p. 18) and :math:`R = \frac{abc}{4\Delta}`,

  .. math::

     \rho R = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{64\Delta^2}.

  Under :math:`a \mapsto -a` (holding :math:`+\Delta` positive), **both** :math:`R` **and** :math:`\rho` **reverse sign** (:math:`R \mapsto -R` and :math:`\rho \mapsto -\rho`), so their product :math:`\rho R` is **strictly invariant**!
  The true exact identities over :math:`\mathbb{Q}(a,b,c)` are :math:`\overline{OS^{(k)}}^2 = 2r^{(k)2} - 2\rho R`, and the true sum is :math:`\sum \overline{OS_i}^2 = 16R(R - \rho)`.
