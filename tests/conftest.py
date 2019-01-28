import os
import tempfile

import pytest
from datetime import datetime
from timeless import create_app
from timeless.models import Location
from timeless.models import Floor

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
def new_location():
    location = Location(name="Test location", code="L", company_id=123, poster_id=100, synchronized_on=datetime.utcnow)
    return location

@pytest.fixture(scope='module')
def new_floor():
    floor = Floor(id=1, location_id=456, description="First floor")
    return floor

