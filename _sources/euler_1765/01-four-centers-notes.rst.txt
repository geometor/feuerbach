:title: Euler (1765) §§ 1–9 — Critical & Symbolic Notes
:layout: book

.. _euler-01-notes:

=========================================================================
Critical & Symbolic Notes — Unit I: The Four Classical Centers (§§ 1–9)
=========================================================================

.. rubric:: Philological Apparatus, 1767 Folio Errata & Symbolic Verification

1. Concurrency Foundations: Euclid, Ceva (1678) & Euler (1765)
--------------------------------------------------------------

In **§ 1** (p. 103), :person:`Euler <euler>` takes for granted the concurrency of all four cevian and perpendicular families. Historically:

* The concurrency of the internal angle bisectors at :math:`G = X(1)` and of the perpendicular bisectors at :math:`H = X(3)` appears explicitly in :person:`Euclid <euclid>`'s *Elements* :just:`[IV. 4] <IV.4>` and :just:`[IV. 5] <IV.5>`.
* The concurrency of the medians at the center of gravity :math:`F = X(2)` goes back to Archimedes (*On the Equilibrium of Planes*, I.13–14).
* Unified ratio concurrency for medians, altitudes, and internal/external angle bisectors was established synthetically via static moments and ratio products by :person:`Giovanni Ceva <ceva>` in :cite:`*De lineis rectis se invicem secantibus statica constructio* <ceva_1678>` (Milan, 1678), paired with transversal collinearity from :person:`Menelaus of Alexandria <menelaus>`'s :cite:`*Sphaerica* <menelaus_sphaerica>` (Book III, Lemma 1). Notably, Euclid's *Elements* contains no proposition naming the orthocenter :math:`E = X(4)`, making Euler's uniform treatment of :math:`(E, F, G, H)` in **E325** the foundational watershed of modern triangle-center geometry.

2. Three Typographical Slips Verified on the 1767 St. Petersburg Folio
----------------------------------------------------------------------

Direct visual inspection of the 1767 *Novi Commentarii* page scans reveals three minor compositorial slips in §§ 4–8, all preserved with ``[sic; lege ...]`` annotations in the Latin track:

* **p. 104, § 4, line 5**: Printed ``rectae AM, BN et CN in latera opposita sunt normales``. Because the altitude from :math:`C` onto :math:`AB` has foot :math:`P` (as Euler immediately writes in § 5 ``EP`` and § 7 ``CP``), ``CN`` is a slip for ``CP``.
* **p. 106, § 7, lines 7–10**: In computing the abscissa of the centroid :math:`F`, Euler denotes the midpoint of :math:`AB = c` by lowercase :math:`c`, writes :math:`cP = \frac{bb - aa}{2c}`, and then dividing by :math:`3` prints ``bc`` instead of ``6c`` three times in succession:

  .. math::

     cQ = \frac{bb - aa}{bc} \quad [\text{lege } 6c], \qquad AQ = \frac{3cc + bb - aa}{bc} \quad [\text{lege } 6c].

  Handwritten ``6`` and ``b`` are nearly indistinguishable in 18th-century cursive; Euler uses the true denominator ``6c`` when expanding :math:`EF^2` on p. 109 (§ 12) and :math:`AQ - AS = \frac{bb - aa}{6c}` on p. 112 (§ 16).
* **p. 106, § 8, last line**: Printed ``si a latere BC ex A aequale interuallum c - x rescindatur``. Since :math:`A` does not lie on :math:`BC` and Euler has just noted :math:`BR = c - x`, ``ex A`` is a slip for ``ex B``.

3. Exact Rational Verification on the Canonical (15, 13, 14) Triangle
---------------------------------------------------------------------

In :func:`geometor.feuerbach.euler.construct_euler_1765_centers`, placing :math:`A = (0, 0)`, :math:`B = (14, 0)`, :math:`C = (5, 12)` gives integer side lengths :math:`a = 15`, :math:`b = 13`, :math:`c = 14` and integer area :math:`\mathcal{A} = 84`. Evaluating Euler's four coordinate pairs from §§ 6–9 yields exact rational points with zero radicals:

.. math::

   E = X(4) = \left(5,\; \frac{15}{4}\right), \quad
   F = X(2) = \left(\frac{19}{3},\; 4\right), \quad
   G = X(1) = (6,\; 4), \quad
   H = X(3) = \left(7,\; \frac{33}{8}\right).
