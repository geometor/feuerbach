:title: Euler (1765) §§ 19–24 — Summary
:layout: book

.. _euler-03-summary:

====================================================================
Summary — Unit III: Inverse Reconstruction & Side Cubic (§§ 19–24)
====================================================================

.. rubric:: Analytical Synopsis of §§ 19–24 (pp. 114–118)

1. **Why the System Collapses to Rational Linear Equations (§§ 19–21)**:
   Introducing homogeneous dimension-2 invariants :math:`P = p^2`, :math:`Q = \frac{r}{p} = 2R_{\text{circ}}r_{\text{in}}`, and :math:`R = \frac{r^2}{4\mathcal{A}^2} = 4R_{\text{circ}}^2` turns Equations I, II, III of § 21 into:

   * :math:`R = 4(f^2 + Q)` from Equation I;
   * Eliminating :math:`\frac{Q^2}{R}` between Equations II and III via :math:`5\,\text{II} - 2\,\text{III}` gives a *purely linear* relation among :math:`P, Q, R`:

     .. math::

        5g^2 - 2h^2 = \frac{5}{4}R - \frac{1}{3}P + 4Q.

   Substituting :math:`R = 4(f^2 + Q)` yields :math:`P = 27Q + 15f^2 - 15g^2 + 6h^2`, and substituting into :math:`\frac{Q^2}{R}` cancels :math:`Q^2` identically! Hence :math:`(R, Q, P)` are **rational** functions of the given quadrances :math:`(f^2, g^2, h^2) = (GH^2, FH^2, FG^2)`.

2. **Viète's Side-Length Cubic (§ 22)**:
   A single square root :math:`p = \sqrt{P}` recovers the perimeter :math:`p`, symmetric sum :math:`q`, and product :math:`r = Qp`, yielding :math:`(z - a)(z - b)(z - c) = z^3 - pz^2 + qz - r = 0`.

3. **Benchmark Reconstructions (:func:`~geometor.feuerbach.euler.solve_euler_reconstruction_cubic`)**:

   * **Euler's Example (§§ 23–24)**: :math:`(f^2, g^2, h^2) = \left(\frac{35}{32}, \frac{155}{288}, \frac{1}{9}\right) \implies z^3 - 18z^2 + 107z - 210 = 0 \implies (5, 6, 7)`.
   * **GEOMETOR Canonical Heronian Example**: :math:`(f^2, g^2, h^2) = \left(\frac{65}{64}, \frac{265}{576}, \frac{1}{9}\right) \implies z^3 - 42z^2 + 587z - 2730 = 0 \implies (13, 14, 15)`.
