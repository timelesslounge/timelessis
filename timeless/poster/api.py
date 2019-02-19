"""Poster API"""
import attr
import requests

from urllib.parse import urljoin

from timeless.poster import exceptions


class Poster:
    """Poster application API.

    """

    GET = "GET"
    POST = "POST"
    client_id = 0
    token = ""

    def __init__(self, auth_token=None, **kwargs):
        self.url = kwargs.get("url", "https://joinposter.com/api")
        self.account = kwargs.get("client_id", 0)
        self.auth_token = auth_token

    def locations(self):
        """Fetches location data

        :return:
            Location data
        """
        return self.send(method=self.GET, action="clients.getLocations").json()

    def tables(self):
        """Fetches data about tables

        :return:
            Data about tables
        """
        return self.send(method=self.GET, action="clients.getTables").json()

    def customers(self):
        """Fetches data about customers

        :return:
            Data about customers
        """
        return self.send(method=self.GET, action="clients.getClients").json()

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


@attr.s
class PosterAuthData:
    """ Poster auth data class """
    application_id = attr.ib()
    application_secret = attr.ib()
    redirect_uri = attr.ib()
    code = attr.ib()


class Authenticated:
    """ Poster Auth class """
    auth_url = "https://joinposter.com/api/v2/auth/access_token"

    def __init__(self, auth_data: PosterAuthData, **kwargs):
        self.auth_data = auth_data

    def auth(self):
        """
        Authentication into poster API
        https://dev.joinposter.com/en/docs/api#authorization-in-api and use
        """
        auth_data = {
            "application_id": self.auth_data.application_id,
            "application_secret": self.auth_data.application_secret,
            "grant_type": "authorization_code",
            "redirect_uri": self.auth_data.redirect_uri,
            "code": self.auth_data.code,
        }

        response = requests.post(self.auth_url, data=auth_data)

        if not response.ok:
            raise exceptions.PosterAPIError("Problem accessing poster api")

        token = response.json().get("access_token")

        if not token:
            raise exceptions.PosterAPIError("Token not found")

        return token
