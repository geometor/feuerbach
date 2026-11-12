:title: Euler (1765) §§ 10–18 — Latina (1767)
:track_label: Latina (1767)
:layout: book

.. _euler-02-la:

===============================================================================
Caput II: Sex Interualla Mutua et Linea Recta Per Puncta E, F, H (§§ 10–18)
===============================================================================

.. rubric:: L. Eulerus — *Solutio facilis problematum quorumdam geometricorum difficillimorum* (*Novi Commentarii*, Tom. XI, MDCCLXVII, pp. 107–114)

.. contents:: Paragraphi huius partis
   :local:
   :depth: 2
   :backlinks: none

.. _euler-la-s10:

.. folio:: § 10
   :page: 107

§ 10. Expressiones sex distantiarum inter quaterna puncta
---------------------------------------------------------

Hinc iam definire poterimus distantias inter haec quaterna puncta, si quidem in eadem figura exprimerentur, erit enim:

.. math::

   EF^2 &= (AP - AQ)^2 + (PE - QF)^2 \\
   EG^2 &= (AP - AR)^2 + (PE - RG)^2 \\
   EH^2 &= (AP - AS)^2 + (PE - SH)^2

.. folio:: § 10 (cont.)
   :page: 108

.. math::

   FG^2 &= (AQ - AR)^2 + (QF - RG)^2 \\
   FH^2 &= (AQ - AS)^2 + (QF - SH)^2 \\
   GH^2 &= (AR - AS)^2 + (RG - SH)^2.

Haec autem interualla ideo colligi oportet, quod si proponantur terna horum quatuor punctorum quaeque tanquam data, nihil aliud praeter eorum mutuas distantias pro cognito assumatur, vnde deinceps latera trianguli sint inuestiganda.

.. _euler-la-s11:

§ 11. Quantitates symmetricae p, q, r et area A
-----------------------------------------------

Hic autem imprimis est obseruandum distantias illas inter quatuor nostra puncta necessario ita exprimi debere, vt tria trianguli latera in expressiones aequaliter ingrediantur, cum nulli lateri prae reliquis respectu harum distantiarum vlla praerogatiua tribui queat. Quam ob causam latera trianguli sine vllo discrimine contemplaturus ponam:

.. math::

   a + b + c = p; \qquad ab + ac + bc = q \qquad \text{et} \qquad abc = r

ita vt loco laterum iam istas ternas quantitates :math:`p, q` et :math:`r` ad singula aeque relatas in calculum sim introducturus. Hinc cum sit:

.. math::

   aa + bb + cc &= pp - 2q; \qquad aabb + aacc + bbcc = qq - 2pr \\
   a^4 + b^4 + c^4 &= p^4 - 4ppq + 2qq + 4pr

area :math:`\mathcal{A}` ita exprimitur vt sit:

.. math::

   \mathcal{A}\mathcal{A} = \frac{1}{16}p(-p^3 + 4pq - 8r) = \frac{-p^4 + 4ppq - 8pr}{16}.

Hoc notato superiores sex distantias ad has nouas quantitates seorsim sum reuocaturus.

.. _euler-la-s12:

.. folio:: § 12
   :page: 109

§ 12. I. Inuestigatio distantiae punctorum E et F
-------------------------------------------------

Hic primo habemus:

.. math::

   AP - AQ &= \frac{cc + bb - aa}{2c} - \frac{3cc - bb + aa}{6c} \text{ [*sic*; lege } {+bb - aa}\text{]} = \frac{bb - aa}{3c} \\
   PE - QF &= \frac{(cc + bb - aa)(aa + cc - bb)}{8c\mathcal{A}} - \frac{2\mathcal{A}}{3c}
           = \frac{3(cc + bb - aa)(aa + cc - bb) - 16\mathcal{A}\mathcal{A}}{24c\mathcal{A}}

quae expressiones ad communem denominatorem reductae, fiunt:

.. math::

   AP - AQ &= \frac{(bb - aa)\sqrt{2aabb + 2aacc + 2bbcc - a^4 - b^4 - c^4}}{12c\mathcal{A}} \\
   PE - QF &= \frac{2c^4 - a^4 - b^4 + 2aabb - bbcc - aacc}{12c\mathcal{A}}

quarum quadrata addita praebent:

.. math::

   EF^2 = \frac{1}{16\mathcal{A}\mathcal{A}} \text{ [*sic*; lege } 36\mathcal{A}\mathcal{A}\text{]}
   \left(+a^6 + b^6 + c^6 - a^4bb - aab^4 - a^4cc - aac^4 - b^4cc - bbc^4 + 3aabbcc\right)

vbi vtique litterae :math:`a, b, c` aequaliter insunt. Est vero:

.. math::

   a^4bb + aab^4 + \text{etc.} &= ppqq - 2q^3 - 2p^3r + 4pqr - 3rr \\
   a^6 + b^6 + c^6 &= p^6 - 6p^4q + 9ppqq - 2q^3 + 6p^3r - 12pqr + 3rr \text{ [impr. } {-3rr}\text{]}

ex quo obtinemus:

.. math::

   EF^2 = \frac{1}{36\mathcal{A}\mathcal{A}}\left(p^6 - 6p^4q + 8ppqq + 8p^3r - 16pqr + 9rr\right)

quae expressionem ad hanc formam reducere licet:

.. math::

   EF^2 = \frac{rr}{4\mathcal{A}\mathcal{A}} = \frac{4}{9}(pp - 2q) \quad [\text{*sic*; lege } \frac{rr}{4\mathcal{A}\mathcal{A}} - \frac{4}{9}(pp - 2q)].

.. _euler-la-s13:

.. folio:: § 13
   :page: 110

§ 13. II. Inuestigatio distantiae punctorum E et G
--------------------------------------------------

Hic habemus:

.. math::

   AP - AR &= \frac{cc + bb - aa}{2c} - \frac{c - b + a}{2} = \frac{bb - bc - aa + ac}{2c} \\
   PE - RG &= \frac{(cc + bb - aa)(aa + cc - bb)}{8c\mathcal{A}} - \frac{2\mathcal{A}}{a + b + c} \quad \text{seu} \\
   PE - RG &= \frac{c^4 - a^4 - b^4 + 2aabb}{8c\mathcal{A}} + \frac{p^3 - 4pq + 8r}{8\mathcal{A}}

atque ad communem denominatorem reducendo:

.. math::

   AP - AR &= \frac{(bb - bc - aa + ac)\sqrt{2aabb + 2aacc + 2bbcc - a^4 - b^4 - c^4}}{8c\mathcal{A}} \\
   PE - RG &= \frac{2c^4 - (a + b)c^3 - (a - b)^2 cc + (a + b)(a - b)^2 c - (aa - bb)^2}{8c\mathcal{A}}

quorum quadratorum summa per :math:`4cc` diuisa ad hanc formam redit:

.. math::

   EG^2 = \frac{1}{16\mathcal{A}\mathcal{A}}
   \left(\begin{aligned}
   &+ a^6 - a^5b - a^4bb + 3a^4bc - 2a^3bbc + 2a^3b^3 \\
   &+ b^6 - ab^5 - aab^4 + 3ab^4c - 2a^3bcc + 2a^3c^3 + 6aabbcc \\
   &+ c^6 - a^5c - a^4cc + 3abc^4 - 2aab^3c + 2b^3c^3 \\
   &\phantom{+ c^6} - ac^5 - aac^4 - 2ab^3cc - b^5c - b^4cc - 2aabc^3 - bc^5 - bbc^4 - 2abbc^3
   \end{aligned}\right).

Antequam hanc expressionem ad litteras :math:`p, q` et :math:`r` reduco, obseruo esse:

.. math::

   EG^2 + aa + bb + cc - ab - ac - bc
   &= \frac{abc}{4\mathcal{A}\mathcal{A}}\left(a^3 + b^3 + c^3 - aab - abb - aac - acc - bbc - bcc + 3abc\right) \\
   &= \frac{abc(aa + bb + cc - 2ab - 2ac - 2bc)(a + b + c)}{4\mathcal{A}\mathcal{A}} + \frac{9aabbcc}{4\mathcal{A}\mathcal{A}}.

.. folio:: § 13 (cont.)
   :page: 111

Iam cum sit :math:`aa + bb + cc = pp - 2q` reductio est facilis, quippe prodit:

.. math::

   EG^2 + pp - 3q = \frac{pr(pp - 4q) + 9rr}{4\mathcal{A}\mathcal{A}}

sicque haec distantia ita definitur vt sit:

.. math::

   EG^2 = \frac{r(p^3 - 4pq + 9r)}{4\mathcal{A}\mathcal{A}} - pp + 3q = \frac{rr}{4\mathcal{A}\mathcal{A}} - \frac{4r}{p} - pp + 3q.

.. _euler-la-s14:

§ 14. III. Inuestigatio distantiae punctorum E et H
---------------------------------------------------

Cum hic sit:

.. math::

   AP - AS &= \frac{cc + bb - aa}{2c} - \frac{1}{2}c = \frac{bb - aa}{2c} \\
   PE - SH &= \frac{(cc + bb - aa)(aa + cc - bb)}{8c\mathcal{A}} - \frac{c(aa + bb - cc)}{8\mathcal{A}}
           = \frac{2c^4 - (aa + bb)cc - (aa - bb)^2}{8c\mathcal{A}}

et quadratis addendis diuisione facta per :math:`4cc` obtinetur:

.. math::

   EH^2 = \frac{1}{16\mathcal{A}\mathcal{A}}\left(a^6 + b^6 + c^6 - a^4bb - aac^4 - a^4cc - b^4cc - aab^4 - bbc^4 + 3aabbcc\right)

quae ob :math:`16\mathcal{A}\mathcal{A} = -a^4 - b^4 - c^4 + 2aabb + 2aacc + 2bbcc` reducitur ad hanc formam:

.. math::

   EH^2 = \frac{9aabbcc}{16\mathcal{A}\mathcal{A}} - aa - bb - cc

vbi substitutio facile conficitur, resultat enim:

.. math::

   EH^2 = \frac{9rr}{16\mathcal{A}\mathcal{A}} - pp + 2q.

.. _euler-la-s15:

.. folio:: § 15
   :page: 112

§ 15. IV. Inuestigatio distantiae punctorum F et G
--------------------------------------------------

Ex formulis supra inuentis habemus hic:

.. math::

   AQ - AR &= \frac{3cc + bb - aa}{6c} - \frac{c - b + a}{2} = \frac{3(a - b)c - aa + bb}{6c} \\
   GF - RG \text{ [*sic*; lege } QF - RG\text{]} &= \frac{2\mathcal{A}}{3c} - \frac{2\mathcal{A}}{a + b + c} = \frac{2\mathcal{A}(a + b - 2c)}{3c(a + b + c)}

quorum quadratorum summa reducitur ad hanc formam:

.. math::

   FG^2 = \frac{1}{9(a + b + c)^2}
   \left(-a^4 - b^4 - c^4 + a^3b + ab^3 + a^3c + ac^3 + b^3c + bc^3 + 4aabb + 4aacc + 4bbcc - 5abcc - 5abbc - 5aabc\right).

Cum nunc sit:

.. math::

   a^4 + b^4 + c^4 &= p^4 - 4ppq + 2qq + 4pr \\
   aabb + aacc + bbcc &= qq - 2pr \\
   a^3b + ab^3 + a^3c + ac^3 + b^3c + bc^3 &= ppq - 2qq - pr \\
   abcc + abbc + aabc &= pr

expressio inuenta hanc induit formam:

.. math::

   FG^2 = \frac{1}{9pp}\left(-p^4 + 5ppq - 18pr\right) = \frac{-p^3 + 5pq - 18r}{9p}.

.. _euler-la-s16:

§ 16. V. Inuestigatio distantiae punctorum F et H
-------------------------------------------------

Pro hoc casu habemus:

.. math::

   AQ - AS &= \frac{3cc + bb - aa}{6c} - \frac{1}{2}c = \frac{bb - aa}{6c} \\
   QF - SH &= \frac{2\mathcal{A}}{3c} - \frac{c(aa + bb - cc)}{8\mathcal{A}} = \frac{2c^4 - (aa + bb)cc - (aa - bb)^2}{24c\mathcal{A}}.

.. folio:: § 16 (cont.)
   :page: 113

Quodsi has formulas cum casu primo comparemus, deprehendimus esse:

.. math::

   AQ - AS = \frac{1}{2}(AP - AQ) \qquad \text{et} \qquad QF - SH = \frac{1}{2}(PE - QF)

vnde manifestum est fore :math:`FH = \tfrac{1}{2}EF` ideoque

.. math::

   FH^2 = \frac{rr}{16\mathcal{A}\mathcal{A}} - \frac{1}{9}(pp - 2q).

.. _euler-la-s17:

§ 17. VI. Inuestigatio distantiae punctorum G et H
--------------------------------------------------

Pro hoc casu postremo habetur:

.. math::

   AR - AS &= \frac{c + b - a}{2} - \frac{1}{2}c = \frac{b - a}{2} \\
   RG - SH &= \frac{2\mathcal{A}}{a + b + c} - \frac{c(aa + bb - cc)}{8\mathcal{A}}
           = \frac{(a + b)c^3 + (aa + bb)cc - (a + b)(aa + bb)c - (aa - bb)^2}{8(a + b + c)\mathcal{A}}

quarum binarum formularum quadrata si addantur reperitur sequens expressio:

.. math::

   GH^2 = \frac{abc}{16(a + b + c)\mathcal{A}\mathcal{A}}\left(a^4 + b^4 + c^4 + aabc + abbc + abcc - 2aabb - 2aacc - 2bbcc\right)

vnde facta substitutione colligitur

.. math::

   GH^2 = \frac{r}{16p\mathcal{A}\mathcal{A}}(p^4 - 4ppq + 9pr) = \frac{r(p^3 - 4pq + 9r)}{16\mathcal{A}\mathcal{A}} \qquad \text{seu} \qquad GH^2 = \frac{rr}{16\mathcal{A}\mathcal{A}} - \frac{r}{p}.

.. _euler-la-s18:

.. folio:: § 18
   :page: 114

§ 18. Sex quadrata sub vno conspectu et linea Euleri
----------------------------------------------------

En ergo sub vno conspectu quadrata sex horum interuallorum:

.. math::

   \text{I.} \quad EF^2 &= \frac{rr}{4\mathcal{A}\mathcal{A}} - \frac{4}{9}(pp - 2q) \\
   \text{II.} \quad EG^2 &= \frac{rr}{4\mathcal{A}\mathcal{A}} - pp + 3q - \frac{4r}{p} \\
   \text{III.} \quad EH^2 &= \frac{9rr}{16\mathcal{A}\mathcal{A}} - pp + 2q \\
   \text{IV.} \quad FG^2 &= -\frac{1}{9}pp + \frac{5}{9}q - \frac{2r}{p} \\
   \text{V.} \quad FH^2 &= \frac{rr}{16\mathcal{A}\mathcal{A}} - \frac{1}{9}(pp - 2q) \\
   \text{VI.} \quad GH^2 &= \frac{rr}{16\mathcal{A}\mathcal{A}} - \frac{r}{p}

vbi (`Tab. II. Fig. 5.`) euidens est, esse :math:`EH = \tfrac{3}{2}EF` et :math:`FH = \tfrac{1}{2}EF`, sicque punctum :math:`H` per puncta :math:`E, F` sponte determinatur, scilicet si tria puncta :math:`E, F, G` forment triangulum :math:`EFG` tum quartum punctum :math:`H` ita in recta :math:`EF` producta erit situm vt sit :math:`FH = \tfrac{1}{2}EF` ideoque :math:`EH = \tfrac{3}{2}EF`. Hinc vero deducitur

.. math::

   4GH^2 + 2EG^2 = 3EF^2 + 6FG^2,

quod cum valoribus inuentis apprime congruit.
