"""Regression anchor for the separable Goldstone-Wilczek normalization."""

import math
from pathlib import Path

from scripts.goldstone_wilczek.c_gw_loop import c_gw


ROOT = Path(__file__).resolve().parents[2]


def test_goldstone_wilczek_normalization_is_unity() -> None:
    value, _loop, _reference = c_gw(
        0.30,
        a=0.005,
        nmc=32768,
        seed=11,
        Rmax=4.0,
    )
    # The legacy hard gate uses 0.005 at 262144 points; this deterministic
    # reduced sample reproduces unity more closely than 0.001.
    assert math.isclose(value.real, 1.0, abs_tol=0.001)
    assert abs(value.imag) < 1e-10

