""" Tests for the items.
"""

import pytest

from datetime import datetime

from timeless.items.models import Item, ItemHistory


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


@pytest.mark.skip(reason="Item.history() not implemented")
def test_item_assign():
    """ Test item assign """
    new_item = Item(
        id=1,
        name="Nanomedikit",
        stock_date=datetime.utcnow,
        comment="Medikit with nano particles",
        company_id=223
    )
    employee_id=15
    assert not new_item.employee_id
    new_item.assign(emp_id=employee_id)
    assert (new_item.employee_id == employee_id,
            "Item assigned to wrong employee" )
    assert (new_item.item_history()[0].employee_id == employee_id,
            "ItemHistory with wrong employee")


@pytest.mark.skip(reason="Item.history() not implemented")
def test_item_assign_history():
    """ Test item assign history """
    first_employee_id=15
    second_employee_id=60
    new_item = Item(
        id=1,
        name="Duck Eggs",
        stock_date=datetime.utcnow,
        comment="Eggs from ducks",
        company_id=223,
        employee_id=first_employee_id
    )
    new_item.assign(emp_id=second_employee_id)
    assert (new_item.item_history()[0].employe_id == second_employee_id,
            "Last ItemHistory with wrong employee")
    assert (new_item.item_history()[1].employe_id == first_employee_id,
            "First ItemHistory with wrong employee")
