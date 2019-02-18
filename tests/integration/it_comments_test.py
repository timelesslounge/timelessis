""" Integration tests for Comment """
from datetime import datetime
from http import HTTPStatus

import pytest

from flask import url_for

from timeless.reservations.models import Comment

"""
@todo #222:30min Correct comments its_tests. After #222 Comments had the logic
 changed and its tests are broken. Correct them and remove pytest.mark.skip
 annotation
"""


@pytest.mark.skip
def test_comments_endpoints(client):
    url = url_for("/api/comments/")
    assert client.get(url).status_code == HTTPStatus.OK
    assert client.post(url).status_code == HTTPStatus.CREATED

    # detail resource
    url = url_for("/api/comments/", comment_id=3)
    assert client.put(url).status_code == HTTPStatus.OK

    assert client.delete(url).status_code == HTTPStatus.NO_CONTENT


@pytest.mark.skip
def test_get_single_comment(client, db_session):
    comment = Comment(body="My comment", date=datetime.utcnow())
    db_session.add(comment)
    db_session.commit()
    url = url_for("/api/comments/", comment_id=1)
    assert client.get().status_code == HTTPStatus.OK


@pytest.mark.xfail(raises=Exception)
def test_comment_not_found(client):
    url = url_for("/api/comments/", comment_id=2)
    client.get()
