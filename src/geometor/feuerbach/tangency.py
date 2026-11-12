"""Exact Euclidean construction and deductive proof of Feuerbach's Theorem (1822, § 57).

Constructs on the canonical Heronian ``(15, 13, 14)`` triangle ``A = (0, 0)``, ``B = (14, 0)``,
``C = (5, 12)``:

- Side midpoints ``Ma, Mb, Mc`` (medial triangle),
- Altitude feet ``Ha, Hb, Hc`` (orthic triangle ``MNP``) and orthocenter ``X4 = (5, 15/4)``,
- Euler midpoints ``Ea, Eb, Ec`` bisecting ``AX4, BX4, CX4``,
- Circumcenter ``X3 = (7, 33/8)``, centroid ``X2 = (19/3, 4)``, and nine-point center
  ``X5 = (6, 63/16)`` along the harmonic Euler range ``(X4, X2; X5, X3) = -1``,
- The nine-point circle passing through all nine canonical points (radius ``65/16``),
- Incenter ``X1 = (6, 4)`` with its incircle (radius ``4``) and excenters
  ``Ja = (21, 14)``, ``Jb = (-7, 21/2)``, ``Jc = (8, -12)`` with their three excircles,
- The internal tangency **Feuerbach point** ``X11 = (6, 8)`` and the three external
  excircle tangency points ``Fea = (2709/289, 1792/289)``, ``Feb = (553/233, 1344/233)``,
  and ``Fec = (1672/257, -24/257)`` computed directly via :meth:`~geometor.model.Model.intersect`.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
    cross_ratio,
    is_harmonic,
    proposition,
    quadrance,
    zero_test,
)

from geometor.feuerbach.primitives import (
    construct_altitude_foot,
    construct_altitude_line,
    construct_angle_bisectors,
    construct_midpoint,
    construct_perp_bisector,
)

__all__ = [
    "FeuerbachTangencyResult",
    "construct_feuerbach_tangency",
]


@dataclass(frozen=True)
class FeuerbachTangencyResult:
    """Complete structured output of :func:`construct_feuerbach_tangency`."""

    model: Model
    vertices: tuple[spg.Point, spg.Point, spg.Point]
    triangle: spg.Polygon
    medial_points: tuple[spg.Point, spg.Point, spg.Point]
    orthic_points: tuple[spg.Point, spg.Point, spg.Point]
    euler_points: tuple[spg.Point, spg.Point, spg.Point]
    orthic_triangle: spg.Polygon
    medial_triangle: spg.Polygon
    feuerbach_triangle: spg.Polygon
    x1_incenter: spg.Point
    x2_centroid: spg.Point
    x3_circumcenter: spg.Point
    x4_orthocenter: spg.Point
    x5_nine_point_center: spg.Point
    x11_feuerbach_point: spg.Point
    excenters: tuple[spg.Point, spg.Point, spg.Point]
    excircle_tangencies: tuple[spg.Point, spg.Point, spg.Point]
    euler_line: spg.Line
    circumcircle: spg.Circle
    nine_point_circle: spg.Circle
    incircle: spg.Circle
    excircles: tuple[spg.Circle, spg.Circle, spg.Circle]
    harmonic_cross_ratio: sp.Expr


@proposition(
    "Feuerbach.1822.57",
    kind="theorem",
    title="The Nine-Point Circle and Feuerbach's Fourfold Tritangent Circle Tangency (1822)",
    hide_guides=True,
)
def construct_feuerbach_tangency(model: Model | None = None) -> FeuerbachTangencyResult:
    """Construct the nine-point circle, tritangent circles, and four Feuerbach tangency points.

    Args:
        model: Optional existing :class:`~geometor.model.Model`. When ``None``, initializes
            a clean model with ``auto_intersect=False``.

    Returns:
        :class:`FeuerbachTangencyResult` with all exact :class:`sympy.Rational` points and circles.

    Raises:
        ProofAssertionError: If any nine-point incidence, harmonic cross-ratio, or tangency
            quadrance assertion fails.
    """
    if model is None:
        model = Model("feuerbach_1822_sec57", auto_intersect=False, enable_logging=False)

    # Act I: Given Heronian (15, 13, 14) triangle ABC
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(14), sp.Integer(0), ID="B")
    pt_c = model.given_point(sp.Integer(5), sp.Integer(12), ID="C")

    line_bc = model.construct_line(pt_b, pt_c, ID="a", classes=["side"], intersect=False, by="Post.1")
    line_ca = model.construct_line(pt_c, pt_a, ID="b", classes=["side"], intersect=False, by="Post.1")
    line_ab = model.construct_line(pt_a, pt_b, ID="c", classes=["side"], intersect=False, by="Post.1")
    triangle = model.set_polygon([pt_a, pt_b, pt_c], classes=["given", "triangle"], ID="ABC")

    # Act II: Construct Nine-Point Locus, Euler Line, and Four Tritangent Circles
    # 1. Medial midpoints Ma, Mb, Mc (Feuerbach § 56: a, b, c)
    ma = construct_midpoint(model, pt_b, pt_c, ID="Ma", classes=["nine_point", "midpoint", "result"])
    mb = construct_midpoint(model, pt_c, pt_a, ID="Mb", classes=["nine_point", "midpoint", "result"])
    mc = construct_midpoint(model, pt_a, pt_b, ID="Mc", classes=["nine_point", "midpoint", "result"])
    medial_triangle = model.set_polygon([ma, mb, mc], classes=["medial_triangle"], ID="MaMbMc")

    # 2. Altitudes, orthic feet Ha, Hb, Hc (Feuerbach § 19: M, N, P), and orthocenter X4 (O)
    alt_a = construct_altitude_line(model, pt_a, pt_b, pt_c, ID="alt_A", classes=["altitude"])
    alt_b = construct_altitude_line(model, pt_b, pt_c, pt_a, ID="alt_B", classes=["altitude"])
    alt_c = construct_altitude_line(model, pt_c, pt_a, pt_b, ID="alt_C", classes=["altitude"])
    ha = model.intersect(line_bc, alt_a, ID="Ha", classes=["nine_point", "orthic", "result"], by="I.12")
    hb = model.intersect(line_ca, alt_b, ID="Hb", classes=["nine_point", "orthic", "result"], by="I.12")
    hc = model.intersect(line_ab, alt_c, ID="Hc", classes=["nine_point", "orthic", "result"], by="I.12")
    orthic_triangle = model.set_polygon([ha, hb, hc], classes=["orthic_triangle", "result"], ID="HaHbHc")
    x4 = model.intersect(
        alt_a, alt_b, ID="X4", classes=["center", "orthocenter", "result"], by="FB.19"
    )

    # 3. Euler midpoints Ea, Eb, Ec bisecting AX4, BX4, CX4
    ea = construct_midpoint(model, pt_a, x4, ID="Ea", classes=["nine_point", "euler_mid", "result"])
    eb = construct_midpoint(model, pt_b, x4, ID="Eb", classes=["nine_point", "euler_mid", "result"])
    ec = construct_midpoint(model, pt_c, x4, ID="Ec", classes=["nine_point", "euler_mid", "result"])

    # 4. Centroid X2 (G), Circumcenter X3 (K), Euler line [X3 X4], and Nine-point center X5 (L)
    med_a = model.construct_line(pt_a, ma, ID="med_A", classes=["median"], intersect=False, by="Post.1")
    med_b = model.construct_line(pt_b, mb, ID="med_B", classes=["median"], intersect=False, by="Post.1")
    x2 = model.intersect(
        med_a, med_b, ID="X2", classes=["center", "centroid", "result"], by="FB.60"
    )

    pbis_ab = construct_perp_bisector(model, pt_a, pt_b, ID="pbis_c", classes=["perp_bisector"])
    pbis_bc = construct_perp_bisector(model, pt_b, pt_c, ID="pbis_a", classes=["perp_bisector"])
    x3 = model.intersect(
        pbis_ab, pbis_bc, ID="X3", classes=["center", "circumcenter", "result"], by="IV.5"
    )
    circumcircle = model.construct_circle(
        x3, pt_a, ID="circumcircle", classes=["circumcircle"], intersect=False, by="IV.5"
    )
    euler_line = model.construct_line(
        x3, x4, ID="euler_line", classes=["euler_line", "result"], intersect=False, by="FB.54"
    )

    x5 = construct_midpoint(
        model, x4, x3, ID="X5", classes=["center", "nine_point_center", "result"]
    )
    nine_point_circle = model.construct_circle(
        x5, ha, ID="nine_point_circle", classes=["nine_point_circle", "result"], intersect=False, by="FB.56"
    )

    # 5. Internal & external angle bisectors -> Incenter X1 (S) and Excenters Ja, Jb, Jc (S', S'', S''')
    int_a, ext_a = construct_angle_bisectors(
        model, pt_a, pt_c, pt_b, internal_id="int_bis_A", external_id="ext_bis_A", classes=["bisector"]
    )
    int_b, ext_b = construct_angle_bisectors(
        model, pt_b, pt_c, pt_a, internal_id="int_bis_B", external_id="ext_bis_B", classes=["bisector"]
    )
    int_c, ext_c = construct_angle_bisectors(
        model, pt_c, pt_a, pt_b, internal_id="int_bis_C", external_id="ext_bis_C", classes=["bisector"]
    )

    x1 = model.intersect(
        int_a, int_b, ID="X1", classes=["center", "incenter", "result"], by="FB.1"
    )
    ja = model.intersect(
        int_a, ext_b, ID="Ja", classes=["center", "excenter", "result"], by="FB.1"
    )
    jb = model.intersect(
        ext_a, int_b, ID="Jb", classes=["center", "excenter", "result"], by="FB.1"
    )
    jc = model.intersect(
        ext_a, ext_b, ID="Jc", classes=["center", "excenter", "result"], by="FB.1"
    )

    # Orthogonal contact points on line AB -> exact Euclidean radii of the four tritangent circles
    tc_in = construct_altitude_foot(model, x1, pt_a, pt_b, ID="Tc", classes=["contact"])
    tc_ea = construct_altitude_foot(model, ja, pt_a, pt_b, ID="T_ea", classes=["contact"])
    tc_eb = construct_altitude_foot(model, jb, pt_a, pt_b, ID="T_eb", classes=["contact"])
    tc_ec = construct_altitude_foot(model, jc, pt_a, pt_b, ID="T_ec", classes=["contact"])

    incircle = model.construct_circle(
        x1, tc_in, ID="incircle", classes=["incircle", "tritangent", "result"], intersect=False, by="IV.4"
    )
    excircle_a = model.construct_circle(
        ja, tc_ea, ID="excircle_a", classes=["excircle", "tritangent", "result"], intersect=False, by="FB.1"
    )
    excircle_b = model.construct_circle(
        jb, tc_eb, ID="excircle_b", classes=["excircle", "tritangent", "result"], intersect=False, by="FB.1"
    )
    excircle_c = model.construct_circle(
        jc, tc_ec, ID="excircle_c", classes=["excircle", "tritangent", "result"], intersect=False, by="FB.1"
    )

    # 6. Exact Tangency Points via closed-form radical-axis intersection (discriminant == 0)
    x11 = model.intersect(
        nine_point_circle,
        incircle,
        ID="X11",
        classes=["tangency", "feuerbach_point", "result"],
        by="FB.57",
    )
    fea = model.intersect(
        nine_point_circle,
        excircle_a,
        ID="Fea",
        classes=["tangency", "excircle_tangency", "result"],
        by="FB.57",
    )
    feb = model.intersect(
        nine_point_circle,
        excircle_b,
        ID="Feb",
        classes=["tangency", "excircle_tangency", "result"],
        by="FB.57",
    )
    fec = model.intersect(
        nine_point_circle,
        excircle_c,
        ID="Fec",
        classes=["tangency", "excircle_tangency", "result"],
        by="FB.57",
    )
    feuerbach_triangle = model.set_polygon(
        [fea, feb, fec], classes=["feuerbach_triangle", "result"], ID="FeaFebFec"
    )

    # Act III: Deductive Verification
    # Concurrency at orthocenter and tritangent centers
    model.assert_incident(x4, alt_c, by="FB.19")
    model.assert_incident(x1, int_c, by="FB.1")
    model.assert_incident(ja, ext_c, by="FB.1")
    model.assert_incident(jb, ext_c, by="FB.1")
    model.assert_incident(jc, int_c, by="FB.1")

    # Incidence of all 9 canonical points on the nine-point circle (Feuerbach § 56 & 9. Satz)
    for pt_nine in (ma, mb, mc, ha, hb, hc, ea, eb, ec):
        model.assert_incident(
            pt_nine,
            nine_point_circle,
            by="FB.56",
            label=f"Nine-point incidence of {model[pt_nine].ID}",
        )

    # Euler line collinearity and harmonic cross-ratio (X4, X2; X5, X3) = -1 (Feuerbach § 60)
    model.assert_collinear(x4, x5, x2, x3, by="FB.60")
    cr_val = cross_ratio(x4, x2, x5, x3)
    if not is_harmonic(x4, x2, x5, x3):
        raise ProofAssertionError(
            f"Expected harmonic Euler range (X4, X2; X5, X3) = -1, got {cr_val}."
        )

    # Feuerbach § 57 center-distance quadrance criteria:
    # Q(X5, X1) == (R_9 - r)^2 and Q(X5, Jk) == (R_9 + r_k)^2
    r9 = nine_point_circle.radius
    r_in = incircle.radius
    if not zero_test(quadrance(x5, x1) - (r9 - r_in) ** 2):
        raise ProofAssertionError("Internal tangency condition Q(X5, X1) = (R9 - r)^2 failed.")

    for ex_ctr, ex_circ, fe_pt in (
        (ja, excircle_a, fea),
        (jb, excircle_b, feb),
        (jc, excircle_c, fec),
    ):
        if not zero_test(quadrance(x5, ex_ctr) - (r9 + ex_circ.radius) ** 2):
            raise ProofAssertionError(
                f"External tangency condition failed for {model[ex_ctr].ID}."
            )
        model.assert_collinear(
            x5,
            ex_ctr,
            fe_pt,
            by="III.12",
            label=f"Centers X5, {model[ex_ctr].ID} and tangency {model[fe_pt].ID} are collinear",
        )

    model.assert_collinear(
        x5,
        x1,
        x11,
        by="III.11",
        label="Nine-point center X5, incenter X1, and Feuerbach point X11 are collinear",
    )

    model.conclude(
        triangle,
        orthic_triangle,
        medial_triangle,
        feuerbach_triangle,
        nine_point_circle,
        incircle,
        excircle_a,
        excircle_b,
        excircle_c,
        euler_line,
        x1,
        x2,
        x3,
        x4,
        x5,
        x11,
        fea,
        feb,
        fec,
        line_bc,
        line_ca,
        line_ab,
        kind="qed",
        by="Feuerbach.1822.57",
        label="Feuerbach's nine-point circle and fourfold tangency theorem demonstrated",
    )

    return FeuerbachTangencyResult(
        model=model,
        vertices=(pt_a, pt_b, pt_c),
        triangle=triangle,
        medial_points=(ma, mb, mc),
        orthic_points=(ha, hb, hc),
        euler_points=(ea, eb, ec),
        orthic_triangle=orthic_triangle,
        medial_triangle=medial_triangle,
        feuerbach_triangle=feuerbach_triangle,
        x1_incenter=x1,
        x2_centroid=x2,
        x3_circumcenter=x3,
        x4_orthocenter=x4,
        x5_nine_point_center=x5,
        x11_feuerbach_point=x11,
        excenters=(ja, jb, jc),
        excircle_tangencies=(fea, feb, fec),
        euler_line=euler_line,
        circumcircle=circumcircle,
        nine_point_circle=nine_point_circle,
        incircle=incircle,
        excircles=(excircle_a, excircle_b, excircle_c),
        harmonic_cross_ratio=cr_val,
    )
