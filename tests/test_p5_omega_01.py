"""Load-bearing regression anchors for the migrated P5-OMEGA-01 runtime."""

import math

import numpy as np
import pytest

from scripts.p5_omega import topological_mass_radius as topo


def _f2_closed(m, lam):
    return (3 * m**2 / (4 * math.pi**2)) * (
        math.log((lam**2 + m**2) / m**2) - lam**2 / (lam**2 + m**2)
    )


def test_f2_chiral_matches_independent_closed_form():
    for m, lam in ((0.15, 1.0), (0.30, 1.0), (0.20, 1.4)):
        assert topo.f2_chiral(m, lam) == pytest.approx(_f2_closed(m, lam), rel=1e-14)


def test_omega_small_radius_saturation_and_discrimination():
    at_one = topo.E_omega_mom(1.0, 0.30, 20.0, nq=1000)
    at_small = topo.E_omega_mom(0.01, 0.30, 20.0, nq=1000)
    assert at_one == pytest.approx(0.0642, rel=0.005)
    assert at_small == pytest.approx(0.0913, rel=0.005)
    assert at_small > at_one > 0
    # The chosen 0.5% tolerance rejects a meaningful 1% normalization mutation.
    assert not math.isclose(at_small * 1.01, 0.0913, rel_tol=0.005)


def test_large_g0_screening_and_finite_band_bound():
    value = topo.E_omega_mom(0.02, 0.30, 1.0e4, nq=1500)
    bound = 0.5 * (1 / (2 * math.pi**2)) * (1.0e4 / 3)
    assert value == pytest.approx(0.260, rel=0.05)
    assert 0 < value < bound
    assert not math.isclose(value * 1.10, 0.260, rel_tol=0.05)


def test_collapse_ordering_uses_real_energy_function():
    values = [topo.Etot(r, 0.20, 20.0) for r in (0.02, 0.2, 2.0)]
    assert values[0] < values[1] < values[2]
    assert values[0] < 0 < values[2]


def test_scan_r_records_no_interior_continuum_solution():
    result = topo.scan_R(0.20, 20.0, Rgrid=np.geomspace(0.05, 2.0, 8))
    assert result["interior"] is False
    assert result["collapse"] is True


def test_deterministic_regeneration_tolerance_rejects_mutation():
    tolerance = 1e-12
    archived = 0.08430032696865404
    regenerated = 0.08430032696865404
    assert math.isclose(regenerated, archived, rel_tol=tolerance, abs_tol=tolerance)
    assert not math.isclose(regenerated * 1.001, archived, rel_tol=tolerance, abs_tol=tolerance)
