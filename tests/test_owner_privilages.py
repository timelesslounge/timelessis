from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege


def test_can_access_location():
    assert (
        has_privilege(method=Method.CREATE, resource="location") == True
    )

def test_cant_access_unknown_resource():
    assert (
        has_privilege(method=Method.CREATE, resource="unknown") == False
    )