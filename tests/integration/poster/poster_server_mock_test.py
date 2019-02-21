import requests

from http.server import HTTPStatus

from tests.integration.poster.poster_server_mock import PosterServerMock


class TestPosterServerMock():
    """ Tests for PosterServerMock. Tests the generic behaviors of
    PosterServerMock.
    """

    def test_get_on_invalid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.get(
            url=f"http://localhost:{server.port}/otherthing"
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_get_on_valid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.get(
            url=f"http://localhost:{server.port}/anything"
        )
        assert response.content.decode("utf-8") == '"get content"'
        assert response.status_code == HTTPStatus.OK

    def test_post_on_invalid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.post(
            url=f"http://localhost:{server.port}/strangerthing"
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_post_on_valid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.post(
            url=f"http://localhost:{server.port}/anything"
        )
        assert response.content.decode("utf-8") == '"post content"'
        assert response.status_code == HTTPStatus.OK
