from timeless.models import Company
from timeless.models import Location
from timeless.models import Floor

def test_new_company():
    ''' Test creating new company '''
    new_company = Company(name="First company", code="C")
    assert (new_company.name is not None
            and new_company.code is not None)

def test_new_location():
    name = "Test location"
    code = "L"
    company_id = 123
    new_location = Location(name=name, code=code, company_id=company_id)
    assert (new_location.name == name
            and new_location.code == code
            and new_location.company_id == company_id)

def test_new_floor():
    id = 1
    location_id = 456
    description = "First floor"
    new_floor = Floor(id=id, location_id=location_id, description=description)
    assert (new_floor.id == id
            and new_floor.location_id == location_id
            and new_floor.description == description)
