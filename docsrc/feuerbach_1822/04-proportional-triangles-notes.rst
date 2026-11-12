:title: Feuerbach (1822) §§ 61–87 — Critical & Symbolic Notes
:layout: book

.. _fb-04-notes:

======================================================================================
Critical & Symbolic Notes — Unit IV: Homothety & Derived Triangles (§§ 61–87)
======================================================================================

.. rubric:: Why Two Dual Pedal/Contact Operations Restore Parallel Sides

1. **Angle-Doubling & Homothety**:
   In any acute triangle :math:`ABC` with angles :math:`(\alpha, \beta, \gamma)`:

   * Passing to the **contact triangle** :math:`\triangle DEF` replaces :math:`(\alpha, \beta, \gamma)` by :math:`\left(90^\circ - \tfrac{1}{2}\alpha, 90^\circ - \tfrac{1}{2}\beta, 90^\circ - \tfrac{1}{2}\gamma\right)`.
   * Passing from :math:`\triangle DEF` to its **orthic triangle** :math:`\triangle mnp` (:math:`\mu`) applies :math:`\theta \mapsto 180^\circ - 2\theta`, restoring :math:`180^\circ - 2(90^\circ - \tfrac{1}{2}\alpha) = \alpha`! Moreover, the tangent-chord theorem :just:`[III. 32] <III.32>` aligns each side of :math:`\triangle mnp` parallel to the corresponding side of :math:`\triangle ABC` with homothety ratio :math:`\frac{r}{2R}` (hence area ratio :math:`\frac{r^2}{4R^2}`, proving **§ 63** and **§ 65** simultaneously!).

2. **Exact Verification of § 64 on the Canonical (15, 13, 14) Triangle**:
   With :math:`\Delta = 84`, :math:`R = \frac{65}{8}`, :math:`4R^2 = \frac{4225}{16}`, :math:`(r, r_a, r_b, r_c) = \left(4, 14, \frac{21}{2}, 12\right)`, and :math:`\rho = \frac{99}{52}`:

   * :math:`\mu + \mu' + \mu'' + \mu''' = \frac{84}{4225/16}\left(16 + 196 + \frac{441}{4} + 144\right) = \frac{1344}{4225} \cdot \frac{1865}{4} = \frac{336 \cdot 373}{845} = \frac{125328}{845}`.
   * :math:`\triangle MNP = \frac{\rho}{R}\Delta = \frac{99/52}{65/8} \cdot 84 = \frac{198}{845} \cdot 84 = \frac{16632}{845}`, whence :math:`\sum \mu^{(k)} + \triangle MNP = \frac{125328 + 16632}{845} = \frac{141960}{845} = 168 = 2\Delta`.
