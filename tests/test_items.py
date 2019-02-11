""" Tests for the items.
"""

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
    assert (
        new_item.id == id and
        new_item.name == name and
        new_item.stock_date == stock_date and
        new_item.comment == comment and
        new_item.company_id == company_id
    )

def test_new_item_history():
    """ Test creation of new ItemHistory """
    emp_id = 2
    item_id = 1
    item_history = ItemHistory(employee_id=emp_id, item_id=item_id)
    assert (
        item_history.employee_id == emp_id and
        item_history.item_id == item_id
    )
