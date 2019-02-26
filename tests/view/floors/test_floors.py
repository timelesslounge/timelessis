import pytest

from http import HTTPStatus

from tests.view.floors.mock_floors import FloorMock
from timeless.restaurants.models import Floor
from timeless.restaurants.floors.views import FloorListView

""" Tests for floors. """


def test_list(client):
    """ Test list is okay """
    FloorListView.model = FloorMock(
        floors=
        [
            {
                "id": 1,
                "description": "1st Floor",
                "location_id": 1
            },
            {
                "id": 2,
                "description": "2nd Floor",
                "location_id": 1
            },
            {
                "id": 3,
                "description": "3rd Floor",
                "location_id": 1
            },
            {
                "id": 4,
                "description": "4th Floor",
                "location_id": 1
            }
        ]
    )
    response = client.get("/floors/")
    print(response.data)
    assert response.status_code == HTTPStatus.OK
    assert b"<p class=\"description\">1st Floor</p>" in response.data
    assert b"<p class=\"description\">2nd Floor</p>" in response.data
    assert b"<p class=\"description\">3rd Floor</p>" in response.data
    assert b"<p class=\"description\">4th Floor</p>" in response.data
    FloorListView.model = Floor


@pytest.mark.skip(reason="/floors/create not implemented")
def test_create(client):
    """ Test create is okay """
    assert client.get("/floors/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/floors/edit not implemented")
def test_edit(client):
    """ Test edit is okay """
    assert client.get("/floors/edit").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/floors/delete not implemented")
def test_delete(client):
    """ Test delete is okay """
    response = client.post("/floors/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/restaurant/floors"
