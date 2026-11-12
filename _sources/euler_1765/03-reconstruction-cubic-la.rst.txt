:title: Euler (1765) §§ 19–24 — Latina (1767)
:track_label: Latina (1767)
:layout: book

.. _euler-03-la:

===========================================================================
Caput III: Problema Inuersum et Aequatio Cubica Laterum (§§ 19–24)
===========================================================================

.. rubric:: L. Eulerus — *Solutio facilis problematum quorumdam geometricorum difficillimorum* (*Novi Commentarii*, Tom. XI, MDCCLXVII, pp. 114–118)

.. contents:: Paragraphi huius partis
   :local:
   :depth: 2
   :backlinks: none

.. _euler-la-s19:

.. folio:: § 19
   :page: 114

§ 19. Quantitates auxiliares duarum dimensionum P, Q, R
-------------------------------------------------------

Quo nunc has formulas ad maiorem simplicitatem reuocemus, ponamus :math:`4pq - p^3 - 8r = 4s` vt sit :math:`4\mathcal{A}\mathcal{A} = ps` et :math:`4q = pp + \frac{8r}{p} + \frac{4s}{p}`; tum vero faciamus:

.. math::

   \frac{rr}{ps} = R, \qquad \frac{r}{p} = Q \qquad \text{et} \qquad pp = P

ita vt :math:`P, Q, R` sint quantitates duas dimensiones inuoluentes. Quoniam igitur hinc est :math:`\frac{-s}{p} = \frac{QQ}{R}` [*sic*; lege :math:`\frac{s}{p} = \frac{QQ}{R}`] erit :math:`p = \sqrt{P}`; :math:`q = \frac{1}{4}P + 2Q + \frac{QQ}{R}`, et :math:`r = Q\sqrt{P}`, at-

.. folio:: § 19 (cont.)
   :page: 115

que :math:`4\mathcal{A}\mathcal{A} = \frac{PQQ}{R}` et interualla nostra ita exprimentur:

.. math::

   \text{I.} \quad EF^2 &= R - \frac{2}{9}P + \frac{16}{9}Q + \frac{8QQ}{9R} \\
   \text{II.} \quad EG^2 &= R - \frac{1}{4}P + 2Q + \frac{3QQ}{R} \\
   \text{III.} \quad EH^2 &= \frac{9}{4}R - \frac{1}{2}P + 4Q + \frac{2QQ}{R} \\
   \text{IV.} \quad FG^2 &= +\frac{1}{36}P - \frac{8}{9}Q + \frac{5QQ}{9R} \\
   \text{V.} \quad FH^2 &= \frac{1}{4}R - \frac{1}{18}P + \frac{4}{9}Q + \frac{2QQ}{9R} \\
   \text{VI.} \quad GH^2 &= \frac{1}{4}R - Q.

.. _euler-la-s20:

§ 20. Problema vnicum
---------------------

Cum igitur horum quatuor punctorum terna nisi capiantur haec tria :math:`E, F` et :math:`H` iam contineant determinationem quarti, vnicum resultat problema, quod ita se habet.

**Problema** (`Tab. II. Fig. 5.`). *Datis positione his quatuor punctis in quolibet triangulo assignabilibus 1°. Intersectione perpendicularium ex singulis angulis in latera opposita ductarum* :math:`E`, *2°. Centro grauitatis* :math:`F`, *3°. Centro circuli inscripti* :math:`G` *et 4° centro circuli circumscripti* :math:`H`; *construere triangulum.*

Quod problema ex hactenus erutis horum punctorum affectionibus satis concinne resoluere licebit.

.. _euler-la-s21:

§ 21. Solutio
-------------

**Solutio.** Cum positio horum quatuor punctorum per eorum distantias detur, vocemus:

.. folio:: § 21 (cont.)
   :page: 116

.. math::

   GH = f, \qquad FH = g \qquad \text{et} \qquad FG = h

nouimusque fore :math:`EF = 2g` et :math:`EH = 3g`, itemque :math:`EG = \sqrt{6gg + 3hh - 2ff}`.

Nunc igitur statim habemus has tres aequationes

.. math::

   \text{I.} \quad ff &= \frac{1}{4}R - Q \\
   \text{II.} \quad gg &= \frac{1}{4}R - \frac{1}{18}P + \frac{4}{9}Q + \frac{2QQ}{9R} \\
   \text{III.} \quad hh &= \frac{1}{36}P - \frac{8}{9}Q + \frac{6QQ}{9R} \quad [\text{*sic*; lege } \frac{5QQ}{9R}]

ex quarum resolutione colligimus:

.. math::

   R &= \frac{4f^4}{3gg + 6hh - 2ff}; \qquad Q = \frac{3ff(ff - gg - 2hh)}{3gg + 6hh - 2ff} \\
   \text{et } P &= \frac{27f^4}{3gg + 6hh - 2ff} - 12ff - 15gg + 6hh

vnde fit :math:`\frac{QQ}{R} = \frac{9(ff - gg - 2hh)^2}{4(3gg + 6hh - 2ff)}`.

.. _euler-la-s22:

§ 22. Aequatio cubica laterum
-----------------------------

His valoribus inuentis inuestigentur tres sequentes expressiones:

.. math::

   p = \sqrt{P}, \qquad q = \frac{1}{4}P + 2Q + \frac{QQ}{R}, \qquad \text{et} \qquad r = Q\sqrt{P}

indeque formetur haec aequatio cubica:

.. math::

   z^3 - pzz + qz - r = 0

cuius tres radices dabunt tria latera trianguli quaesiti, quo pacto eius constructio facillima habetur.

.. _euler-la-s23:

§ 23. Exemplum (a = 5, b = 6, c = 7)
------------------------------------

**Exemplum.** Sumtis lateribus trianguli :math:`a = 5`, :math:`b = 6` et :math:`c = 7`, vt sit area :math:`\mathcal{A} = 6\sqrt{6}`, inde colliguntur distantiae quaternorum punctorum:

.. folio:: § 23 (cont.)
   :page: 117

.. math::

   EF^2 = \frac{155}{72}; \quad EG^2 = \frac{11}{8}; \quad EH^2 = \frac{155}{32}; \quad FG^2 = \frac{1}{9}; \quad FH^2 = \frac{155}{288}; \quad GH^2 = \frac{35}{32}

vnde situs horum punctorum talis prodit vti in `Tab. II. fig. 6.` repraesentatur. Cum igitur habeamus:

.. math::

   ff = \frac{35}{32}; \qquad gg = \frac{155}{288} \qquad \text{et} \qquad hh = \frac{1}{9}

videamus num solutio inuenta ad triangulum assumtum perducat.

.. _euler-la-s24:

§ 24. Evolutio exempli
----------------------

Hinc autem fit :math:`3gg + 6hh - 2ff = \frac{3}{32}`, tum vero :math:`ff - gg - 2hh = \frac{1}{3}`; :math:`4ff + 5gg - 2hh = \frac{219}{32}`; colligitur

.. math::

   R = \frac{1225}{24}; \qquad Q = \frac{35}{3}; \qquad P = 324 \qquad \text{et} \qquad \frac{QQ}{R} = \frac{24}{9} = \frac{8}{3}

vnde nanciscimur:

.. math::

   p = \sqrt{P} = 18; \qquad q = 107 \qquad \text{et} \qquad r = \frac{35}{3} \cdot 18 = 5 \cdot 6 \cdot 7 = 210

et aequatio cubica hinc oritur:

.. math::

   z^3 - 18zz + 107z - 210 = 0

cuius tres radices manifesto sunt :math:`5, 6, 7` quae sunt ipsa tria latera trianguli satisfacientis.
