"""Comprehensive test suite for geometor.feuerbach.

Verifies:
1. 100% exact symbolic zero residuals across all 26 Euler (1765) and Feuerbach (1822) identities.
2. Exact cubic reconstruction on Euler's (5, 6, 7) triangle and canonical (15, 13, 14) triangle.
3. Exact sympy.Rational coordinates for X(1)..X(5), X(11), Ja, Jb, Jc, Fea, Feb, Fec with
   strict zero-Float enforcement across every element in Model.
4. Nine-point incidence, harmonic Euler cross-ratio (X4, X2; X5, X3) == -1, and fourfold
   radical-axis circle tangencies.
5. Interactive .euclid-graphic SVG generation and scholarly JSON concordance integrity.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import sympy as sp
from geometor.model import is_harmonic, quadrance

from geometor.feuerbach import (
    construct_euler_1765_centers,
    construct_feuerbach_tangency,
    export_all_codex_svgs,
    load_concordance,
    load_sources_manifest,
    prove_euler_1765_identities,
    solve_euler_reconstruction_cubic,
)


def _assert_zero_floats_in_model(model: object) -> None:
    """Ensure no sympy.Float atoms exist anywhere in constructed Model points or circles."""
    from geometor.model import Model

    assert isinstance(model, Model)
    for pt in model.points:
        assert not pt.x.atoms(sp.Float), f"Float found in point {model[pt].ID}.x: {pt.x}"
        assert not pt.y.atoms(sp.Float), f"Float found in point {model[pt].ID}.y: {pt.y}"
    for circ in model.circles:
        assert not circ.radius.atoms(sp.Float), f"Float found in circle {model[circ].ID} radius"


def test_symbolic_identities_euler_and_feuerbach() -> None:
    """All 26 polynomial identities of Euler (1765) and Feuerbach (1822) cancel to exact 0."""
    report = prove_euler_1765_identities()
    assert report.all_verified
    assert len(report.symbolic_residuals) >= 26
    for name, residual in report.symbolic_residuals.items():
        assert residual == sp.Integer(0), f"Non-zero residual for {name}: {residual}"


def test_euler_cubic_reconstruction_567_and_heronian() -> None:
    """Euler's §§ 21–24 reconstruction recovers z^3 - 18z^2 + 107z - 210 = 0 on (5, 6, 7)."""
    report = prove_euler_1765_identities()
    cub = report.euler_cubic_567
    assert cub.p_sum == sp.Integer(18)
    assert cub.q_pairs == sp.Integer(107)
    assert cub.r_prod == sp.Integer(210)
    assert cub.recovered_roots == (sp.Integer(5), sp.Integer(6), sp.Integer(7))

    # Also reconstruct (15, 13, 14) -> sorted roots (13, 14, 15)
    h = report.heronian_15_13_14
    assert h.area == sp.Integer(84)
    assert h.circumradius == sp.Rational(65, 8)
    assert h.nine_point_radius == sp.Rational(65, 16)
    assert h.inradius == sp.Integer(4)
    assert h.exradii == (sp.Integer(14), sp.Rational(21, 2), sp.Integer(12))
    assert h.orthic_inradius == sp.Rational(99, 52)

    p_h, q_h, r_h, _, roots_h = solve_euler_reconstruction_cubic(
        h.quadrances_euler["EF2"],
        h.quadrances_euler["FG2"],
        h.quadrances_euler["GH2"],
    )
    assert (p_h, q_h, r_h) == (sp.Integer(42), sp.Integer(587), sp.Integer(2730))
    assert roots_h == (sp.Integer(13), sp.Integer(14), sp.Integer(15))

    with pytest.raises(ValueError, match="Incompatible distances"):
        solve_euler_reconstruction_cubic(
            h.quadrances_euler["EF2"],
            h.quadrances_euler["FG2"],
            h.quadrances_euler["GH2"],
            eg_sq=sp.Integer(999),
        )


def test_construct_euler_1765_centers_exact_rational() -> None:
    """Euler's four centers land on exact rational coordinates with zero floats."""
    res = construct_euler_1765_centers()
    _assert_zero_floats_in_model(res.model)

    assert (res.x1_incenter_G.x, res.x1_incenter_G.y) == (sp.Integer(6), sp.Integer(4))
    assert (res.x2_centroid_F.x, res.x2_centroid_F.y) == (sp.Rational(19, 3), sp.Integer(4))
    assert (res.x3_circumcenter_H.x, res.x3_circumcenter_H.y) == (
        sp.Integer(7),
        sp.Rational(33, 8),
    )
    assert (res.x4_orthocenter_E.x, res.x4_orthocenter_E.y) == (
        sp.Integer(5),
        sp.Rational(15, 4),
    )


def test_construct_feuerbach_tangency_exact_coordinates() -> None:
    """Feuerbach's Theorem constructs X(5), X(11), and Fea, Feb, Fec over Q without floats."""
    res = construct_feuerbach_tangency()
    _assert_zero_floats_in_model(res.model)

    # Nine-point center X(5) = (6, 63/16) and radius 65/16
    assert (res.x5_nine_point_center.x, res.x5_nine_point_center.y) == (
        sp.Integer(6),
        sp.Rational(63, 16),
    )
    assert res.nine_point_circle.radius == sp.Rational(65, 16)

    # Internal tangency: Feuerbach point X(11) = (6, 8)
    assert (res.x11_feuerbach_point.x, res.x11_feuerbach_point.y) == (
        sp.Integer(6),
        sp.Integer(8),
    )
    assert quadrance(res.x5_nine_point_center, res.x1_incenter) == sp.Rational(1, 256)

    # Excenters Ja, Jb, Jc
    ja, jb, jc = res.excenters
    assert (ja.x, ja.y) == (sp.Integer(21), sp.Integer(14))
    assert (jb.x, jb.y) == (sp.Integer(-7), sp.Rational(21, 2))
    assert (jc.x, jc.y) == (sp.Integer(8), sp.Integer(-12))

    # Three external excircle tangency points Fea, Feb, Fec
    fea, feb, fec = res.excircle_tangencies
    assert (fea.x, fea.y) == (sp.Rational(2709, 289), sp.Rational(1792, 289))
    assert (feb.x, feb.y) == (sp.Rational(553, 233), sp.Rational(1344, 233))
    assert (fec.x, fec.y) == (sp.Rational(1672, 257), sp.Rational(-24, 257))

    # Harmonic division along the Euler line: (X4, X2; X5, X3) = -1
    assert res.harmonic_cross_ratio == sp.Integer(-1)
    assert is_harmonic(
        res.x4_orthocenter,
        res.x2_centroid,
        res.x5_nine_point_center,
        res.x3_circumcenter,
    )


def test_svg_export_and_scholarly_resources(tmp_path: Path) -> None:
    """Exported SVGs satisfy .euclid-graphic schema and JSON resources validate cleanly."""
    written = export_all_codex_svgs(tmp_path)
    assert set(written.keys()) == {
        "euler_1765_centers",
        "nine_point_circle",
        "feuerbach_tangency",
        "feuerbach_incircle_zoom",
    }
    for svg_path in written.values():
        content = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in content
        assert 'id="highlights"' in content
        assert 'id="geom-tick-1"' in content
        assert "data-ref=" in content

    entries = load_concordance()
    assert len(entries) >= 12
    manifest = load_sources_manifest()
    assert "euler_1765" in manifest["treatises"]
    assert "feuerbach_1822" in manifest["treatises"]
