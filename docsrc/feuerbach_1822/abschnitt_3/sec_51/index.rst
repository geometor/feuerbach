:layout: book
:canonical_id: § 51
:breadcrumb_title: § 51
:order: 3
:folio: p. 35
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _fb-en-s51:

.. folio:: § 51
   :page: 35

§ 51: Squared Distance from the Orthocenter O to S (and the Excenter Sign Slip)
===============================================================================

If :math:`O` [:g:`X_4 <0038.g1:X4>`] is as hitherto the intersection point of the altitudes :math:`AM, BN, CP` of triangle :math:`ABC`, and one draws :math:`OS`, then :math:`\overline{OS}^2 = (AF - AP)^2 + (OP - SF)^2`, where :math:`F` is the contact point of the incircle on :math:`AB`. Now since :math:`AF = \tfrac{1}{2}(-a+b+c)` and :math:`AP = \frac{-a^2+b^2+c^2}{2c}`, while (§ 35) :math:`OP = \frac{(-a^2+b^2+c^2)(a^2-b^2+c^2)}{8c\Delta}` and (§ 2) :math:`SF = \frac{2\Delta}{a+b+c}`, we have:

.. math::

   AF - AP &= \frac{(a - b + c)(a + b - c) - c(a + b - c)}{2c}, \\
   OP - SF &= \frac{(-a^2 + b^2 + c^2)(a^2 - b^2 + c^2) - c(-a + b + c)(a - b + c)(a + b - c)}{8c\Delta}.

Substituting into the expression for :math:`\overline{OS}^2`, one brings it at length into the symmetric form:

.. math::

   \overline{OS}^2 = \frac{(-a+b+c)^2(a-b+c)^2(a+b-c)^2 - (-a^2+b^2+c^2)(a^2-b^2+c^2)(a^2+b^2-c^2)}{32\Delta^2},

whence, introducing the circle radii :math:`r, \rho, R`, there results:

.. math::

   \overline{OS}^2 = 2r^2 - 2\rho R;

that is: *In every acute-angled triangle, the square of the distance from the intersection point of its altitudes to the center of the inscribed circle equals twice the square on the radius of this circle, diminished by the rectangle contained by the diameter of the circumscribed circle and the radius of the circle inscribed in the orthic triangle.*

Setting :math:`a, b, c` negative successively in this expression, Feuerbach writes for the distances from :math:`O` to :math:`S', S'', S'''`:

.. math::

   \overline{OS'}^2 = 2r'^2 + 2\rho R, \qquad
   \overline{OS''}^2 = 2r''^2 + 2\rho R, \qquad
   \overline{OS'''}^2 = 2r'''^2 + 2\rho R

*[Editor's Critical Note: Because both :math:`R` and :math:`\rho` negate simultaneously under :math:`a \mapsto -a`, their product :math:`\rho R` is invariant; the true exact identities over :math:`\mathbb{Q}(a,b,c)` are :math:`\overline{OS^{(k)}}^2 = 2r^{(k)2} - 2\rho R`. Crucially, this slip does not affect §§ 53–59 at all; see :ref:`Unit III Critical Notes <fb-03-notes>` for the complete SymPy proof.]*

.. toctree::
   :hidden:

   de
   summary
   notes
