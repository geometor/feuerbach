:title: Euler (1765) §§ 1–9 — Summary
:layout: book

.. _euler-01-summary:

======================================================
Summary — Unit I: The Four Classical Centers (§§ 1–9)
======================================================

.. rubric:: Analytical Synopsis of §§ 1–9 (pp. 103–107)

1. **Problem Statement (§§ 1–3)**: :person:`Euler <euler>` isolates the four classical concurrency centers of a non-equilateral plane triangle :math:`\triangle ABC` with side lengths :math:`BC = a`, :math:`AC = b`, :math:`AB = c`, and area :math:`\mathcal{A}`:

   * :math:`E = X(4)` — orthocenter (intersection of altitudes),
   * :math:`F = X(2)` — centroid (intersection of medians),
   * :math:`G = X(1)` — incenter (intersection of internal angle bisectors),
   * :math:`H = X(3)` — circumcenter (intersection of perpendicular bisectors).

   Given any three of these four points in position, the triangle is determined (save in the equilateral case where all four coalesce).

2. **Orthogonal Coordinate Table on Base AB (§§ 5–9)**: Taking vertex :math:`A` as origin and base :math:`AB = c` along the positive abscissa axis, Euler expresses every abscissa and ordinate purely as rational functions of :math:`(a, b, c)` and :math:`\mathcal{A}`:

   .. list-table:: Euler's Base Coordinates (§§ 6–9)
      :header-rows: 1
      :widths: 18 18 32 32

      * - Euler Point
        - Kimberling ID
        - Abscissa along :math:`AB`
        - Ordinate normal to :math:`AB`
      * - :math:`E` (Orthocenter)
        - :math:`X(4)`
        - :math:`AP = \dfrac{c^2 + b^2 - a^2}{2c}`
        - :math:`PE = \dfrac{(c^2 + b^2 - a^2)(a^2 + c^2 - b^2)}{8c\mathcal{A}}`
      * - :math:`F` (Centroid)
        - :math:`X(2)`
        - :math:`AQ = \dfrac{3c^2 + b^2 - a^2}{6c}`
        - :math:`QF = \dfrac{2\mathcal{A}}{3c}`
      * - :math:`G` (Incenter)
        - :math:`X(1)`
        - :math:`AR = \dfrac{c + b - a}{2}`
        - :math:`RG = \dfrac{2\mathcal{A}}{a + b + c}`
      * - :math:`H` (Circumcenter)
        - :math:`X(3)`
        - :math:`AS = \dfrac{c}{2}`
        - :math:`SH = \dfrac{c(a^2 + b^2 - c^2)}{8\mathcal{A}}`

3. **Immediate Vectorial Consequence**: Even before computing squared distances in Unit II, comparing :math:`(AP, PE)`, :math:`(AQ, QF)`, and :math:`(AS, SH)` already reveals :math:`AQ - AS = \frac{b^2 - a^2}{6c} = \frac{1}{3}(AP - AS)` and :math:`QF - SH = \frac{1}{3}(PE - SH)` via Heron's expansion :math:`16\mathcal{A}^2 = 2a^2b^2 + 2a^2c^2 + 2b^2c^2 - a^4 - b^4 - c^4`, foreshadowing the :term:`Euler Line <euler-line>` vector law :math:`\overrightarrow{HF} = \frac{1}{3}\overrightarrow{HE}`.
