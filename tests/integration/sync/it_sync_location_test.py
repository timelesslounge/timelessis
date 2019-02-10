
import pytest

from tests.poster_mock import free_port, start_server
from timeless.companies.models import Company
from timeless.restaurants.models import Location
from timeless.sync.synced_location import SyncedLocation
from timeless.poster.api import Poster

"""Integration tests for Location Sync with database

"""



@pytest.mark.skip("sync for location not implemented yet")
def test_sync_location(db_session):
    port = free_port()
    start_server(port,
        locations = [
            {
                "id":100,
                "name":"Coco Bongo",
                "code":"C",
                "company_id":50,
                "country":"United States",
                "region":"East Coast",
                "city":"Edge City",
                "address":"Blvd. Kukulcan Km 9.5 #30, Plaza Forum",
                "longitude":21.1326063,
                "latitude":-86.7473191,
                "type":"L",
                "status":"open",
                "comment":"Nightclub from a famous movie"
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
    synced_location = SyncedLocation(location).sync(
        Poster(
            url="http://localhost:{port}".format(port=port)
        )
    )
    row = db_session.query(Location).get(synced_location.id)
    assert(
        row.id == 100 and
        row.name == "Coco Bongo" and
        row.code == "C" and
        row.company_id == 50 and
        row.country == "United States" and
        row.region == "East Coast" and
        row.city == "Edge City" and
        row.address == "Blvd. Kukulcan Km 9.5 #30, Plaza Forum" and
        row.longitude == 21.1326063 and
        row.latitude == -86.7473191 and
        row.type == "L" and
        row.status == "open" and
        row.comment == "Nightclub from a famous movie"
    )
