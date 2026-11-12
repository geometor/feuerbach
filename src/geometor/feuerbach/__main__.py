"""Command-line entrypoint for verifying Euler–Feuerbach symbolic proofs and exporting SVGs."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from rich.console import Console
from rich.table import Table

from geometor.feuerbach.euler import (
    construct_euler_1765_centers,
    prove_euler_1765_identities,
)
from geometor.feuerbach.render import export_all_codex_svgs
from geometor.feuerbach.tangency import construct_feuerbach_tangency


def main(argv: Sequence[str] | None = None) -> int:
    """Run exact symbolic checks and optionally export ``.euclid-graphic`` SVGs.

    Args:
        argv: Optional CLI argument list.

    Returns:
        Process exit code (``0`` on full symbolic verification).
    """
    parser = argparse.ArgumentParser(
        prog="feuerbach",
        description="Verify Euler (1765, E325) and Feuerbach (1822) symbolic proofs and constructions.",
    )
    parser.add_argument(
        "--export-svg",
        type=Path,
        default=None,
        help="Optional directory to export the four interactive .euclid-graphic SVGs.",
    )
    args = parser.parse_args(argv)

    console = Console()
    report = prove_euler_1765_identities()
    euler_res = construct_euler_1765_centers()
    fb_res = construct_feuerbach_tangency()

    table = Table(title="Euler (1765) & Feuerbach (1822) — Exact Heronian (15, 13, 14) Locus")
    table.add_column("Symbol", style="bold cyan")
    table.add_column("Historical Role", style="white")
    table.add_column("Exact Coordinates / Invariant", style="bold green")

    table.add_row("G = S = X(1)", "Incenter (Euler § 4; Feuerbach § 1)", f"({fb_res.x1_incenter.x}, {fb_res.x1_incenter.y})")
    table.add_row("F = G = X(2)", "Centroid (Euler § 3; Feuerbach § 60)", f"({fb_res.x2_centroid.x}, {fb_res.x2_centroid.y})")
    table.add_row("H = K = X(3)", "Circumcenter (Euler § 5; Feuerbach § 49)", f"({fb_res.x3_circumcenter.x}, {fb_res.x3_circumcenter.y})")
    table.add_row("E = O = X(4)", "Orthocenter (Euler § 2; Feuerbach § 19)", f"({fb_res.x4_orthocenter.x}, {fb_res.x4_orthocenter.y})")
    table.add_row("L = X(5)", "Nine-Point Center (Feuerbach § 54)", f"({fb_res.x5_nine_point_center.x}, {fb_res.x5_nine_point_center.y})")
    table.add_row("X(11)", "Feuerbach Point (Feuerbach § 57)", f"({fb_res.x11_feuerbach_point.x}, {fb_res.x11_feuerbach_point.y})")
    for lbl, pt in zip(("Fea", "Feb", "Fec"), fb_res.excircle_tangencies, strict=True):
        table.add_row(lbl, "Excircle Tangency (Feuerbach § 57)", f"({pt.x}, {pt.y})")
    table.add_row("(X4, X2; X5, X3)", "Harmonic Euler Cross-Ratio", str(fb_res.harmonic_cross_ratio))
    table.add_row(
        "Polynomial Proofs",
        f"{len(report.symbolic_residuals)} symbolic identities + {len(euler_res.model.steps) + len(fb_res.model.steps)} Model steps",
        "ALL VERIFIED = 0" if report.all_verified else "FAILED",
    )
    console.print(table)

    if args.export_svg is not None:
        written = export_all_codex_svgs(args.export_svg)
        for name, svg_path in written.items():
            console.print(f"[green]Exported[/green] {name}: {svg_path}")

    return 0 if report.all_verified else 1


if __name__ == "__main__":
    raise SystemExit(main())
