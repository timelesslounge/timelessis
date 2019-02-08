"""Module for sms sending"""
import functools
import hashlib
import time
from datetime import datetime
from http import HTTPStatus

import requests


class SMS:
    """Interface for SMS"""

    def send(self):
        """Abstract method send"""
        raise NotImplementedError


class RetrySendSMS:
    """Decorator class for resending requests"""
    def __init__(self, retry_count=3, timeout=1):
        self.retry_count = retry_count
        self.timeout = timeout
        self.counter = 0
        self.unavailable_status_codes = [
            HTTPStatus.NOT_FOUND,
            HTTPStatus.INTERNAL_SERVER_ERROR
        ]

    def __call__(self, send):
        @functools.wraps(send)
        def decorated(*args, **kwargs):
            response = send(*args, **kwargs)
            response_status_code = response.status_code
            while (response_status_code in self.unavailable_status_codes and
                   self.counter < self.retry_count):
                time.sleep(self.timeout)
                response = send(*args, **kwargs)
                response_status_code = response.status_code
                self.counter += 1
            return response
        return decorated


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
        """Make base payload with basic data for provider
        """
        timestamp = datetime.now().timestamp()
        return {
            "login": self.login,
            "ts": timestamp,
            "secret": hashlib.sha512(
                f"{timestamp}{self.api_key}".encode()
            ).hexdigest(),
            "route": "sms",
        }

    @RetrySendSMS()
    def send(self):
        """
        Sends sms via provider
        """
        base_payload = self.make_base_payload()
        return requests.post(self.api_url, data={
            "to": self.recipient,
            "text": self.message,
            "from": self.sender,
            **base_payload
        })
