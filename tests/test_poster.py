from tests.poster_mock import free_port, start_server
from timeless.poster import Poster


class TestPoster(object):

    @classmethod
    def setup_class(cls):
        cls.port = free_port()
        start_server(cls.port, locations={"data": "testData"})

    def test_request_response(self):
        assert (Poster(url="http://localhost:{port}".format(port=self.port)).locations()["data"] == "testData")
