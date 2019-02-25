""" Tests for CrudeAPIView. """
from http import HTTPStatus
import pytest
from werkzeug.exceptions import NotFound
from timeless.views import FakeAPIView


def test_get_found_object(app):
    """ Tests for CrudeAPIView get method when the object exists. """
    with app.test_request_context(
            "/test/crudapitest",
            data={"some_id":5}
    ):
        apiview = FakeAPIView()
        result = apiview.get()
    assert result[0] == {"Found the object"}, "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


def test_get_not_found_object(app):
    """ Tests for CrudeAPIView get method when the object does not exists. """
    with app.test_request_context(
            "/api/crudapi",
            data={"some_id":0}
    ):
        apiview = FakeAPIView()
        with pytest.raises(NotFound, message="Fake object not found"):
            apiview.get()

"""
    @todo #289:30min Add CrudAPIView tests for post, put and delete methods.
     Refer to timeless/views.py CrudAPIView for documentation.
     tests/view/crudeapi/test_comment.py is probably good reference test code for this.
"""
