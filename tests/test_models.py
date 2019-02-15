from datetime import datetime
from pytest import raises

from timeless.companies.models import Company
from timeless.customers.models import Customer
from timeless.reservations.models import ReservationSettings, Comment
from timeless.restaurants.models import (Location, Floor, TableShape, Table,
                                         ReservationStatus, Reservation)
from timeless.roles.models import Role
from timeless.employees.models import Employee
from timeless.items.models import Item, ItemHistory
from timeless.schemetypes.models import (SchemeCondition, SchemeType, WeekDay,
                                         MonthDay, Date)


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
    assert (new_company.name is not None and new_company.code is not None)


def test_new_location():
    name = "Test location"
    code = "L"
    company_id = 123
    poster_id = 100
    synchronized_on = datetime.utcnow
    working_hours = SchemeType()
    closed_days = SchemeType()

    new_location = Location(
        name=name, code=code, company_id=company_id, poster_id=poster_id,
        synchronized_on=synchronized_on, working_hours=working_hours.id,
        closed_days=closed_days.id
    )
    assert (
        new_location.name == name
        and new_location.code == code
        and new_location.company_id == company_id
        and new_location.poster_id == 100
        and new_location.synchronized_on == synchronized_on
        and new_location.working_hours == working_hours.id
        and new_location.closed_days == closed_days.id
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
    new_table = Role(id=id, name=name, works_on_shifts=works_on_shifts,
                     company_id=company_id)
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


def test_new_table():
    id = 42
    name = "Philosopher's Table"
    floor_id = 600
    x = 40
    y = 50
    width = 320
    height = 200
    status = "available"
    max_capacity = 5
    multiple = False
    playstation = False
    shape_id = 3
    created = datetime.utcnow
    updated = datetime.utcnow
    min_capacity = SchemeType()
    deposit_hour = SchemeType()

    new_table = Table(
        id=id,
        name=name,
        floor_id=floor_id,
        x=x,
        y=y,
        width=width,
        height=height,
        status=status,
        max_capacity=max_capacity,
        multiple=multiple,
        playstation=playstation,
        shape_id=shape_id,
        created=created,
        updated=updated,
        min_capacity=min_capacity.id,
        deposit_hour=deposit_hour.id
    )
    assert (new_table.id == id and
            new_table.name == name and
            new_table.floor_id == floor_id and
            new_table.x == x and
            new_table.y == y and
            new_table.width == width and
            new_table.height == height and
            new_table.status == status and
            new_table.max_capacity == max_capacity and
            new_table.multiple == multiple and
            new_table.playstation == playstation and
            new_table.shape_id == shape_id and
            new_table.created == created and
            new_table.updated == updated and
            new_table.min_capacity == min_capacity.id and
            new_table.deposit_hour == deposit_hour.id
            )


def test_new_customer():
    first_name = "First"
    last_name = "Last"
    phone_number = "+3859136281"
    customer = Customer(first_name=first_name, last_name=last_name,
                        phone_number=phone_number)
    assert (
        customer.first_name == first_name and
        customer.last_name == last_name and
        customer.phone_number == phone_number
    )


def test_new_employee():
    employee = Employee(username="alice", password="coop1", first_name="Alice",
                        last_name="Cooper", phone_number="112233",
                        birth_date=datetime.utcnow(), email="test@test.com")
    assert (employee.first_name == "Alice" and
            employee.last_name == "Cooper" and
            employee.account_status == "Not Activated" and
            employee.user_status == "Working" and
            employee.created_on is not None and
            len(str(employee.pin_code)) == 4 and
            employee.validate_password("coop1") is True)


def test_employee_missing_required_params():
    with raises(KeyError, match="Missing required param: password"):
        Employee(username="bob", first_name="Bob")
    with raises(KeyError, match="Missing required param: phone_number"):
        Employee(username="bob", password="bob1", first_name="Bob",
                 last_name="Dylan", birth_date=datetime.utcnow,
                 email="bob@bob.com")


def test_new_item():
    """ Test creation on new Item """
    id = 1
    name = "First Item"
    stock_date = datetime.utcnow
    comment = "Commentary of the first item"
    company_id = 123
    new_item = Item(
        id=id,
        name=name,
        stock_date=stock_date,
        comment=comment,
        company_id=company_id
    )
    assert new_item.id == id
    assert new_item.name == name
    assert new_item.stock_date == stock_date
    assert new_item.comment == comment
    assert new_item.company_id == company_id


def test_new_item_history():
    """ Test creation of new ItemHistory """
    emp_id = 2
    item_id = 1
    item_history = ItemHistory(employee_id=emp_id, item_id=item_id)
    assert item_history.employee_id == emp_id
    assert item_history.item_id == item_id


def test_new_reservation():
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    customer_id = 1
    num_of_persons = 4
    comment = "My comment"
    status = ReservationStatus.confirmed
    new_reservation = Reservation(
        start_time=start_time,
        end_time=end_time,
        customer_id=customer_id,
        num_of_persons=num_of_persons,
        comment=comment,
        status=status
    )
    assert (
        new_reservation.start_time == start_time and
        new_reservation.end_time == end_time and
        new_reservation.customer_id == customer_id and
        new_reservation.num_of_persons == num_of_persons and
        new_reservation.comment == comment and
        new_reservation.status == status
    )


def test_reservation_duration():
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    customer_id = 5
    num_of_persons = 4
    comment = "This is a reservation for duration test"
    status = ReservationStatus.confirmed
    new_reservation = Reservation(
        start_time=start_time,
        end_time=end_time,
        customer_id=customer_id,
        num_of_persons=num_of_persons,
        comment=comment,
        status=status
    )
    assert new_reservation.duration() == end_time - start_time


def test_new_scheme_condition():
    condition = SchemeCondition(id=1, value="test", priority=2)
    assert (condition.id == 1
            and condition.value == "test"
            and condition.priority == 2)


def test_new_scheme_type():
    scheme_type = SchemeType(id=1, description="description",
                             default_value="2", value_type="STRING")
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
    test_date = Date(id=1, date=datetime.strptime(month_year, date_format),
                     scheme_condition_id=2)
    assert (test_date.id == 1
            and test_date.date == datetime.strptime(month_year, date_format)
            and test_date.scheme_condition_id == 2)
