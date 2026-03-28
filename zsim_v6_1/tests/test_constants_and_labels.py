from fractions import Fraction

from zsim.core.constants import (
    A_DENOMINATOR,
    A_FRACTION,
    A_LOCKED,
    A_NUMERATOR,
    DIM_X,
    DIM_Y,
    DIM_Z,
    Q_TOTAL,
    get_sector_dims,
)
from zsim.core.labels import (
    EpistemicOverclaimError,
    LabeledValue,
    Status,
    assert_status_not_overclaimed,
    ensure_minimum_status,
)


def test_locked_constants_match_expected_values():
    assert A_NUMERATOR == 35
    assert A_DENOMINATOR == 437
    assert A_FRACTION == Fraction(35, 437)
    assert abs(A_LOCKED - (35 / 437)) < 1e-15
    assert (DIM_X, DIM_Z, DIM_Y) == (3, 2, 6)
    assert Q_TOTAL == 11


def test_sector_dims_copy_is_stable():
    dims = get_sector_dims()
    assert dims == {"X": 3, "Z": 2, "Y": 6}
    dims["X"] = 999
    assert get_sector_dims()["X"] == 3


def test_labeled_value_to_dict():
    value = LabeledValue(
        name="phase_mode",
        value="bounded_sine",
        status=Status.TRANSLATED,
        rationale="Implementation closure choice for v0.1",
        metadata={"module": "kernel.phase"},
    )
    payload = value.to_dict()
    assert payload["status"] == "TRANSLATED"
    assert payload["metadata"]["module"] == "kernel.phase"


def test_overclaim_guard_rejects_promotions():
    try:
        assert_status_not_overclaimed(
            actual=Status.TRANSLATED,
            claimed=Status.PROVEN,
            name="phase gate",
        )
    except EpistemicOverclaimError:
        pass
    else:
        raise AssertionError("Expected EpistemicOverclaimError for overclaim promotion.")


def test_minimum_status_guard_accepts_stronger_status():
    ensure_minimum_status(actual=Status.PROVEN, minimum=Status.DERIVED, name="A")
