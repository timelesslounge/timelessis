def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
