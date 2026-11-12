"""Executable demonstration of Karl Wilhelm Feuerbach's Theorem (1822, § 57).

Constructs the nine-point circle, the four tritangent circles, the Feuerbach point X(11),
and the three excircle tangency points Fea, Feb, Fec in exact rational coordinates on
A = (0, 0), B = (14, 0), C = (5, 12) using geometor.model.Model(..., auto_intersect=False),
and exports interactive .euclid-graphic SVGs.
"""

from __future__ import annotations

from pathlib import Path

from geometor.model import quadrance
from rich.console import Console
from rich.table import Table

from geometor.feuerbach.render import export_all_codex_svgs
from geometor.feuerbach.tangency import construct_feuerbach_tangency


def run_demo(svg_dir: Path | None = None) -> None:
    """Execute the exact Feuerbach tangency construction and print verified invariants."""
    console = Console()
    res = construct_feuerbach_tangency()

    table = Table(title="Feuerbach (1822, § 57) — Exact Rational Locus on (15, 13, 14)")
    table.add_column("Element", style="bold cyan")
    table.add_column("Exact Coordinates / Radius", style="green")
    table.add_column("Tangency / Incidence Check", style="yellow")

    r9 = res.nine_point_circle.radius
    r_in = res.incircle.radius
    table.add_row(
        "Nine-Point Circle (X5)",
        f"center=({res.x5_nine_point_center.x}, {res.x5_nine_point_center.y}), R₉={r9}",
        "9 canonical points verified",
    )
    table.add_row(
        "Incircle (X1) & X(11)",
        f"X₁=({res.x1_incenter.x}, {res.x1_incenter.y}), r={r_in}, X₁₁=({res.x11_feuerbach_point.x}, {res.x11_feuerbach_point.y})",
        f"Q(X₅,X₁)={quadrance(res.x5_nine_point_center, res.x1_incenter)} == (R₉-r)²={(r9 - r_in) ** 2}",
    )
    for name, ctr, circ, fe_pt in zip(
        ("Excircle A", "Excircle B", "Excircle C"),
        res.excenters,
        res.excircles,
        res.excircle_tangencies,
        strict=True,
    ):
        rk = circ.radius
        table.add_row(
            f"{name} & {res.model[fe_pt].ID}",
            f"J=({ctr.x}, {ctr.y}), r={rk}, Fe=({fe_pt.x}, {fe_pt.y})",
            f"Q(X₅,J)={quadrance(res.x5_nine_point_center, ctr)} == (R₉+r)²={(r9 + rk) ** 2}",
        )
    table.add_row(
        "Harmonic Euler Range",
        f"(X₄, X₂; X₅, X₃) = {res.harmonic_cross_ratio}",
        f"{len(res.model.steps)} deductive Model steps",
    )
    console.print(table)

    if svg_dir is not None:
        written = export_all_codex_svgs(svg_dir)
        for slug, path in written.items():
            console.print(f"[green]Wrote SVG[/green] {slug} -> {path}")


if __name__ == "__main__":
    default_out = Path(__file__).resolve().parents[1] / "docsrc" / "_static" / "constructions"
    run_demo(default_out)
