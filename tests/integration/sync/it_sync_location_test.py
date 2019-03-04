import unittest.mock

import pytest

from timeless.companies.models import Company
from timeless.poster.api import Poster, Authenticated
from timeless.poster.tasks import sync_locations
from timeless.restaurants.models import Location


"""Integration tests for Location Sync with database

    @todo #232:30min Location poster mock refactor. To simplify future 
     poster mock creation PosterServerMock were refactored as a 
     generic server for postermocks (PosterServerMock in
     tests/integration/poster/poster_integration_mock.py). Implement a mock 
     location server based on PosterServerMock implementation.
    @todo #232:30min Refactor it_sync_location_test.py to use factory-created 
     mocks. Create Location in factories so we can use it instead fixed
     mocks. The refactor the tests below so they pass again 
"""


@pytest.mark.skip
@unittest.mock.patch.object(Authenticated, 'auth')
@unittest.mock.patch.object(Poster, 'locations')
def test_sync_location(locations_mock, auth_mock, db_session):
    company = Company(
        id=50,
        name="Company of Heroes",
        code="Cpny",
        address="Somewhere in the bermuda triangle"
    )
    db_session.add(company)
    db_session.commit()

    auth_mock.return_value = 'token'
    locations_mock.return_value = [{
            "id": 100,
            "name": "Coco Bongo",
            "code": "C",
            "company_id": company.id,
            "country": "United States",
            "region": "East Coast",
            "city": "Edge City",
            "address": "Blvd. Kukulcan Km 9.5 #30, Plaza Forum",
            "longitude": 21.1326063,
            "latitude": -86.7473191,
            "type": "L",
            "status": "open",
            "comment": "Nightclub from a famous movie"
        }]

    sync_locations()

    row = Location.query.filter_by(id=100).one()
    assert row.id == 100
    assert row.name == "Coco Bongo"
    assert row.code == "C"
    assert row.company_id == 50
    assert row.country == "United States"
    assert row.region == "East Coast"
    assert row.city == "Edge City"
    assert row.address == "Blvd. Kukulcan Km 9.5 #30, Plaza Forum"
    assert row.longitude == 21.1326063
    assert row.latitude == -86.7473191
    assert row.type == "L"
    assert row.status == "open"
    assert row.comment == "Nightclub from a famous movie"
