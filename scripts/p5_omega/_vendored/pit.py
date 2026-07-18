"""Minimal accepted Paper 3 polarization runtime dependency.

Scientific ownership remains with zetacheng/3-vector-sector. This file is
limited to the function required by the Paper 5 mass/radius executable.
"""

import numpy as np


def PiT_single(q2E, m, Lam, nx=4000):
    """Paper 3 accepted transverse-polarization quadrature, copied verbatim."""
    x = (np.arange(nx) + 0.5) / nx
    w = x * (1 - x)
    arg = Lam**2 / (m**2 + w * q2E)
    return np.trapezoid(w * np.log(arg), x) / (2 * np.pi**2)
