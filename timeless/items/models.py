"""File for models in items module"""
from datetime import datetime
from timeless import DB

class Item(DB.Model):
    """Model for item entity
    @todo #15:30min Continue the implementation. Items must have their own
     management pages to list, create, edit, and delete them. On the index
     page, you should be able to sort and filter for each column.
    @todo #15:30min A new function to assign items to users should also be
     developed. They should also store their historical data in a table, with
     start and end times.
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

    def __repr__(self):
        """Return object information - String"""
        return "<Item %r>" % self.name
