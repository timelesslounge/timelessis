"""File for all models in Timeless"""
from datetime import datetime
from timeless import DB


class Location(DB.Model):
    """Model for location business entity
    @todo #10:30min Continue implementation. Locations should have its own management pages to
     list, create, edit and delete them. In the index page it should
     be possible to sort and filter for every column.
    """
    __tablename__ = 'locations'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    company_id = DB.Column(DB.Integer, DB.ForeignKey('companies.id'))
    country = DB.Column(DB.String, nullable=False)
    region = DB.Column(DB.String, nullable=False)
    city = DB.Column(DB.String, nullable=False)
    address = DB.Column(DB.String, nullable=False)
    longitude = DB.Column(DB.String, nullable=False)
    latitude = DB.Column(DB.String, nullable=False)
    type = DB.Column(DB.String, nullable=False)
    status = DB.Column(DB.String, nullable=False)
    comment = DB.Column(DB.String, nullable=True)

    company = DB.relationship("Company", back_populates="locations")

    def __repr__(self):
        return '<Location %r>' % self.name

class Company(DB.Model):
    """Model for company business entity.
    @todo #3:30min Create management pages for Companies to list, create, edit
     and delete them. In the index page it should be possible to sort and filter
     for every column.
    @todo #3:30min Implement TimestampMixin, like in the example
     (http://flask-sqlalchemy.pocoo.org/2.3/customizing/). Change all the models
     to use this mixin instead of existing created_on and updated_on fields.
    """
    __tablename__ = 'companies'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    address = DB.Column(DB.String)
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)

    locations = DB.relationship("Location", order_by=Location.id,
                                back_populates="company")
    
    def __init__(self, name, code, address=""):
        self.name = name
        self.code = code
        self.address = address
        self.created_on = datetime.utcnow

    def __repr__(self):
        return '<Company %r>' % self.name
