""" Tests for CrudeAPIView. """
from http import HTTPStatus
import pytest
import json
from werkzeug.exceptions import NotFound
from timeless.views import FakeAPIView


def test_get_found_object(app):
    """ Tests for CrudeAPIView get method when the object exists. """
    with app.test_request_context(
            "/test/crudapitest"
    ):
        apiview = FakeAPIView()
        result = apiview.get(5)
    json_result = json.loads(result[0].get_data(as_text=True))
    assert json_result == {"some_id":5, "some_attr":"attr"}, "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


def test_get_not_found_object(app):
    """ Tests for CrudeAPIView get method when the object does not exists. """
    with app.test_request_context(
            "/api/crudapi"
    ):
        apiview = FakeAPIView()
        with pytest.raises(NotFound, message="Fake object not found"):
            apiview.get(0)

"""
    @todo #289:30min Add CrudAPIView tests for post, put and delete methods.
     Refer to timeless/views.py CrudAPIView for documentation.
     tests/view/crudeapi/test_comment.py is probably good reference test code for this.
"""
