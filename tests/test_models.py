from datetime import datetime

from timeless.companies.models import Company
from timeless.customers.models import Customer
from timeless.reservations.models import ReservationSettings, Comment
from timeless.restaurants.models import Location, Floor, TableShape, Table, Reservation
from timeless.roles.models import Role
from timeless.schemetypes.models import SchemeType


def test_new_company():
    """
    @todo #31:30min We need to move tests in this file
     to the appropriate module tests folder, for example
     test_companies test_locations test_tables and so on
    """
    """
     Test creating new company
    """
    new_company = Company(name="First company", code="C")
    assert (new_company.name is not None
            and new_company.code is not None)


def test_new_location():
    name = "Test location"
    code = "L"
    country = "Country"
    region = "Region"
    city = "City"
    type = "Type"
    address = "Address"
    longitude = "11223344"
    latitude = "44332211"
    status = "T"
    company_id = 123
    poster_id = 100
    synchronized_on = datetime.utcnow
    working_hours = 1
    closed_days = 2
    new_location = Location(
        name=name, code=code, company_id=company_id, poster_id=poster_id,
        country=country, region=region, city=city, type=type, address=address,
        longitude=longitude, latitude=latitude, status=status,
        synchronized_on=synchronized_on, working_hours=working_hours,
        closed_days=closed_days
    )
    assert (
        new_location.name == name
        and new_location.code == code
        and new_location.company_id == company_id
        and new_location.poster_id == 100
        and new_location.synchronized_on == synchronized_on
        and new_location.working_hours == working_hours
        and new_location.closed_days == closed_days
        and new_location.country == country
        and new_location.region == region
        and new_location.city == city
        and new_location.type == type
        and new_location.address == address
        and new_location.longitude == longitude
        and new_location.latitude == latitude
        and new_location.status == status
    )


def test_new_comment():
    body = "My comment"
    date = datetime.utcnow
    comment = Comment(body=body, date=date)
    assert (comment.body == body
            and comment.date == date)


def test_new_floor():
    id = 1
    location_id = 456
    description = "First floor"
    new_floor = Floor(id=id, location_id=location_id, description=description)
    assert (new_floor.id == id
            and new_floor.location_id == location_id
            and new_floor.description == description)


def test_new_table_shape():
    id = 1
    description = "Round table"
    picture = "/static/pictures/roundtable.png"
    new_table_shape = TableShape(
        id=id, description=description, picture=picture
    )
    assert (new_table_shape.id == id
            and new_table_shape.description == description
            and new_table_shape.picture == picture)


def test_new_roles():
    id = 1
    name = "Cleaner"
    works_on_shifts = True
    company_id = 10
    new_table = Role(
        id=id, name=name, works_on_shifts=works_on_shifts, company_id=company_id
    )
    assert (new_table.id == id
            and new_table.name == name
            and new_table.works_on_shifts == works_on_shifts
            and new_table.company_id == company_id)


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


def test_new_customer():
    first_name="First"
    last_name="Last"
    phone_number="+3859136281"
    created_on=datetime.utcnow
    updated_on=datetime.utcnow
    customer = Customer(first_name=first_name, last_name=last_name,
                        phone_number=phone_number, created_on=created_on,
                        updated_on=updated_on)
    assert (
        customer.first_name == first_name and
        customer.last_name == last_name and
        customer.phone_number == phone_number and
        customer.created_on == created_on and
        customer.updated_on == updated_on
    )
