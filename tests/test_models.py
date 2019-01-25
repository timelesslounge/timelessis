def test_new_company(new_company):
    print(new_company)
    assert new_company.id != None


def test_new_location(new_location):
    assert (new_location.name == "Test location"
            and new_location.code == "L"
            and new_location.company_id == 123)


def test_new_floor(new_floor):
    assert (new_floor.id == 1
            and new_floor.location_id == 456
            and new_floor.description == "First floor")
