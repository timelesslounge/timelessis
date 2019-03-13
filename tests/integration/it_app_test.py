def test_hello(client):
    response = client.get("/")
    assert b"<h1>TIMELESS IS</h1>" and b"<h3>Login</h3>" in response.data
