"""Tests for models in the schemetypes package."""
from timeless.schemetypes.models import SchemeCondition, SchemeType, WeekDay, MonthDay, Date
from datetime import datetime

def test_new_scheme_condition():
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    condition = SchemeCondition(id=1, value="test", priority=2,
                                start_time=start_time,
                                end_time=end_time)
    assert (condition.id == 1
            and condition.value == "test"
            and condition.priority == 2
            and start_time == start_time
            and end_time == end_time)


def test_new_scheme_type():
    scheme_type = SchemeType(id=1, description="description", default_value="2", value_type="STRING")
    assert (scheme_type.id == 1
            and scheme_type.description == "description"
            and scheme_type.default_value == "2"
            and scheme_type.value_type == "STRING")

def test_new_weekday():
    day = WeekDay(id=1, weekday=1, scheme_condition_id=2)
    assert (day.id == 1
            and day.weekday == 1
            and day.scheme_condition_id == 2)

def test_new_monthday():
    day = MonthDay(id=1, monthday=1, scheme_condition_id=2)
    assert (day.id == 1
            and day.monthday == 1
            and day.scheme_condition_id == 2)

def test_new_date():
    month_year = "01-2019"
    date_format = "%m-%Y"
    test_date = Date(id=1, date=datetime.strptime(month_year, date_format), scheme_condition_id=2)
    assert (test_date.id == 1
            and test_date.date == datetime.strptime(month_year, date_format)
            and test_date.scheme_condition_id == 2)
