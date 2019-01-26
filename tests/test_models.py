def test_new_company(new_company):
    print(new_company)
    assert new_company.id != None


def test_new_location(new_location):
    assert (new_location.name == "Test location"
            and new_location.code == "L"
            and new_location.company_id == 123)


def test_new_scheme_condition(new_scheme_condition):
    assert (new_scheme_condition.id == 1
            and new_scheme_condition.value == "test"
            and new_scheme_condition.priority == 2)
