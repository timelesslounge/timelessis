import os
import tempfile

import pytest

from timeless import create_app, cache
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
        return self._client.post(
            "/auth/login",
            data={"username": username, "password": password}
        )

    def logout(self):
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


@pytest.fixture
def clear_cache(app):
    with app.app_context():
        cache.clear()
