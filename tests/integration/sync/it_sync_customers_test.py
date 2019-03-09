import unittest.mock

import pytest

from timeless.customers.models import Customer
from timeless.poster.api import Poster, Authenticated
from timeless.poster.tasks import sync_customers


@pytest.mark.skip(
    "Skipped until ticket #410 is fixed")
@unittest.mock.patch.object(Authenticated, 'auth')
@unittest.mock.patch.object(Poster, 'customers')
def test_sync_customers(customers_mock, auth_mock):
    auth_mock.return_value = 'token'
    poster_customer = {
        "client_id": "55",
        "firstname": "",
        "lastname": "John",
        "patronymic": "",
        "discount_per": "0",
        "bonus": "10000",
        "total_payed_sum": "0",
        "date_activale": "2017-10-09 15:28:14",
        "phone": "+7 963 031-38-44",
        "phone_number": "79630313844",
        "email": "bezmuki@gmail.com",
        "birthday": "0000-00-00",
        "card_number": "0",
        "client_sex": "0",
        "country": "0",
        "city": "0",
        "comment": "0",
        "address": "0",
        "client_groups_id": "3",
        "client_groups_name": "Group name",
        "client_groups_discount": "0",
        "loyalty_type": "1",
        "birthday_bonus": "0",
        "delete": "0",
        "ewallet": "0"
    }

    customers_mock.return_value = {
        "response": [
            poster_customer,
        ]
    }

    sync_customers()

    customer = Customer.query.get(poster_id=poster_customer["client_id"])
    assert customer.first_name == poster_customer["firstname"]
    assert customer.last_name == poster_customer["lastname"]
    assert customer.phone_number == poster_customer["phone_number"]
