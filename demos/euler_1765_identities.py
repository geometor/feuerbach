"""Executable demonstration of Leonhard Euler's 1765 memoir (E325, §§ 1–34).

Verifies:
1. All six squared mutual center distances (§ 18, I–VI) as exact rational functions of (a, b, c).
2. Collinearity of E = X(4), F = X(2), H = X(3) with EH = (3/2)*EF and FH = (1/2)*EF.
3. Stewart's collinearity law 4*GH^2 + 2*EG^2 = 3*EF^2 + 6*FG^2.
4. Euler's inverse cubic reconstruction z^3 - p*z^2 + q*z - r = 0 on (5, 6, 7).
5. Compass-and-straightedge Model construction on Heronian (15, 13, 14).
"""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.feuerbach.euler import (
    construct_euler_1765_centers,
    prove_euler_1765_identities,
)


def run_demo() -> None:
    """Execute and print the Euler 1765 symbolic proof and construction report."""
    console = Console()
    report = prove_euler_1765_identities()
    constructed = construct_euler_1765_centers()

    id_table = Table(title="Euler (1765/1767, E325) — Symbolic Polynomial Identities")
    id_table.add_column("Identity Key", style="cyan")
    id_table.add_column("Residual", style="bold green")
    for key, res in report.symbolic_residuals.items():
        if key.startswith("euler_"):
            id_table.add_row(key, str(res))
    console.print(id_table)

    cub = report.euler_cubic_567
    console.print(
        f"\n[bold]Euler §§ 21–24 Reconstruction on {cub.sides_expected}:[/bold] "
        f"EF²={cub.ef_sq}, FG²={cub.fg_sq}, GH²={cub.gh_sq}, EG²={cub.eg_sq}\n"
        f"Recovered (p, q, r) = ({cub.p_sum}, {cub.q_pairs}, {cub.r_prod}) -> "
        f"{cub.cubic_poly} = 0 -> roots {cub.recovered_roots}"
    )

    h = report.heronian_15_13_14
    console.print(
        f"\n[bold]Canonical Heronian {h.sides}:[/bold] Δ={h.area}, R={h.circumradius}, r={h.inradius}\n"
        f"E = X(4) = ({constructed.x4_orthocenter_E.x}, {constructed.x4_orthocenter_E.y}), "
        f"F = X(2) = ({constructed.x2_centroid_F.x}, {constructed.x2_centroid_F.y}), "
        f"G = X(1) = ({constructed.x1_incenter_G.x}, {constructed.x1_incenter_G.y}), "
        f"H = X(3) = ({constructed.x3_circumcenter_H.x}, {constructed.x3_circumcenter_H.y})"
    )


if __name__ == "__main__":
    run_demo()
