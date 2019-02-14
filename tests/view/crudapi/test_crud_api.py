import pytest


from http import HTTPStatus

from timeless.views import FakeAPIView
from timeless.reservations.views import CommentView
from werkzeug.exceptions import NotFound
"""
    Tests for CrudeAPIView.
    
"""

@pytest.mark.skip
def test_get_found_object(app):
    with app.test_request_context(
        '/test/crudapitest',
        data = {'some_id':5}
    ):
        apiview = FakeAPIView
        result = apiview.get(apiview)
    assert result[0] == { "some_id" : 5}, "Wrong result returned from CrudeAPI view"
    assert result[1] == HTTPStatus.OK, "Wrong response from CrudeAPI view"


@pytest.mark.skip
def test_get_not_found_object(app):
    with app.test_request_context(
            '/api/crudeapi',
            data = {'some_id':5}
    ):
        apiview = FakeAPIView
        with pytest.raises(NotFound, message="Fake object not found"):
            apiview.get(apiview)

