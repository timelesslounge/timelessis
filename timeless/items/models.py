"""File for models in items module"""
from timeless import DB
from datetime import datetime


class Item(DB.Model):
    """Model for item entity
    @todo #15:30min Items should store their historical data in a separate
     table, with start and end time.
    @todo #15:30min Develop management page so companies can list, create,
     edit and delete items. On the index page, it should be possible to sort
     and filter for each column.
    @todo #15:30min A new function to assign items to users should also be
     developed.
    """
    __tablename__ = "items"

    id=DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name=DB.Column(DB.String, nullable=False)
    stock_date=DB.Column(DB.DateTime, nullable=False)
    comment=DB.Column(DB.String, nullable=True)
    company_id=DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    created_on=DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on=DB.Column(DB.DateTime, onupdate=datetime.utcnow)

    company=DB.relationship("Company", back_populates="items")

    def __repr__(self):
        """Return object information - String"""
        return "<Item %r>" % self.name

