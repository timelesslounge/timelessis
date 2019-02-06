"""File for models in restaurants module"""
from timeless.db import DB
from timeless.poster.models import PosterSyncMixin


class TableShape(DB.Model):
    """Model for a Table's Shape.
    @todo #13:30min Continue implementation. Table Shape should have its
     own management pages to list, create, edit and delete them. In the
     index page it should be possible to sort and filter for every column.
    """

    __tablename__ = "table_shapes"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, nullable=True)
    picture = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<TableShape %r>" % self.picture


class Floor(DB.Model):
    """Model for floor business entity. A Location may have 1 or more floors.
    """
    __tablename__ = "floors"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    location_id = DB.Column(DB.Integer, DB.ForeignKey("locations.id"))
    description = DB.Column(DB.String, nullable=True)

    location = DB.relationship("Location", back_populates="floors")

    def __repr__(self):
        return "<Floor %r>" % self.id


class Location(PosterSyncMixin, DB.Model):
    """Model for location business entity"""
    __tablename__ = "locations"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
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
    floors = DB.relationship("Floor", order_by=Floor.id, back_populates="location")
    working_hours = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))
    closed_days = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))

    def __repr__(self):
        return "<Location %r>" % self.name

class Table(DB.Model):
    """Model for a Table
    @todo #12:30min Continue implementation for Tables. Tables should have its own management pages to
     list, create, edit and delete them. In the index page it should be possible to sort and filter for every column.
     Table management pages should be accessed by the Location and Floor pages.
    """

    __tablename__ = "tables"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, nullable=False)
    floor_id = DB.Column(DB.Integer, DB.ForeignKey("floors.id"))
    x = DB.Column(DB.Integer, nullable=False)
    y = DB.Column(DB.Integer, nullable=False)
    width = DB.Column(DB.Integer, nullable=False)
    height = DB.Column(DB.Integer, nullable=False)
    status = DB.Column(DB.Integer, nullable=False)
    max_capacity = DB.Column(DB.Integer, nullable=False)
    multiple = DB.Column(DB.Boolean, default=False)
    playstation = DB.Column(DB.Boolean, default=False)
    shape_id = DB.Column(DB.Integer, DB.ForeignKey("table_shapes.id"))
    min_capacity = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))
    deposit_hour = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))
    created = DB.Column(DB.DateTime, nullable=False)
    updated = DB.Column(DB.DateTime, nullable=False)

    DB.UniqueConstraint(u"name", u"floor_id")

    def __repr__(self):
        return "<Table %r>" % self.name
