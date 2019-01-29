"""File for models in reservations module"""
from timeless import DB


class Comment(DB.Model):
    """Model for location business entity
    @todo #10:30min Continue implementation. Locations should have its own management pages to
     list, create, edit and delete them. In the index page it should
     be possible to sort and filter for every column.
    """
    __tablename__ = 'comments'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    description = DB.Column(DB.String, nullable=False)
    employee_id = DB.Column(DB.Integer, DB.ForeignKey('employees.id'))

    employee = DB.relationship("Employee", back_populates="comments")

    def __repr__(self):
        return "<Comment %r>" % self.description