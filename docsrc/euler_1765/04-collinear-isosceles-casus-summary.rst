:title: Euler (1765) §§ 25–34 — Summary
:layout: book

.. _euler-04-summary:

===============================================================================
Summary — Unit IV: Collinear Centers, 60° Family & Angle Trisection (§§ 25–34)
===============================================================================

.. rubric:: Analytical Synopsis of §§ 25–34 (pp. 117–123)

1. **Isosceles Characterization of Euler-Line Collinearity (§§ 25–29)**:
   The incenter :math:`G = X(1)` lies on the :term:`Euler Line <euler-line>` :math:`EH` if and only if :math:`\triangle ABC` is **isosceles** (:math:`a = b`). Setting :math:`EH = 2d` around the midpoint of :math:`EH` (namely the **nine-point center** :math:`L = X(5)`!) and :math:`EG = d \mp e`:

   * When :math:`a > c` (tall isosceles, `Fig. 8`), :math:`EG < d = \frac{1}{2}EH`, so :math:`G` lies between :math:`E` and the nine-point center!
   * When :math:`a < c` (wide isosceles, `Fig. 9`), :math:`d < EG < \frac{4}{3}d = EF` (:math:`d > 3e`), so :math:`G` lies strictly between the nine-point center and the centroid :math:`F`!

2. **Symmetric (e, f, k) = (EG, GH, EH) Parameterization (§§ 30–31)**:
   Eliminating the centroid :math:`F` expresses :math:`R, Q, P` directly in terms of the three sides :math:`(e, f, k)` of :math:`\triangle EGH`, requiring :math:`2e^2 + f^2 < k^2 < 2e^2 + 2f^2` (equivalent to :math:`Q > 0` and :math:`R > 0`, i.e., :math:`EG^2 < 2FH^2 + FG^2` and :math:`GH^2 > 0`).

3. **Two Compass-Constructible vs. Trisection Regimes (§§ 32–34)**:

   * **Equidistant Locus EG = GH (§§ 32–33)**: Whenever :math:`e = f` (:math:`X(1)` equidistant from :math:`X(4)` and :math:`X(3)`), one angle of :math:`\triangle ABC` equals :math:`60^\circ` (:math:`\cos\gamma = \frac{1}{2}`), giving :math:`c = R_{\text{circ}}\sqrt{3}` and splitting the cubic into a rational linear factor and a quadratic!
   * **General Casus Irreducibilis (§ 34)**: For generic :math:`(e, f, k)` such as :math:`(e^2, f^2, k^2) = (3, 2, 9)`, the cubic :math:`z^3 - \sqrt{71}\,z^2 + 22z - 2\sqrt{71} = 0` is irreducible with three real positive roots, requiring trigonometric **angle trisection**.
