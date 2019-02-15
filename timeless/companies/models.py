"""File for models in test_companies module"""
from timeless.db import DB
from timeless.models import TimestampsMixin


class Company(TimestampsMixin, DB.Model):
    """Model for company business entity.
    @todo #3:30min Create management pages for Companies to list, create, edit
     and delete them. In the index page it should be possible to sort and filter
     for every column.
    """
    __tablename__ = "companies"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    address = DB.Column(DB.String)

    locations = DB.relationship("Location", order_by="Location.id",
                                back_populates="company")
    employees = DB.relationship("Employee", order_by="Employee.id",
                                back_populates="company")
    roles = DB.relationship("Role", order_by="Role.id",
                            back_populates="company")
    items = DB.relationship("Item", order_by="Item.id",
                            back_populates="company")

    @validate_required("name", "code")

    def __repr__(self):
        return "<Company %r>" % self.name
