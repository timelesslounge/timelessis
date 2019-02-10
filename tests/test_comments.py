from datetime import datetime
from http import HTTPStatus

import pytest
from timeless.reservations.models import Comment


def test_comments_endpoints(client):
    url = "/api/comments/"
    assert client.get(url).status_code == HTTPStatus.OK

    assert client.post(url).status_code == HTTPStatus.CREATED

    # detail resource
    url = "/api/comments/1"
    assert client.put(url).status_code == HTTPStatus.OK

    assert client.delete(url).status_code == HTTPStatus.NO_CONTENT


def test_get_single_comment(client, db_session):
    comment = Comment(body="My comment", date=datetime.utcnow())
    db_session.add(comment)
    db_session.commit()
    url = "/api/comments/1"
    assert client.get(url).status_code == HTTPStatus.OK

@pytest.mark.xfail(raises=Exception)
def test_comment_not_found(client):
    url = "/api/comments/1"
    client.get(url)
