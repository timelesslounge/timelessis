"""File for models in restaurants module"""
import enum

from timeless.db import DB
from timeless.models import TimestampsMixin, validate_required
from timeless.poster.models import PosterSyncMixin


class ReservationStatus(enum.Enum):
    """Reservation status"""
    unconfirmed = 1
    confirmed = 2
    started = 3
    finished = 4
    canceled = 5
    late = 6
    not_contacting = 7


class TableShape(DB.Model):
    """Model for a Table's Shape."""

    __tablename__ = "table_shapes"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, nullable=True)
    picture = DB.Column(DB.String, nullable=False)

    @validate_required("picture")
    def __init__(self, **kwargs):
        super(TableShape, self).__init__(**kwargs)

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
    tables = DB.relationship("Table", order_by="Table.id",
                             back_populates="floor")

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

    @validate_required("name", "code", "country", "region", "city", "type",
                       "address", "longitude", "latitude", "status")
    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)

    def __repr__(self):
        return "<Location %r>" % self.name


class TableReservation(DB.Model):
    """Association table for reservations and tables"""

    __tablename__ = "table_reservations"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    reservation_id = DB.Column(DB.Integer, DB.ForeignKey("reservations.id"))
    table_id = DB.Column(DB.Integer, DB.ForeignKey("tables.id"))
    table = DB.relationship("Table", back_populates="reservations")
    reservation = DB.relationship("Reservation", back_populates="tables")


class Table(TimestampsMixin, PosterSyncMixin, DB.Model):
    """Model for a Table"""

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

    reservations = DB.relationship("TableReservation", back_populates="table")
    floor = DB.relationship("Floor", back_populates="tables")

    DB.UniqueConstraint(u"name", u"floor_id")

    def __repr__(self):
        return "<Table %r>" % self.name


class Reservation(TimestampsMixin, DB.Model):
    """Model for a Reservation

    """

    __tablename__ = "reservations"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    start_time = DB.Column(DB.DateTime, nullable=False)
    end_time = DB.Column(DB.DateTime, nullable=False)
    customer_id = DB.Column(DB.Integer, DB.ForeignKey("customers.id"))
    num_of_persons = DB.Column(DB.Integer, nullable=False)
    comment = DB.Column(DB.String, nullable=False)
    status = DB.Column(DB.Enum(ReservationStatus), nullable=False)

    tables = DB.relationship("TableReservation", back_populates="reservation")

    @validate_required("start_time", "end_time", "num_of_persons", "comment",
                       "status")
    def __init__(self, **kwargs):
        super(Reservation, self).__init__(**kwargs)

    def duration(self):
        return self.end_time - self.start_time

    def __repr__(self):
        return "<Reservation %r>" % self.id
