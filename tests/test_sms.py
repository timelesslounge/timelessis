import hashlib

from unittest import mock
from timeless.sms import RedSMS


@mock.patch("timeless.sms.datetime")
@mock.patch("timeless.sms.requests")
def test_red_sms_provider(requests_mock, timestamp_mock):
    login = "test_login"
    api_key = "api_key"
    timestamp = 1549208808.562239
    timestamp_mock.now.return_value = type(
        'Mock date', (), {'timestamp': lambda: timestamp})
    secret = hashlib.sha512(
        "{0}{1}".format(timestamp, api_key).encode()).hexdigest()
    recipient = "recipient"
    route = "sms"
    sender = "sender"
    message = "message"

    sms = RedSMS(
        login=login,
        api_key=api_key,
        recipient=recipient,
        message=message,
        sender=sender,
    )
    sms.send()

    requests_mock.post.assert_called_with(
        "https://cp.redsms.ru/api/message",
        data={
            "login": login,
            "ts": timestamp,
            "secret": secret,
            "to": recipient,
            "text": message,
            "route": route,
            "from": sender,
        }
    )
