"""Module for sms sending"""
import hashlib
from datetime import datetime

import requests
from requests.models import Response


class RedSMS:
    """Class for RedSMS provider with send method
    API docs - https://redsms.ru/api-doc/
    """
    api_url = "https://cp.redsms.ru/api/message"

    def __init__(self, login: str, api_key: str) -> None:
        self.login = login
        self.api_key = api_key

    def send(self, recipient: str, message: str, sender: str) -> Response:
        """Sends http post request for sms sending"""
        timestamp = datetime.now().timestamp()
        payload = {
            "login": self.login,
            "ts": timestamp,
            "secret": hashlib.sha512(
                f"{timestamp}{self.api_key}".encode()).hexdigest(),
            "to": recipient,
            "text": message,
            "route": "sms",
            "from": sender,
        }
        return requests.post(self.api_url, data=payload)


class SMS:
    """Class for sms sending"""
    def __init__(
            self,
            provider: RedSMS,
            recipient: str,
            message: str,
            sender: str
    ) -> None:
        self.provider = provider
        self.recipient = recipient
        self.message = message
        self.sender = sender

    def send(self) -> Response:
        """Sends sms via  provider"""
        return self.provider.send(self.recipient, self.message, self.sender)
