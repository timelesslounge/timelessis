"""File for models in roles module"""

from timeless import DB
from enum import Enum
from sqlalchemy_utils.types.choice import ChoiceType


class RoleType(Enum):
    """ Types of roles """
    Master = 1
    Intern = 2
    Director = 3
    Manager = 4


class Role(DB.Model):
    """Settings model for Role."""

    __tablename__ = "roles"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    """
        @todo #397:30m After adding role type, name is not useful and may make confusion.
         It should be deleted and all tests or code using it should use type instead.
    """
    name = DB.Column(DB.String, unique=True)
    works_on_shifts = DB.Column(DB.Boolean)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    role_type = DB.Column(ChoiceType(RoleType, impl=DB.Integer()), unique=True)

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
