import pytest

from http import HTTPStatus
from flask import g

from timeless.roles.models import RoleType
from tests import factories


""" Tests for the Table views.
@todo #430:30min Fix TableListView problem of returning empty list. 
 TableListView is returning an empty list when it should return valid values. 
 Test below is valid, it calls TableListViews with an authenticated user but it 
 isn't retrieving the tables. Fix the TableListView class and then uncomment the
 test below.
"""


@pytest.mark.skip(reason="TableListView is not behaving correctly")
def test_list(client):
    """ Test list is okay """
    role = factories.RoleFactory(name=RoleType.Intern.name)
    company = factories.CompanyFactory()
    employee = factories.EmployeeFactory(
     company=company, role_id=role.id
    )
    location = factories.LocationFactory(company=company)
    floor = factories.FloorFactory(location=location)
    with client.session_transaction() as session:
        session["user_id"] = employee.id
    g.user = employee
    factories.TableFactory(floor_id=floor.id, name="Table 01")
    factories.TableFactory(floor_id=floor.id, name="Table 01")
    factories.TableFactory(floor_id=floor.id, name="Table 01")
    response = client.get("/tables/")
    print(response.data)
    assert response.status_code == HTTPStatus.OK
    assert b"<div><h1>Table 01</h1></div>" in response.data
    assert b"<div><h1>Table 02</h1></div>" in response.data
    assert b"<div><h1>Table 03</h1></div>" in response.data
    assert b"<div><h1>Table " in response.data.count == 3


def test_required_authentication(client):
    """ Test list is okay """
    response = client.get("/tables/")
    assert response.status_code == HTTPStatus.OK
    assert b"<li><a href=\"#\">Register</a>" in response.data
    assert b"<li><a href=\"/auth/login\">Log In</a>" in response.data


@pytest.mark.skip(reason="/tables/create not implemented")
def test_create(client):
    """ Test create is okay """
    assert client.get("/tables/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/tables/edit not implemented")
def test_edit(client):
    """ Test edit is okay """
    assert client.get("/tables/edit").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/tables/delete not implemented")
def test_delete(client):
    """ Test delete is okay """
    response = client.post("/tables/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost//tables"
