import flask
import pytest

from tests import factories

"""
@todo #182:30min Inject user privileges into the test below. Test is broken
 because we do not set user privileges and global user privilege logic defined
 in #182 (get roles from user in session). We must simulate this role to user
 for text execution and then uncomment the test. Use factories and cerate a
 roles enumeration for tests with the values in authorization.py
"""


@pytest.mark.skip(reason="Test must set user privileges")
def test_company_endpoints(client):
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory()
    )

    with client.session_transaction() as session:
        session["user_id"] = employee.id

    url = flask.url_for('companies.api', company_id=employee.company_id)
    assert client.get(url).status_code == 200
    assert client.put(url).status_code == 200
    assert client.delete(url).status_code == 204
