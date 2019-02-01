import unittest
from timeless.poster import Poster

"""Integration tests for Poster"""


class PosterITTests(unittest.TestCase):

    """
    @todo #67:30min Implement auth process for Poster API.
     client_id is required for authentication process, this id is the public key
     provided by the poster service to identify the applications
    """

    @unittest.skip("poster.auth not implemented yet")
    def test_auth(self):
        poster = Poster(clientid="$0m3C1i3ntId")
        poster.auth()
        assert poster.token != "", "Poster did not authenticated user"
