"""Poster API"""
import requests

from urllib.parse import urljoin


class Poster(object):
    """Poster application API.

    """

    __GET = "GET"
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
        return self.__send(method=self.__GET, action="clients.getLocations").json()

    def __send(self, **kwargs):
        """Sends http request for specific poster action

        :return: response
        """
        response = requests.request(
            kwargs.get("method"),
            urljoin(self.url, kwargs.get("action", "")),
            params={"format": kwargs.get("format", "json"), "token": kwargs.get("token", self.token)})
        response.raise_for_status()
        return response


class Authenticated(Poster):

    origin = ""

    def __init__(self, **kwargs):
        self.origin = kwargs.get("origin", "")
        self.acount = kwargs.get("client_id", 0)

    def token(self):
        if self.token == "":
            self.auth()
        return self.token

    def auth(self):
        """Authenticates user into poster API
        @todo #67:30min Implement auth process following the Poster API
         https://dev.joinposter.com/en/docs/api#authorization-in-api and use
         real token for sending HTTP requests instead of an empty string. After
         implementing uncomment test of poster auth in it_test_poster.py

        """
        raise("poster.auth not implemented yet")
