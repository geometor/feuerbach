"""Theme-adaptive ``.euclid-graphic`` SVG exporter for Euler (1765) and Feuerbach (1822).

Generates clean, standards-compliant ``<svg class="euclid-graphic">`` diagrams directly
from exact :class:`~geometor.model.Model` constructions. Every geometric element carries:

- 3-vertex midpoint paths ``M x1 y1 L mx my L x2 y2`` supporting ``#geom-tick-1..3`` equality ticks,
- Canonical ``data-ref`` tokens (``A``, ``X5``, ``X11``, ``/ A B /``, ``[ X3 X4 ]``,
  ``( X5 H1 )``, ``< A B C >``) compatible with ``geometor_interactive.js``,
- Presentation attributes bound to ``var(--geom-fg)``, ``var(--geom-accent)``,
  ``var(--geom-assert)``, and ``var(--geom-coincide)`` so both standalone SVGs and
  ``publish`` inline ``.. picture::`` book figures adapt seamlessly to light and dark themes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.feuerbach.euler import EulerCentersResult, construct_euler_1765_centers
from geometor.feuerbach.tangency import (
    FeuerbachTangencyResult,
    construct_feuerbach_tangency,
)

__all__ = [
    "SvgSpec",
    "export_all_codex_svgs",
    "render_euler_1765_svg",
    "render_feuerbach_full_svg",
    "render_feuerbach_zoom_svg",
    "render_model_svg",
    "render_nine_point_svg",
]


@dataclass(frozen=True)
class SvgSpec:
    """Viewport and graphic metadata for an exported ``.euclid-graphic`` SVG."""

    folio: str
    graphic: str
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    width_px: int = 680

    @property
    def graphic_id(self) -> str:
        """Return canonical ``<folio>.<graphic>`` identifier."""
        return f"{self.folio}.{self.graphic}"


class _Canvas:
    """Coordinate transformer from exact Cartesian ``(x, y)`` to SVG screen pixels."""

    def __init__(self, spec: SvgSpec) -> None:
        self.spec = spec
        span_x = spec.xmax - spec.xmin
        span_y = spec.ymax - spec.ymin
        self.scale = spec.width_px / span_x
        self.width = spec.width_px
        self.height = round(span_y * self.scale)

    def xy(self, pt: spg.Point | tuple[sp.Expr | float, sp.Expr | float]) -> tuple[float, float]:
        """Map math point ``(x, y)`` to SVG pixel coordinates ``(sx, sy)``."""
        if isinstance(pt, spg.Point):
            rx = float(pt.x.evalf())
            ry = float(pt.y.evalf())
        else:
            rx = float(sp.sympify(pt[0]).evalf())
            ry = float(sp.sympify(pt[1]).evalf())
        sx = (rx - self.spec.xmin) * self.scale
        sy = (self.spec.ymax - ry) * self.scale
        return sx, sy

    def radius(self, r_expr: sp.Expr | float) -> float:
        """Map exact math radius to SVG pixel radius."""
        return float(sp.sympify(r_expr).evalf()) * self.scale


def _fmt(val: float) -> str:
    return f"{val:.2f}"


def _mid_seg_d(x1: float, y1: float, x2: float, y2: float) -> str:
    mx = 0.5 * (x1 + x2)
    my = 0.5 * (y1 + y2)
    return f"M {_fmt(x1)} {_fmt(y1)} L {_fmt(mx)} {_fmt(my)} L {_fmt(x2)} {_fmt(y2)}"


def _clip_line_to_box(
    line: spg.Line, xmin: float, xmax: float, ymin: float, ymax: float
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an infinite SymPy ``Line`` to the viewport rectangle."""
    x1, y1 = float(line.p1.x.evalf()), float(line.p1.y.evalf())
    x2, y2 = float(line.p2.x.evalf()), float(line.p2.y.evalf())
    dx, dy = x2 - x1, y2 - y1
    hits: list[tuple[float, float]] = []
    eps = 1e-9
    if abs(dx) > eps:
        for xb in (xmin, xmax):
            t = (xb - x1) / dx
            yb = y1 + t * dy
            if ymin - 1e-6 <= yb <= ymax + 1e-6:
                hits.append((xb, yb))
    if abs(dy) > eps:
        for yb in (ymin, ymax):
            t = (yb - y1) / dy
            xb = x1 + t * dx
            if xmin - 1e-6 <= xb <= xmax + 1e-6:
                hits.append((xb, yb))
    unique: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(abs(hx - ux) < 1e-4 and abs(hy - uy) < 1e-4 for ux, uy in unique):
            unique.append((hx, hy))
    if len(unique) < 2:
        return None
    return unique[0], unique[1]


def _format_svg_label(label: str) -> str:
    """Convert ``X_b`` or ``Fe_c`` subscript notation into ``<tspan>`` SVG markup."""
    if "_" not in label:
        return label
    base, sub = label.split("_", 1)
    return f'{base}<tspan dy="3" font-size="10.5">{sub}</tspan>'


def _svg_header(canvas: _Canvas, title: str) -> list[str]:
    gid = canvas.spec.graphic_id
    clip_id = f"clip-{gid.replace('.', '-')}"
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'data-graphic-id="{gid}" data-folio="{canvas.spec.folio}" '
        f'data-graphic="{canvas.spec.graphic}" '
        f'viewBox="0 0 {canvas.width} {canvas.height}" '
        f'width="{canvas.width}" height="{canvas.height}" role="img" aria-label="{title}">',
        f"  <title>{title}</title>",
        "  <style>",
        "    :root { --geom-fg: #18181b; --geom-accent: #c88a1e; --geom-assert: #16a34a; --geom-coincide: #0891b2; --geom-point-stroke: #ffffff; }",
        "    @media (prefers-color-scheme: dark) { :root { --geom-fg: #d6cfc5; --geom-accent: #e8b85a; --geom-assert: #5ec27e; --geom-coincide: #38bdf8; --geom-point-stroke: #1e1e20; } }",
        "    #highlights > * { opacity: 0; pointer-events: none; }",
        "  </style>",
        "  <defs>",
        f'    <clipPath id="{clip_id}"><rect x="0" y="0" width="{canvas.width}" height="{canvas.height}"/></clipPath>',
        '    <marker id="geom-tick-1" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M 0 -4.5 L 0 4.5" stroke="var(--geom-assert, #5ec27e)" stroke-width="1.6" fill="none"/>',
        "    </marker>",
        '    <marker id="geom-tick-2" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M -2 -4.5 L -2 4.5 M 2 -4.5 L 2 4.5" stroke="var(--geom-assert, #5ec27e)" stroke-width="1.6" fill="none"/>',
        "    </marker>",
        '    <marker id="geom-tick-3" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M -3.5 -4.5 L -3.5 4.5 M 0 -4.5 L 0 4.5 M 3.5 -4.5 L 3.5 4.5" stroke="var(--geom-assert, #5ec27e)" stroke-width="1.6" fill="none"/>',
        "    </marker>",
        "  </defs>",
    ]


def _build_svg(
    canvas: _Canvas,
    title: str,
    *,
    polygons: Sequence[tuple[Sequence[spg.Point], str, str, str, float]],
    lines: Sequence[tuple[spg.Line, str, str, float, str | None, float]],
    segments: Sequence[tuple[spg.Point, spg.Point, str, str, float, str | None, float]],
    circles: Sequence[tuple[spg.Circle, str, str | None, str, float, str | None, float]],
    points: Sequence[tuple[spg.Point, str, str | None, str, float, str, tuple[float, float]]],
) -> str:
    """Assemble ordered ``.euclid-graphic`` SVG groups with interactive overlays."""
    out = _svg_header(canvas, title)
    clip_id = f"clip-{canvas.spec.graphic_id.replace('.', '-')}"
    elements_g: list[str] = [f'  <g id="elements" clip-path="url(#{clip_id})">']
    graphics_g: list[str] = [f'  <g id="graphics" clip-path="url(#{clip_id})">']
    highlights_g: list[str] = [
        f'  <g id="highlights" clip-path="url(#{clip_id})" style="pointer-events: none;">'
    ]
    points_g: list[str] = ['  <g id="points">']
    labels_g: list[str] = ['  <g id="labels">']

    for pts_seq, ref, stroke, fill_col, fill_op in polygons:
        coords = [canvas.xy(p) for p in pts_seq]
        pts_attr = " ".join(f"{_fmt(x)},{_fmt(y)}" for x, y in coords)
        elements_g.append(
            f'    <polygon class="polygon" data-ref="{ref}" points="{pts_attr}" '
            f'fill="{fill_col}" fill-opacity="{fill_op:.2f}" stroke="{stroke}" stroke-width="1.6"/>'
        )
        highlights_g.append(
            f'    <polygon class="polygon geom-overlay" data-ref="{ref}" points="{pts_attr}" '
            f'fill="var(--geom-accent)" fill-opacity="0.20" stroke="var(--geom-accent)" stroke-width="2.0"/>'
        )

    for ln, ref, stroke, width, dash, opacity in lines:
        clipped = _clip_line_to_box(
            ln,
            canvas.spec.xmin,
            canvas.spec.xmax,
            canvas.spec.ymin,
            canvas.spec.ymax,
        )
        if clipped is None:
            continue
        (x1, y1), (x2, y2) = canvas.xy(clipped[0]), canvas.xy(clipped[1])
        d_str = _mid_seg_d(x1, y1, x2, y2)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        graphics_g.append(
            f'    <path class="line" data-ref="{ref}" d="{d_str}" fill="none" '
            f'stroke="{stroke}" stroke-width="{width:.2f}" stroke-opacity="{opacity:.2f}"{dash_attr}/>'
        )
        highlights_g.append(
            f'    <path class="line geom-overlay" data-ref="{ref}" d="{d_str}" fill="none" '
            f'stroke="var(--geom-accent)" stroke-width="2.4"/>'
        )

    for p1, p2, ref, stroke, width, dash, opacity in segments:
        x1, y1 = canvas.xy(p1)
        x2, y2 = canvas.xy(p2)
        d_str = _mid_seg_d(x1, y1, x2, y2)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        elements_g.append(
            f'    <path class="segment" data-ref="{ref}" d="{d_str}" fill="none" '
            f'stroke="{stroke}" stroke-width="{width:.2f}" stroke-opacity="{opacity:.2f}"{dash_attr}/>'
        )
        highlights_g.append(
            f'    <path class="segment geom-overlay" data-ref="{ref}" d="{d_str}" fill="none" '
            f'stroke="var(--geom-accent)" stroke-width="2.6"/>'
        )

    for circ, ref, aliases, stroke, width, dash, opacity in circles:
        cx, cy = canvas.xy(circ.center)
        r_px = canvas.radius(circ.radius)
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        alias_attr = f' data-aliases="{aliases}"' if aliases else ""
        elements_g.append(
            f'    <circle class="circle" data-ref="{ref}"{alias_attr} '
            f'cx="{_fmt(cx)}" cy="{_fmt(cy)}" r="{_fmt(r_px)}" fill="none" '
            f'stroke="{stroke}" stroke-width="{width:.2f}" stroke-opacity="{opacity:.2f}"{dash_attr}/>'
        )
        highlights_g.append(
            f'    <circle class="circle geom-overlay" data-ref="{ref}"{alias_attr} '
            f'cx="{_fmt(cx)}" cy="{_fmt(cy)}" r="{_fmt(r_px)}" fill="none" '
            f'stroke="var(--geom-accent)" stroke-width="2.6"/>'
        )

    for pt, ref, aliases, color, rad, display_lbl, (dx, dy) in points:
        px, py = canvas.xy(pt)
        alias_attr = f' data-aliases="{aliases}"' if aliases else ""
        points_g.append(
            f'    <circle class="point geom-point" data-ref="{ref}"{alias_attr} '
            f'cx="{_fmt(px)}" cy="{_fmt(py)}" r="{rad:.1f}" fill="{color}" '
            f'stroke="var(--geom-point-stroke, #1e1e20)" stroke-width="1.2"/>'
        )
        if display_lbl:
            lx, ly = px + dx, py + dy
            labels_g.append(
                f'    <text class="label geom-label" data-ref="{ref}"{alias_attr} '
                f'x="{_fmt(lx)}" y="{_fmt(ly)}" fill="{color}" '
                f'font-family="EB Garamond, Georgia, serif" font-size="14" font-style="italic">'
                f"{_format_svg_label(display_lbl)}</text>"
            )

    elements_g.append("  </g>")
    graphics_g.append("  </g>")
    highlights_g.append("  </g>")
    points_g.append("  </g>")
    labels_g.append("  </g>")
    out.extend(elements_g)
    out.extend(graphics_g)
    out.extend(highlights_g)
    out.extend(points_g)
    out.extend(labels_g)
    out.append("</svg>")
    return "\n".join(out) + "\n"


def render_euler_1765_svg(res: EulerCentersResult | None = None) -> str:
    """Render Euler's 1765 memoir configuration (``E, F, G, H`` and the Euler line)."""
    if res is None:
        res = construct_euler_1765_centers()
    pt_a, pt_b, pt_c = res.vertices
    x1, x2, x3, x4 = (
        res.x1_incenter_G,
        res.x2_centroid_F,
        res.x3_circumcenter_H,
        res.x4_orthocenter_E,
    )

    spec = SvgSpec(folio="0114", graphic="g1", xmin=-2.5, xmax=16.5, ymin=-5.0, ymax=13.5)
    canvas = _Canvas(spec)

    ma = spg.Point((pt_b.x + pt_c.x) / 2, (pt_b.y + pt_c.y) / 2)
    mb = spg.Point((pt_c.x + pt_a.x) / 2, (pt_c.y + pt_a.y) / 2)
    mc = spg.Point((pt_a.x + pt_b.x) / 2, (pt_a.y + pt_b.y) / 2)
    ha = res.model.get_element_by_ID("Tc")  # incircle foot on AB
    alt_a = res.model.get_element_by_ID("alt_A")
    alt_b = res.model.get_element_by_ID("alt_B")
    alt_c = res.model.get_element_by_ID("alt_C")

    return _build_svg(
        canvas,
        "Euler (1765/1767, E325): Four Classical Triangle Centers E, F, G, H and the Euler Line",
        polygons=[([pt_a, pt_b, pt_c], "< A B C >", "var(--geom-fg)", "var(--geom-fg)", 0.04)],
        lines=[
            (alt_a, "[ A X4 ]", "var(--geom-fg)", 0.85, "3,3", 0.42),
            (alt_b, "[ B X4 ]", "var(--geom-fg)", 0.85, "3,3", 0.42),
            (alt_c, "[ C X4 ]", "var(--geom-fg)", 0.85, "3,3", 0.42),
            (res.euler_line, "[ X3 X4 ]", "var(--geom-accent)", 2.1, None, 0.95),
        ],
        segments=[
            (pt_a, pt_b, "/ A B /", "var(--geom-fg)", 1.7, None, 0.95),
            (pt_b, pt_c, "/ B C /", "var(--geom-fg)", 1.7, None, 0.95),
            (pt_c, pt_a, "/ C A /", "var(--geom-fg)", 1.7, None, 0.95),
            (pt_a, ma, "/ A M1 /", "var(--geom-fg)", 0.85, "5,3", 0.40),
            (pt_b, mb, "/ B M2 /", "var(--geom-fg)", 0.85, "5,3", 0.40),
            (pt_c, mc, "/ C M3 /", "var(--geom-fg)", 0.85, "5,3", 0.40),
            (x4, x1, "/ X4 X1 /", "var(--geom-coincide)", 1.15, "2,2", 0.78),
            (x2, x1, "/ X2 X1 /", "var(--geom-coincide)", 1.15, "2,2", 0.78),
            (x3, x1, "/ X3 X1 /", "var(--geom-coincide)", 1.15, "2,2", 0.78),
        ],
        circles=[
            (res.circumcircle, "( X3 A )", "( A B C )", "var(--geom-fg)", 1.25, "6,3", 0.65),
            (res.incircle, "( X1 T0 )", None, "var(--geom-assert)", 1.45, None, 0.88),
        ],
        points=[
            (pt_a, "A", None, "var(--geom-fg)", 4.2, "A", (-16, 15)),
            (pt_b, "B", None, "var(--geom-fg)", 4.2, "B", (8, 15)),
            (pt_c, "C", None, "var(--geom-fg)", 4.2, "C", (-4, -10)),
            (ma, "M1", None, "var(--geom-fg)", 2.6, "a", (7, -3)),
            (mb, "M2", None, "var(--geom-fg)", 2.6, "b", (-14, -3)),
            (mc, "M3", None, "var(--geom-fg)", 2.6, "S", (-4, 15)),
            (ha, "T0", None, "var(--geom-assert)", 2.6, "R", (-5, 15)),
            (x4, "X4", "E", "var(--geom-accent)", 4.6, "E (X₄)", (-42, 13)),
            (x2, "X2", "F", "var(--geom-accent)", 4.4, "F (X₂)", (-6, -10)),
            (x1, "X1", "G", "var(--geom-assert)", 4.6, "G (X₁)", (-14, 17)),
            (x3, "X3", "H", "var(--geom-accent)", 4.6, "H (X₃)", (9, -5)),
        ],
    )


def render_nine_point_svg(res: FeuerbachTangencyResult | None = None) -> str:
    """Render the Nine-Point Circle, Orthic/Medial triangles, and Harmonic Euler Range."""
    if res is None:
        res = construct_feuerbach_tangency()
    pt_a, pt_b, pt_c = res.vertices
    ma, mb, mc = res.medial_points
    ha, hb, hc = res.orthic_points
    ea, eb, ec = res.euler_points

    spec = SvgSpec(folio="0038", graphic="g1", xmin=-2.2, xmax=16.2, ymin=-4.6, ymax=13.2)
    canvas = _Canvas(spec)

    return _build_svg(
        canvas,
        "Feuerbach (1822, §§ 54–56 & 9. Satz): The Nine-Point Circle and Harmonic Euler Range",
        polygons=[
            ([pt_a, pt_b, pt_c], "< A B C >", "var(--geom-fg)", "var(--geom-fg)", 0.03),
            ([ha, hb, hc], "< H1 H2 H3 >", "var(--geom-coincide)", "var(--geom-coincide)", 0.08),
            ([ma, mb, mc], "< M1 M2 M3 >", "var(--geom-fg)", "var(--geom-fg)", 0.02),
        ],
        lines=[
            (res.euler_line, "[ X3 X4 ]", "var(--geom-accent)", 1.9, None, 0.92),
        ],
        segments=[
            (pt_a, pt_b, "/ A B /", "var(--geom-fg)", 1.65, None, 0.94),
            (pt_b, pt_c, "/ B C /", "var(--geom-fg)", 1.65, None, 0.94),
            (pt_c, pt_a, "/ C A /", "var(--geom-fg)", 1.65, None, 0.94),
            (pt_a, ha, "/ A H1 /", "var(--geom-fg)", 0.9, "3,3", 0.45),
            (pt_b, hb, "/ B H2 /", "var(--geom-fg)", 0.9, "3,3", 0.45),
            (pt_c, hc, "/ C H3 /", "var(--geom-fg)", 0.9, "3,3", 0.45),
        ],
        circles=[
            (res.circumcircle, "( X3 A )", "( A B C )", "var(--geom-fg)", 1.1, "6,4", 0.48),
            (res.nine_point_circle, "( X5 H1 )", "( H1 H2 H3 )", "var(--geom-accent)", 2.2, None, 0.98),
        ],
        points=[
            (pt_a, "A", None, "var(--geom-fg)", 4.0, "A", (-15, 14)),
            (pt_b, "B", None, "var(--geom-fg)", 4.0, "B", (7, 14)),
            (pt_c, "C", None, "var(--geom-fg)", 4.0, "C", (-4, -10)),
            (ma, "M1", None, "var(--geom-assert)", 3.8, "Mₐ", (7, -3)),
            (mb, "M2", None, "var(--geom-assert)", 3.8, "M_b", (-22, -3)),
            (mc, "M3", None, "var(--geom-assert)", 3.8, "M_c", (4, 15)),
            (ha, "H1", "M", "var(--geom-coincide)", 4.0, "M (Hₐ)", (7, 5)),
            (hb, "H2", "N", "var(--geom-coincide)", 4.0, "N (H_b)", (-44, -2)),
            (hc, "H3", "P", "var(--geom-coincide)", 4.0, "P (H_c)", (-18, 15)),
            (ea, "E1", None, "var(--geom-accent)", 3.5, "Eₐ", (-16, 12)),
            (eb, "E2", None, "var(--geom-accent)", 3.5, "E_b", (6, -5)),
            (ec, "E3", None, "var(--geom-accent)", 3.5, "E_c", (6, 4)),
            (res.x4_orthocenter, "X4", "O", "var(--geom-fg)", 4.2, "O (X₄)", (-38, 6)),
            (res.x5_nine_point_center, "X5", "L", "var(--geom-accent)", 4.5, "L (X₅)", (-14, -9)),
            (res.x2_centroid, "X2", "G", "var(--geom-fg)", 3.8, "G (X₂)", (4, 14)),
            (res.x3_circumcenter, "X3", "K", "var(--geom-fg)", 4.2, "K (X₃)", (8, -4)),
        ],
    )


def render_feuerbach_full_svg(res: FeuerbachTangencyResult | None = None) -> str:
    """Render Feuerbach's full fourfold tangency configuration (incircle + 3 excircles)."""
    if res is None:
        res = construct_feuerbach_tangency()
    pt_a, pt_b, pt_c = res.vertices
    ja, jb, jc = res.excenters
    fea, feb, fec = res.excircle_tangencies
    exa, exb, exc = res.excircles
    ha, _, _ = res.orthic_points

    spec = SvgSpec(folio="0038", graphic="g2", xmin=-18.8, xmax=36.2, ymin=-25.2, ymax=29.2)
    canvas = _Canvas(spec)

    side_ab = spg.Line(pt_a, pt_b)
    side_bc = spg.Line(pt_b, pt_c)
    side_ca = spg.Line(pt_c, pt_a)

    return _build_svg(
        canvas,
        "Feuerbach's Theorem (1822, § 57): Nine-Point Circle Tangent to the Incircle and Three Excircles",
        polygons=[
            ([pt_a, pt_b, pt_c], "< A B C >", "var(--geom-fg)", "var(--geom-fg)", 0.06),
            ([fea, feb, fec], "< F1 F2 F3 >", "var(--geom-assert)", "var(--geom-assert)", 0.08),
        ],
        lines=[
            (side_ab, "[ A B ]", "var(--geom-fg)", 0.75, "4,4", 0.35),
            (side_bc, "[ B C ]", "var(--geom-fg)", 0.75, "4,4", 0.35),
            (side_ca, "[ C A ]", "var(--geom-fg)", 0.75, "4,4", 0.35),
        ],
        segments=[
            (pt_a, pt_b, "/ A B /", "var(--geom-fg)", 1.7, None, 0.95),
            (pt_b, pt_c, "/ B C /", "var(--geom-fg)", 1.7, None, 0.95),
            (pt_c, pt_a, "/ C A /", "var(--geom-fg)", 1.7, None, 0.95),
            (res.x5_nine_point_center, ja, "/ X5 J1 /", "var(--geom-coincide)", 0.95, "3,2", 0.65),
            (res.x5_nine_point_center, jb, "/ X5 J2 /", "var(--geom-coincide)", 0.95, "3,2", 0.65),
            (res.x5_nine_point_center, jc, "/ X5 J3 /", "var(--geom-coincide)", 0.95, "3,2", 0.65),
        ],
        circles=[
            (exa, "( J1 F1 )", None, "var(--geom-coincide)", 1.35, None, 0.80),
            (exb, "( J2 F2 )", None, "var(--geom-coincide)", 1.35, None, 0.80),
            (exc, "( J3 F3 )", None, "var(--geom-coincide)", 1.35, None, 0.80),
            (res.incircle, "( X1 X11 )", None, "var(--geom-assert)", 1.45, None, 0.90),
            (res.nine_point_circle, "( X5 H1 )", None, "var(--geom-accent)", 2.25, None, 1.00),
        ],
        points=[
            (pt_a, "A", None, "var(--geom-fg)", 3.6, "A", (-13, 13)),
            (pt_b, "B", None, "var(--geom-fg)", 3.6, "B", (6, 13)),
            (pt_c, "C", None, "var(--geom-fg)", 3.6, "C", (-4, -9)),
            (res.x1_incenter, "X1", "S", "var(--geom-assert)", 3.4, "S", (5, 4)),
            (res.x5_nine_point_center, "X5", "L", "var(--geom-accent)", 3.6, "L", (-12, 3)),
            (ja, "J1", None, "var(--geom-coincide)", 4.0, "S′ (Jₐ)", (7, -5)),
            (jb, "J2", None, "var(--geom-coincide)", 4.0, "S″ (J_b)", (-44, -5)),
            (jc, "J3", None, "var(--geom-coincide)", 4.0, "S‴ (J_c)", (7, 13)),
            (res.x11_feuerbach_point, "X11", None, "var(--geom-assert)", 4.8, "X₁₁", (-8, -9)),
            (fea, "F1", None, "var(--geom-accent)", 4.6, "Feₐ", (7, -4)),
            (feb, "F2", None, "var(--geom-accent)", 4.6, "Fe_b", (-28, -5)),
            (fec, "F3", None, "var(--geom-accent)", 4.6, "Fe_c", (7, 12)),
            (ha, "H1", None, "var(--geom-fg)", 2.4, "", (0, 0)),
        ],
    )


def render_feuerbach_zoom_svg(res: FeuerbachTangencyResult | None = None) -> str:
    """Render magnified close-up of the internal tangency at the Feuerbach point ``X(11)``."""
    if res is None:
        res = construct_feuerbach_tangency()
    pt_a, pt_b, pt_c = res.vertices
    ma, mb, mc = res.medial_points
    ha, hb, hc = res.orthic_points
    fea, feb, fec = res.excircle_tangencies
    exa, exb, exc = res.excircles

    spec = SvgSpec(folio="0038", graphic="g3", xmin=-1.4, xmax=15.4, ymin=-1.8, ymax=13.0)
    canvas = _Canvas(spec)

    return _build_svg(
        canvas,
        "Magnified Detail: Internal Tangency at X(11) = (6, 8) and External Excircle Arcs",
        polygons=[
            ([pt_a, pt_b, pt_c], "< A B C >", "var(--geom-fg)", "var(--geom-fg)", 0.03),
            ([fea, feb, fec], "< F1 F2 F3 >", "var(--geom-assert)", "var(--geom-assert)", 0.06),
        ],
        lines=[
            (spg.Line(res.x5_nine_point_center, res.x1_incenter), "[ X5 X1 ]", "var(--geom-assert)", 1.1, "3,3", 0.60),
            (res.euler_line, "[ X3 X4 ]", "var(--geom-accent)", 1.3, "5,3", 0.65),
        ],
        segments=[
            (pt_a, pt_b, "/ A B /", "var(--geom-fg)", 1.6, None, 0.92),
            (pt_b, pt_c, "/ B C /", "var(--geom-fg)", 1.6, None, 0.92),
            (pt_c, pt_a, "/ C A /", "var(--geom-fg)", 1.6, None, 0.92),
        ],
        circles=[
            (exa, "( J1 F1 )", None, "var(--geom-coincide)", 1.15, "5,3", 0.55),
            (exb, "( J2 F2 )", None, "var(--geom-coincide)", 1.15, "5,3", 0.55),
            (exc, "( J3 F3 )", None, "var(--geom-coincide)", 1.15, "5,3", 0.55),
            (res.incircle, "( X1 X11 )", None, "var(--geom-assert)", 1.9, None, 0.95),
            (res.nine_point_circle, "( X5 H1 )", None, "var(--geom-accent)", 2.2, None, 0.98),
        ],
        points=[
            (pt_a, "A", None, "var(--geom-fg)", 3.8, "A (0,0)", (-14, 15)),
            (pt_b, "B", None, "var(--geom-fg)", 3.8, "B (14,0)", (-8, 15)),
            (pt_c, "C", None, "var(--geom-fg)", 3.8, "C (5,12)", (-16, -9)),
            (ma, "M1", None, "var(--geom-fg)", 3.0, "Mₐ", (7, -3)),
            (mb, "M2", None, "var(--geom-fg)", 3.0, "M_b", (-22, -3)),
            (mc, "M3", None, "var(--geom-fg)", 3.0, "M_c", (-6, 15)),
            (ha, "H1", None, "var(--geom-fg)", 3.0, "Hₐ", (7, 5)),
            (hb, "H2", None, "var(--geom-fg)", 3.0, "H_b", (-22, 4)),
            (hc, "H3", None, "var(--geom-fg)", 3.0, "H_c", (-10, 15)),
            (res.x1_incenter, "X1", "S", "var(--geom-assert)", 4.2, "S = X₁ (6, 4)", (9, 13)),
            (res.x5_nine_point_center, "X5", "L", "var(--geom-accent)", 4.2, "L = X₅ (6, 63/16)", (-108, -6)),
            (res.x11_feuerbach_point, "X11", None, "var(--geom-assert)", 5.2, "X₁₁ (6, 8)", (9, -7)),
            (fea, "F1", None, "var(--geom-coincide)", 4.4, "Feₐ", (8, -5)),
            (feb, "F2", None, "var(--geom-coincide)", 4.4, "Fe_b", (-28, -5)),
            (fec, "F3", None, "var(--geom-coincide)", 4.4, "Fe_c", (8, 13)),
        ],
    )


def render_model_svg(model: Model, spec: SvgSpec, title: str = "GEOMETOR Diagram") -> str:
    """Generic ``.euclid-graphic`` SVG serializer for an arbitrary :class:`~geometor.model.Model`."""
    canvas = _Canvas(spec)
    lines = [
        (el, f"[ {model[el.p1].ID} {model[el.p2].ID} ]", "var(--geom-fg)", 1.1, None, 0.65)
        for el in model.lines
        if not model[el].guide and el.p1 in model and el.p2 in model
    ]
    circles = [
        (
            el,
            f"( {model[el.center].ID} {model[model[el].pt_radius].ID} )",
            None,
            "var(--geom-accent)",
            1.5,
            None,
            0.85,
        )
        for el in model.circles
        if not model[el].guide and el.center in model and model[el].pt_radius in model
    ]
    points = [
        (pt, model[pt].ID, None, "var(--geom-fg)", 3.6, model[pt].ID, (6.0, -6.0))
        for pt in model.points
        if not model[pt].guide and model[pt].ID
    ]
    return _build_svg(
        canvas,
        title,
        polygons=[],
        lines=lines,
        segments=[],
        circles=circles,
        points=points,
    )


def export_all_codex_svgs(output_dir: Path | str) -> dict[str, Path]:
    """Generate and write all four canonical codex SVGs into ``output_dir``.

    Args:
        output_dir: Destination directory (typically ``docsrc/_static/constructions``).

    Returns:
        Mapping from diagram slug to written SVG :class:`pathlib.Path`.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    euler_res = construct_euler_1765_centers()
    fb_res = construct_feuerbach_tangency()

    files = {
        "euler_1765_centers": out_path / "euler_1765_centers.svg",
        "nine_point_circle": out_path / "nine_point_circle.svg",
        "feuerbach_tangency": out_path / "feuerbach_tangency.svg",
        "feuerbach_incircle_zoom": out_path / "feuerbach_incircle_zoom.svg",
    }
    files["euler_1765_centers"].write_text(render_euler_1765_svg(euler_res), encoding="utf-8")
    files["nine_point_circle"].write_text(render_nine_point_svg(fb_res), encoding="utf-8")
    files["feuerbach_tangency"].write_text(render_feuerbach_full_svg(fb_res), encoding="utf-8")
    files["feuerbach_incircle_zoom"].write_text(render_feuerbach_zoom_svg(fb_res), encoding="utf-8")
    return files
