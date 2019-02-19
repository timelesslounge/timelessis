import pytest
from werkzeug.exceptions import abort, NotFound

from http import HTTPStatus
from timeless.reservations.views import CommentView

"""
    Tests for CommentView
    @todo #222:30min Finish CommentView implementation and CommentView tests. 
     Methods for GET, POST, PUT and DELETE operation must be implemented, after the 
     implementation remove the skip annotations from these tests.

"""
found_comment = {
    "comment" : {
        "comment_id" : 5,
        "employee_id" : 10,
        "body" : "This is a comment that exists",
        "date" : "4000-01-01"
    }
}

created_comment = {
    "comment" : {
        "employee_id" : 10,
        "body" : "This is a comment that is newly created",
        "date" : "4000-01-01"
    }
}


class FakeComment():
    def get(comment_id):
        if comment_id == 5:
            return found_comment, HTTPStatus.OK
        abort(HTTPStatus.NOT_FOUND)

    def post(comment_id):
        if comment_id == 5:
            return found_comment, HTTPStatus.OK
        abort(HTTPStatus.NOT_FOUND)

    def put(comment):
        if comment.id:
            return found_comment, HTTPStatus.OK
        else:
            return created_comment, HTTPStatus.CREATED

    def delete(comment_id):
        if comment_id == 5:
            return "", HTTPStatus.NO_CONTENT
        abort(HTTPStatus.NOT_FOUND)


@pytest.mark.skip
def test_get_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = {"comment_id" : 5}
    ):
        commentview = CommentView()
        commentview.model = FakeComment
        result = commentview.get()
    assert result[0] == found_comment, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


@pytest.mark.skip
def test_get_not_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = {"comment_id" : 100}
    ):
        commentview = CommentView()
        commentview.model = FakeComment
    with pytest.raises(NotFound):
        commentview.get()


@pytest.mark.skip
def test_post_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = {"comment_id" : 5}
    ):
        commentview = CommentView()
        commentview.model = FakeComment
        result = commentview.post()
    assert result[0] == found_comment, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


@pytest.mark.skip
def test_post_not_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = {"comment_id" : 100}
    ):
        commentview = CommentView()
        commentview.model = FakeComment
    with pytest.raises(NotFound):
        commentview.post()


@pytest.mark.skip
def test_put_existing_comment(app):
    with app.test_request_context(
        "commentview",
        data = found_comment
    ):
        commentview = CommentView()
        commentview.model = FakeComment
        result = commentview.put()
    assert result[0] == found_comment, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.OK, "Wrong status returned from CommentView"


@pytest.mark.skip
def test_put_not_existing_comment(app):
    with app.test_request_context(
            "commentview",
            data = created_comment
    ):
        commentview = CommentView()
        commentview.model = FakeComment
        result = commentview.put()
    assert result[0] == created_comment, "Wrong comment returned from CommentView"
    assert result[1] == HTTPStatus.CREATED, "Wrong status returned from CommentView"


@pytest.mark.skip
def test_delete_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = {"comment_id" : 5}
    ):
        commentview = CommentView()
        commentview.model = FakeComment
        result = commentview.delete()
    assert result[1] == HTTPStatus.NO_CONTENT, "Wrong status returned from CommentView"


@pytest.mark.skip
def test_delete_not_found_comment(app):
    with app.test_request_context(
        "commentview",
        data = created_comment
    ):
        commentview = CommentView()
        commentview.model = FakeComment
    with pytest.raises(NotFound):
        commentview.delete()
