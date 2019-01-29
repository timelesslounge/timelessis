from timeless.companies.models import Company
from timeless.restaurants.models import Location
from timeless.restaurants.models import Floor
from timeless.reservations.models import ReservationSettings


def test_new_company():
    """
    @todo #31:30min Move tests to related module tests folder
    Test creating new company"""
    new_company = Company(name="First company", code="C")
    assert (new_company.name is not None
            and new_company.code is not None)


def test_new_location():
    name = "Test location"
    code = "L"
    company_id = 123
    new_location = Location(name=name, code=code, company_id=company_id)
    assert (new_location.name == name
            and new_location.code == code
            and new_location.company_id == company_id)


def test_new_floor():
    id = 1
    location_id = 456
    description = "First floor"
    new_floor = Floor(id=id, location_id=location_id, description=description)
    assert (new_floor.id == id
            and new_floor.location_id == location_id
            and new_floor.description == description)


def test_reservation_settings():
    greeting_by_time = {
            "6": "Good morning",
            "12": "Good afternoon",
            "18": "Good morning",
        }

    reservation_settings = ReservationSettings(
        id=1,
        name="Test name",
        default_duration=10,
        default_deposit=100,
        sms_notifications=False,
        threshold_sms_time=None,
        greeting_by_time=greeting_by_time,
        sex="M",
    )

    assert (
        reservation_settings.id == 1 and
        reservation_settings.name == "Test name" and
        reservation_settings.default_duration == 10 and
        reservation_settings.default_deposit == 100 and
        reservation_settings.sms_notifications is False and
        reservation_settings.threshold_sms_time is None and
        reservation_settings.greeting_by_time == greeting_by_time and
        reservation_settings.sex == "M"
    )
