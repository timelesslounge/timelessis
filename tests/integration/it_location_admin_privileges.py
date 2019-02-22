from datetime import datetime
import flask

from timeless.access_control.manager_privileges import has_privilege
from timeless.access_control.methods import Method
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.restaurants.models import Location, Floor, Table


def test_can_access_location_tables(app, db_session):
    """User with Location Admin role can access the tables
    from a Location owned by the company they work at"""
    company = Company(
        name="Foo Inc.", code="code1", address="addr"
    )
    location = Location(
        name="name",
        code="123",
        company_id=company.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    floor = Floor (
        description="1st Floor", location_id=location.id
    )
    table = Table(
        name="some table",
        floor_id=floor.id,
        x=40,
        y=50,
        width=320,
        height=150,
        status="available",
        max_capacity=12,
        multiple=false,
        playstation=false,
        shape_id=2,
        min_capacity=6,
        deposit_hour=2
    )
    db_session.add(company)
    db_session.add(location)
    db_session.add(floor)
    db_session.add(table)
    user = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3333,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(user)
    db_session.commit()
    assert has_privilege(
        method=Method.READ, resource="tables", id=table.id
    )


def test_cannot_access_tables_from_other_locations(app, db_session):
    """User with Location Admin role cannot access the tables
    from a Location which is not owned by the company they work at"""
    company = Company(
        name="Foo Inc.", code="code1", address="addr"
    )
    other = Company(
        name="Other Foo Inc.", code="code2", address="addr2"
    )
    location = Location(
        name="name",
        code="123",
        company_id=other.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    floor = Floor (
        description="1st Floor", location_id=location.id
    )
    table = Table(
        name="some table",
        floor_id=floor.id,
        x=40,
        y=50,
        width=320,
        height=150,
        status="available",
        max_capacity=12,
        multiple=false,
        playstation=false,
        shape_id=2,
        min_capacity=6,
        deposit_hour=2
    )
    db_session.add(company)
    db_session.add(other)
    db_session.add(location)
    db_session.add(floor)
    db_session.add(table)
    user = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3333,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(user)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="tables", id=table.id
    )
