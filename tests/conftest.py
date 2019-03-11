import os
import tempfile

import pytest

from tests import factories
from timeless import create_app
from timeless.cache import CACHE
from timeless.db import DB


@pytest.fixture(scope='session')
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app("config.TestingConfig")
    app_context = app.test_request_context()
    app_context.push()
    DB.create_all()
    yield app
    DB.session.remove()
    DB.drop_all()
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(autouse=True)
def corrected_factories(db_session):
    """ It patches factories with correct db session """
    for factory in (
        factories.TableShapeFactory,
        factories.EmployeeFactory,
        factories.CompanyFactory,
        factories.RoleFactory,
        factories.ReservationFactory,
        factories.SchemeTypeFactory,
        factories.LocationFactory,
    ):
        factory._meta.sqlalchemy_session = db_session


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions():
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        employee = factories.EmployeeFactory(
            company=factories.CompanyFactory(),
        )
        with self._client.session_transaction() as session:
            session["user_id"] = employee.id
            session["logged_in"] = True
        return True

    def logout(self):
        with self._client.session_transaction() as session:
            session["user_id"] = None
            session["logged_in"] = False
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)


@pytest.fixture(scope='session')
def _db(app):
    """
    Provide the transactional fixtures with access to the database via a
    Flask-SQLAlchemy database connection.
    """
    return DB


@pytest.fixture(autouse=True)
def clear_cache(app):
    """ Clean the cache for every test """
    with app.app_context():
        CACHE.clear()
