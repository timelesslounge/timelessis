"""Poster API"""
import requests

from urllib.parse import urljoin


class Poster(object):
    """Poster application API.

    """

    GET = "GET"
    POST = "POST"
    client_id = 0
    token = ""

    def __init__(self, **kwargs):
        self.url = kwargs.get("url", "https://joinposter.com/api")
        self.account = kwargs.get("client_id", 0)

    def locations(self):
        """Fetches location data

        :return:
            Location data
        """
        return self.send(method=self.GET, action="clients.getLocations").json()

    def send(self, **kwargs):
        """Sends http request for specific poster action

        :return: response
        """
        response = requests.request(
            kwargs.get("method"),
            urljoin(self.url, kwargs.get("action", "")),
            params=kwargs
        )
        response.raise_for_status()
        return response


class Authenticated(Poster):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def access_token(self):
        """Fetches authorization tokens
        
        :return: Token retrieved from Poster api or error returned by poster pi
        """
        response = self.send(
            method=self.POST,
            action="auth/access_token"
        )
        if not response.ok:
            raise Exception("Problem accessing poster api")
        token = response.json().get("access_token")
        if not token:
            raise Exception("Token not found")

        return token

    def auth(self):
        """Authenticates user into poster API
        @todo #101:30min Implement auth process following the Poster API
         https://dev.joinposter.com/en/docs/api#authorization-in-api and use
         real token for sending HTTP requests instead of an empty string. After
         implementing fix the test of poster auth in it_test_poster.py to
         receive the correct paramters and uncomment it.

        """
        raise("poster.auth not implemented yet")
