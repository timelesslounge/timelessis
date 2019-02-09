from tests.poster_mock import free_port, start_server
from timeless.poster.api import Poster


class TestPoster(object):

    @classmethod
    def setup_class(cls):
        cls.port = free_port()
        start_server(cls.port, locations={"data": "testData"}, tables={"data": "testTables"})
        cls.poster = Poster(url=f"http://localhost:{cls.port}")

    def test_locations(self):
        assert (self.poster.locations()["data"] == "testData")

    def test_tables(self):
        assert (self.poster.tables()["data"] == "testTables")