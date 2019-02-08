import os
import tempfile

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from timeless import create_app
from timeless.db import DB


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app("config.TestingConfig")
    app_context = app.test_request_context()
    app_context.push()
    Migrate(app, DB)
    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(autouse=True)
def app_test_context(app):
    with app.test_request_context():
        DB.create_all()
        yield app
        DB.session.remove()
        DB.drop_all()


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
def setup_test_app():
    """
    Create a Flask app context for the tests.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.TestingConfig")

    return app


@pytest.fixture(scope='session')
def _db(setup_test_app):
    """
    Provide the transactional fixtures with access to the database via a
    Flask-SQLAlchemy database connection.
    """
    db = SQLAlchemy(app=setup_test_app)
    Migrate(setup_test_app, db)
    # apply any/all pending migrations.
    with setup_test_app.app_context():
        from flask_migrate import upgrade as _upgrade
        _upgrade()
    return db
