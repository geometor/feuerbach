:title: Feuerbach (1822) §§ 49–60 — Critical & Symbolic Notes
:layout: book

.. _fb-03-notes:

============================================================================================
Critical & Symbolic Notes — Unit III: Exact SymPy Audit of §§ 49–60 & The § 51 Sign Slip
============================================================================================

.. rubric:: Why Symbolic Verification Matters in Historical Editions

1. Discovery & Diagnosis of Feuerbach's § 51 / § 52 / § 60 Sign-Substitution Slip
---------------------------------------------------------------------------------

When encoding every equation of :cite:`Feuerbach (1822) <feuerbach_1822>` §§ 49–60 in :func:`geometor.feuerbach.euler.prove_euler_1765_identities` over :math:`\mathbb{Q}(a, b, c)` in :mod:`sympy`, a striking philological fact emerged on pages 35, 36, and 40–41:

* In **§ 51** (p. 35), :person:`Feuerbach <feuerbach>` proves directly from coordinates the 100% exact incenter quadrance

  .. math::

     \overline{OS}^2 = 2r^2 - 2\rho R.

* Immediately below on p. 35, he applies his customary substitution :math:`(a, b, c) \mapsto (-a, b, c)` (introduced in § 8, p. 6, where he noted ``r wird zu r' und +R zu -R``) to write

  .. math::

     \overline{OS^{(k)}}^2 \stackrel{\text{1822 text}}{=} 2r^{(k)2} + 2\rho R \qquad \text{(printed slip!)}.

* **Why this fails algebraically**: By **§ 24** (p. 18) and :math:`R = \frac{abc}{4\Delta}`,

  .. math::

     \rho = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{16abc\Delta},
     \qquad
     \rho R = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{64\Delta^2}.

  Under :math:`a \mapsto -a` (holding :math:`+\Delta` positive), **both** :math:`R` **and** :math:`\rho` **reverse sign** (:math:`R \mapsto -R` and :math:`\rho \mapsto -\rho`), so their product :math:`\rho R`—which depends solely on :math:`a^2, b^2, c^2`—is **strictly invariant**!

.. list-table:: Exact Symbolic Comparison on ``(a, b, c) = (15, 13, 14)`` (:math:`R = \tfrac{65}{8}, r = 4, r_a = 14, \rho = \tfrac{99}{52}`)
   :header-rows: 1
   :widths: 18 28 28 26

   * - Locus
     - 1822 Printed Formula
     - True Exact Formula (:mod:`sympy`)
     - Value on ``(15, 13, 14)`` (:math:`2\rho R = \frac{495}{16}`)
   * - **§ 51** (:math:`\overline{OS}^2`)
     - :math:`2r^2 - 2\rho R` (**exact**)
     - :math:`2r^2 - 2\rho R`
     - :math:`32 - \frac{495}{16} = \frac{17}{16}`
   * - **§ 51** (:math:`\overline{OS_a}^2`)
     - :math:`2r_a^2 + 2\rho R` (*slip*)
     - :math:`2r_a^2 - 2\rho R`
     - :math:`392 - \frac{495}{16} = \frac{5777}{16}` (printed gives :math:`\frac{6767}{16}`)
   * - **§ 52** (:math:`\sum \overline{OS_i}^2`)
     - :math:`4R(4R - \rho)` (*slip*)
     - :math:`16R(R - \rho)`
     - :math:`\frac{12935}{16}`
   * - **§ 57** (:math:`LS, LS_k`)
     - :math:`\frac{1}{2}R - r,\; \frac{1}{2}R + r_k` (**exact!**)
     - :math:`\left|\frac{1}{2}R - r\right|,\; \frac{1}{2}R + r_k`
     - :math:`\frac{1}{16},\; \frac{289}{16},\; \frac{233}{16},\; \frac{257}{16}`
   * - **§ 59** (:math:`\sum \overline{LS_i}^2`)
     - :math:`13R^2 - 4\rho R` (**exact!**)
     - :math:`13R^2 - 4\rho R`
     - :math:`\frac{52945}{64}`
   * - **§ 60** (:math:`\overline{GS}^2`)
     - :math:`\frac{2}{9}R(2R+\rho) - \frac{2}{3}r(2R-r)` (**exact**)
     - :math:`\frac{2}{9}R(2R+\rho) - \frac{2}{3}r(2R-r)`
     - :math:`\frac{1}{9}`
   * - **§ 60** (:math:`9\sum \overline{GS_i}^2`)
     - :math:`7\sum \overline{OS_i}^2 = 28R(4R-\rho)` (*slip*)
     - :math:`16R(7R - \rho)`
     - :math:`\frac{116855}{16}`

2. Why **§ 57 (Feuerbach's Theorem)** and **§ 59** Are 100% Unscathed!
----------------------------------------------------------------------

Why did the § 51 sign slip fail to corrupt **§ 57** or **§ 59**? Look at the exact order of operations on page 38 (`fb_058.jpg`):

1. First, for the **incenter** :math:`S` (where :math:`\overline{OS}^2 = 2r^2 - 2\rho R` is 100% exact!), Apollonius's median theorem :math:`2\overline{LS}^2 + 2\overline{OL}^2 = \overline{KS}^2 + \overline{OS}^2` cancels :math:`-2\rho R` against :math:`2\overline{OL}^2 = \frac{1}{2}R^2 - 2\rho R`, leaving :math:`LS = \frac{1}{2}R - r` **with** :math:`\rho` **eliminated**.
2. Second, rather than substituting his § 51 expression for :math:`\overline{OS'}^2` into the median theorem (which would have left a spurious :math:`+4\rho R`), Feuerbach substituted :math:`a, b, c \mapsto -a, -b, -c` **directly into** :math:`LS = \frac{1}{2}R - r`, where :math:`\rho` was already gone! Thus :math:`R \mapsto -R` and :math:`r \mapsto r^{(k)}` yielded the completely exact :math:`LS^{(k)} = \frac{1}{2}R + r^{(k)}`, and squaring those exact expressions in **§ 59** gave the exact sum :math:`13R^2 - 4\rho R` (which also validates :math:`\sum \overline{OS_i}^2 = 16R(R - \rho)` via :math:`2\sum \overline{LS_i}^2 + 8\overline{OL}^2 = \sum \overline{KS_i}^2 + \sum \overline{OS_i}^2`!).

3. Compositorial Typo in § 55 (p. 37) and Nine-Point History
------------------------------------------------------------

* **p. 37, § 55, line 6**: Prints ``OL^2 = 1/2 R^2 - rho R`` where § 54 (three lines above on p. 37) established ``OL^2 = 1/4 R^2 - rho R``; the immediately following deduction ``LP^2 - OL^2 = OP . Kc = rho R`` uses the true ``1/4 R^2 - rho R``.
* **From Six Points to Nine Points (1821–1842)**: In §§ 54–56 (and synthetically in `9. Satz`), Feuerbach explicitly proves concyclicity of the **six** points (three altitude feet + three side midpoints), while :person:`Brianchon <brianchon>` and :person:`Poncelet <poncelet>` (:cite:`1821 <brianchon_poncelet_1821>`) independently proved concyclicity of all nine points (adding the three Euler midpoints :g:`E_1 <0038.g1:E1>`, :g:`E_2 <0038.g1:E2>`, :g:`E_3 <0038.g1:E3>` of :math:`AO, BO, CO`), and :person:`Olry Terquem <terquem>` (:cite:`1842 <terquem_1842>`) coined the name *cercle des neuf points* (:term:`nine-point circle <nine-point-circle>`). Notably, Feuerbach already knew :math:`AO = 2\,Ka` (§ 47) and :math:`L = \operatorname{mid}(KO)` (§ 55), from which :math:`LE_a = LK_a`? Rather, :math:`LE_a = \frac{1}{2}AK = \frac{1}{2}R` follows in a single line by midline homothety!
