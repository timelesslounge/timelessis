"""File for models in items module"""
from datetime import datetime

from timeless import DB
from timeless.models import validate_required


class Item(DB.Model):
    """Model for item entity
    """
    __tablename__ = "items"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, nullable=False)
    stock_date = DB.Column(DB.DateTime, nullable=False)
    comment = DB.Column(DB.String, nullable=True)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)
    company = DB.relationship("Company", back_populates="items")
    employee_id = DB.Column(DB.Integer, DB.ForeignKey("employees.id"))
    empolyee = DB.relationship("Employee", back_populates="items")
    history = DB.relationship("ItemHistory", back_populates="item")

    @validate_required("name", "stock_date", "comment", "created_on")
    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)

    def assign(self, employee):
        """ Assigning the item to an employee """
        self.employee_id = employee.id
        item_history = ItemHistory(employee_id=self.employee_id, item_id=self.id)

    def item_history(self):
        """ Returns item history
        @todo #217:30min Implement function to return item history.
         history() function must return item assignement history, a list of
         ItemHistory with all the items assignment history. Then remove skip
         annotation from test_items.test_item_assign
        """
        pass

    def __repr__(self):
        """Return object information - String"""
        return "<Item %r>" % self.name


class ItemHistory(DB.Model):
    """Model for item assigning history
    """
    __tablename__ = "itemsHistory"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    start_time = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    end_time = DB.Column(DB.DateTime)
    employee_id = DB.Column(DB.Integer, DB.ForeignKey("employees.id"))
    employee = DB.relationship("Employee", back_populates="history")
    item_id = DB.Column(DB.Integer, DB.ForeignKey("items.id"))
    item = DB.relationship("Item", back_populates="history")

    @validate_required("start_time")
    def __init__(self, **kwargs):
        super(ItemHistory, self).__init__(**kwargs)

    def __repr__(self):
        """Return object information - String"""
        return "<Item {self.id}>"
