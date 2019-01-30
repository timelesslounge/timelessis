"""Tests for models in the schemetypes package."""
from timeless.schemetypes.models import SchemeCondition, SchemeType


def test_new_scheme_condition():
    condition = SchemeCondition(id=1, value="test", priority=2)
    assert (condition.id == 1
            and condition.value == "test"
            and condition.priority == 2)


def test_new_scheme_type():
    scheme_type = SchemeType(id=1, description="description", default_value="2", value_type="STRING")
    assert (scheme_type.id == 1
            and scheme_type.description == "description"
            and scheme_type.default_value == "2"
            and scheme_type.value_type == "STRING")
