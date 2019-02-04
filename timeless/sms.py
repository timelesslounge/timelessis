"""Module for sms sending"""
import hashlib
from datetime import datetime

import requests


class SMS:
    """Interface for SMS"""

    def send(self):
        """Abstract method send"""
        raise NotImplementedError


class RedSMS(SMS):
    """Class for sms sending
    API docs - https://redsms.ru/api-doc/
    """
    api_url = "https://cp.redsms.ru/api/message"

    def __init__(
            self, login, api_key, recipient, message, sender):
        self.login = login
        self.api_key = api_key
        self.recipient = recipient
        self.message = message
        self.sender = sender

    def make_base_payload(self):
        """Make base payload with basic data for provider"""
        timestamp = datetime.now().timestamp()
        return {
            "login": self.login,
            "ts": timestamp,
            "secret": hashlib.sha512(
                f"{timestamp}{self.api_key}".encode()).hexdigest(),
            "route": "sms",
        }

    def send(self):
        """
        Sends sms via provider
        @todo #46:30min handle exceptional cases and maybe write a
         decorator, some kind of retrial mechanism
         (if the response is 404, the RedSMS api is down at the moment)
        """
        base_payload = self.make_base_payload()
        return requests.post(self.api_url, data={
            "to": self.recipient,
            "text": self.message,
            "from": self.sender,
            **base_payload
        })
