import pytest


@pytest.mark.skip
def test_company_endpoints(client):
    """
    @todo #183:30min This test is broken when checking permissions in
     SecuredView has been implemented. Check how permissions are implemeted
     and fix this test or permissions. Sounds like there is a mistake in
     permission functions.
    """
    url = "/api/companies/"
    assert client.get(url).status_code == 200

    assert client.post(url).status_code == 201

    # detail resource
    url = "/api/companies/1"
    assert client.get(url).status_code == 200

    assert client.put(url).status_code == 200

    assert client.delete(url).status_code == 204
