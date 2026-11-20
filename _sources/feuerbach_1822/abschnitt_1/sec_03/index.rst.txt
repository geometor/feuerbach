:layout: book
:canonical_id: §§ 3–7
:breadcrumb_title: §§ 3–7
:order: 3
:folio: §§ 3–5
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-en-s03:

.. folio:: §§ 3–5
   :page: 3

§§ 3–7: Symmetric Polynomial Laws Among the Four Tritangent Radii
=================================================================

* **§ 3 (Pairwise Exradius Sum)**: Multiplying the values of :math:`r', r'', r'''` two by two and summing the products yields

  .. math::

     r'r'' + r'r''' + r''r''' = \frac{4\Delta^2(a + b + c)}{(-a + b + c)(a - b + c)(a + b - c)} = \frac{1}{4}(a + b + c)^2,

  that is, the sum of the three rectangles formed by the three exradii taken in pairs equals the square on the semiperimeter :math:`s = \tfrac{1}{2}(a+b+c)`.

* **§ 4 (Reciprocal & Volume Relation)**: Substituting :math:`a+b+c = \frac{2\Delta}{r}` and :math:`\Delta^2 = rr'r''r'''` gives

  .. math::

     r'\,r''\,r''' = r\left(r'r'' + r'r''' + r''r'''\right) = \frac{1}{2}(a + b + c)\Delta
     \qquad \Longleftrightarrow \qquad
     \frac{1}{r'} + \frac{1}{r''} + \frac{1}{r'''} = \frac{1}{r}.

* **§ 5 (Linear Sum of Exradii, pp. 3–4)**: Adding :math:`r', r'', r'''` via the algebraic identity :math:`(a+b+c)\big[(-a+b+c)(a-b+c) + (-a+b+c)(a+b-c) + (a-b+c)(a+b-c)\big] = (-a+b+c)(a-b+c)(a+b-c) + 8abc` and introducing the circumradius :math:`R = \frac{abc}{4\Delta}` yields

  .. math::

     r' + r'' + r''' = \frac{(-a+b+c)(a-b+c)(a+b-c) + 8abc}{8\Delta} = r + 4R.

  *The sum of the three exradii equals the inradius increased by twice the diameter of the circumcircle.*

.. folio:: §§ 6–7
   :page: 4

* **§ 6 (All Six Pairwise Products & Side-Squares)**: Combining :math:`r(r'+r''+r''') = ab + ac + bc - \frac{1}{4}(a+b+c)^2` with § 3 by addition and subtraction produces the twin symmetric laws:

  .. math::

     rr' + rr'' + rr''' + r'r'' + r'r''' + r''r''' &= ab + ac + bc, \tag{1} \\
     r'r'' + r'r''' + r''r''' - r(r' + r'' + r''') &= \frac{1}{2}(a^2 + b^2 + c^2). \tag{2}

* **§ 7 (Sum of Exradius Squares)**: From :math:`r'^2 + r''^2 + r'''^2 = (r'+r''+r''')^2 - 2(r'r''+r'r'''+r''r''')` and §§ 3, 5:

  .. math::

     r'^2 + r''^2 + r'''^2 = (r + 4R)^2 - \frac{1}{2}(a + b + c)^2.

.. toctree::
   :hidden:

   de
   summary
   notes
