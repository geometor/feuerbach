"""Euclidean compass-and-straightedge sub-constructions for triangle geometry.

Every helper in this module operates strictly inside a :class:`~geometor.model.Model`
using exact symbolic :mod:`sympy` coordinates, targeted :meth:`~geometor.model.Model.intersect`
selectors, and :func:`~geometor.model.proposition` guide encapsulation—never injecting
floating-point numbers or synthetic coordinate formulas.
"""

from __future__ import annotations

import sympy.geometry as spg
from geometor.model import Model, proposition

__all__ = [
    "construct_altitude_foot",
    "construct_altitude_line",
    "construct_angle_bisectors",
    "construct_midpoint",
    "construct_perp_bisector",
]


@proposition(
    "Euclid.I.10.bisector",
    g_id="G.42",
    kind="problem",
    title="Construct the perpendicular bisector of a segment",
    hide_guides=True,
)
def construct_perp_bisector(
    model: Model,
    pt_a: spg.Point,
    pt_b: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the perpendicular bisector of segment ``AB`` via equilateral poles.

    Args:
        model: Target :class:`~geometor.model.Model`.
        pt_a: First endpoint ``A``.
        pt_b: Second endpoint ``B``.
        ID: Optional identifier for the constructed line.
        classes: Optional CSS/semantic class labels.

    Returns:
        The exact :class:`sympy.geometry.Line` perpendicularly bisecting ``AB``.
    """
    c_ab = model.construct_circle(pt_a, pt_b, guide=True, intersect=False, by="Post.3")
    c_ba = model.construct_circle(pt_b, pt_a, guide=True, intersect=False, by="Post.3")
    pole_pos = model.intersect(c_ab, c_ba, side_of=(pt_a, pt_b, +1), guide=True, by="I.1")
    pole_neg = model.intersect(c_ab, c_ba, side_of=(pt_a, pt_b, -1), guide=True, by="I.1")
    return model.construct_line(
        pole_pos,
        pole_neg,
        ID=ID,
        classes=classes,
        intersect=False,
        by="Post.1",
    )


@proposition(
    "Euclid.I.10",
    g_id="G.42",
    kind="problem",
    title="Bisect a given finite straight line",
    hide_guides=True,
)
def construct_midpoint(
    model: Model,
    pt_a: spg.Point,
    pt_b: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact Euclidean midpoint of ``pt_a`` and ``pt_b``.

    Args:
        model: Target :class:`~geometor.model.Model`.
        pt_a: First endpoint ``A``.
        pt_b: Second endpoint ``B``.
        ID: Optional identifier for the midpoint.
        classes: Optional CSS/semantic class labels.

    Returns:
        The exact midpoint :class:`sympy.geometry.Point` on ``[pt_a, pt_b]``.
    """
    line_ab = model.construct_line(pt_a, pt_b, guide=True, intersect=False, by="Post.1")
    bisector = construct_perp_bisector(model, pt_a, pt_b)
    return model.intersect(
        line_ab,
        bisector,
        ID=ID,
        classes=classes,
        by="I.10",
    )


@proposition(
    "Euclid.I.12",
    g_id="G.46",
    kind="problem",
    title="Drop a perpendicular straight line from a point not on an infinite straight line",
    hide_guides=True,
)
def construct_altitude_line(
    model: Model,
    vertex: spg.Point,
    side_p1: spg.Point,
    side_p2: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the perpendicular line from ``vertex`` onto line ``[side_p1, side_p2]``.

    Reflects ``vertex`` across ``[side_p1, side_p2]`` via circles ``(side_p1, vertex)``
    and ``(side_p2, vertex)`` so that no irrational intermediate radicals are introduced
    when ``vertex``, ``side_p1``, and ``side_p2`` have rational coordinates.

    Args:
        model: Target :class:`~geometor.model.Model`.
        vertex: Point outside the line ``[side_p1, side_p2]``.
        side_p1: First distinct point defining the target line.
        side_p2: Second distinct point defining the target line.
        ID: Optional identifier for the altitude line.
        classes: Optional CSS/semantic class labels.

    Returns:
        The exact perpendicular :class:`sympy.geometry.Line` through ``vertex``.
    """
    c1 = model.construct_circle(side_p1, vertex, guide=True, intersect=False, by="Post.3")
    c2 = model.construct_circle(side_p2, vertex, guide=True, intersect=False, by="Post.3")
    mirror = model.intersect(c1, c2, other_than=vertex, guide=True, by="I.12")
    return model.construct_line(
        vertex,
        mirror,
        ID=ID,
        classes=classes,
        intersect=False,
        by="Post.1",
    )


@proposition(
    "Euclid.I.12.foot",
    g_id="G.46",
    kind="problem",
    title="Construct the orthogonal foot of a point on a straight line",
    hide_guides=True,
)
def construct_altitude_foot(
    model: Model,
    vertex: spg.Point,
    side_p1: spg.Point,
    side_p2: spg.Point,
    *,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the orthogonal projection (pedal foot) of ``vertex`` onto ``[side_p1, side_p2]``.

    Args:
        model: Target :class:`~geometor.model.Model`.
        vertex: Point outside the line ``[side_p1, side_p2]``.
        side_p1: First distinct point defining the target line.
        side_p2: Second distinct point defining the target line.
        ID: Optional identifier for the pedal foot.
        classes: Optional CSS/semantic class labels.

    Returns:
        The orthogonal foot :class:`sympy.geometry.Point` on ``[side_p1, side_p2]``.
    """
    base_line = model.construct_line(side_p1, side_p2, guide=True, intersect=False, by="Post.1")
    alt_line = construct_altitude_line(model, vertex, side_p1, side_p2)
    return model.intersect(
        base_line,
        alt_line,
        ID=ID,
        classes=classes,
        by="I.12",
    )


@proposition(
    "Euclid.I.9",
    g_id="G.40",
    kind="problem",
    title="Bisect a given rectilineal angle internally and externally",
    hide_guides=True,
)
def construct_angle_bisectors(
    model: Model,
    vertex: spg.Point,
    ray_p1: spg.Point,
    ray_p2: spg.Point,
    *,
    internal_id: str = "",
    external_id: str = "",
    classes: list[str] | None = None,
) -> tuple[spg.Line, spg.Line]:
    """Construct both the internal and external angle bisectors at ``vertex``.

    Marks equal segments along ``[vertex, ray_p2]`` via circle ``(vertex, ray_p1)``
    and connects ``vertex`` to the midpoints of the two chords from ``ray_p1``.

    Args:
        model: Target :class:`~geometor.model.Model`.
        vertex: Angle vertex ``V``.
        ray_p1: Point on the first side ray ``VP1``.
        ray_p2: Point on the second side ray ``VP2``.
        internal_id: Optional identifier for the internal angle bisector.
        external_id: Optional identifier for the external angle bisector.
        classes: Optional CSS/semantic class labels.

    Returns:
        Tuple ``(internal_bisector, external_bisector)`` of orthogonal lines through ``vertex``.
    """
    line_vp2 = model.construct_line(vertex, ray_p2, guide=True, intersect=False, by="Post.1")
    transfer_circle = model.construct_circle(
        vertex, ray_p1, guide=True, intersect=False, by="Post.3"
    )
    q_int = model.intersect(
        transfer_circle,
        line_vp2,
        on_ray=(vertex, ray_p2),
        guide=True,
        by="I.3",
    )
    q_ext = model.intersect(
        transfer_circle,
        line_vp2,
        other_than=q_int,
        guide=True,
        by="Post.2",
    )
    mid_int = construct_midpoint(model, ray_p1, q_int)
    mid_ext = construct_midpoint(model, ray_p1, q_ext)
    internal = model.construct_line(
        vertex,
        mid_int,
        ID=internal_id,
        classes=list(classes) if classes else None,
        intersect=False,
        by="I.9",
    )
    external = model.construct_line(
        vertex,
        mid_ext,
        ID=external_id,
        classes=list(classes) if classes else None,
        intersect=False,
        by="I.9",
    )
    return internal, external
