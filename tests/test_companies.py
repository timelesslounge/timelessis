def test_company_endpoints(client):
    url = "/api/companies/"
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 201

    # detail resource
    url = "/api/companies/1"
    response = client.get(url)
    assert response.status_code == 200

    response = client.put(url)
    assert response.status_code == 200

    response = client.delete(url)
    assert response.status_code == 204
