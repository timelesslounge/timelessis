""" Tests for the items.
"""

import pytest

from datetime import datetime

from timeless.items.models import Item, ItemHistory
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.restaurants.models import Location


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
        company_id=company_id,
        created_on=datetime.utcnow
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
    item_history = ItemHistory(
        employee_id=emp_id,
        item_id=item_id,
        start_time=datetime.utcnow
    )
    assert item_history.employee_id == emp_id
    assert item_history.item_id == item_id


def test_item_assign():
    """ Test item assign """

    company = Company(
        id=223,
        name="Bad Company",
        code="Bad Cmpny",
        address="addr"
    )

    item = Item(
        id=1,
        name="Duck Eggs",
        stock_date=datetime.utcnow,
        comment="Eggs from ducks",
        company_id=company.id,
        created_on=datetime.utcnow,
        updated_on=datetime.utcnow,
        company=company
    )

    assignee = Employee(
        id=15,
        first_name="Johnny",
        last_name="Cash",
        username="meninblack",
        phone_number="555-5555",
        birth_date=datetime.utcnow(),
        registration_date=datetime.utcnow(),
        account_status="active",
        user_status="active",
        email="meninblack@johnncash.com",
        password="carterjune",
        pin_code=55,
        comment="A famous american country singer",
        company_id=223
    )

    assert not item.employee_id
    item.assign(employee=assignee)
    assert (item.employee_id == assignee.id,
            "Item assigned to wrong employee")
    assert (item.item_history()[0].employee_id == assignee.id,
            "ItemHistory with wrong employee")


def test_item_assign_history():
    """ Test item assign history """

    company = Company(
        id=223,
        name="Bad Company",
        code="Bad Cmpny",
        address="addr"
    )

    first_employee = Employee(
        id=20,
        first_name="Elvis",
        last_name="Presley",
        username="king",
        phone_number="555-5555",
        birth_date=datetime.utcnow(),
        registration_date=datetime.utcnow(),
        account_status="active",
        user_status="active",
        email="theking@king.com",
        password="theking",
        pin_code=100,
        comment="Famous artist known as The King of Rock and Roll",
        company_id=company.id
    )

    second_employee = Employee(
        id=60,
        first_name="Frank",
        last_name="Sinatra",
        username="blueeyes",
        phone_number="555-5555",
        birth_date=datetime.utcnow(),
        registration_date=datetime.utcnow(),
        account_status="active",
        user_status="active",
        email="blueeyes@sinatra.com",
        password="nancy",
        pin_code=55,
        comment="One of the most popular musical artists of the 20th century",
        company_id=company.id
    )

    item = Item(
        id=1,
        name="Duck Eggs",
        stock_date=datetime.utcnow,
        comment="Eggs from ducks",
        company_id=company.id,
        employee_id=first_employee.id,
        created_on=datetime.utcnow,
        updated_on=datetime.utcnow,
        company=company
    )
    item.assign(employee=first_employee)
    item.assign(employee=second_employee)
    assert (
        item.item_history()[0].employee_id == second_employee,
        "Last ItemHistory with wrong employee"
    )
    assert (
        item.item_history()[1].employee_id == first_employee.id,
        "First ItemHistory with wrong employee"
    )
    assert (
        item.item_history()[1].end_time is not None,
        "First ItemHistory end_time not set"
    )
