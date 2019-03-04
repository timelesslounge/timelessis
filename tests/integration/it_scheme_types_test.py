""" Integration tests for Scheme Types """
from datetime import datetime
from http import HTTPStatus

from flask import url_for

from tests import factories
from timeless.schemetypes.models import SchemeType, SchemeCondition


def test_list(client, db_session):
    """ Test getting list of Scheme types """
    db_session.add(SchemeType(description="Test scheme type",
                              default_value="1", value_type="Integer"))
    db_session.commit()
    types = client.get(url_for("scheme_type.list"))
    assert types.status_code == HTTPStatus.OK
    assert b"Test scheme type" in types.data


def test_scheme_condition_list(client, db_session):
    """ Test getting list of Scheme conditions for Scheme type """
    scheme_type = SchemeType(description="Scheme type", default_value="2",
                             value_type="String")
    db_session.add(scheme_type)
    db_session.commit()
    db_session.add(SchemeCondition(scheme_type_id=scheme_type.id,
                                   value="Test condition", priority=1,
                                   start_time=datetime.utcnow(),
                                   end_time=datetime.utcnow()))
    db_session.commit()
    conditions = client.get(url_for("scheme_type.scheme_condition_list",
                                    scheme_type_id=scheme_type.id))
    assert conditions.status_code == HTTPStatus.OK
    assert b"Test condition" in conditions.data


def test_scheme_condition_create(client, db_session):
    """ Test that CreateView works correctly and creates an instance """
    scheme_type = factories.SchemeTypeFactory()
    client.post(
        url_for(
            "scheme_type.scheme_condition_create",
            scheme_type_id=scheme_type.id),
        data={
            "priority": 123,
            "value": "Value",
            "end_time": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        })
    assert SchemeCondition.query.filter_by(value="Value").count() == 1
