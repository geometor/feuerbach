:title: Euler (1765) §§ 10–18 — Summary
:layout: book

.. _euler-02-summary:

====================================================================
Summary — Unit II: Six Mutual Quadrances & The Euler Line (§§ 10–18)
====================================================================

.. rubric:: Analytical Synopsis of §§ 10–18 (pp. 107–114)

1. **Symmetric Basis (§ 11)**: Because the mutual distances among :math:`E, F, G, H` cannot privilege any side of :math:`\triangle ABC`, :person:`Euler <euler>` introduces :math:`p = a+b+c`, :math:`q = ab+ac+bc`, :math:`r = abc`, rewriting Heron's formula as :math:`16\mathcal{A}^2 = -p^4 + 4p^2q - 8pr`. Since :math:`R_{\text{circ}} = \frac{abc}{4\mathcal{A}} = \frac{r}{4\mathcal{A}}` and :math:`r_{\text{in}} = \frac{2\mathcal{A}}{p}`, the ubiquitous quantity :math:`\frac{r^2}{16\mathcal{A}^2}` is simply :math:`R_{\text{circ}}^2`, and :math:`\frac{r}{p} = 2R_{\text{circ}}r_{\text{in}}`.

2. **Euler's Six Squared-Distance Table (§ 18, Formulas I–VI)** (alongside modern radius forms):

   .. list-table:: Euler's Six Mutual Quadrances (§ 18, p. 114)
      :header-rows: 1
      :widths: 16 44 40

      * - Segment
        - Euler's Symmetric Form (:math:`p, q, r, \mathcal{A}`)
        - Radius / Side-Square Form (:math:`R, r_{\text{in}}, a, b, c`)
      * - :math:`EF^2`
        - :math:`\dfrac{r^2}{4\mathcal{A}^2} - \dfrac{4}{9}(p^2 - 2q)`
        - :math:`4R^2 - \dfrac{4}{9}(a^2 + b^2 + c^2)`
      * - :math:`EG^2`
        - :math:`\dfrac{r^2}{4\mathcal{A}^2} - p^2 + 3q - \dfrac{4r}{p}`
        - :math:`4R^2 + 4Rr_{\text{in}} + 3r_{\text{in}}^2 - s^2 = 2r_{\text{in}}^2 - 4R^2\cos\alpha\cos\beta\cos\gamma`
      * - :math:`EH^2`
        - :math:`\dfrac{9r^2}{16\mathcal{A}^2} - p^2 + 2q`
        - :math:`9R^2 - (a^2 + b^2 + c^2)`
      * - :math:`FG^2`
        - :math:`-\dfrac{1}{9}p^2 + \dfrac{5}{9}q - \dfrac{2r}{p}`
        - :math:`\dfrac{1}{9}(s^2 + 5r_{\text{in}}^2 - 16Rr_{\text{in}})`
      * - :math:`FH^2`
        - :math:`\dfrac{r^2}{16\mathcal{A}^2} - \dfrac{1}{9}(p^2 - 2q)`
        - :math:`R^2 - \dfrac{1}{9}(a^2 + b^2 + c^2)`
      * - :math:`GH^2`
        - :math:`\dfrac{r^2}{16\mathcal{A}^2} - \dfrac{r}{p}`
        - :math:`R^2 - 2Rr_{\text{in}} = R(R - 2r_{\text{in}})`

3. **Three Landmark Theorems on One Page (p. 114)**:

   * **Euler's Incenter–Circumcenter Theorem (§ 17, VI)**: :math:`GH^2 = R^2 - 2Rr_{\text{in}}` (whence :math:`R \ge 2r_{\text{in}}` with equality iff equilateral).
   * **The Euler Line (§§ 16, 18)**: :math:`E, F, H` are collinear in every triangle with :math:`F` between :math:`E` and :math:`H` and :math:`EF : FH = 2 : 1` (:math:`EH = \frac{3}{2}EF`).
   * **Stewart's Collinearity Constraint (§ 18)**: Because :math:`F` divides :math:`EH` in the ratio :math:`2 : 1`, the four centers satisfy :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2`, meaning the four inverse problems of § 2 Collapse into a **single** three-parameter problem!
