"""File for models in roles module"""

from timeless import DB


class Role(DB.Model):
    """Settings model for Role."""

    __tablename__ = "roles"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True)
    works_on_shifts = DB.Column(DB.Boolean)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))

    company = DB.relationship("Company", back_populates="roles")

    def __repr__(self):
        return "<Role %r>" % self.name
