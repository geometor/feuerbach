:title: Feuerbach (1822) §§ 1–18 — Critical & Symbolic Notes
:layout: book

.. _fb-01-notes:

==============================================================================
Critical & Symbolic Notes — Unit I: The Four Tritangent Centers (§§ 1–18)
==============================================================================

.. rubric:: Feuerbach's Sign-Flip Automorphism :math:`a \mapsto -a` and Circumcircle Duality

1. **The Algebraic Sign-Flip Principle (§ 8, p. 6)**: Already on page 6, :person:`Feuerbach <feuerbach>` explicitly articulates the algebraic transformation that governs his entire monograph: replacing :math:`+a` by :math:`-a` while holding :math:`+b, +c` and the positive magnitude of :math:`\Delta` fixed sends

   .. math::

      r = \frac{2\Delta}{a+b+c} \longmapsto r' = \frac{2\Delta}{-a+b+c},
      \qquad
      R = \frac{abc}{4\Delta} \longmapsto \frac{(-a)bc}{4\Delta} = -R.

   Notice how carefully Feuerbach records ``+R zu -R`` on p. 6! In §§ 8, 11, 13, and 57 this rule works without flaw because :math:`R` appears linearly (or after :math:`\rho` has cancelled). In **§ 51** (p. 35), however, applying the same rule mechanically to :math:`\overline{OS}^2 = 2r^2 - 2\rho R` without tracking that :math:`\rho` *also* negates under :math:`a \mapsto -a` produces the celebrated sign slip analyzed in :ref:`Unit III Notes <fb-03-notes>`.

2. **Circumcircle of ABC as Nine-Point Circle of the Excentral Triangle**: In **§ 1** (p. 2) Feuerbach proves that :math:`\triangle ABC` is the :term:`orthic triangle <orthic-triangle>` of the excentral triangle :math:`\triangle S'S''S'''`, with :math:`S = X(1)` as its orthocenter. Combined with **§ 17** (:math:`SS'^2 + S''S'''^2 = (4R)^2`), this means that the circumcircle :math:`(ABC)` of radius :math:`R` is simultaneously the :term:`nine-point circle <nine-point-circle>` of :math:`\triangle S'S''S'''`, whose circumradius is :math:`R_{\text{ex}} = 2R`!

3. **Exact Benchmark Values on the Canonical (15, 13, 14) Triangle**:
   In :func:`~geometor.feuerbach.primitives.construct_fundamental_centers` and :func:`~geometor.feuerbach.tangency.construct_feuerbach_tangency`, with :math:`(a, b, c) = (15, 13, 14)`, :math:`\Delta = 84`, :math:`s = 21`, :math:`R = \frac{65}{8}`:

   * Tritangent radii: :math:`r = 4`, :math:`r' = r_a = 14`, :math:`r'' = r_b = \frac{21}{2}`, :math:`r''' = r_c = 12`.
   * Verification of **§ 2**: :math:`rr'r''r''' = 4 \cdot 14 \cdot \frac{21}{2} \cdot 12 = 7056 = 84^2 = \Delta^2`.
   * Verification of **§ 5**: :math:`r' + r'' + r''' - r = 14 + \frac{21}{2} + 12 - 4 = \frac{65}{2} = 4 \cdot \frac{65}{8} = 4R`.
