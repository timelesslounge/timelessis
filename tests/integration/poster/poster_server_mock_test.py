
from tests.integration.poster.poster_server_mock import PosterServerMock

import requests


class TestPosterServerMock():
    """ Tests for PosterServerMock. Tests the generic behaviors of
    PosterServerMock.
    """

    def test_get_on_invalid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.get(
            url="http://localhost:{port}/otherthing".format(
                port=server.port
            )
        )
        assert response.status_code == 404

    def test_get_on_valid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.get(
            url="http://localhost:{port}/anything".format(
                port=server.port
            )
        )
        assert response.content == b'"get content"' \
            and response.status_code == 200

    def test_post_on_invalid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.post(
            url="http://localhost:{port}/otherthing".format(
                port=server.port
            )
        )
        assert response.status_code == 404

    def test_post_on_valid_url(self):
        server = PosterServerMock
        server.start(server)
        server.PATTERN=r"anything"
        response = requests.post(
            url="http://localhost:{port}/anything".format(
                port=server.port
            )
        )
        assert response.content == b'"post content"' \
            and response.status_code == 200
