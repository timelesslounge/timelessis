from http import HTTPStatus


def test_comments_endpoints(client):
    url = "/api/comments/"
    assert client.get(url).status_code == HTTPStatus.OK

    assert client.post(url).status_code == HTTPStatus.CREATED

    # detail resource
    url = "/api/comments/1"
    assert client.get(url).status_code == HTTPStatus.OK

    assert client.put(url).status_code == HTTPStatus.OK

    assert client.delete(url).status_code == HTTPStatus.NO_CONTENT


