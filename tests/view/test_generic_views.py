from timeless.views import ListView
from timeless.customers.models import Customer


class TestListView(ListView):
    model = Customer


def test_view_ordering(app):
    view = TestListView()
    query = Customer.query
    with app.test_request_context("/?ordering=id,-first_name"):
        query = view.sort_query(query)
        assert "ORDER BY customers.id ASC, customers.first_name DESC" \
               in str(query)
