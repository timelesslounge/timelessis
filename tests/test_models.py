def test_new_company(new_company):
    print(new_company)
    assert new_company.id != None


def test_new_location(new_location):
    assert (new_location.name == "Test location"
            and new_location.code == "L"
            and new_location.company_id == 123)
