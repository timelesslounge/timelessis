import unittest.mock

import pytest
import re

from tests.integration.poster.poster_server_mock import PosterServerMock
from timeless.companies.models import Company
from timeless.poster.api import Poster, Authenticated
from timeless.poster.tasks import sync_locations
from timeless.restaurants.models import Location


"""Integration tests for Location Sync with database

    @todo #232:30min Refactor it_sync_location_test.py to use factory-created
     mocks. Create Location in factories so we can use it instead fixed
     mocks. The refactor the tests below so they pass again
"""
class LocationsPosterServerMock(PosterServerMock):
    PATTERN = re.compile(r"/clients.getLocations")
    company = None

    def get_content(self):
        return {
            "response": [{
                "id": 100,
                "name": "Coco Bongo",
                "code": "C",
                "company_id": self.company.id,
                "country": "United States",
                "region": "East Coast",
                "city": "Edge City",
                "address": "Blvd. Kukulcan Km 9.5 #30, Plaza Forum",
                "longitude": 21.1326063,
                "latitude": -86.7473191,
                "type": "L",
                "status": "open",
                "comment": "Nightclub from a famous movie"
            }, {
                "id": 150,
                "name": "Cook Pirata",
                "code": "CP",
                "company_id": self.company.id,
                "country": "Brazil",
                "region": "South Region",
                "city": "Curitiba",
                "address": "Mateus Leme 1020",
                "longitude": 19.13063,
                "latitude": -15.91,
                "type": "H",
                "status": "open",
                "comment": "Famous pirate-themed seafood restaurant"
            }
            ]
        }



@pytest.mark.skip(
    "Skipped until ticket #453 is fixed")
@unittest.mock.patch.object(Authenticated, "auth")
@unittest.mock.patch.object(Poster, "locations")
def test_sync_location(locations_mock, auth_mock, db_session):
    company = Company(
        id=50,
        name="Company of Heroes",
        code="Cpny",
        address="Somewhere in the bermuda triangle"
    )
    db_session.add(company)
    db_session.commit()
    auth_mock.return_value = "token"

    poster_locations = LocationsPosterServerMock
    poster_locations.company = company

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
