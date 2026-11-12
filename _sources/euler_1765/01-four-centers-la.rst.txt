:title: Euler (1765) §§ 1–9 — Latina (1767)
:track_label: Latina (1767)
:layout: book

.. _euler-01-la:

=========================================================================
Caput I: Quatuor Puncta Notabilia et Coordinatae Orthogonales (§§ 1–9)
=========================================================================

.. rubric:: L. Eulerus — *Solutio facilis problematum quorumdam geometricorum difficillimorum* (*Novi Commentarii*, Tom. XI, MDCCLXVII, pp. 103–107)

.. contents:: Paragraphi huius partis
   :local:
   :depth: 2
   :backlinks: none

.. _euler-la-s1:

.. folio:: § 1
   :page: 103

§ 1. Enumeratio quatuor punctorum trianguli
-------------------------------------------

In omni triangulo quatuor potissimum dantur puncta, quae in Geometria considerari solent.

1. Intersectio ternorum perpendiculorum, quae ex singulis angulis in latera opposita demittuntur.
2. Intersectio ternarum rectarum, quae ex singulis angulis ductae latera opposita bisecant; quod punctum simul est centrum grauitatis trianguli.
3. Intersectio ternarum rectarum, quae singulos angulos bifariam secant, in quod punctum incidit centrum circuli triangulo inscripti.
4. Intersectio ternarum rectarum ad singula latera normalium eaque bisecantium, in quo puncto reperitur centrum circuli triangulo circumscripti.

.. _euler-la-s2:

§ 2. Quatuor problemata inuersa
-------------------------------

Ex his quatuor punctis, si dentur positione terna quaecunque, euidens est, triangulum inde determinari, nisi forte illa puncta in vno coalescant, quod cum eueniat in triangulo aequilatero, hoc casu omnia triangula aequilatera problemati aeque

.. folio:: § 2 (cont.)
   :page: 104

satisfacient. Hinc igitur quatuor nascentur problemata, prout quodque eorum quatuor punctorum, pro trianguli determinatione praetermittitur, quae quemadmodum commodissime resolui queant, hic ostendere constitui.

.. _euler-la-s3:

§ 3. De electione quantitatum incognitarum
------------------------------------------

Problemata autem haec solutu esse difficillima, mox experietur, quicunque ea fuerit aggressus, cum vix perspiciatur, cuiusmodi quantitates incognitas in calculum introduci oporteat, vt saltem ad aequationes solutionem continentes perueniatur. Totum ergo negotium ad idoneam quantitatum incognitarum electionem reducitur, in quo id imprimis est cauendum, ne in calculos taediosissimos et omnino inextricabiles delabamur. Tum vero omnibus difficultatibus feliciter superatis insignes quaedam affectiones inter illa quatuor puncta se prodent, quarum cognitio in Geometria haud leuis momenti est censenda.

.. _euler-la-s4:

§ 4. Descriptio quatuor figurarum (Tab. II, Fig. 1–4)
-----------------------------------------------------

Ne figurae nimia linearum in iis ducendarum multitudine onerentur, idem triangulum :math:`ABC` quater exhibeo, in primo scilicet (`fig. 1.`) rectae :math:`AM`, :math:`BN` et :math:`CN` [*sic*; lege :math:`CP`] in latera opposita sunt normales, earumque intersectionem littera :math:`E` designo, vbi primum situm est punctum eorum quatuor, quae commemoraui. In secunda figura rectae :math:`Aa`, :math:`Bb` et :math:`Cc` latera opposita bisecant, quarum intersectionem indicat punctum :math:`F` secundum, de quatuor illis punctis memoratis et centrum grauitatis trianguli.

.. folio:: § 4 (cont.)
   :page: 105

In tertia figura rectae :math:`A\alpha`, :math:`B\beta`, :math:`C\gamma` angulos :math:`A, B, C` bisecant, earumque intersectio :math:`G` praebet tertium punctum ante memoratum, nempe centrum circuli inscripti. Tandem in quarta figura ex singulorum laterum punctis mediis :math:`S, T, V` erectae sunt perpendiculares :math:`SH`, :math:`TH` et :math:`VH` sua intersectione :math:`H` centrum circuli circumscripti exhibentes.

.. _euler-la-s5:

§ 5. Latera, perpendicula in basin AB, et area A
------------------------------------------------

Quo horum quatuor punctorum positionem facilius definire eaque deinceps inter se comparare queam, ex singulis in latus :math:`AB` pro basi assumtum demitto perpendicula :math:`EP`, :math:`FQ`, :math:`GR` et :math:`HS`, quorum quidem primum et quartum iam in constructione ipsa occurrunt. Tum vero voco terna trianguli latera:

.. math::

   AB = c; \qquad AC = b \qquad \text{et} \qquad BC = a

praeterea vero etiam aream trianguli in computum duci decet, quae sit :math:`= \mathcal{A}`, eritque vti constat:

.. math::

   \mathcal{A}\mathcal{A} = \frac{1}{16}(a + b + c)(a + b - c)(b + c - a)(c + a - b)

seu

.. math::

   \mathcal{A}\mathcal{A} = \frac{1}{16}\left(2aabb + 2aacc + 2bbcc - a^4 - b^4 - c^4\right).

Hinc igitur situm cuiusque horum quatuor punctorum respectu basis :math:`AB` seorsim inuestigo sequenti modo (`Tab. II. Fig. 1.`).

.. _euler-la-s6:

§ 6. I. Pro intersectione perpendiculorum E
-------------------------------------------

Primo ex elementis constat fore:

.. math::

   AP = \frac{cc + bb - aa}{2c}, \qquad \text{similique modo} \qquad BM = \frac{aa + cc - bb}{2a}.

Deinde vero ob :math:`\tfrac{1}{2}AM \cdot BC = \mathcal{A}` erit :math:`AM = \frac{2\mathcal{A}}{a}`,

.. folio:: § 6 (cont.)
   :page: 106

vnde similitudo triangulorum :math:`ABM` et :math:`AEP` praebet

.. math::

   AM : BM = AP : EP

hincque fit

.. math::

   EP = \frac{(cc + bb - aa)(aa + cc - bb)}{8c\mathcal{A}}.

Quocirca situs puncti :math:`E` respectu basis :math:`AB` ita definitur vt sit

.. math::

   AP = \frac{cc + bb - aa}{2c} \qquad \text{et} \qquad PE = \frac{(cc + bb - aa)(aa + cc - bb)}{8c\mathcal{A}}.

.. _euler-la-s7:

§ 7. II. Pro centro grauitatis F
--------------------------------

Demisso ex angulo :math:`C` in basin :math:`AB` perpendiculo :math:`CP` (`Tab. II. Fig. 2.`) habemus vt ante :math:`AP = \frac{cc + bb - aa}{2c}` et :math:`CP = \frac{2\mathcal{A}}{c}`. Iam vero ex elementis constat esse :math:`FQ = \tfrac{1}{3}CP = \frac{2\mathcal{A}}{3c}` et :math:`cQ = \tfrac{1}{3}cP`. Cum autem sit :math:`Ac = \tfrac{1}{2}c` erit :math:`cP = \frac{bb - aa}{2c}` ideoque :math:`cQ = \frac{bb - aa}{bc}` [*sic*; lege :math:`6c`], et consequenter :math:`AQ = \frac{3cc + bb - aa}{bc}` [*sic*; lege :math:`6c`]. Quam ob rem situs puncti :math:`F` respectu basis :math:`AB` ita definitur, vt sit:

.. math::

   AQ = \frac{3cc + bb - aa}{bc} \text{ [lege } 6c\text{]} \qquad \text{et} \qquad QF = \frac{2\mathcal{A}}{3c}.

.. _euler-la-s8:

§ 8. III. Pro centro circuli inscripti G
----------------------------------------

Cum :math:`GR` (`Fig. 3.`) sit radius circuli inscripti, erit :math:`\tfrac{1}{2}GR(a + b + c)` area trianguli :math:`= \mathcal{A}` vnde fit :math:`GR = \frac{2\mathcal{A}}{a + b + c}`. Tum vero posito segmento :math:`AR = x`, si ab :math:`AC` ex :math:`A` par portio rescindatur, habebitur ibi punctum contactus, a quo proinde punctum :math:`C` distat interuallo :math:`= b - x`. Deinde ob :math:`BR = c - x` si a latere :math:`BC` ex :math:`A` [*sic*; lege :math:`B`] aequale interuallum :math:`c - x` rescindatur,

.. folio:: § 8 (cont.)
   :page: 107

ibi hoc latus a circulo tangetur, vnde punctum :math:`C` ab isto puncto distabit interuallo :math:`= a - c + x`, quod cum ex circuli natura illi :math:`b - x` sit aequale, erit :math:`x = \frac{c + b - a}{2}`. Quare hoc punctum :math:`G` respectu basis :math:`AB` ita definitur vt sit:

.. math::

   AR = \frac{c + b - a}{2} \qquad \text{et} \qquad RG = \frac{2\mathcal{A}}{a + b + c}.

.. _euler-la-s9:

§ 9. IV. Pro centro circuli circumscripti H
-------------------------------------------

Hic quidem (`Tab. II. Fig. 4.`) statim est ex constructione :math:`AS = \tfrac{1}{2}c`. Tum vero ex :math:`A` in :math:`BC` ducto perpendiculo :math:`AM`, erit :math:`AM = \frac{2\mathcal{A}}{a}` et :math:`CM = \frac{aa + bb - cc}{2a}`. Iuncta autem recta :math:`AH` ex natura circuli liquet fore angulum :math:`AHS` aequalem angulo :math:`ACB`, ideoque triangulum :math:`AHS` simile erit triangulo :math:`ACM` vnde fit:

.. math::

   AM : CM = AS : HS

sicque colligitur :math:`HS = \frac{c(aa + bb - cc)}{8\mathcal{A}}`. Quare situs puncti :math:`H` respectu basis :math:`AB` ita definitur vt sit:

.. math::

   AS = \frac{1}{2}c \qquad \text{et} \qquad SH = \frac{c(aa + bb - cc)}{8\mathcal{A}}.
