def test_list(client):
    assert client.get("/floors/").status_code == 200

def test_create(client):
    assert client.get("/floors/create").status_code == 200    

def test_edit(client):
    assert client.get("/floors/edit/1").status_code == 200     

def test_delete(client):
    response = client.post("/floors/delete", data={"id":1})
    assert response.headers["Location"] == "http://localhost/floors/"
