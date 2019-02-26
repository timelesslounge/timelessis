import flask

from tests import factories


def test_company_endpoints(client):
    employee = factories.EmployeeFactory(company=factories.CompanyFactory())

    with client.session_transaction() as session:
        session["user_id"] = employee.id

    url = flask.url_for('companies.api', company_id=employee.company_id)
    assert client.get(url).status_code == 200
    assert client.put(url).status_code == 200
    assert client.delete(url).status_code == 200
