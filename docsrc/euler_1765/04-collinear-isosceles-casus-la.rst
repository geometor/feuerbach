:title: Euler (1765) §§ 25–34 — Latina (1767)
:track_label: Latina (1767)
:layout: book

.. _euler-04-la:

=====================================================================================
Caput IV: Casus Punctorum in Directum Sitorum et Trisectio Anguli (§§ 25–34)
=====================================================================================

.. rubric:: L. Eulerus — *Solutio facilis problematum quorumdam geometricorum difficillimorum* (*Novi Commentarii*, Tom. XI, MDCCLXVII, pp. 117–123)

.. contents:: Paragraphi huius partis
   :local:
   :depth: 2
   :backlinks: none

.. _euler-la-s25:

.. folio:: § 25
   :page: 117

§ 25. Casus quo quatuor puncta in directum sunt sita
----------------------------------------------------

Hoc ergo casu (`Fig. 7.`) cum sit:

.. math::

   FH = g; \quad FG = h; \quad GH = f; \quad EF = 2g; \quad EH = 3g \quad \text{et} \quad EG = 2g - h

.. folio:: § 25 (cont.)
   :page: 118

erit :math:`g = f - h`, vnde facta hac substitutione colligimus:

.. math::

   R = \frac{4f^4}{(3h - f)^2}; \qquad Q = \frac{3ffh(2f - 3h)}{(f - 3h)^2}; \qquad P = \frac{3h(4f - 3h)^3}{(f - 3h)^2}

ideoque :math:`\frac{QQ}{R} = \frac{9hh(2f - 3h)^2}{4(f - 3h)^2}`. Ex his vero porro elicimus:

.. math::

   p &= \frac{(4f - 3h)\sqrt{3h(4f - 3h)}}{f - 3h} \\
   q &= \frac{3fh(4f - 3h)(5f - 6h)}{(f - 3h)^2} \\
   r &= \frac{3ffh(2f - 3h)(4f - 3h)\sqrt{3h(4f - 3h)}}{(f - 3h)^3}.

.. _euler-la-s26:

§ 26. Resolutio aequationis cubicae in casu isosceli
----------------------------------------------------

Cum iam radices huius aequationis cubicae:

.. math::

   z^3 - pzz + qz - r = 0

praebeant tria latera :math:`a, b, c` trianguli quaesiti, ponamus ad eam concinniorem reddendam

.. math::

   z = \frac{y\sqrt{3h(4f - 3h)}}{f - 3h}

et prodibit haec aequatio:

.. math::

   y^3 - (4f - 3h)yy + f(5f - 6h)y - ff(2f - 3h) = 0

cuius radices manifesto sunt :math:`f, f`, et :math:`2f - 3h`. Quocirca trianguli quaesiti, quod fit isosceles, latera erunt:

.. math::

   a = b = \frac{f\sqrt{3h(4f - 3h)}}{f - 3h}; \qquad \text{et} \qquad c = \frac{(2f - 3h)\sqrt{3h(4f - 3h)}}{f - 3h}.

.. _euler-la-s27:

§ 27. Solutio directa trianguli isoscelis
-----------------------------------------

Hic autem casus per se solutu est facilis, cum recta illa, in qua sunt puncta data triangu-

.. folio:: § 27 (cont.)
   :page: 119

lum in duas partes similes necessario secet, ideoque triangulum sit isosceles. Posito autem statim a principio :math:`b = a`, fit :math:`\mathcal{A} = \tfrac{1}{4}c\sqrt{4aa - cc}` et :math:`AP = AQ = AR = AS = \tfrac{1}{2}c`, tum vero

.. math::

   PE = \frac{c^3}{4\mathcal{A}}; \qquad QF = \frac{2\mathcal{A}}{3c}; \qquad RG = \frac{2\mathcal{A}}{2a + c}; \qquad SH = \frac{c(2aa - cc)}{8\mathcal{A}}

vnde ob puncta :math:`P, Q, R, S` coincidentia in basis puncto medio, quod sit :math:`O`, interualla inter haec puncta erunt:

.. math::

   OF - OE &= \frac{2(aa - cc)}{3\sqrt{4aa - cc}}; \qquad
   OG - OE = \frac{c(a - c)}{\sqrt{4aa - cc}}; \qquad
   OH - OE = \frac{aa - cc}{\sqrt{4aa - cc}}; \\
   OF - OG &= \frac{(a - c)(2a - c)}{3\sqrt{4aa - cc}}; \qquad
   OH - OF = \frac{aa - cc}{3\sqrt{4aa - cc}}; \qquad
   OH - OG = \frac{a(a - c)}{\sqrt{4aa - cc}}.

.. _euler-la-s28:

§ 28. Dispositio punctorum prout a > c vel a < c
------------------------------------------------

Hic duos casus contemplari conuenit prout fuerit vel :math:`a > c` vel :math:`a < c`, nam si :math:`a = c`, seu triangulum aequilaterum, omnia quatuor puncta in vnum coalescunt;

**I.** Si :math:`a > c` puncta erunt disposita vti `Tab. II. fig. 8.` refert, vbi est :math:`HF = \tfrac{1}{3}EH` seu :math:`EF = \tfrac{2}{3}EH` et :math:`EG < \tfrac{1}{2}EH` hocque casu punctum basis medium :math:`O` in recta :math:`HE` producta vltra :math:`E` cadit: vt sit :math:`OE = \frac{cc}{2\sqrt{4aa - cc}}`.

**II.** Si :math:`a < c`, puncta erunt disposita vti `fig. 9.` refert, vbi est iterum :math:`HF = \tfrac{1}{3}EH` seu :math:`EF = \tfrac{2}{3}EH` at :math:`EG > \tfrac{1}{2}EH`. Hoc autem casu punctum basis medium :math:`O` in recta :math:`EH` producta vltra :math:`H` cadit; vt sit

.. folio:: § 28 (cont.)
   :page: 120

:math:`HO = \frac{2aa - cc}{2\sqrt{4aa - cc}}`, vnde si :math:`2aa < cc` punctum :math:`O` adeo intra :math:`H` et :math:`E` cadit.

.. _euler-la-s29:

§ 29. Formulae explicitae per d et e
------------------------------------

Datis ergo in recta punctis tribus :math:`E, G` et :math:`H`, ita vt :math:`G` intra extrema :math:`E` et :math:`H` sit situm, videndum est vtrum sit :math:`EG < \tfrac{1}{2}EH` an :math:`EG > \tfrac{1}{2}EH`.

Priori casu quo :math:`EG < \tfrac{1}{2}EH` (`Tab. II. Fig. 8.`) solutio ita se habet. Sit :math:`EH = 2d` et :math:`EG = d - e`, hincque reperitur

.. math::

   a = b = \frac{d + e}{2e}\sqrt{(d + 3e)(3d + e)}, \qquad
   c = \frac{d - e}{2e}\sqrt{(d + 3e)(3d + e)}, \qquad
   \text{et } OE = \frac{(d - e)^2}{4e}.

Posteriori casu :math:`EG > \tfrac{1}{2}EH` (`Fig. 9.`) solutio erit haec: sit :math:`EH = 2d` et :math:`EG = d + e`, hincque colligitur

.. math::

   a = b = \frac{d - e}{2e}\sqrt{(d - 3e)(3d - e)}; \qquad
   c = \frac{d + e}{2e}\sqrt{(d - 3e)(3d - e)} \qquad
   \text{et } OE = \frac{(d + e)^2}{2e} \text{ [*sic*; lege } 4e\text{]},

vnde patet hunc casum locum habere non posse, si :math:`d` intra limites :math:`3e` et :math:`\tfrac{1}{3}e` contineatur. Cum enim esse debet :math:`2a > c` necesse est sit :math:`d > 3e`.

.. _euler-la-s30:

§ 30. Solutio concinnior omisso puncto F
----------------------------------------

Ex hoc casu colligere licet, etiam in genere (`Fig. 5.`) solutionem concinniorem esse prodituram, si omisso puncto :math:`F` tria puncta :math:`E, G` et :math:`H` considerentur. Ponamus ergo:

.. math::

   EG = e, \qquad GH = f \qquad \text{et} \qquad EH = k

eritque :math:`FH = g = \tfrac{1}{3}k`, :math:`EF = \tfrac{2}{3}k` et :math:`FG = h = \sqrt{\tfrac{1}{3}ee + \tfrac{2}{3}ff - \tfrac{2}{9}kk}` hincque adipiscimur

.. math::

   R = \frac{4f^4}{2ff + 2ee - kk}, \qquad Q = \frac{ff(kk - ff - 2ee)}{2ee + 2ff - kk}

.. folio:: § 30 (cont.)
   :page: 121

.. math::

   \text{et } P = \frac{27f^4}{2ee + 2ff - kk} + 2ee - 8ff - 3kk = \frac{4e^4 + 11f^4 + 3k^4 - 12eeff + 2ffkk - 8eekk}{2ee + 2ff - kk}

tum vero :math:`\frac{QQ}{R} = \frac{(kk - ff - 2ee)^2}{4(2ee + 2ff - kk)}`, vnde fit

.. math::

   p = \sqrt{P}, \qquad q = \frac{2e^4 + f^4 + k^4 - 6eeff - 3eekk + 2ffkk}{2ee + 2ff - kk} \qquad \text{et} \qquad r = Q\sqrt{P}

et aequationis :math:`z^3 - pzz + qz - r = 0` radices dant latera trianguli quaesiti: quae aequatio posito :math:`z = y\sqrt{P}` abit in hanc:

.. math::

   y^3 - yy + \frac{(2e^4 + f^4 + k^4 - 6eeff + 3eekk + 2ffkk)y - ff(kk - 2ee - ff)}{4e^4 + 11f^4 + 3k^4 - 12eeff - 8eekk + 2ffkk} = 0 \quad [\text{*sic*; vide notas}].

.. _euler-la-s31:

§ 31. Limites quantitatum e, f, k
---------------------------------

Hic autem obseruo quantitates has datas :math:`e, f, k` non solum ita assumi oportere, vt triangulum constituant, sed quoniam latera trianguli quaesiti :math:`a, b, c` tanquam positiua spectari possunt, etiam tam :math:`P` quam :math:`Q` et :math:`R` valores positiuos recipere debent. Non solum ergo esse debet :math:`kk < 2ee + 2ff` sed etiam :math:`kk > 2ee + ff`, tum vero vt :math:`P` fiat positiuum, necesse est sit

.. math::

   3kk > 4ee + ff + 2\sqrt{e^4 + 11eeff - 8f^4}

qua conditione cum illis collata sequitur esse debere

.. math::

   ff > \frac{8}{19}ee \qquad \text{et} \qquad ff < \frac{11 + \sqrt{153}}{16}ee \quad \text{seu} \quad ff < \frac{19}{13}ee \quad [\text{*sic*; vide notas}]

alioquin problema nullam admitteret solutionem.

.. _euler-la-s32:

§ 32. Exemplum casus ee = ff
----------------------------

*Exempl.* Sit :math:`ee = ff` erit :math:`R = \frac{4f^4}{4ff - kk}`; :math:`Q = \frac{ff(kk - 3ff)}{4ff - kk}` et :math:`P = \frac{27f^4}{4ff - kk} - 6ff - 3kk = \frac{3(kk - ff)^2}{4ff - kk}`; atque :math:`\frac{QQ}{R} = \frac{(kk - 3ff)^2}{4(4ff - kk)}` ideoque :math:`p = \frac{(kk - ff)\sqrt{3}}{\sqrt{4ff - kk}}`; :math:`q = \frac{k^4 - ffkk - 3f^4}{4ff - kk}`; et :math:`r = \frac{ff(kk - 3ff)(kk - ff)\sqrt{3}}{4(4ff - kk)\sqrt{4ff - kk}}`

.. folio:: § 32 (cont.)
   :page: 122

sit iam :math:`ee = ff = 2` et :math:`kk = 7`; fietque :math:`p = 5\sqrt{3}`; :math:`q = 23`, et :math:`r = 10\sqrt{3}` et latera trianguli quaesiti erunt radices huius aequationis cubicae :math:`z^3 - 5zz\sqrt{3} + 23z - 10\sqrt{3} = 0`, quae posito :math:`z = \frac{y}{\sqrt{3}}` abit in :math:`y^3 - 15yy + 69y - 90 = 0` cuius vna radix est :math:`y = 6`, vnde binae reliquae sunt :math:`y = \frac{9 + \sqrt{21}}{2}` et :math:`y = \frac{9 - \sqrt{21}}{2}` sicque trianguli quaesiti latera sunt:

.. math::

   a = \frac{3\sqrt{3} + \sqrt{7}}{2}; \qquad b = \frac{3\sqrt{3} - \sqrt{7}}{2}; \qquad c = 2\sqrt{3}.

.. _euler-la-s33:

§ 33. Resolutio generalis manente ee = ff
-----------------------------------------

Verum etiam generalius manente :math:`ee = ff` quomodocunque accipiatur :math:`k`, si ponatur :math:`z = \frac{y}{\sqrt{3(4ff - kk)}}` habetur haec aequatio resoluenda:

.. math::

   y^3 - 3(kk - ff)yy + 3(k^4 - ffkk - 3f^4)y - 9ff(kk - 3ff)(kk - ff) = 0

cui primo satisfacit :math:`y = 3ff`, et duae reliquae radices ex hac aequatione

.. math::

   yy - 3(kk - 2ff)y + 3(kk - 3ff)(kk - ff) = 0

quae sunt :math:`y = \frac{3(kk - 2ff) \pm k\sqrt{3(4ff - kk)}}{2}` sicque tria latera trianguli quaesiti fiunt:

.. math::

   a = \frac{(kk - 2ff)\sqrt{3}}{2\sqrt{4ff - kk}} + \frac{1}{2}k, \qquad
   b = \frac{(kk - 2ff)\sqrt{3}}{2\sqrt{4ff - kk}} - \frac{1}{2}k, \qquad
   c = \frac{ff\sqrt{3}}{\sqrt{4ff - kk}}.

.. _euler-la-s34:

.. folio:: § 34
   :page: 123

§ 34. Casus irreducibilis et anguli trisectio
---------------------------------------------

Reliquis casibus negotium non tam facile expeditur, quia aequatio cubica factores non admittit. Quod vt exemplo ostendatur sit :math:`ee = 3`, :math:`ff = 2` et :math:`kk = 9`; vnde trianguli latera sunt radices huius aequationis cubicae :math:`z^3 - zz\sqrt{71} + 22z - 2\sqrt{71} = 0`; ad quam resoluendam quaeratur angulus :math:`\alpha`, cuius cosinus sit :math:`= +\sqrt{\frac{71}{75}}` [*sic*; vide notas], qui erit acutus, quo inuento latera trianguli erunt:

.. math::

   a = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cdot\cos\left(60^\circ - \frac{1}{3}\alpha\right), \quad
   b = \frac{1}{3}\sqrt{71} + \frac{2}{3}\sqrt{5}\cdot\cos\left(60^\circ + \frac{1}{3}\alpha\right), \quad
   c = \frac{1}{3}\sqrt{71} - \frac{2}{3}\sqrt{5}\cdot\cos\frac{1}{3}\alpha

vbi est proxime :math:`\alpha = 11^\circ\, 32'\, 13''` [*sic*] sicque per anguli trisectionem problema semper satis expedite resoluetur.
