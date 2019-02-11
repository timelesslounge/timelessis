
from timeless.restaurants.models import Location
from timeless.companies.models import Company

def test_create_location(db_session):
    """Integration test for adding and selecting Location"""
    location = create_location(db_session)
    row = db_session.query(Location).get(location.id)
    assert row and row.name == location.name


def test_edit_location(db_session):
    """Integration test for editing Location"""
    location = create_location(db_session)
    location.name="Another fast food restaurant"
    location.code="NAKB"
    location.country="France"
    location.region="Normandy"
    location.city="Caen"
    location.address="Numéro de rue 2"
    location.longitude=49
    location.latitude=0
    location.type="B"
    location.status="open"
    location.comment="An unknown fast food restaurant."
    db_session.merge(location)
    row = db_session.query(Location).get(location.id)
    assert row and row.name == location.name


def test_delete_location(db_session):
    """Integration test for deleting Location"""
    location = create_location(db_session)
    db_session.delete(location)
    db_session.commit()
    assert not db_session.query(Location).get(location.id)

def create_location(db_session):
    company = Company(
        name="Krusty Inc.",
        code="KI",
        address="Springfield Lane,12"
    )
    location =  Location(
        name="Krusty Burger",
        code="KB",
        company_id=company.id,
        country="United States",
        region="Middle East",
        city="Springfield",
        address="Jebediah Street, NN",
        longitude=23,
        latitude=25,
        type="B",
        status="open",
        comment="Fast food restaurant from a famous animated sitcom."
    )
    db_session.add(company)
    db_session.add(location)
    db_session.commit()
    return location