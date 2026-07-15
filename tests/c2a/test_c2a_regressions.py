"""Regression anchors for the migrated C2a scientific record."""

from __future__ import annotations

import ast
import math
import re
from itertools import permutations
from pathlib import Path

import numpy as np

from scripts.c2a import skyrme_fast, skyrme_full
from scripts.c2a.aggregate import build, load
from scripts.c2a.derive_classes import (
    CLASSES,
    amp_phys_single_p,
    analytic_density,
    trf,
)
from scripts.c2a.production_scan import make_cfg
from scripts.c2a.pv_check import a0_density_pv, kappa_pv


ROOT = Path(__file__).resolve().parents[2]
SCAN_DATA = ROOT / "results" / "c2a" / "raw" / "scan_data.csv"
AGGREGATE_OUTPUT = ROOT / "results" / "c2a" / "raw" / "aggregate_output.txt"


def exact_kappa(m: float, cutoff: float = 1.0) -> float:
    """Exact legacy sharp-four-ball result from commit 4a0de1e."""
    numerator = cutoff**4 * (
        -17 * cutoff**6
        - 85 * cutoff**4 * m**2
        - 170 * cutoff**2 * m**4
        - 90 * m**6
    )
    denominator = 1152 * math.pi**2 * (cutoff**2 + m**2) ** 5
    return numerator / denominator


def test_five_class_pointwise_a0_cancellation() -> None:
    """Source Rider #4a reports machine-precision pointwise cancellation."""
    rng = np.random.default_rng(7)
    points = rng.normal(size=(8, 4))
    points /= np.linalg.norm(points, axis=1, keepdims=True)
    points *= rng.uniform(size=8)[:, None] ** 0.25
    zero = [np.zeros(4)] * 4
    flavors = [1, 2, 1, 2]

    for point in points:
        numeric = sum(
            amp_phys_single_p(CLASSES[name], zero, flavors, 0.30, point)
            for name in CLASSES
        )
        analytic = sum(analytic_density(name, float(point @ point), 0.30) for name in CLASSES)
        assert abs(numeric) < 1e-10
        assert abs(analytic) < 1e-14


def test_flavor_weights_and_symmetry_factor_anchor() -> None:
    flavors = [1, 2, 1, 2]
    representatives = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
    assert [trf([flavors[i] for i in rep]) for rep in representatives] == [-2, 2, 2]

    weights = {
        name: sum(
            trf([flavors[perm[slot]] for slot in range(4)])
            for _composition in compositions
            for perm in permutations(range(4))
        )
        for name, compositions in CLASSES.items()
    }
    assert weights == {
        "BOX": 16,
        "TRIANGLE": 48,
        "BUBBLE": 16,
        "SUNSET": 32,
        "CONTACT": 16,
    }


def test_startup_regression_targets_are_locked() -> None:
    """Lock the costly legacy startup targets, seed, and sample size in CI."""
    source = (ROOT / "scripts" / "c2a" / "startup_regression.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    targets = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "targets" for target in node.targets
        ):
            targets = ast.literal_eval(node.value)
    assert targets == [
        (0.30, 0.10, -0.07973, -0.235),
        (0.30, 0.05, -0.07973, -0.280),
        (0.15, 0.05, -0.14327, -5.561),
    ]
    assert "NMC = 400_000" in source
    assert "default_rng(11)" in source


def test_ward_m4_normalization_anchor() -> None:
    aggregate = build(load(str(SCAN_DATA)))
    for mass, row in aggregate.items():
        assert row["kappa_U"] == mass**4 * row["kappa_raw"]
    plateau = np.array([row["kappa_U"] for row in aggregate.values()])
    assert np.ptp(plateau) < 4e-6


def test_independent_matrix_and_analytic_evaluators_agree() -> None:
    points = skyrme_fast.make_sample(16, seed=7)
    config = make_cfg(0.02, math.pi / 2)
    for class_name in skyrme_fast.CLASSES:
        fast = skyrme_fast.amplitude(class_name, config, 0.30, points)
        full = skyrme_full.amplitude(class_name, config, 0.30, points)
        assert math.isclose(fast, full, rel_tol=1e-12, abs_tol=1e-14)


def test_exact_closed_form_agrees_with_production_evaluation() -> None:
    aggregate = build(load(str(SCAN_DATA)))
    for mass, row in aggregate.items():
        # Source Task A reports 0.26--0.35% deviations from finite-sample production.
        assert math.isclose(exact_kappa(mass), row["kappa_U"], rel_tol=0.004)


def test_negative_sign_survives_pv_regulator_comparison() -> None:
    points, _weights = skyrme_fast.make_sample_importance(
        256, seed=11, m=0.15, a=4, qmc=True
    )
    for pv_mass in (2.0, 4.0, 8.0):
        assert np.max(np.abs(a0_density_pv(0.15, points, pv_mass))) < 1e-9

    value, _error = kappa_pv(0.15, 4.0, seeds=(11,), nmc=2048)
    assert value < 0
    assert math.isclose(value, -17 / (1152 * math.pi**2), abs_tol=3e-5)


def test_aggregation_reproduces_committed_table() -> None:
    aggregate = build(load(str(SCAN_DATA)))
    expected = {}
    row_pattern = re.compile(
        r"^\s+(0\.\d{2})\s+(-?\d+\.\d+)\s+(-?0\.\d+)\s+(0\.\d+)"
    )
    for line in AGGREGATE_OUTPUT.read_text(encoding="utf-8").splitlines():
        match = row_pattern.match(line)
        if match:
            mass, raw, kappa, band = map(float, match.groups())
            expected[mass] = (raw, kappa, band)

    assert set(expected) == set(aggregate)
    for mass, (raw, kappa, band) in expected.items():
        row = aggregate[mass]
        assert round(row["kappa_raw"], 5) == raw
        assert round(row["kappa_U"], 6) == kappa
        assert round(row["band_U"], 6) == band


def test_exact_limiting_value() -> None:
    expected = -17 / (1152 * math.pi**2)
    assert expected < 0
    assert math.isclose(exact_kappa(1e-8), expected, rel_tol=0, abs_tol=1e-15)

