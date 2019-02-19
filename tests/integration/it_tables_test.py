"""
@todo #234:30min Timeless ModelForm is not working properly, the
 Table form in test_create cannot be saved. The problem is that it
 does not pass form data parameters to model constructor properly.
 Parameters are passed through *args but ModelForm works uses **kwargs
 to instantiate model. Once this is fixed, remove skip annotations
 form tests.
"""
import pytest

from http import HTTPStatus

from flask import url_for

from timeless.restaurants.models import Table


def test_list(client):
    assert client.get("/tables/").status_code == HTTPStatus.OK

@pytest.mark.skip()
def test_create(client):
    name = "test table"
    response = client.post(url_for("table.create"), data={
        "name": name,
        "x": 1,
        "y": 2,
        "width": 100,
        "height": 75,
        "status": 1,
        "max_capacity": 4,
        "multiple": False,
        "playstation": True
    })
    assert response.location.endswith(url_for('table.list_tables'))
    assert Table.query.count() == 1
    assert Table.query.get(1).name == name


@pytest.mark.skip()
def test_edit(client, db_session):
    table = Table(
        name="first name",
        x=1,
        y=2,
        width=100,
        height=75,
        status=1,
        max_capacity=4,
        multiple=False,
        playstation=True
    )
    db_session.add(table)
    db_session.commit()
    name = "updated name"
    response = client.post(url_for("table.edit", id=1), data={
        "name": name,
        "x": 1,
        "y": 2,
        "width": 100,
        "height": 75,
        "status": 1,
        "max_capacity": 4,
        "multiple": False,
        "playstation": True
    })
    assert response.location.endswith(url_for('table.list_tables'))
    assert Table.query.count() == 1
    assert Table.query.get(1).name == name


def test_delete(client, db_session):
    table = Table(
        name="test name",
        x=1,
        y=2,
        width=100,
        height=75,
        status=1,
        max_capacity=4,
        multiple=False,
        playstation=True
    )
    db_session.add(table)
    db_session.commit()
    response =  client.post(url_for("table.delete", id=1))
    assert response.location.endswith(url_for('table.list_tables'))
    assert Table.query.count() == 0

