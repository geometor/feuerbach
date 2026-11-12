r"""Symbolic proofs and Euclidean construction for Euler's 1765 memoir (E325) and Feuerbach (1822).

Implements:

1. :func:`prove_euler_1765_identities`: 100% exact rational-function proofs in :mod:`sympy`
   over free side symbols :math:`(a, b, c)` for:

   - Euler's six squared mutual center distances (§ 18, Formulas I–VI, p. 114),
   - Euler's collinearity ratio :math:`EH = \frac{3}{2}EF`, :math:`FH = \frac{1}{2}EF` (§ 16 & § 18),
   - Euler's Stewart relation :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2` (§ 18, p. 114),
   - Feuerbach's tritangent & orthic identities (§§ 5, 28, 49–60, pp. 4–41), including
     the four nine-point tangency quadrances :math:`\overline{LS}^2 = (\frac{1}{2}R - r)^2`
     and :math:`\overline{LS^{(k)}}^2 = (\frac{1}{2}R + r^{(k)})^2` (§ 57, pp. 37–38) and the
     corrected centroid-orthocenter sums :math:`\sum \overline{OS_i}^2 = 16R(R - \rho)` (§ 52)
     and :math:`9\sum \overline{GS_i}^2 = 16R(7R - \rho)` (§ 60),

   evaluated concretely in exact :class:`sympy.Rational` arithmetic on the canonical Heronian
   ``(15, 13, 14)`` triangle.
2. :func:`solve_euler_reconstruction_cubic`: Exact symbolic solver for Euler's inverse
   problem (§§ 19–24, pp. 114–118), recovering :math:`z^3 - pz^2 + qz - r = 0` from the
   mutual quadrances of ``(E, F, G, H)`` and verifying Euler's ``(5, 6, 7)`` test case.
3. :func:`construct_euler_1765_centers`: Pure compass-and-straightedge :class:`~geometor.model.Model`
   proposition constructing ``E = X(4)``, ``F = X(2)``, ``G = X(1)``, ``H = X(3)``, the
   circumcircle, the incircle, and the Euler line ``[H E]``.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    ProofAssertionError,
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
    "EulerCentersResult",
    "EulerCubicExample",
    "EulerIdentitiesReport",
    "HeronianNumericCheck",
    "construct_euler_1765_centers",
    "prove_euler_1765_identities",
    "solve_euler_reconstruction_cubic",
]


@dataclass(frozen=True)
class EulerCubicExample:
    """Exact polynomial data for Euler's §§ 21–24 triangle reconstruction problem."""

    sides_expected: tuple[sp.Rational, sp.Rational, sp.Rational]
    ef_sq: sp.Rational
    eg_sq: sp.Rational
    eh_sq: sp.Rational
    fg_sq: sp.Rational
    fh_sq: sp.Rational
    gh_sq: sp.Rational
    p_sum: sp.Rational
    q_pairs: sp.Rational
    r_prod: sp.Rational
    cubic_poly: sp.Expr
    recovered_roots: tuple[sp.Rational, sp.Rational, sp.Rational]


@dataclass(frozen=True)
class HeronianNumericCheck:
    """Exact rational invariants on the canonical Heronian ``(15, 13, 14)`` triangle."""

    sides: tuple[sp.Integer, sp.Integer, sp.Integer]
    area: sp.Rational
    semiperimeter: sp.Rational
    circumradius: sp.Rational
    nine_point_radius: sp.Rational
    inradius: sp.Rational
    exradii: tuple[sp.Rational, sp.Rational, sp.Rational]
    orthic_inradius: sp.Rational
    euler_p_sum: sp.Rational
    euler_q_pairs: sp.Rational
    euler_r_prod: sp.Rational
    quadrances_euler: dict[str, sp.Rational]
    quadrances_feuerbach: dict[str, sp.Rational]


@dataclass(frozen=True)
class EulerIdentitiesReport:
    """Verified symbolic residuals and concrete evaluations for Euler (1765) & Feuerbach (1822)."""

    symbolic_residuals: dict[str, sp.Expr]
    euler_formulas_pqr: dict[str, sp.Expr]
    feuerbach_formulas: dict[str, sp.Expr]
    euler_cubic_567: EulerCubicExample
    heronian_15_13_14: HeronianNumericCheck

    @property
    def all_verified(self) -> bool:
        """Return ``True`` iff every symbolic polynomial residual simplifies to exact zero."""
        return all(res == sp.Integer(0) for res in self.symbolic_residuals.values())


@dataclass(frozen=True)
class EulerCentersResult:
    """Constructed elements for Euler's 1765 memoir (E325) on ``A=(0,0), B=(14,0), C=(5,12)``."""

    model: Model
    vertices: tuple[spg.Point, spg.Point, spg.Point]
    triangle: spg.Polygon
    x1_incenter_G: spg.Point
    x2_centroid_F: spg.Point
    x3_circumcenter_H: spg.Point
    x4_orthocenter_E: spg.Point
    euler_line: spg.Line
    circumcircle: spg.Circle
    incircle: spg.Circle


def solve_euler_reconstruction_cubic(
    ef_sq: sp.Rational,
    fg_sq: sp.Rational,
    gh_sq: sp.Rational,
    eg_sq: sp.Rational | None = None,
) -> tuple[sp.Rational, sp.Rational, sp.Rational, sp.Expr, tuple[sp.Rational, ...]]:
    r"""Recover :math:`(p, q, r)` and the side-length cubic :math:`z^3 - pz^2 + qz - r = 0`.

    Follows Euler's E325 §§ 19–22 (pp. 114–117):

    - If ``eg_sq`` is omitted, determines :math:`EG^2` from Stewart's collinearity law
      :math:`4GH^2 + 2EG^2 = 3EF^2 + 6FG^2`.
    - Sets :math:`f = EG^2 - GH^2`, :math:`g = FG^2 - EF^2`, :math:`h = \frac{9}{4}EF^2 - 3GH^2`,
      recovers :math:`Q = r/p`, :math:`R = r^2/(4A^2) = 4(GH^2 + Q)`, :math:`P = p^2`,
      :math:`q`, and :math:`r = pQ`.

    Args:
        ef_sq: Exact squared distance :math:`EF^2 = Q(X_4, X_2)`.
        fg_sq: Exact squared distance :math:`FG^2 = Q(X_2, X_1)`.
        gh_sq: Exact squared distance :math:`GH^2 = Q(X_3, X_1)`.
        eg_sq: Optional :math:`EG^2 = Q(X_4, X_1)`; verified against Stewart's law if given.

    Returns:
        Tuple ``(p, q, r, cubic_expr, sorted_rational_roots)``.

    Raises:
        ValueError: If ``eg_sq`` violates Euler's collinearity relation or :math:`P = p^2` is
            not a positive rational square.
    """
    stewart_eg_sq = sp.Rational(3, 2) * ef_sq + 3 * fg_sq - 2 * gh_sq
    if eg_sq is None:
        eg_sq = stewart_eg_sq
    elif sp.simplify(eg_sq - stewart_eg_sq) != 0:
        raise ValueError(
            f"Incompatible distances: 4*GH^2 + 2*EG^2 != 3*EF^2 + 6*FG^2 "
            f"(expected EG^2={stewart_eg_sq}, got {eg_sq})."
        )

    # Euler §§ 19–21:
    #   Q = r / p,   P = p^2,   4*A^2 = P * (q - P/4 - 2*Q),
    #   R_eul = r^2 / (4*A^2) = Q^2 / (q - P/4 - 2*Q) = 4*(GH^2 + Q).
    # Notice that in Q^2 = 4*(GH^2 + Q)*(q - P/4 - 2*Q), substituting the linear
    # expressions for P(Q) and q(Q) cancels Q^2 identically, yielding a unique rational Q!
    p_sq_sym, q_sym, big_q_sym = sp.symbols("P q Q")
    eq_r = sp.Eq(
        big_q_sym**2,
        4 * (gh_sq + big_q_sym) * (q_sym - sp.Rational(1, 4) * p_sq_sym - 2 * big_q_sym),
    )
    eq2 = sp.Eq(-p_sq_sym + 3 * q_sym, eg_sq - 4 * gh_sq)
    eq3 = sp.Eq(-sp.Rational(1, 9) * p_sq_sym + sp.Rational(5, 9) * q_sym - 2 * big_q_sym, fg_sq)
    sol = sp.solve([eq_r, eq2, eq3], [p_sq_sym, q_sym, big_q_sym], dict=True)
    if not sol:
        raise ValueError("Invariant system for (P, q, Q) has no solution.")

    p_sq_val = sp.Rational(sol[0][p_sq_sym])
    q_val = sp.Rational(sol[0][q_sym])
    big_q_val = sp.Rational(sol[0][big_q_sym])
    p_root = sp.sqrt(p_sq_val)
    if not isinstance(p_root, sp.Rational) or p_root <= 0:
        raise ValueError(f"Recovered P = p^2 = {p_sq_val} does not have a positive rational root.")

    p_val = sp.Rational(p_root)
    r_val = sp.Rational(p_val * big_q_val)
    z = sp.Symbol("z")
    cubic_poly = sp.expand(z**3 - p_val * z**2 + q_val * z - r_val)
    roots = tuple(sorted(sp.Rational(rt) for rt in sp.roots(cubic_poly, z) if rt.is_rational))
    return p_val, q_val, r_val, cubic_poly, roots


def prove_euler_1765_identities() -> EulerIdentitiesReport:
    """Prove all distance and proportion identities of Euler (1765) and Feuerbach (1822).

    Uses pure rational-function cancellation (:func:`sympy.cancel`) over free side lengths
    :math:`(a, b, c)` without floating-point arithmetic or square-root branch ambiguity.

    Returns:
        A complete :class:`EulerIdentitiesReport` with symbolic zero residuals and concrete
        rational evaluations on ``(5, 6, 7)`` and ``(15, 13, 14)``.
    """
    a, b, c = sp.symbols("a b c", positive=True)

    # Heron's polynomial 16*Delta^2 and Euler's elementary symmetric polynomials (p, q, r_eul)
    sixteen_area_sq = (
        2 * a**2 * b**2 + 2 * a**2 * c**2 + 2 * b**2 * c**2 - a**4 - b**4 - c**4
    )
    area_sq = sp.Rational(1, 16) * sixteen_area_sq
    p_eul = a + b + c
    q_eul = a * b + a * c + b * c
    r_eul = a * b * c

    # Verify Euler § 10: 16*A^2 = -p^4 + 4*p^2*q - 8*p*r
    res_heron_sym = sp.expand(sixteen_area_sq - (-p_eul**4 + 4 * p_eul**2 * q_eul - 8 * p_eul * r_eul))

    # Auxiliary area placeholder A_sym whose odd powers vanish in all squared distances;
    # we replace A_sym**2 -> area_sq before rational-function cancellation.
    area_sym = sp.Symbol("A_area", positive=True)

    # Euler §§ 6–9 coordinates relative to A = (0, 0), B = (c, 0), C = ((b^2+c^2-a^2)/(2c), 2A/c)
    x_e = (c**2 + b**2 - a**2) / (2 * c)
    y_e = (c**2 + b**2 - a**2) * (a**2 + c**2 - b**2) / (8 * c * area_sym)

    x_f = (3 * c**2 + b**2 - a**2) / (6 * c)
    y_f = 2 * area_sym / (3 * c)

    x_g = (c + b - a) / 2
    y_g = 2 * area_sym / p_eul

    x_h = c / 2
    y_h = c * (a**2 + b**2 - c**2) / (8 * area_sym)

    # Nine-point center L = X(5) = midpoint(E, H) (Feuerbach § 54)
    x_l = (x_e + x_h) / 2
    y_l = (y_e + y_h) / 2

    # Three excenters S', S'', S''' (Ja, Jb, Jc) in the same Cartesian frame
    x_ja = (a + b + c) / 2
    y_ja = 2 * area_sym / (-a + b + c)

    x_jb = (c - b - a) / 2
    y_jb = 2 * area_sym / (a - b + c)

    x_jc = (a - b + c) / 2
    y_jc = -2 * area_sym / (a + b - c)

    def _dist_sq(x1: sp.Expr, y1: sp.Expr, x2: sp.Expr, y2: sp.Expr) -> sp.Expr:
        raw = sp.expand((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return sp.cancel(raw.subs(area_sym**2, area_sq))

    ef_sq_coord = _dist_sq(x_e, y_e, x_f, y_f)
    eg_sq_coord = _dist_sq(x_e, y_e, x_g, y_g)
    eh_sq_coord = _dist_sq(x_e, y_e, x_h, y_h)
    fg_sq_coord = _dist_sq(x_f, y_f, x_g, y_g)
    fh_sq_coord = _dist_sq(x_f, y_f, x_h, y_h)
    gh_sq_coord = _dist_sq(x_g, y_g, x_h, y_h)

    # Euler § 18 (p. 114), Formulas I–VI
    euler_i = sp.cancel(r_eul**2 / (4 * area_sq) - sp.Rational(4, 9) * (p_eul**2 - 2 * q_eul))
    euler_ii = sp.cancel(
        r_eul**2 / (4 * area_sq) - p_eul**2 + 3 * q_eul - 4 * r_eul / p_eul
    )
    euler_iii = sp.cancel(sp.Rational(9, 16) * r_eul**2 / area_sq - p_eul**2 + 2 * q_eul)
    euler_iv = sp.cancel(
        -sp.Rational(1, 9) * p_eul**2 + sp.Rational(5, 9) * q_eul - 2 * r_eul / p_eul
    )
    euler_v = sp.cancel(
        r_eul**2 / (16 * area_sq) - sp.Rational(1, 9) * (p_eul**2 - 2 * q_eul)
    )
    euler_vi = sp.cancel(r_eul**2 / (16 * area_sq) - r_eul / p_eul)

    # Vectorial Euler-line identity (§ 16): x_F - x_H = (x_E - x_F)/2 and y_F - y_H = (y_E - y_F)/2
    res_euler_line_x = sp.cancel((x_e + 2 * x_h) / 3 - x_f)
    res_euler_line_y = sp.cancel(((y_e + 2 * y_h) / 3 - y_f) * area_sym).subs(
        area_sym**2, area_sq
    )
    res_euler_line_y = sp.cancel(res_euler_line_y)

    # Feuerbach (1822) invariants: circumradius R, inradius r_inc, exradii ra, rb, rc, orthic rho
    r_circ_sq = sp.cancel(r_eul**2 / sixteen_area_sq)
    r_inc_sq = sp.cancel(4 * area_sq / p_eul**2)
    ra_sq = sp.cancel(4 * area_sq / (-a + b + c) ** 2)
    rb_sq = sp.cancel(4 * area_sq / (a - b + c) ** 2)
    rc_sq = sp.cancel(4 * area_sq / (a + b - c) ** 2)

    # Rational products R*r_inc, R*ra, R*rb, R*rc, and R*rho (all rational in a, b, c!)
    r_circ_times_r_inc = sp.cancel(r_eul / (2 * p_eul))
    r_circ_times_ra = sp.cancel(r_eul / (2 * (-a + b + c)))
    r_circ_times_rb = sp.cancel(r_eul / (2 * (a - b + c)))
    r_circ_times_rc = sp.cancel(r_eul / (2 * (a + b - c)))
    r_circ_times_rho = sp.cancel(
        (b**2 + c**2 - a**2)
        * (a**2 + c**2 - b**2)
        * (a**2 + b**2 - c**2)
        / (4 * sixteen_area_sq)
    )

    # Feuerbach § 5: r' + r'' + r''' - r = 4*R  (compare both sides multiplied by 1/(2*Delta))
    res_fb_sec5_exradii_sum = sp.cancel(
        (
            2 / (-a + b + c)
            + 2 / (a - b + c)
            + 2 / (a + b - c)
            - 2 / (a + b + c)
        )
        * area_sq
        - 4 * (r_eul / 4)
    )

    # Feuerbach § 28: r^2 + r'^2 + r''^2 + r'''^2 = 8*R^2 - 4*R*rho
    res_fb_sec28_radii_sq = sp.cancel(
        (r_inc_sq + ra_sq + rb_sq + rc_sq) - (8 * r_circ_sq - 4 * r_circ_times_rho)
    )

    # Feuerbach §§ 49–53: KS_k^2, OS_k^2, KO^2
    ks_ja_sq = _dist_sq(x_h, y_h, x_ja, y_ja)
    ks_jb_sq = _dist_sq(x_h, y_h, x_jb, y_jb)
    ks_jc_sq = _dist_sq(x_h, y_h, x_jc, y_jc)

    os_g_sq = eg_sq_coord
    os_ja_sq = _dist_sq(x_e, y_e, x_ja, y_ja)
    os_jb_sq = _dist_sq(x_e, y_e, x_jb, y_jb)
    os_jc_sq = _dist_sq(x_e, y_e, x_jc, y_jc)

    # Feuerbach § 57: LS^2 = (R/2 - r)^2 and LS^(k)^2 = (R/2 + r^(k))^2
    ls_inc_sq = _dist_sq(x_l, y_l, x_g, y_g)
    ls_ja_sq = _dist_sq(x_l, y_l, x_ja, y_ja)
    ls_jb_sq = _dist_sq(x_l, y_l, x_jb, y_jb)
    ls_jc_sq = _dist_sq(x_l, y_l, x_jc, y_jc)

    fb_ls_inc_target = sp.cancel(sp.Rational(1, 4) * r_circ_sq - r_circ_times_r_inc + r_inc_sq)
    fb_ls_ja_target = sp.cancel(sp.Rational(1, 4) * r_circ_sq + r_circ_times_ra + ra_sq)
    fb_ls_jb_target = sp.cancel(sp.Rational(1, 4) * r_circ_sq + r_circ_times_rb + rb_sq)
    fb_ls_jc_target = sp.cancel(sp.Rational(1, 4) * r_circ_sq + r_circ_times_rc + rc_sq)

    # Feuerbach § 60: 9*(GS^2 + GS'^2 + GS''^2 + GS'''^2) = 7*(OS^2 + OS'^2 + OS''^2 + OS'''^2)
    gs_ja_sq = _dist_sq(x_f, y_f, x_ja, y_ja)
    gs_jb_sq = _dist_sq(x_f, y_f, x_jb, y_jb)
    gs_jc_sq = _dist_sq(x_f, y_f, x_jc, y_jc)

    symbolic_residuals: dict[str, sp.Expr] = {
        "euler_sec10_heron_pqr": res_heron_sym,
        "euler_sec16_collinear_x": res_euler_line_x,
        "euler_sec16_collinear_y": res_euler_line_y,
        "euler_sec18_I_EF2": sp.cancel(ef_sq_coord - euler_i),
        "euler_sec18_II_EG2": sp.cancel(eg_sq_coord - euler_ii),
        "euler_sec18_III_EH2": sp.cancel(eh_sq_coord - euler_iii),
        "euler_sec18_IV_FG2": sp.cancel(fg_sq_coord - euler_iv),
        "euler_sec18_V_FH2": sp.cancel(fh_sq_coord - euler_v),
        "euler_sec18_VI_GH2": sp.cancel(gh_sq_coord - euler_vi),
        "euler_sec18_ratio_EH2_9_4_EF2": sp.cancel(eh_sq_coord - sp.Rational(9, 4) * ef_sq_coord),
        "euler_sec18_ratio_FH2_1_4_EF2": sp.cancel(fh_sq_coord - sp.Rational(1, 4) * ef_sq_coord),
        "euler_sec18_stewart_4GH2_2EG2": sp.cancel(
            4 * gh_sq_coord + 2 * eg_sq_coord - (3 * ef_sq_coord + 6 * fg_sq_coord)
        ),
        "feuerbach_sec05_exradii_4R": res_fb_sec5_exradii_sum,
        "feuerbach_sec28_sum_radii_sq": res_fb_sec28_radii_sq,
        "feuerbach_sec49_KS_inc": sp.cancel(
            gh_sq_coord - (r_circ_sq - 2 * r_circ_times_r_inc)
        ),
        "feuerbach_sec49_KS_exa": sp.cancel(ks_ja_sq - (r_circ_sq + 2 * r_circ_times_ra)),
        "feuerbach_sec49_KS_exb": sp.cancel(ks_jb_sq - (r_circ_sq + 2 * r_circ_times_rb)),
        "feuerbach_sec49_KS_exc": sp.cancel(ks_jc_sq - (r_circ_sq + 2 * r_circ_times_rc)),
        "feuerbach_sec50_sum_KS2_12R2": sp.cancel(
            (gh_sq_coord + ks_ja_sq + ks_jb_sq + ks_jc_sq) - 12 * r_circ_sq
        ),
        "feuerbach_sec51_OS_inc": sp.cancel(os_g_sq - (2 * r_inc_sq - 2 * r_circ_times_rho)),
        "feuerbach_sec51_OS_exa": sp.cancel(os_ja_sq - (2 * ra_sq - 2 * r_circ_times_rho)),
        "feuerbach_sec51_OS_exb": sp.cancel(os_jb_sq - (2 * rb_sq - 2 * r_circ_times_rho)),
        "feuerbach_sec51_OS_exc": sp.cancel(os_jc_sq - (2 * rc_sq - 2 * r_circ_times_rho)),
        "feuerbach_sec52_sum_OS2_16R_R_minus_rho": sp.cancel(
            (os_g_sq + os_ja_sq + os_jb_sq + os_jc_sq)
            - (16 * r_circ_sq - 16 * r_circ_times_rho)
        ),
        "feuerbach_sec53_KO2": sp.cancel(eh_sq_coord - (r_circ_sq - 4 * r_circ_times_rho)),
        "feuerbach_sec57_LS_inc_tangency": sp.cancel(ls_inc_sq - fb_ls_inc_target),
        "feuerbach_sec57_LS_exa_tangency": sp.cancel(ls_ja_sq - fb_ls_ja_target),
        "feuerbach_sec57_LS_exb_tangency": sp.cancel(ls_jb_sq - fb_ls_jb_target),
        "feuerbach_sec57_LS_exc_tangency": sp.cancel(ls_jc_sq - fb_ls_jc_target),
        "feuerbach_sec59_sum_LS2_13R2_4Rrho": sp.cancel(
            (ls_inc_sq + ls_ja_sq + ls_jb_sq + ls_jc_sq)
            - (13 * r_circ_sq - 4 * r_circ_times_rho)
        ),
        "feuerbach_sec60_9sumGS2_16R_7R_minus_rho": sp.cancel(
            9 * (fg_sq_coord + gs_ja_sq + gs_jb_sq + gs_jc_sq)
            - (112 * r_circ_sq - 16 * r_circ_times_rho)
        ),
    }

    # Verify Euler's §§ 23–24 worked example (a, b, c) = (5, 6, 7)
    subs_567 = {a: sp.Integer(5), b: sp.Integer(6), c: sp.Integer(7)}
    ef_567 = sp.Rational(euler_i.subs(subs_567))
    eg_567 = sp.Rational(euler_ii.subs(subs_567))
    eh_567 = sp.Rational(euler_iii.subs(subs_567))
    fg_567 = sp.Rational(euler_iv.subs(subs_567))
    fh_567 = sp.Rational(euler_v.subs(subs_567))
    gh_567 = sp.Rational(euler_vi.subs(subs_567))
    p_567, q_567, r_567, poly_567, roots_567 = solve_euler_reconstruction_cubic(
        ef_567, fg_567, gh_567, eg_567
    )
    cubic_example = EulerCubicExample(
        sides_expected=(sp.Integer(5), sp.Integer(6), sp.Integer(7)),
        ef_sq=ef_567,
        eg_sq=eg_567,
        eh_sq=eh_567,
        fg_sq=fg_567,
        fh_sq=fh_567,
        gh_sq=gh_567,
        p_sum=p_567,
        q_pairs=q_567,
        r_prod=r_567,
        cubic_poly=poly_567,
        recovered_roots=(roots_567[0], roots_567[1], roots_567[2]),
    )

    # Evaluate on canonical Heronian (a, b, c) = (15, 13, 14)
    subs_heron = {a: sp.Integer(15), b: sp.Integer(13), c: sp.Integer(14)}
    area_h = sp.Rational(sp.sqrt(area_sq.subs(subs_heron)))
    r_circ_h = sp.Rational(sp.sqrt(r_circ_sq.subs(subs_heron)))
    r_inc_h = sp.Rational(sp.sqrt(r_inc_sq.subs(subs_heron)))
    ra_h = sp.Rational(sp.sqrt(ra_sq.subs(subs_heron)))
    rb_h = sp.Rational(sp.sqrt(rb_sq.subs(subs_heron)))
    rc_h = sp.Rational(sp.sqrt(rc_sq.subs(subs_heron)))
    rho_h = sp.Rational((r_circ_times_rho / r_circ_h).subs(subs_heron))

    heronian_check = HeronianNumericCheck(
        sides=(sp.Integer(15), sp.Integer(13), sp.Integer(14)),
        area=area_h,
        semiperimeter=sp.Rational(p_eul.subs(subs_heron), 2),
        circumradius=r_circ_h,
        nine_point_radius=r_circ_h / 2,
        inradius=r_inc_h,
        exradii=(ra_h, rb_h, rc_h),
        orthic_inradius=rho_h,
        euler_p_sum=sp.Rational(p_eul.subs(subs_heron)),
        euler_q_pairs=sp.Rational(q_eul.subs(subs_heron)),
        euler_r_prod=sp.Rational(r_eul.subs(subs_heron)),
        quadrances_euler={
            "EF2": sp.Rational(euler_i.subs(subs_heron)),
            "EG2": sp.Rational(euler_ii.subs(subs_heron)),
            "EH2": sp.Rational(euler_iii.subs(subs_heron)),
            "FG2": sp.Rational(euler_iv.subs(subs_heron)),
            "FH2": sp.Rational(euler_v.subs(subs_heron)),
            "GH2": sp.Rational(euler_vi.subs(subs_heron)),
        },
        quadrances_feuerbach={
            "LS2": sp.Rational(ls_inc_sq.subs(subs_heron)),
            "LSa2": sp.Rational(ls_ja_sq.subs(subs_heron)),
            "LSb2": sp.Rational(ls_jb_sq.subs(subs_heron)),
            "LSc2": sp.Rational(ls_jc_sq.subs(subs_heron)),
        },
    )

    return EulerIdentitiesReport(
        symbolic_residuals=symbolic_residuals,
        euler_formulas_pqr={
            "I_EF2": euler_i,
            "II_EG2": euler_ii,
            "III_EH2": euler_iii,
            "IV_FG2": euler_iv,
            "V_FH2": euler_v,
            "VI_GH2": euler_vi,
        },
        feuerbach_formulas={
            "LS2": fb_ls_inc_target,
            "LSa2": fb_ls_ja_target,
            "LSb2": fb_ls_jb_target,
            "LSc2": fb_ls_jc_target,
        },
        euler_cubic_567=cubic_example,
        heronian_15_13_14=heronian_check,
    )


@proposition(
    "Euler.E325",
    kind="theorem",
    title="Euler's Four Classical Centers, Collinearity Ratio, and Stewart Relation (1765)",
    hide_guides=True,
)
def construct_euler_1765_centers(model: Model | None = None) -> EulerCentersResult:
    r"""Construct Euler's four centers ``(E, F, G, H)`` and prove his 1765 collinearity theorems.

    Uses the canonical acute scalene Heronian triangle ``A = (0, 0)``, ``B = (14, 0)``,
    ``C = (5, 12)`` with integer sides ``a = 15``, ``b = 13``, ``c = 14`` so every classical
    center lands on exact rational coordinates over :math:`\mathbb{Q}`.

    Args:
        model: Optional existing :class:`~geometor.model.Model`. When ``None``, creates a new
            model with ``auto_intersect=False``.

    Returns:
        :class:`EulerCentersResult` containing the model and constructed geometric entities.

    Raises:
        ProofAssertionError: If any deductive concurrency, collinearity, or metric assertion fails.
    """
    if model is None:
        model = Model("euler_1765_e325", auto_intersect=False, enable_logging=False)

    # Act I: Given Heronian triangle ABC (a=15, b=13, c=14)
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(14), sp.Integer(0), ID="B")
    pt_c = model.given_point(sp.Integer(5), sp.Integer(12), ID="C")

    line_bc = model.construct_line(pt_b, pt_c, ID="a", classes=["side"], intersect=False, by="Post.1")
    line_ca = model.construct_line(pt_c, pt_a, ID="b", classes=["side"], intersect=False, by="Post.1")
    line_ab = model.construct_line(pt_a, pt_b, ID="c", classes=["side"], intersect=False, by="Post.1")
    triangle = model.set_polygon([pt_a, pt_b, pt_c], classes=["given", "triangle"], ID="ABC")

    # Act II: Construct the four classical centers by Euclidean compass-and-straightedge
    # 1. Orthocenter E = X(4) (Euler § 2, Tab. II Fig. 1)
    alt_a = construct_altitude_line(model, pt_a, pt_b, pt_c, ID="alt_A", classes=["altitude"])
    alt_b = construct_altitude_line(model, pt_b, pt_c, pt_a, ID="alt_B", classes=["altitude"])
    alt_c = construct_altitude_line(model, pt_c, pt_a, pt_b, ID="alt_C", classes=["altitude"])
    x4_e = model.intersect(
        alt_a, alt_b, ID="X4", classes=["center", "orthocenter", "result"], by="E325.2"
    )

    # 2. Centroid F = X(2) (Euler § 3, Tab. II Fig. 2)
    ma = construct_midpoint(model, pt_b, pt_c, ID="Ma", classes=["midpoint"])
    mb = construct_midpoint(model, pt_c, pt_a, ID="Mb", classes=["midpoint"])
    mc = construct_midpoint(model, pt_a, pt_b, ID="Mc", classes=["midpoint"])
    med_a = model.construct_line(pt_a, ma, ID="med_A", classes=["median"], intersect=False, by="Post.1")
    med_b = model.construct_line(pt_b, mb, ID="med_B", classes=["median"], intersect=False, by="Post.1")
    med_c = model.construct_line(pt_c, mc, ID="med_C", classes=["median"], intersect=False, by="Post.1")
    x2_f = model.intersect(
        med_a, med_b, ID="X2", classes=["center", "centroid", "result"], by="E325.3"
    )

    # 3. Incenter G = X(1) and incircle (Euler § 4, Tab. II Fig. 3; Euclid IV.4)
    bis_a, _ = construct_angle_bisectors(
        model, pt_a, pt_c, pt_b, internal_id="bis_A", classes=["bisector"]
    )
    bis_b, _ = construct_angle_bisectors(
        model, pt_b, pt_c, pt_a, internal_id="bis_B", classes=["bisector"]
    )
    bis_c, _ = construct_angle_bisectors(
        model, pt_c, pt_a, pt_b, internal_id="bis_C", classes=["bisector"]
    )
    x1_g = model.intersect(
        bis_a, bis_b, ID="X1", classes=["center", "incenter", "result"], by="IV.4"
    )
    inc_foot = construct_altitude_foot(model, x1_g, pt_a, pt_b, ID="Tc", classes=["contact"])
    incircle = model.construct_circle(
        x1_g, inc_foot, ID="incircle", classes=["incircle", "result"], intersect=False, by="IV.4"
    )

    # 4. Circumcenter H = X(3) and circumcircle (Euler § 5, Tab. II Fig. 4; Euclid IV.5)
    pbis_ab = construct_perp_bisector(model, pt_a, pt_b, ID="pbis_c", classes=["perp_bisector"])
    pbis_bc = construct_perp_bisector(model, pt_b, pt_c, ID="pbis_a", classes=["perp_bisector"])
    pbis_ca = construct_perp_bisector(model, pt_c, pt_a, ID="pbis_b", classes=["perp_bisector"])
    x3_h = model.intersect(
        pbis_ab, pbis_bc, ID="X3", classes=["center", "circumcenter", "result"], by="IV.5"
    )
    circumcircle = model.construct_circle(
        x3_h, pt_a, ID="circumcircle", classes=["circumcircle", "result"], intersect=False, by="IV.5"
    )

    # 5. The Euler line [H E] (Euler §§ 16–18, Tab. II Fig. 5)
    euler_line = model.construct_line(
        x3_h, x4_e, ID="euler_line", classes=["euler_line", "result"], intersect=False, by="E325.16"
    )

    # Act III: Deductive Verification
    model.assert_incident(x4_e, alt_c, by="E325.2", label="Three altitudes concur at E = X(4)")
    model.assert_incident(x2_f, med_c, by="E325.3", label="Three medians concur at F = X(2)")
    model.assert_incident(x1_g, bis_c, by="IV.4", label="Three angle bisectors concur at G = X(1)")
    model.assert_incident(x3_h, pbis_ca, by="IV.5", label="Three perpendicular bisectors concur at H = X(3)")
    model.assert_incident(pt_b, circumcircle, by="IV.5")
    model.assert_incident(pt_c, circumcircle, by="IV.5")

    model.assert_collinear(
        x4_e, x2_f, x3_h, by="E325.16", label="Orthocenter E, centroid F, circumcenter H are collinear"
    )
    model.assert_incident(x2_f, euler_line, by="E325.16")

    # Verify Euler's exact metric invariants on the constructed points
    q_ef = quadrance(x4_e, x2_f)
    q_eg = quadrance(x4_e, x1_g)
    q_eh = quadrance(x4_e, x3_h)
    q_fg = quadrance(x2_f, x1_g)
    q_fh = quadrance(x2_f, x3_h)
    q_gh = quadrance(x1_g, x3_h)
    q_r_circ = quadrance(x3_h, pt_a)
    q_r_inc = quadrance(x1_g, inc_foot)

    if not zero_test(q_ef - 4 * q_fh):
        raise ProofAssertionError(f"Euler ratio EF^2 = 4*FH^2 failed: {q_ef} != {4 * q_fh}")
    if not zero_test(4 * q_eh - 9 * q_ef):
        raise ProofAssertionError(f"Euler ratio 4*EH^2 = 9*EF^2 failed: {4 * q_eh} != {9 * q_ef}")
    if not zero_test(4 * q_gh + 2 * q_eg - (3 * q_ef + 6 * q_fg)):
        raise ProofAssertionError("Euler-Stewart relation 4*GH^2 + 2*EG^2 = 3*EF^2 + 6*FG^2 failed.")

    # Euler's Theorem (§ 18 VI): GH^2 = R^2 - 2*R*r  <=>  (R^2 - GH^2)^2 == 4 * R^2 * r^2
    if not zero_test((q_r_circ - q_gh) ** 2 - 4 * q_r_circ * q_r_inc):
        raise ProofAssertionError("Euler's Theorem GH^2 = R^2 - 2*R*r failed.")

    model.conclude(
        triangle,
        x1_g,
        x2_f,
        x3_h,
        x4_e,
        euler_line,
        circumcircle,
        incircle,
        line_bc,
        line_ca,
        line_ab,
        kind="qed",
        by="Euler.E325",
        label="Euler's four centers and collinearity theorem demonstrated",
    )

    return EulerCentersResult(
        model=model,
        vertices=(pt_a, pt_b, pt_c),
        triangle=triangle,
        x1_incenter_G=x1_g,
        x2_centroid_F=x2_f,
        x3_circumcenter_H=x3_h,
        x4_orthocenter_E=x4_e,
        euler_line=euler_line,
        circumcircle=circumcircle,
        incircle=incircle,
    )
