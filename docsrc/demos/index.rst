:navigation: header
:order: 30
:layout: book

.. _demos:

Exact Symbolic Demonstrations
=============================

.. rubric:: 100% Exact SymPy Polynomial Proofs & ``geometor.model`` Compass-and-Straightedge Constructions

Unlike floating-point dynamic geometry sketches, every theorem in :cite:`Euler (1765) <euler_1765>` and :cite:`Feuerbach (1822) <feuerbach_1822>` is executed and verified symbolically in ``geometor.feuerbach`` with **zero floating-point approximations**.

Canonical Heronian ``(15, 13, 14)`` Rational Locus
--------------------------------------------------

Placing the vertices of the acute scalene Heronian triangle with sides :math:`a = 15, b = 13, c = 14` (area :math:`\Delta = 84`, semiperimeter :math:`s = 21`) at integer Cartesian coordinates ``A = (0, 0)``, ``B = (14, 0)``, ``C = (5, 12)`` places **all classical centers, tritangent centers, and Feuerbach tangencies** strictly inside :math:`\mathbb{Q}^2`:

.. picture:: /_static/constructions/feuerbach_incircle_zoom.svg
   :alt: Magnified rational coordinate detail of X(1) = (6, 4), X(5) = (6, 63/16), and the Feuerbach point X(11) = (6, 8)

* **Incenter & Incircle:** :g:`S = X_1 <0038.g3:X1>` ``= (6, 4)``, inradius :math:`r = 4`.
* **Centroid:** ``F = G = X(2) = (19/3, 4)``.
* **Circumcenter & Circumcircle:** ``H = K = X(3) = (7, 33/8)``, circumradius :math:`R = \frac{65}{8}`.
* **Orthocenter & Orthic Inradius:** ``E = O = X(4) = (5, 15/4)``, orthic inradius :math:`\rho = \frac{99}{52}`.
* **Nine-Point Center & Circle:** :g:`L = X_5 <0038.g3:X5>` ``= (6, 63/16)``, radius :math:`R_9 = \frac{65}{16}`.
* **Internal Tangency (Feuerbach Point):** :g:`X_{11} <0038.g3:X11>` ``= (6, 8)``, where :math:`Q(X_5, X_1) = \left(\frac{65}{16} - 4\right)^2 = \frac{1}{256}`.
* **Three External Excircle Tangencies:**
  :g:`Fe_a <0038.g3:F1>` ``= (2709/289, 1792/289)``,
  :g:`Fe_b <0038.g3:F2>` ``= (553/233, 1344/233)``, and
  :g:`Fe_c <0038.g3:F3>` ``= (1672/257, -24/257)``, forming the :term:`Feuerbach Triangle <feuerbach-triangle>` :g:`\triangle Fe_a Fe_b Fe_c <0038.g3:< F1 F2 F3 >>`.

Demonstration I: ``demos/euler_1765_identities.py``
---------------------------------------------------

Verifies all 30 polynomial residuals across Euler (1765) and Feuerbach (1822), solves Euler's inverse cubic reconstruction :math:`z^3 - 18z^2 + 107z - 210 = 0` on ``(5, 6, 7)``, and constructs Euler's four centers by pure compass-and-straightedge:

.. literalinclude:: ../../demos/euler_1765_identities.py
   :language: python
   :linenos:

Demonstration II: ``demos/feuerbach_tangency.py``
-------------------------------------------------

Constructs the nine-point circle, all four tritangent circles, ``X(11)``, and ``Fea, Feb, Fec`` via ``Model(..., auto_intersect=False)`` and ``model.intersect(...)``, verifying the harmonic Euler cross-ratio ``(X4, X2; X5, X3) = -1`` and exporting the four interactive ``.euclid-graphic`` SVGs:

.. literalinclude:: ../../demos/feuerbach_tangency.py
   :language: python
   :linenos:
