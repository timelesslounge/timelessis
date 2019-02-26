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
    employees = DB.relationship("Employee", back_populates="role")

    def __repr__(self):
        return "<Role %r>" % self.name

    def is_master_or_intern(self):
        """
        @todo #341:30m Need to find nice way to understand what is role of this
         instance. May be it's better to introduce `type` field with choices.
        """
        return self.name in ("Master", "Intern",)
