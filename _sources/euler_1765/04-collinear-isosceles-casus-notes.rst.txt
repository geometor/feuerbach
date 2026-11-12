:title: Euler (1765) §§ 25–34 — Critical & Symbolic Notes
:layout: book

.. _euler-04-notes:

===========================================================================================
Critical & Symbolic Notes — Unit IV: Isosceles Locus, 60° Family & Trisection (§§ 25–34)
===========================================================================================

.. rubric:: Foreshadowing X(5), the 60° Locus EG = GH, and Philological Audit of §§ 29–34

1. Euler's Half-Segment d = ½ EH (§ 29) and the Nine-Point Center X(5)
----------------------------------------------------------------------

In **§§ 28–29** (pp. 119–120), :person:`Euler <euler>` bisects the segment :math:`EH` (:math:`= 2d`) and classifies every isosceles triangle according as :math:`EG < d` (`Fig. 8`, :math:`a > c`) or :math:`EG > d` (`Fig. 9`, :math:`a < c`). Geometrically, the midpoint of :math:`EH` is precisely :person:`Feuerbach <feuerbach>`'s **nine-point center** :math:`L = X(5)`. By Feuerbach's Theorem (**§ 57**), :math:`LG = \tfrac{1}{2}R_{\text{circ}} - r_{\text{in}}`, which vanishes only when :math:`R_{\text{circ}} = 2r_{\text{in}}` (the equilateral triangle). Since :math:`E, G, L, F, H` all lie along the axis of symmetry of an isosceles triangle with :math:`EL = LH = d`, the non-vanishing distance :math:`LG > 0` explains geometrically why Euler's two regimes :math:`EG < d` (:math:`a > c`, where :math:`G` lies inside :math:`EL`) and :math:`EG > d` (:math:`a < c`, where :math:`G` lies inside :math:`LF`) are separated exclusively by the equilateral coalescence.

2. Why EG = GH (§§ 32–33) Characterizes Triangles with a 60° Angle
------------------------------------------------------------------

In **§§ 32–33** (pp. 121–122), Euler discovers algebraically that whenever :math:`e = f` (:math:`EG = GH`), the side-length cubic factors rationally with root :math:`c = \frac{f^2\sqrt{3}}{\sqrt{4f^2 - k^2}} = R_{\text{circ}}\sqrt{3}`. Geometrically, :math:`c = 2R_{\text{circ}}\sin C = R_{\text{circ}}\sqrt{3}` means :math:`C = 60^\circ` (or :math:`120^\circ`, excluded here since :math:`Q > 0` fixes :math:`C = 60^\circ`)! Indeed, at a :math:`60^\circ` vertex :math:`C`, the distance from the circumcenter :math:`H` to :math:`AB` is :math:`R_{\text{circ}}\cos 60^\circ = \tfrac{1}{2}R_{\text{circ}}`, and reflection properties of :math:`X(1), X(3), X(4)` force :math:`X(1)X(4) = X(1)X(3)`. For Euler's numerical choice :math:`e^2 = f^2 = 2, k^2 = 7` (§ 32), the sides :math:`a = \frac{3\sqrt{3}+\sqrt{7}}{2}`, :math:`b = \frac{3\sqrt{3}-\sqrt{7}}{2}`, :math:`c = 2\sqrt{3}` satisfy :math:`a^2 + b^2 - ab = \frac{27 + 7}{2} - \frac{27 - 7}{4} = 17 - 5 = 12 = c^2`, confirming :math:`\angle C = 60^\circ`!

3. Audit of Four Arithmetic/Printing Slips in §§ 29–34 (pp. 120–123)
--------------------------------------------------------------------

* **p. 120, § 29**: In the second case (:math:`EG = d + e`), the folio prints ``OE = (d + e)^2 / (2e)``; substituting :math:`a, c` into :math:`HO = \frac{2a^2 - c^2}{2\sqrt{4a^2 - c^2}}` gives :math:`OE = \frac{(d + e)^2}{4e}` (matching ``(d - e)^2 / (4e)`` in the first case).
* **p. 121, § 30, last line**: In the normalized cubic :math:`y^3 - y^2 + \frac{q}{P}y - \frac{Q}{P} = 0`, the folio's numerator prints ``+ 3eekk`` for ``- 3eekk`` in :math:`q` and omits the factor :math:`(2e^2 + 2f^2 - k^2)` multiplying :math:`f^2(k^2 - 2e^2 - f^2)` in the constant term.
* **p. 121, § 31**: Euler's positivity conditions :math:`2e^2 + f^2 < k^2 < 2e^2 + 2f^2` are exact (equivalent to :math:`Q > 0` and :math:`R > 0`, i.e., :math:`2Rr_{\text{in}} > 0` and :math:`4R^2 > 0`), whereas his quick elimination for :math:`f^2 / e^2` treats :math:`P > 0` as binding; in fact, on any real triangle :math:`P = p^2 > 0` holds automatically once the depressed cubic discriminant (Blundon's inequality) is non-negative! Indeed, in Euler's own valid example in **§ 34** (:math:`e^2 = 3, f^2 = 2, k^2 = 9`), :math:`\frac{f^2}{e^2} = \frac{2}{3} = \frac{38}{57}` satisfies :math:`\frac{8}{19} < \frac{2}{3} < \frac{19}{13}`, and even triangles with :math:`e = 0` (:math:`X(1) = X(4)`, impossible for non-equilateral) are excluded by Blundon's fundamental triangle inequality.
* **p. 123, § 34**: For :math:`e^2 = 3, f^2 = 2, k^2 = 9`, we get :math:`2e^2 + 2f^2 - k^2 = 1`, :math:`R = 16`, :math:`Q = 2`, :math:`P = 71`, :math:`q = 22`, so Euler's cubic :math:`z^3 - \sqrt{71}\,z^2 + 22z - 2\sqrt{71} = 0` is **100% exact**! Depressing via :math:`z = \frac{1}{3}\sqrt{71} + t` gives

  .. math::

     t^3 - \frac{5}{3}t + \frac{2\sqrt{71}}{27} = 0.

  Comparing with :math:`\cos\alpha` in :math:`t = -\frac{2}{3}\sqrt{5}\cos\frac{\theta}{3}` gives :math:`\cos\alpha = \frac{\sqrt{71}}{5\sqrt{5}} = \sqrt{\frac{71}{125}}` (Euler's manuscript slipped :math:`5^3 = 125 \to 75`, and his angle :math:`11^\circ 32' 13'' = \arccos\sqrt{24/25}` corresponds to :math:`72/75`). With the exact :math:`\alpha = \arccos\sqrt{\frac{71}{125}} \approx 41^\circ 03' 16''`, Euler's trisection formulas :math:`a = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cos(60^\circ - \frac{1}{3}\alpha) \approx 3.84713`, :math:`b = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cos(60^\circ + \frac{1}{3}\alpha) \approx 3.06379`, :math:`c = \frac{1}{3}\sqrt{71} - \frac{2}{3}\sqrt{5}\cos\frac{1}{3}\alpha \approx 1.51523` satisfy :math:`a + b + c = \sqrt{71}`, :math:`ab + ac + bc = 22`, and :math:`abc = 2\sqrt{71}` to full precision!
