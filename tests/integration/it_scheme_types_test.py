from http import HTTPStatus
from timeless.schemetypes.models import SchemeType


def test_list(client, db_session):
    """ Test getting list of Scheme types """
    db_session.add(SchemeType(description="Test scheme type",
                              default_value="1", value_type="Integer"))
    db_session.commit()
    types = client.get("/schemetypes/")
    assert types.status_code == HTTPStatus.OK
    assert b"Test scheme type" in types.data
