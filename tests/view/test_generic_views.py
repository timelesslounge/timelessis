import pytest

from timeless.views import ListView
from timeless.customers.models import Customer


class TestListView(ListView):
    model = Customer


@pytest.mark.parametrize("query_string,sql_query", (
        ("/?ordering=id,-first_name",
         "ORDER BY customers.id ASC, customers.first_name DESC"),
        ("/?ordering=id,+first_name",
         "ORDER BY customers.id ASC"),
        ("/?ordering=id,foobar",
         "ORDER BY customers.id ASC"),
))
def test_view_ordering(query_string, sql_query, app):
    view = TestListView()
    query = Customer.query
    with app.test_request_context(query_string):
        query = view.sort_query(query)
        assert sql_query in str(query)
