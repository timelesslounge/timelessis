import datetime
import unittest

from tests.poster_mock import free_port, start_server
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.poster.api import Poster
from timeless.sync.sync import PosterSync
from timeless.restaurants.models import Location


class TestSync(unittest.TestCase):

    locations = [
        {
            "id":40,
            "name":"Pao Pao Cafe",
            "code":"P",
            "company_id":50,
            "country":"United States",
            "region":"Nay",
            "city":"South",
            "address":"Delta Park, 145",
            "longitude":640,
            "latitude":480,
            "type":"L",
            "status":"open",
            "comment":"Brazilian cafe"
        },
        {
            "id":150,
            "name":"Central Perk",
            "code":"C",
            "company_id":100,
            "country":"United States",
            "region":"Manhattan",
            "city":"New York",
            "address":"5th Avenue 145",
            "longitude":1024,
            "latitude":720,
            "type":"C",
            "status":"open",
            "comment":"Cafe from famous sitcom"
        },

    ]

    @classmethod
    def setup_class(cls):
        cls.port = free_port()
        start_server(cls.port, locations=cls.locations)
        cls.company = Company(
            name="Any company",
            code="Cpny",
            employees=[
                Employee(first_name="Richard", last_name="Myers")
            ],
            locations=[
                Location(
                    name="Tapper",
                    code="T",
                    company_id=1,
                    poster_id=2,
                    synchronized_on=datetime.datetime(1983, 5, 10)
                ),
                Location(
                    name="Hard Rock",
                    code="H",
                    company_id=5,
                    poster_id=10,
                    synchronized_on=datetime.datetime(1983, 5, 10)
                )
            ])
        cls.poster_sync = PosterSync
        cls.poster = Poster(
            url="http://localhost:{port}".format(port=cls.port)
        )

    @unittest.skip("sync.sync_location not implemented yet")
    def test_sync_location(self):
        self.poster_sync.sync_location(self.poster, self.company)
        assert (self.poster.locations() == self.company.locations)
