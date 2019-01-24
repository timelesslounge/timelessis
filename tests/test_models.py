def test_new_company(new_company):
    print(new_company)
    assert new_company.id != None


def test_new_location(new_location):
    assert new_location.name == "Test location"
    assert new_location.code == "L"
    assert new_location.company_id == "123"
