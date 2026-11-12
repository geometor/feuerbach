:title: Feuerbach (1822) §§ 19–48 — Critical & Symbolic Notes
:layout: book

.. _fb-02-notes:

======================================================================================
Critical & Symbolic Notes — Unit II: Orthocenter & Orthic Inradius ρ (§§ 19–48)
======================================================================================

.. rubric:: Parity of :math:`\rho R`, Translation to Euler's :math:`(p, q, r)`, and ``(15, 13, 14)`` Values

1. **Exact Bridge Between Feuerbach's ρ and Euler's (p, q, r)**:
   Comparing **§ 27** (:math:`a^2 + b^2 + c^2 = 8R^2 + 4\rho R`) with :person:`Euler <euler>`'s **§ 14** (:math:`EH^2 = 9R^2 - (a^2 + b^2 + c^2)`) immediately yields

   .. math::

      \overline{KO}^2 = EH^2 = R^2 - 4\rho R = R(R - 4\rho),

   which is precisely **§ 53** of Feuerbach's monograph! Expressing :math:`\rho R` in terms of the side squares (**§ 24** and :math:`R = \frac{abc}{4\Delta}`):

   .. math::

      \rho R = \frac{(-a^2 + b^2 + c^2)(a^2 - b^2 + c^2)(a^2 + b^2 - c^2)}{64\Delta^2}.

   Observe that **every side** :math:`a, b, c` **enters** :math:`\rho R` **exclusively through its square** :math:`a^2, b^2, c^2`! Consequently, :math:`\rho R` is strictly **invariant** under :math:`a \mapsto -a` (because :math:`R \mapsto -R` and :math:`\rho \mapsto -\rho` simultaneously).

2. **Duality Between Sections I and II (§ 1 vs. § 24)**:
   Feuerbach systematically exploits the self-duality of orthocentric quadrangles:

   * For the **excentral quadrangle** :math:`(S, S', S'', S''')`, the pedal triangle is :math:`\triangle ABC` (circumradius :math:`R = \frac{1}{2}R_{\text{ex}}`).
   * For the **orthocentric quadrangle** :math:`(O, A, B, C)`, the pedal triangle is :math:`\triangle MNP` (circumradius :math:`R_{MNP} = \frac{1}{2}R`), so every identity of Section I (§§ 2–7) carries over instantaneously to :math:`(\rho, \rho^{(1)}, \rho^{(2)}, \rho^{(3)})` in **§ 30** (p. 21)!

3. **Exact Rational Values on the Canonical (15, 13, 14) Triangle**:
   On :math:`A = (0, 0), B = (14, 0), C = (5, 12)` (:math:`a = 15, b = 13, c = 14`, :math:`\Delta = 84`, :math:`R = \frac{65}{8}`):

   * Cosine product: :math:`\cos\alpha = \frac{33}{65}`, :math:`\cos\beta = \frac{3}{5}`, :math:`\cos\gamma = \frac{5}{13}`, so :math:`\cos\alpha\cos\beta\cos\gamma = \frac{99}{845}`, whence :math:`\rho = 2 \cdot \frac{65}{8} \cdot \frac{99}{845} = \frac{99}{52}`.
   * Check **§ 27**: :math:`8R^2 + 4\rho R = 8 \cdot \frac{4225}{64} + 4 \cdot \frac{99}{52} \cdot \frac{65}{8} = \frac{4225}{8} + \frac{495}{8} = \frac{4720}{8} = 590 = 15^2 + 13^2 + 14^2`!
   * Check **§ 28**: :math:`4R(2R - \rho) = \frac{65}{2}\left(\frac{65}{4} - \frac{99}{52}\right) = \frac{65}{2} \cdot \frac{746}{52} = \frac{1865}{4} = 4^2 + 14^2 + \left(\frac{21}{2}\right)^2 + 12^2 = 16 + 196 + \frac{441}{4} + 144 = \frac{1865}{4}`!
