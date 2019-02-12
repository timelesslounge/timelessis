from tests.poster_mock import free_port, start_server
from timeless.poster.api import Poster


class TestPoster:

    @classmethod
    def setup_class(cls):
        cls.port = free_port()
        start_server(
            cls.port,
            locations={"data": "test_data"},
            tables={"data": "test_data"},
            customers={"data": "test_data"}

        )
        cls.poster = Poster(url=f"http://localhost:{cls.port}")

    def test_locations(self):
        assert (self.poster.locations()["data"] == "test_data")

    def test_tables(self):
        assert (self.poster.tables()["data"] == "test_data")

    def test_customers(self):
        assert (self.poster.customers()["data"] == "test_data")
