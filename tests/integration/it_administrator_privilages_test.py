from timeless.access_control.administrator_privileges import has_privilege
from timeless.access_control.methods import Method


def test_can_access_and_change_locations(app):
    assert has_privilege(method=Method.READ, resource="location")
    assert has_privilege(method=Method.CREATE, resource="location")
    assert has_privilege(method=Method.UPDATE, resource="location")
    assert has_privilege(method=Method.DELETE, resource="location")


def test_can_access_and_change_employees(app):
    assert has_privilege(method=Method.READ, resource="employee")
    assert has_privilege(method=Method.CREATE, resource="employee")
    assert has_privilege(method=Method.UPDATE, resource="employee")
    assert has_privilege(method=Method.DELETE, resource="employee")


