from http import HTTPStatus

""" Tests for the TableShape views."""


def test_list(client):
    """ Test list is okay """
    response = client.get("/table_shapes/")
    assert response.status_code == HTTPStatus.OK
    assert b'<form name="filter" target="_self" id="table_filter"/>' in response.data

