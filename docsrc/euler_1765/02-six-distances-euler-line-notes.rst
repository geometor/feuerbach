:title: Euler (1765) §§ 10–18 — Critical & Symbolic Notes
:layout: book

.. _euler-02-notes:

===============================================================================
Critical & Symbolic Notes — Unit II: Six Quadrances & The Euler Line (§§ 10–18)
===============================================================================

.. rubric:: Folio Errata, Stewart's Theorem (1746) & Exact Symbolic Verification

1. Compositorial Errata on pp. 109–113 of the 1767 Edition
----------------------------------------------------------

Visual inspection of the 1767 *Novi Commentarii* pages reveals four minor printing slips in the intermediate derivations, all of which :person:`Euler <euler>` silently corrects in his summary table **§ 18** on p. 114:

* **p. 109, § 12**: (a) Line 1 prints ``(3cc - bb + aa)/(6c)`` for ``(3cc + bb - aa)/(6c)``, while giving the true difference ``(bb - aa)/(3c)``; (b) the intermediate display prints denominator ``16 AA`` for ``36 AA`` (stemming from :math:`(12c\mathcal{A})^2 / (4c^2) = 36\mathcal{A}^2`, corrected six lines below); (c) the expansion of :math:`a^6 + b^6 + c^6` prints ``-3rr`` at the end of line 2 for ``+3rr``; and (d) the final line prints ``EF^2 = rr/(4AA) = 4/9(pp - 2q)`` with ``=`` instead of ``-`` (corrected in § 18 I).
* **p. 112, § 15, line 2**: Prints ``GF - RG`` for ``QF - RG``.
* **p. 113, § 17, penult. line**: Prints ``-`` between ``(r / 16pAA)(p^4 - 4ppq + 9pr)`` and ``r(p^3 - 4pq + 9r)/(16AA)`` where ``=`` is intended.

2. Connection to Matthew Stewart's Proposition II (1746)
--------------------------------------------------------

At the close of **§ 18** (p. 114), Euler deduces from :math:`FH = \frac{1}{2}EF` and :math:`EH = \frac{3}{2}EF` the identity

.. math::

   4GH^2 + 2EG^2 = 3EF^2 + 6FG^2.

This is a direct specialization of :person:`Matthew Stewart <stewart>`'s theorem (*Some General Theorems of Considerable Use in the Higher Parts of Mathematics*, Edinburgh, 1746, Prop. II): for collinear points :math:`E - F - H` and any point :math:`G` in the plane,

.. math::

   GH^2 \cdot EF + EG^2 \cdot FH = EH\left(FG^2 + EF \cdot FH\right).

Substituting :math:`FH = \tfrac{1}{2}EF` and :math:`EH = \tfrac{3}{2}EF` gives :math:`GH^2 + \tfrac{1}{2}EG^2 = \tfrac{3}{2}\left(FG^2 + \tfrac{1}{2}EF^2\right)`, and multiplying by :math:`4` yields :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2`. In :func:`geometor.feuerbach.euler.prove_euler_1765_identities`, both each of Formulas I–VI and Stewart's relation simplify to symbolic ``0`` over :math:`\mathbb{Q}(a, b, c)` via ``sp.cancel``.

3. Bridge Forward to Feuerbach (1822, §§ 49–57)
-----------------------------------------------

Formula **VI** (:math:`GH^2 = R^2 - 2Rr_{\text{in}}`) and Formula **III** (:math:`EH^2 = 9R^2 - (a^2 + b^2 + c^2)`) are explicitly cited by :person:`Karl Wilhelm Feuerbach <feuerbach>` in **§ 49** and **§ 53** of his 1822 Nürnberg monograph (:ref:`fb-03-en`). Extending Formula VI to the three excenters (:math:`KS^{(k)2} = R^2 + 2Rr^{(k)}`) and combining it with Apollonius's median theorem applied to the midpoint :math:`L = X(5)` of segment :math:`EH` (renamed :math:`OK` in Feuerbach) produces **Feuerbach's Theorem** (:math:`LS = \tfrac{1}{2}R - r_{\text{in}}`).

4. Rational Quadrances on the (15, 13, 14) Triangle
---------------------------------------------------

On our canonical triangle :math:`(a, b, c) = (15, 13, 14)` with :math:`p = 42, q = 587, r = 2730, \mathcal{A} = 84`:

.. math::

   EF^2 = \frac{265}{144}, \quad
   EG^2 = \frac{17}{16}, \quad
   EH^2 = \frac{265}{64}, \quad
   FG^2 = \frac{1}{9}, \quad
   FH^2 = \frac{265}{576}, \quad
   GH^2 = \frac{65}{64},

satisfying :math:`4\left(\frac{65}{64}\right) + 2\left(\frac{17}{16}\right) = \frac{99}{16} = 3\left(\frac{265}{144}\right) + 6\left(\frac{1}{9}\right)` identically.
