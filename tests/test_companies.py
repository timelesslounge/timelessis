def test_company_endpoints(client):
    url = "/api/companies/"
    assert client.get(url).status_code == 200

    assert client.post(url).status_code == 201

    # detail resource
    url = "/api/companies/1"
    assert client.get(url).status_code == 200

    assert client.put(url).status_code == 200

    assert client.delete(url).status_code == 204
