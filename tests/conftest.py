import os
import tempfile

import pytest
from timeless import create_app
from timeless.models import Company
from timeless.models import Location
from timeless.db.schemetypes.SchemeCondition import SchemeCondition

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app('config.TestingConfig')
    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='module')
def new_company():
    company = Company(1)
    return company


@pytest.fixture(scope='module')
def new_location():
    location = Location(name="Test location", code="L", company_id=123)
    return location


@pytest.fixture(scope='module')
def new_scheme_condition():
    condition = SchemeCondition(id=1, value="test", priority=2)
    return condition
