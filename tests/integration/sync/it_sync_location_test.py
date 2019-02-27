
import pytest

from tests.poster_mock import free_port, start_server
from timeless.companies.models import Company
from timeless.restaurants.models import Location
from timeless.sync.synced_location import SyncedLocation
from timeless.poster.api import Poster

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


def test_sync_location(db_session):
    port = free_port()
    start_server(port,
        locations = [
            {
                "id": 100,
                "name": "Coco Bongo",
                "code": "C",
                "company_id": 50,
                "country": "United States",
                "region": "East Coast",
                "city": "Edge City",
                "address": "Blvd. Kukulcan Km 9.5 #30, Plaza Forum",
                "longitude": 21.1326063,
                "latitude": 86.7473191,
                "type": "L",
                "status": "open",
                "comment": "Nightclub from a famous movie"
            }
        ]
    )
    company = Company(
        id=50,
        name="Company of Heroes",
        code="Cpny",
        address="Somewhere in the bermuda triangle"
    )
    db_session.add(company)
    db_session.commit()
    location = Location(
        id=100,
        name="Coconut Bongolive",
        code="C",
        company_id=50,
        country="United States of America",
        region="West Coast",
        city="Another city",
        address="Some address in Another City",
        longitude=42.2642026,
        latitude=-172.148146,
        type="L",
        status="closed",
        comment="A location with "
    )
    db_session.add(location)
    db_session.commit()
    SyncedLocation(
        location=location,
        poster_sync=Poster(
            url="http://localhost:{port}".format(port=port)
        ),
        db_session=db_session
    ).sync()
    row = db_session.query(Location).get(location.id)
    assert row.id == 100 
    assert row.name[0] == "Coco Bongo"
    assert row.code[0] == "C"
    assert row.company_id[0] == 50
    assert row.country[0] == "United States"
    assert row.region[0] == "East Coast"
    assert row.city[0] == "Edge City"
    assert row.address[0] == "Blvd. Kukulcan Km 9.5 #30, Plaza Forum"
    assert row.longitude[0] == 21.1326063
    assert row.latitude[0] == -86.7473191
    assert row.type[0] == "L"
    assert row.status[0] == "open"
    assert row.comment == "Nightclub from a famous movie"
