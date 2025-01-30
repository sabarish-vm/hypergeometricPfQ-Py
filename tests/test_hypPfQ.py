import numpy as np
from hypPfQ import hypPfQ_np


def test_a0b0():
    a = np.array([])
    b = np.array([])
    z = np.array([0.1, 0.5, 0.9])
    r = np.zeros_like(z)
    hypPfQ_np(a, b, z, r)
    comp = np.exp(z)
    assert np.isclose(
        r, comp, atol=1e-6
    ).all(), "Cannot reproduce the correct values for null a and null b"


def test_a0bN():
    a = np.array([])
    b = np.array([3.0, 4.0])
    z = np.array([0.1, 0.5, 0.9])
    r = np.zeros_like(z)
    hypPfQ_np(a, b, z, r)
    comp = np.array([1.00835418982, 1.0421904021, 1.076704465692])
    assert np.isclose(
        r, comp, atol=1e-6
    ).all(), "Cannot reproduce the correct values for null a and non-null b"


def test_aNb0():
    a = np.array([])
    b = np.array([3.0, 4.0])
    z = np.array([0.1, 0.5, 0.9])
    r = np.zeros_like(z)
    hypPfQ_np(a, b, z, r)
    comp = np.array([1.00835418982, 1.0421904021, 1.076704465692])
    assert np.isclose(
        r, comp, atol=1e-6
    ).all(), "Cannot reproduce the correct values for null b and non-null a"


def test_aNbN():
    a = np.array([1.0, 2.0])
    b = np.array([3.0, 4.0])
    z = np.array([0.1, 0.5, 0.9])
    r = np.zeros_like(z)
    hypPfQ_np(a, b, z, r)
    comp = np.array([1.0169200401, 1.09002619782, 1.1729678493])
    assert np.isclose(
        r, comp, atol=1e-6
    ).all(), "Cannot reproduce the correct values for non-null a and non-null b"
