""" Tests for CrudeAPIView. """
import json
from http import HTTPStatus

import pytest
from werkzeug.exceptions import NotFound

from timeless.views import FakeAPIView, FakeModel


def test_get_found_object(app):
    """
    Tests for CrudeAPIView get method when the object exists.
    FakeAPIView extends CrudeAPIView.
    """
    with app.test_request_context(
        "/test/crudapitest"
    ):
        apiview = FakeAPIView()
        result = apiview.get(FakeModel.FakeQuery.FAKE_OBJECT_ID)
    json_result = json.loads(result[0].get_data(as_text=True))
    assert result[0].is_json is True
    assert json_result == {"some_id": FakeModel.FakeQuery.FAKE_OBJECT_ID, "some_attr": "attr"}, \
        "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


def test_get_not_found_object(app):
    """
    Tests for CrudeAPIView get method when the object does not exists.
    FakeAPIView extends CrudeAPIView.
    """
    with app.test_request_context(
        "/api/crudapi"
    ):
        apiview = FakeAPIView()
        with pytest.raises(NotFound, message="Fake object not found"):
            apiview.get(0)


def test_post_object(app):
    """
    Tests for CrudeAPIView post method.
    FakeAPIView extends CrudeAPIView.
    """
    with app.test_request_context(
        "/test/crudapitest"
    ):
        apiview = FakeAPIView()
        payload = {"some_id": 6, "some_attr": "attr6"}
        result = apiview.post(payload)
    json_result = json.loads(result[0].get_data(as_text=True))
    assert result[0].is_json is True
    assert json_result == payload, "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


def test_put_object(app):
    """
    Tests for CrudeAPIView post method.
    FakeAPIView extends CrudeAPIView.
    """
    with app.test_request_context(
        "/test/crudapitest"
    ):
        apiview = FakeAPIView()
        payload = {"some_id": 6, "some_attr": "attr6"}
        result = apiview.put(payload)
    json_result = json.loads(result[0].get_data(as_text=True))
    assert result[0].is_json is True
    assert json_result == payload, "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


def test_delete_object(app):
    """
    Tests for CrudeAPIView post method.
    FakeAPIView extends CrudeAPIView.
    """
    with app.test_request_context(
        "/test/crudapitest"
    ):
        apiview = FakeAPIView()
        result = apiview.delete(object_id=FakeModel.FakeQuery.FAKE_OBJECT_ID)
    json_result = json.loads(result[0].get_data(as_text=True))
    assert result[0].is_json is True
    assert json_result == {"some_id": FakeModel.FakeQuery.FAKE_OBJECT_ID, "some_attr": "attr"}, \
        "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"
