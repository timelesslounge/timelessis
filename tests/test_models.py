def test_new_company(new_company):
    ''' Test creating new company '''
    print(new_company)
    assert (new_company.name is not None
            and new_company.code is not None)

def test_new_location(new_location):
    assert (new_location.name == "Test location"
            and new_location.code == "L"
            and new_location.company_id == 123)
