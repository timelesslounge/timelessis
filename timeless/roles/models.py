"""File for models in roles module"""

from timeless import DB
from enum import Enum
from sqlalchemy_utils.types.choice import ChoiceType


class RoleType(Enum):
    """ Types of roles """
    Director = "Director"
    Manager = "Manager"
    Master = "Master"
    Intern = "Intern"


class Role(DB.Model):
    """Settings model for Role."""

    __tablename__ = "roles"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    """
        @todo #397:30m After adding role type, name may make confusion.
         It should be deleted and all code using it should use type instead.
         Also, Alter the views of the roles to match the changes.
    """
    name = DB.Column(DB.String, unique=True)
    works_on_shifts = DB.Column(DB.Boolean)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    role_type = DB.Column(ChoiceType(RoleType, impl=DB.String()), unique=True)

    company = DB.relationship("Company", back_populates="roles")
    employees = DB.relationship("Employee", back_populates="role")

    def __repr__(self):
        return "<Role %r>" % self.role_type

    def is_master_or_intern(self):
        """ check if the type is master or intern """
        return self.role_type in (RoleType.Master, RoleType.Intern,)

    def is_director(self):
        """ check if type is director """
        return self.role_type == RoleType.Director
