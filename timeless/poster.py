"""Poster API"""
import requests

from urllib.parse import urljoin


class Poster(object):
    """Poster application API.
    @todo #23:30min Create a job using cron that will synchronize location data from Poster with data in our database.
    Data coming from Poster has priority upon data stored in our database.
    """

    def __init__(self, **kwargs):
        self.url = kwargs.get("url", "https://joinposter.com/api")

    def locations(self):
        """Fetches location data

        :return:
            Location data
        """
        return self.__send(method="GET", action="clients.getLocations").json()

    def __send(self, **kwargs):
        """Sends http request for specific poster action
        @todo #23:30min Implement auth process following the Poster API
        https://dev.joinposter.com/en/docs/api#authorization-in-api and use real token for sending HTTP requests
        instead of an empty string.
        :return: response
        """
        response = requests.request(
            kwargs.get("method"),
            urljoin(self.url, kwargs.get("action", "")),
            params={"format": kwargs.get("format", "json"), "token": kwargs.get("token", "")})
        response.raise_for_status()
        return response
