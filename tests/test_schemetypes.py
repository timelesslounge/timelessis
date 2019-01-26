"""Tests for models in the schemetypes package."""
from timeless.db.schemetypes.scheme_condition import SchemeCondition


def test_new_scheme_condition():
    condition = SchemeCondition(id=1, value="test", priority=2)
    assert (condition.id == 1
            and condition.value == "test"
            and condition.priority == 2)
