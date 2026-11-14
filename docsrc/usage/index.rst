:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Bilingual Codices & Exact Symbolic Engine

The GEOMETOR edition of :cite:`Euler (1765) <euler_1765>` and :cite:`Feuerbach (1822) <feuerbach_1822>` integrates philological fidelity to historical print witnesses with interactive reading tracks and symbolic algebra.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Each unit in both the Euler (1765) and Feuerbach (1822) codices provides synchronized parallel tracks accessible from the book header bar:
   
   * **English Translation:** Direct modern mathematical translation preserving historical notation and nomenclature.
   * **Original Witness:** Verbatim historical text—1767 Latin (*Novi Commentarii*, E325) for Euler and 1822 German for Feuerbach.
   * **Summary:** Conceptual overview, formal mathematical statements, and structural outline.
   * **Notes:** Scholarly commentary, historical notes, errata identifications (e.g. Feuerbach's § 51 sign slip), and cross-references.

2. Primary-Source Folio Milestones
   Marginal page and folio markers (such as ``[p. 103]`` for Euler or ``[p. 38]`` for Feuerbach) link directly to high-resolution archival scans at Munich Digitization Center (BSB MDZ) and Internet Archive. Header **Folio** badges open the primary witness directly in a side drawer or new tab.

3. Interactive Diagrams & Deductive Links
   Throughout the text, geometric entities, assertions, and algebraic expressions link to definitions:
   
   * Geometric labels (:g:`X_1 <0038.g3:X1>`, :g:`X_5 <0038.g3:X5>`, :g:`X_{11} <0038.g3:X11>`) highlight points on companion diagrams.
   * Internal citations cross-reference companion treatises like :cite:`Ceva (1678) <ceva_1678>` and :cite:`Euclid's Elements <euclid_elements>`.
   * Dynamic SVG figures adapt seamlessly to light and dark reading themes.

4. Full-Text Search with In-Page Highlighting
   The sidebar search queries the complete bilingual text and critical notes. Search query parameters automatically append ``?highlight=`` to highlight matched terms directly inside propositions and remarks.

5. Faceted Navigation & Collection Views
   Browse topics, historical figures, and mathematical invariants via the sidebar index. Collection pages support switching between **Cards**, **Banners**, and **List** layout modes.

6. People, Bibliography & Glossary Tooltips
   Hovering over any author or mathematician (:person:`Leonhard Euler <euler>`, :person:`Karl Wilhelm Feuerbach <feuerbach>`, :person:`Karl Buzengeiger <buzengeiger>`), citation (:cite:`euler_1765`, :cite:`feuerbach_1822`), or technical term (:term:`Euler Line <euler-line>`, :term:`orthic triangle <orthic-triangle>`, :term:`Feuerbach Point <feuerbach-point>`) displays an instant context card.

----

Command-Line & Python Verification API
--------------------------------------

In addition to web reading, all thirty algebraic polynomial identities and canonical Heronian constructions are executable from the command line and Python.

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Run exact symbolic verification across all four centers, the nine-point circle, and fourfold tangencies:

.. code-block:: bash

   # Verify all identities and display the Heronian (15, 13, 14) locus table
   feuerbach

   # Export interactive theme-adaptive SVGs to a directory
   feuerbach --export-svg ./build/svgs/

Python API
~~~~~~~~~~

Import the exact symbolic solver directly into your Python scripts or Jupyter notebooks:

.. code-block:: python

   from geometor.feuerbach.euler import construct_euler_1765_centers, prove_euler_1765_identities
   from geometor.feuerbach.tangency import construct_feuerbach_tangency

   # Verify all 30 Euler 1765 symbolic identities to exact zero
   report = prove_euler_1765_identities()
   assert all(report.values())

   # Construct exact rational centers on (15, 13, 14)
   fb = construct_feuerbach_tangency()
   print(f"Nine-Point Center X(5): {fb.x5_nine_point_center.x}, {fb.x5_nine_point_center.y}")
   print(f"Feuerbach Point X(11):  {fb.x11_feuerbach_point.x}, {fb.x11_feuerbach_point.y}")
