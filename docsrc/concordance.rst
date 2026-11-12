:title: Cross-Treatise Concordance & Notation Rosetta Stone
:layout: book

.. _concordance:

Cross-Treatise Concordance
==========================

.. rubric:: Unifying Euler (1765), Feuerbach (1822), Kimberling's ETC, Euclid, Ceva, Menelaus, and Altshiller-Court

Because :person:`Leonhard Euler <euler>` (1765/1767) and :person:`Karl Wilhelm Feuerbach <feuerbach>` (1822) wrote prior to modern standardized notation—and crucially reused letters such as :math:`G`, :math:`O`, and :math:`r` with **different meanings**—this concordance maps every center, circle, invariant, and theorem across the historical editions and the GEOMETOR ecosystem.

Notation Rosetta Stone
----------------------

.. list-table:: Historical vs. Modern Triangle-Center & Invariant Symbols
   :header-rows: 1
   :widths: 22 18 20 16 24

   * - Geometric Entity
     - Euler (1765, E325)
     - Feuerbach (1822)
     - ETC / Modern
     - Canonical ``(15, 13, 14)`` Value
   * - **Incenter**
     - :math:`G` (§ 4, § 8)
     - :math:`S` (§ 1)
     - ``X(1)`` (:math:`I`)
     - :math:`(6,\, 4)`
   * - **Centroid**
     - :math:`F` (§ 3, § 7)
     - :math:`G` (§ 60)
     - ``X(2)`` (:math:`G`)
     - :math:`\left(\frac{19}{3},\, 4\right)`
   * - **Circumcenter**
     - :math:`H` (§ 5, § 9)
     - :math:`K` (§ 4, § 49)
     - ``X(3)`` (:math:`O`)
     - :math:`\left(7,\, \frac{33}{8}\right)`
   * - **Orthocenter**
     - :math:`E` (§ 2, § 6)
     - :math:`O` (§ 19)
     - ``X(4)`` (:math:`H`)
     - :math:`\left(5,\, \frac{15}{4}\right)`
   * - **Nine-Point Center**
     - Midpoint of :math:`EH` (§ 25)
     - :math:`L` (§ 54, 9. Satz)
     - ``X(5)`` (:math:`N`)
     - :math:`\left(6,\, \frac{63}{16}\right)`
   * - **Feuerbach Point**
     - —
     - Inner tangency (§ 57)
     - ``X(11)`` (:math:`F_e`)
     - :math:`(6,\, 8)`
   * - **Three Excenters**
     - —
     - :math:`S', S'', S'''` (§ 1)
     - :math:`J_a, J_b, J_c`
     - :math:`(21, 14),\; (-7, \frac{21}{2}),\; (8, -12)`
   * - **Excircle Tangencies**
     - —
     - Outer tangencies (§ 57)
     - :math:`Fe_a, Fe_b, Fe_c`
     - :math:`(\frac{2709}{289}, \frac{1792}{289}),\; (\frac{553}{233}, \frac{1344}{233}),\; (\frac{1672}{257}, \frac{-24}{257})`
   * - **Symbol** :math:`r`
     - **Side product** :math:`abc` (§ 10)!
     - **Inradius** :math:`\Delta / s` (§ 2)
     - :math:`abc` vs. :math:`r`
     - :math:`r_{\text{Euler}} = 2730` vs. :math:`r_{\text{inc}} = 4`
   * - **Triangle Area**
     - :math:`A` (§ 6)
     - :math:`\Delta` (§ 2)
     - :math:`\Delta`
     - :math:`84`
   * - **Circumradius / Nine-Point Radius**
     - :math:`\frac{r}{4A}` (§ 20: :math:`R = 4R_{\text{circ}}^2`)
     - :math:`R` and :math:`\frac{1}{2}R` (§ 26)
     - :math:`R,\; R_9 = \frac{1}{2}R`
     - :math:`R = \frac{65}{8},\; R_9 = \frac{65}{16}`
   * - **Orthic Inradius**
     - —
     - :math:`\rho = 2R\cos\alpha\cos\beta\cos\gamma` (§ 24)
     - :math:`\rho`
     - :math:`\frac{99}{52}`

Theorem & Proposition Concordance
---------------------------------

.. list-table:: Cross-Corpus Structural & Algebraic Concordance
   :header-rows: 1
   :widths: 22 20 22 18 18

   * - Theorem / Locus
     - Euler (1765/1767)
     - Feuerbach (1822)
     - Sister Codices
     - Symbolic Identity
   * - **Cevian Concurrency of Classical Centers**
     - §§ 2–5 (Tab. II Fig. 1–4)
     - § 1, § 19, § 60, Anhang 1.–4. Satz
     - ``ceva`` (1678); ``euclid`` IV.4, IV.5
     - :math:`\frac{AF}{FB}\frac{BD}{DC}\frac{CE}{EA} = 1`
   * - **Euler Line & Harmonic Cross-Ratio**
     - §§ 16–18 (:math:`EH = \frac{3}{2}EF`)
     - §§ 54–55, § 60 (:math:`GL = \frac{1}{6}KO`)
     - ``menelaus``; ``pappus``; ``altshiller-court`` § 191
     - :math:`(X_4, X_2; X_5, X_3) = -1`
   * - **Euler's Incenter–Circumcenter Theorem**
     - § 15 & § 18 VI
     - § 49 (explicitly cites Euler 1765 & Fuß 1797)
     - ``altshiller-court`` § 186; ``wildberger``
     - :math:`Q(X_3, X_1) = R^2 - 2Rr`
   * - **Euler–Stewart Four-Center Law**
     - § 18 (p. 114)
     - § 60 (p. 40)
     - ``wildberger``
     - :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2`
   * - **Inverse Cubic Reconstruction**
     - §§ 19–24, § 34
     - *Vorrede* (pp. V–XII)
     - ``etc``
     - :math:`z^3 - pz^2 + qz - r = 0`
   * - **Tritangent Radii Symmetry**
     - § 8, § 10
     - §§ 2–5, § 28 (cites L'Huilier 1810)
     - ``altshiller-court`` §§ 144–152
     - :math:`r' + r'' + r''' - r = 4R`
   * - **Orthic Perimeter & Area Mean**
     - —
     - § 19 (cites Fagnano 1775), §§ 61–65, Anhang 5.–8. Satz
     - ``euclid`` VI.4, VI.16
     - :math:`\mu : \delta = \delta : \Delta`
   * - **Nine-Point Circle Locus**
     - —
     - §§ 26, 54–56, Anhang **9. Satz** (p. 62)
     - ``altshiller-court`` §§ 195–201; ``etc`` ``X(5)``
     - :math:`LM = LN = LP = \frac{1}{2}R`
   * - **Feuerbach's Fourfold Tangency Theorem**
     - —
     - **§ 57** (pp. 37–38, Tab. II Fig. 7)
     - ``etc`` ``X(11)``; ``altshiller-court`` § 215
     - :math:`LS = |\frac{1}{2}R - r|,\; LS^{(k)} = \frac{1}{2}R + r^{(k)}`
