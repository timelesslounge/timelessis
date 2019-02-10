import factory

from timeless import DB
from timeless.restaurants import models


class TableShapeFactory(factory.alchemy.SQLAlchemyModelFactory):
    description = factory.Faker('text')
    picture = factory.Faker('text')

    class Meta:
        model = models.TableShape
        sqlalchemy_session = DB.session
        sqlalchemy_session_persistence = 'commit'
