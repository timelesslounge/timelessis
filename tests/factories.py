"""Factories for all models in the project."""
import factory
import random

from timeless import DB
from timeless.employees import models as employee_models
from timeless.restaurants import models as restaurants_models


class TableShapeFactory(factory.alchemy.SQLAlchemyModelFactory):
    """ Factory for creating TableShape instance. """
    description = factory.Faker("text")
    picture = factory.Faker("text")

    class Meta:
        model = restaurants_models.TableShape
        sqlalchemy_session = DB.session
        sqlalchemy_session_persistence = "commit"


class EmployeeFactory(factory.alchemy.SQLAlchemyModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")
    phone_number = factory.Faker("phone_number")
    birth_date = factory.Faker("date")
    registration_date = factory.Faker("date")
    account_status = factory.Faker("text")
    user_status = factory.Faker("text")
    email = factory.Faker("email")
    password = factory.Faker("text")
    pin_code = factory.LazyAttribute(lambda _: random.randint(1, 9999))
    comment = "Test comment"

    class Meta:
        model = employee_models.Employee
        sqlalchemy_session = DB.session
        sqlalchemy_session_persistence = "commit"
